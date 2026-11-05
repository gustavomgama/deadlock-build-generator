import os
import re
import json
import time
import hashlib
import argparse
import pickle
import pathlib
import sys
import tempfile
from typing import List, Dict, Any

RAG_DIR = pathlib.Path(__file__).resolve().parent
ROOT = RAG_DIR
MARKLOCK = ROOT / "corpus"
DEADLOCK_API = ROOT / "corpus" / "deadlock-api"
DATA = ROOT / "data"
DEFAULT_INDEX = RAG_DIR / ".rag_index.json"

SKIP_DIRS = {".venv", "__pycache__", ".git", ".opencode", ".ouroboros", "node_modules", ".idea", ".serena"}
TEXT_EXTS = {
    ".md", ".txt", ".py", ".yaml", ".yml", ".json", ".toml", ".cfg", ".ini",
    ".rst", ".html", ".js", ".ts", ".tsx", ".jsx", ".rb", ".go", ".rs",
    ".java", ".c", ".cpp", ".h", ".css", ".sql",
}

EMBED_DIM = 384

SYNONYMS = {
    "ult": "ultimate",
    "ults": "ultimate",
    "hp": "health",
    "cd": "cooldown",
    "dps": "damage",
    "cc": "crowd control",
    "aa": "auto attack",
    "wp": "weapon",
    "ap": "ability power",
    "tech": "spirit",
    "spirit power": "tech power",
    "mag": "magazine",
    "ms": "movement speed",
    "ls": "lifesteal",
    "ar": "armor",
    "mr": "magic resist",
    "br": "bullet resist",
}


def _is_text(path: pathlib.Path) -> bool:
    return path.suffix.lower() in TEXT_EXTS


def _file_hash(path: pathlib.Path) -> str:
    try:
        import hashlib
        h = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def _skip(path: pathlib.Path) -> bool:
    return any(part in SKIP_DIRS for part in path.parts)


def collect_files(root: pathlib.Path) -> List[pathlib.Path]:
    out = []
    if not root.exists():
        return out
    for dp, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            p = pathlib.Path(dp) / f
            if _skip(p):
                continue
            if _is_text(p):
                out.append(p)
    return out


def source_type_for(path: pathlib.Path) -> str:
    s = str(path).lower().replace("\\", "/")
    if "marklock" in s or "/corpus/" in s:
        return "wiki"
    if "deadlock-api" in s or "deadlock_api" in s:
        if path.name.lower() in ("api-1.yaml", "api-1.yml", "api-1.json"):
            return "api"
        return "repo"
    return "repo"


def chunk_text(text: str, size: int = 1200, overlap: int = 200) -> List[str]:
    text = text.replace("\r\n", "\n")
    chunks = []
    n = len(text)
    if n == 0:
        return chunks
    i = 0
    while i < n:
        chunk = text[i:i + size]
        if chunk.strip():
            chunks.append(chunk)
        if i + size >= n:
            break
        i += size - overlap
        if i < 0:
            i = 0
    return chunks


def _tokenize(text: str) -> List[str]:
    out = []
    for w in re.findall(r"\w+", (text or "").lower()):
        parts = [p for p in w.split("_") if p]
        if parts:
            out.extend(parts)
        else:
            out.append(w)
    return out


def _sections(text: str) -> List[tuple]:
    text = (text or "").replace("\r\n", "\n")
    out: List[tuple] = []
    heading = ""
    buf: List[str] = []
    for line in text.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            if buf and "".join(buf).strip():
                out.append((heading, "\n".join(buf).strip()))
            heading = m.group(2).strip()
            buf = []
        else:
            buf.append(line)
    if buf and "".join(buf).strip():
        out.append((heading, "\n".join(buf).strip()))
    if not out:
        out = [("", text.strip())]
    # drop empty sections
    return [(h, b) for h, b in out if b.strip()]


def _hash_embed(text: str, dim: int = EMBED_DIM) -> List[float]:
    vec = [0.0] * dim
    tokens = _tokenize(text)
    if not tokens:
        return vec
    for tok in tokens:
        h = int.from_bytes(hashlib.sha256(tok.encode("utf-8")).digest()[:8], "big")
        idx = h % dim
        vec[idx] += 1.0
        # second hash for sign
        idx2 = (h // dim) % dim
        vec[idx2] -= 0.5
    norm = sum(x * x for x in vec) ** 0.5
    if norm > 0:
        vec = [x / norm for x in vec]
    return vec


def _chunk_embed_text(record: Dict[str, Any]) -> str:
    heading = record.get("section") or ""
    content = record.get("content", "")
    return (heading + "\n" + content).strip() if heading else content


def _normalize(vec: List[float]) -> List[float]:
    n = sum(x * x for x in vec) ** 0.5
    if n == 0:
        return list(vec)
    return [x / n for x in vec]


def _vec_norm(vec: List[float]) -> float:
    return sum(x * x for x in vec) ** 0.5


def _backup(path: pathlib.Path):
    path = pathlib.Path(path)
    if not path.exists():
        return
    try:
        import shutil
        # rotate: keep up to 3 backups
        for i in (2, 1, 0):
            src = pathlib.Path(str(path) + (".bak" if i == 0 else f".bak.{i}"))
            dst = pathlib.Path(str(path) + f".bak.{i + 1}")
            if src.exists():
                if i == 2:
                    try:
                        src.unlink()
                    except OSError:
                        pass
                else:
                    try:
                        shutil.move(str(src), str(dst))
                    except Exception:
                        pass
        shutil.copy2(path, str(path) + ".bak")
    except Exception:
        pass


def _atomic_write(path: pathlib.Path, writer):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    try:
        with os.fdopen(fd, "wb") as f:
            writer(f)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    except Exception:
        try:
            os.remove(tmp)
        except OSError:
            pass
        raise


OLLAMA_URL = os.getenv("OLLAMA_URL", "http://127.0.0.1:11434").rstrip("/")
OLLAMA_TIMEOUT = float(os.getenv("OLLAMA_TIMEOUT", "30"))
OLLAMA_RETRIES = int(os.getenv("OLLAMA_RETRIES", "2"))
OLLAMA_EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")
OLLAMA_CIRCUIT_THRESHOLD = int(os.getenv("OLLAMA_CIRCUIT_THRESHOLD", "3"))

OPENCODE_BASE_URL = os.getenv("OPENCODE_BASE_URL", "https://opencode.ai/inference/openai/v1").rstrip("/")
OPENCODE_MODEL = os.getenv("OPENCODE_MODEL", "deepseek-v4.1-flash")
OPENCODE_TIMEOUT = float(os.getenv("OPENCODE_TIMEOUT", "120"))
OPENCODE_RETRIES = int(os.getenv("OPENCODE_RETRIES", "2"))
OPENCODE_UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"

_OPENCODE_KEY = {"resolved": False, "value": ""}


def _opencode_key() -> str:
    if _OPENCODE_KEY["resolved"]:
        return _OPENCODE_KEY["value"]
    _OPENCODE_KEY["resolved"] = True
    key = (os.getenv("OPENCODE_API_KEY") or "").strip()
    if not key:
        db = pathlib.Path(os.getenv("OPENCODE_DB") or (pathlib.Path.home() / ".local" / "share" / "opencode" / "opencode.db"))
        try:
            import sqlite3
            con = sqlite3.connect("file:" + db.as_posix() + "?mode=ro", uri=True)
            try:
                for label in ("OpenCode Console", "opencode"):
                    row = con.execute("select value from credential where active=1 and label=? limit 1", (label,)).fetchone()
                    if row:
                        key = (json.loads(row[0]) or {}).get("key") or ""
                        if key:
                            break
            finally:
                con.close()
        except Exception:
            key = ""
    if not key:
        try:
            auth = pathlib.Path.home() / ".local" / "share" / "opencode" / "auth.json"
            key = ((json.loads(auth.read_text(encoding="utf-8")) or {}).get("opencode") or {}).get("key") or ""
        except Exception:
            key = ""
    _OPENCODE_KEY["value"] = key.strip()
    return _OPENCODE_KEY["value"]


def opencode_available() -> bool:
    return bool(_opencode_key())


def opencode_chat(messages, model=None, temperature=0.0, json_mode=False, timeout=None) -> str:
    import urllib.request
    import urllib.error
    key = _opencode_key()
    if not key:
        return ""
    url = f"{OPENCODE_BASE_URL}/chat/completions"
    for attempt in range(max(1, OPENCODE_RETRIES)):
        payload = {"model": model or OPENCODE_MODEL, "messages": messages, "temperature": temperature}
        if json_mode:
            payload["response_format"] = {"type": "json_object"}
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={"Content-Type": "application/json", "Authorization": "Bearer " + key, "User-Agent": OPENCODE_UA},
            )
            with urllib.request.urlopen(req, timeout=timeout or OPENCODE_TIMEOUT) as r:
                data = json.loads(r.read())
            return (((data.get("choices") or [{}])[0].get("message") or {}).get("content") or "").strip()
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read()[:200].decode("utf-8", "replace")
            except Exception:
                pass
            if json_mode and e.code == 400:
                json_mode = False
                continue
            _log(f"opencode chat failed: HTTP {e.code} {body}")
        except Exception as e:
            _log(f"opencode chat failed: {type(e).__name__}: {e}")
        time.sleep(0.5 * (attempt + 1))
    return ""


_METRICS = {"queries": 0, "embed_calls": 0, "ollama_failures": 0, "llm_failures": 0, "cache_hits": 0}


def _maybe_log_query(question: str, top, abstained: bool):
    if os.getenv("RAG_LOG_QUERIES") != "1":
        return
    try:
        path = RAG_DIR / ".rag_query_log.jsonl"
        rec = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "question": question,
            "abstained": bool(abstained),
            "citations": [r.get("citation", r.get("source_path")) for r in (top or [])],
        }
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    except Exception:
        pass
    if os.getenv("RAG_QUIET") == "1":
        return
    try:
        sys.stderr.write(f"[rag] {msg}\n")
        sys.stderr.flush()
    except Exception:
        pass

_OLLAMA_CACHE = {"checked": False, "available": False, "checked_at": 0.0}
_OLLAMA_BREAKER = {"failures": 0, "opened_at": 0.0}


def _ollama_circuit_open() -> bool:
    if _OLLAMA_BREAKER["failures"] < OLLAMA_CIRCUIT_THRESHOLD:
        return False
    if time.time() - _OLLAMA_BREAKER["opened_at"] > 60:
        _OLLAMA_BREAKER["failures"] = 0
        return False
    return True


def _ollama_record(ok: bool):
    if ok:
        _OLLAMA_BREAKER["failures"] = 0
    else:
        _OLLAMA_BREAKER["failures"] += 1
        _METRICS["ollama_failures"] += 1
        if _OLLAMA_BREAKER["failures"] >= OLLAMA_CIRCUIT_THRESHOLD:
            _OLLAMA_BREAKER["opened_at"] = time.time()


def _ollama_available() -> bool:
    if _OLLAMA_CACHE["checked"] and (time.time() - _OLLAMA_CACHE["checked_at"]) < 60:
        return _OLLAMA_CACHE["available"] and not _ollama_circuit_open()
    if _ollama_circuit_open():
        return False
    try:
        import urllib.request
        import urllib.error
        try:
            with urllib.request.urlopen(f"{OLLAMA_URL}/api/tags", timeout=2.0) as r:
                ok = 200 <= r.status < 300
        except urllib.error.HTTPError as e:
            ok = False
        _OLLAMA_CACHE["available"] = ok
        _ollama_record(ok)
    except Exception:
        _OLLAMA_CACHE["available"] = False
        _ollama_record(False)
    _OLLAMA_CACHE["checked"] = True
    _OLLAMA_CACHE["checked_at"] = time.time()
    return _OLLAMA_CACHE["available"] and not _ollama_circuit_open()


def _log(msg: str) -> None:
    if os.getenv("RAG_QUIET"):
        return
    print(msg, file=sys.stderr)


def embed_batch(texts: List[str]) -> List[List[float]]:
    if _ollama_available():
        try:
            out = []
            batch_size = 64
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                embs = None
                for attempt in range(max(1, OLLAMA_RETRIES)):
                    try:
                        import urllib.request, json as _j
                        payload = {"model": OLLAMA_EMBED_MODEL, "input": batch, "keep_alive": "10m"}
                        data_bytes = _j.dumps(payload).encode("utf-8")
                        req = urllib.request.Request(f"{OLLAMA_URL}/api/embed", data=data_bytes, headers={"Content-Type": "application/json"})
                        with urllib.request.urlopen(req, timeout=OLLAMA_TIMEOUT) as r:
                            raw = r.read()
                            status = r.status
                        if 200 <= status < 300:
                            data = _j.loads(raw)
                            got = data.get("embeddings") or data.get("embedding")
                            if got and isinstance(got, list):
                                embs = got
                                break
                    except Exception as e:
                        _log(f"ollama embed attempt {attempt + 1} failed: {type(e).__name__}")
                    time.sleep(0.3 * (attempt + 1))
                if embs:
                    for e in embs:
                        if isinstance(e, list):
                            out.append([float(x) for x in e])
                        else:
                            out.append(_hash_embed(batch[len(out) % len(batch)]))
                    continue
                # fallback for this batch
                _log("ollama embed batch failed; using hash fallback")
                for t in batch:
                    out.append(_hash_embed(t))
            if len(out) == len(texts):
                _ollama_record(True)
                return [_normalize(v) for v in out]
        except Exception:
            _ollama_record(False)
            pass
    return [_hash_embed(t) for t in texts]


_EMBED_CACHE_PATH = pathlib.Path(os.getenv("RAG_EMBED_CACHE") or (RAG_DIR / ".rag_embed_cache.json"))
_EMBED_CACHE: Dict[str, List[float]] = {}
_EMBED_PERSIST_COUNTER = {"n": 0}
_EMBED_CACHE_MAX = 10000


def _embed_cache_key(text: str) -> str:
    return hashlib.sha256((text + "|" + str(_ollama_available())).encode("utf-8")).hexdigest()


def embed(text: str) -> List[float]:
    key = _embed_cache_key(text)
    if key in _EMBED_CACHE:
        _METRICS["cache_hits"] += 1
        return _EMBED_CACHE[key]
    # try disk cache
    try:
        if _EMBED_CACHE_PATH.exists():
            disk = json.loads(_EMBED_CACHE_PATH.read_text(encoding="utf-8"))
            if isinstance(disk, dict) and key in disk:
                val = disk[key]
                _EMBED_CACHE[key] = val
                _METRICS["cache_hits"] += 1
                return val
    except Exception:
        pass
    if _ollama_available():
        res = embed_batch([text])
        if res:
            _EMBED_CACHE[key] = res[0]
            _EMBED_PERSIST_COUNTER["n"] += 1
            _persist_embed_cache()
            return res[0]
    val = _hash_embed(text)
    _EMBED_CACHE[key] = val
    _EMBED_PERSIST_COUNTER["n"] += 1
    _persist_embed_cache()
    return val


def _persist_embed_cache(force=False):
    global _EMBED_CACHE
    try:
        if not force and _EMBED_PERSIST_COUNTER["n"] < 25:
            return
        _EMBED_PERSIST_COUNTER["n"] = 0
        existing = {}
        if _EMBED_CACHE_PATH.exists():
            existing = json.loads(_EMBED_CACHE_PATH.read_text(encoding="utf-8"))
            if not isinstance(existing, dict):
                existing = {}
        existing.update(_EMBED_CACHE)
        # trim to max entries (keep most recent)
        if len(existing) > _EMBED_CACHE_MAX:
            keys = list(existing.keys())
            for k in keys[:-_EMBED_CACHE_MAX]:
                existing.pop(k, None)
        _EMBED_CACHE_PATH.write_text(json.dumps(existing), encoding="utf-8")
        _EMBED_CACHE.clear()
        _EMBED_CACHE.update(existing)
    except Exception:
        pass


def cosine(a: List[float], b: List[float]) -> float:
    n = min(len(a), len(b))
    if n == 0:
        return 0.0
    dot = sum(a[i] * b[i] for i in range(n))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(x * x for x in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def _classify_record(path: pathlib.Path):
    s = str(path).lower().replace("\\", "/")
    if "deadlock-api" in s or "deadlock_api" in s:
        trust = "high"
    elif "marklock" in s or "/corpus/" in s:
        trust = "medium-high"
    else:
        trust = "medium"
    if "/heroes/" in s:
        etype = "hero"
    elif "/items/" in s:
        etype = "item"
    elif "/mechanics/" in s:
        etype = "mechanic"
    elif "/oracle/" in s:
        etype = "oracle"
    else:
        etype = "document"
    m = re.search(r"patch[-_ ]?playtest[-_ ]?(\d{4}-\d{2}-\d{2})", s)
    if not m:
        m = re.search(r"patch[-_ ]?(\d{4}-\d{2}-\d{2})", s)
    patch = m.group(1) if m else "current"
    return etype, trust, patch

def build_index(index_path, limit=None) -> int:
    index_path = pathlib.Path(index_path)
    records: List[Dict[str, Any]] = []
    _roots_env = os.getenv("RAG_ROOTS")
    if _roots_env:
        roots = [pathlib.Path(x.strip()) for x in _roots_env.split(",") if x.strip()]
        roots = [r if r.is_absolute() else (ROOT / r) for r in roots]
    else:
        roots = [MARKLOCK / "organized", DEADLOCK_API]
    # First collect chunks
    chunk_records = []  # list of (meta, text)
    all_files = []
    for root in roots:
        all_files.extend(collect_files(root))
    if limit is not None:
        all_files = all_files[:limit]
    for p in all_files:
        try:
            if p.stat().st_size > 5 * 1024 * 1024:
                _log(f"skip large file: {p}")
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not text.strip():
            continue
        st = source_type_for(p)
        try:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        try:
            mtime = p.stat().st_mtime
            size = p.stat().st_size
        except OSError:
            mtime = 0.0
            size = 0
        chunk_idx = 0
        for heading, section in _sections(text):
            for ch in chunk_text(section):
                embed_text = (heading + "\n" + ch).strip() if heading else ch
                chunk_records.append((st, rel, chunk_idx, ch, heading, embed_text, mtime, size, _file_hash(p)))
                chunk_idx += 1

    texts = [cr[5] for cr in chunk_records]
    embeddings = embed_batch(texts)
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    for (st, rel, idx, ch, heading, embed_text, mtime, size, fhash), emb in zip(chunk_records, embeddings):
        _p = ROOT / rel
        _etype, _trust, _patch = _classify_record(_p)
        records.append({
            "schema_version": 1,
            "source_type": st,
            "source_path": rel,
            "chunk_id": f"{rel}::{idx}",
            "content": ch,
            "embedding": emb,
            "norm": _vec_norm(emb),
            "section": heading,
            "metadata": {"file": rel, "section": heading, "file_mtime": mtime, "file_size": size, "file_hash": fhash, "entity_type": _etype, "trust_level": _trust, "patch_version": _patch},
            "citation": rel,
            "last_synced": now,
            "relationships": [],
        })
    index_path.parent.mkdir(parents=True, exist_ok=True)

    def _w_json(f):
        f.write(json.dumps(records).encode("utf-8"))

    _backup(index_path)
    _atomic_write(index_path, _w_json)
    try:
        sidecar = index_path.with_suffix(".pkl")

        def _w_pkl(f):
            pickle.dump(records, f, protocol=pickle.HIGHEST_PROTOCOL)

        _atomic_write(sidecar, _w_pkl)
    except Exception:
        pass
    return len(records)


def sync(index_path=DEFAULT_INDEX, limit=None) -> int:
    index_path = pathlib.Path(index_path)
    existing = load_index(index_path) if index_path.exists() else []
    by_path: Dict[str, List[Dict[str, Any]]] = {}
    for r in existing:
        by_path.setdefault(r["source_path"], []).append(r)

    _roots_env = os.getenv("RAG_ROOTS")
    if _roots_env:
        roots = [pathlib.Path(x.strip()) for x in _roots_env.split(",") if x.strip()]
        roots = [r if r.is_absolute() else (ROOT / r) for r in roots]
    else:
        roots = [MARKLOCK / "organized", DEADLOCK_API]
    all_files = []
    for root in roots:
        all_files.extend(collect_files(root))
    if limit is not None:
        all_files = all_files[:limit]

    current_rel = {}
    for p in all_files:
        try:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        try:
            current_rel[rel] = (p, p.stat().st_mtime, p.stat().st_size, _file_hash(p))
        except OSError:
            current_rel[rel] = (p, 0.0, 0, "")

    changed = []
    for rel, (p, mtime, size, fhash) in current_rel.items():
        old = by_path.get(rel, [])
        if not old:
            changed.append(p)
            continue
        om = old[0].get("metadata", {}).get("file_mtime")
        osz = old[0].get("metadata", {}).get("file_size")
        oh = old[0].get("metadata", {}).get("file_hash", "")
        if om != mtime or osz != size or (oh and oh != fhash):
            changed.append(p)

    deleted = set(by_path.keys()) - set(current_rel.keys())
    if not changed and not deleted:
        return len(existing)

    changed_rels = set()
    for p in changed:
        try:
            changed_rels.add(str(p.relative_to(ROOT)).replace("\\", "/"))
        except ValueError:
            changed_rels.add(str(p).replace("\\", "/"))

    kept = [r for r in existing if r["source_path"] not in changed_rels and r["source_path"] not in deleted]

    # backfill metadata fields added in newer schema versions
    for r in kept:
        md = r.setdefault("metadata", {})
        if "entity_type" not in md or "trust_level" not in md or "patch_version" not in md:
            try:
                _etype, _trust, _patch = _classify_record(ROOT / r.get("source_path", ""))
            except Exception:
                _etype, _trust, _patch = "document", "medium", "current"
            md.setdefault("entity_type", _etype)
            md.setdefault("trust_level", _trust)
            md.setdefault("patch_version", _patch)

    chunk_records = []
    for p in changed:
        try:
            if p.stat().st_size > 5 * 1024 * 1024:
                _log(f"skip large file: {p}")
                continue
            text = p.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        if not text.strip():
            continue
        st = source_type_for(p)
        try:
            rel = str(p.relative_to(ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p).replace("\\", "/")
        try:
            mtime = p.stat().st_mtime
            size = p.stat().st_size
        except OSError:
            mtime = 0.0
            size = 0
        chunk_idx = 0
        for heading, section in _sections(text):
            for ch in chunk_text(section):
                embed_text = (heading + "\n" + ch).strip() if heading else ch
                chunk_records.append((st, rel, chunk_idx, ch, heading, embed_text, mtime, size, _file_hash(p)))
                chunk_idx += 1

    texts = [cr[5] for cr in chunk_records]
    embeddings = embed_batch(texts) if texts else []
    now = time.strftime("%Y-%m-%dT%H:%M:%S")
    new_records = list(kept)
    for (st, rel, idx, ch, heading, embed_text, mtime, size, fhash), emb in zip(chunk_records, embeddings):
        _p = ROOT / rel
        _etype, _trust, _patch = _classify_record(_p)
        new_records.append({
            "schema_version": 1,
            "source_type": st,
            "source_path": rel,
            "chunk_id": f"{rel}::{idx}",
            "content": ch,
            "embedding": emb,
            "norm": _vec_norm(emb),
            "section": heading,
            "metadata": {"file": rel, "section": heading, "file_mtime": mtime, "file_size": size, "file_hash": fhash, "entity_type": _etype, "trust_level": _trust, "patch_version": _patch},
            "citation": rel,
            "last_synced": now,
            "relationships": [],
        })

    index_path.parent.mkdir(parents=True, exist_ok=True)

    def _w_json(f):
        f.write(json.dumps(new_records).encode("utf-8"))

    _backup(index_path)
    _atomic_write(index_path, _w_json)
    try:
        sidecar = index_path.with_suffix(".pkl")

        def _w_pkl(f):
            pickle.dump(new_records, f, protocol=pickle.HIGHEST_PROTOCOL)

        _atomic_write(sidecar, _w_pkl)
    except Exception:
        pass
    # refresh cache
    _INDEX_CACHE.pop(str(index_path.resolve()), None)
    return len(new_records)


_INDEX_CACHE: Dict[str, tuple] = {}


def load_index(index_path) -> List[Dict[str, Any]]:
    index_path = pathlib.Path(index_path)
    if not index_path.exists():
        return []
    key = str(index_path.resolve())
    try:
        # validate json early if no sidecar
        pass
    except Exception:
        pass
    try:
        mtime = index_path.stat().st_mtime
    except OSError:
        mtime = 0.0
    cached = _INDEX_CACHE.get(key)
    if cached is not None and cached[0] == mtime:
        return cached[1]
    sidecar = index_path.with_suffix(".pkl")
    records = None
    try:
        if sidecar.exists() and sidecar.stat().st_mtime >= mtime:
            with sidecar.open("rb") as f:
                records = pickle.load(f)
    except Exception:
        records = None
    if records is None:
        try:
            records = json.loads(index_path.read_text(encoding="utf-8"))
        except Exception as e:
            _log(f"index load failed: {e}")
            return []
    _INDEX_CACHE[key] = (mtime, records)
    return records


def _opencode_generate(question: str, context: str) -> str:
    txt = opencode_chat([
        {"role": "system", "content": "You are a Deadlock game oracle. Answer only from provided context. Cite sources. Never invent facts."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"},
    ])
    if not txt:
        _METRICS["llm_failures"] += 1
    return txt


def _opencode_rewrite(question: str) -> str:
    if not opencode_available():
        return question
    txt = opencode_chat([
        {"role": "user", "content": f"Rewrite this search query for a Deadlock game wiki. Return only the rewritten query.\n\nQuery: {question}\nRewritten:"},
    ], temperature=0.0)
    if txt and len(txt) < 200:
        return txt
    return question


def _in_scope(question: str) -> bool:
    q = (question or "").lower()
    terms = {"deadlock", "hero", "heroes", "ability", "abilities", "item", "items", "build", "builds", "patch", "patches", "soul", "boon", "lane", "tower", "creep", "minion", "weapon", "spirit", "bullet", "cooldown", "ultimate", "ult", "mod", "upgrade", "mechanic", "mechanics", "match", "player", "game", "stamina", "dash", "dashing", "health", "armor", "resist", "slide", "wall", "jump", "crouch", "parry", "melee", "ranged", "reload", "magazine", "ammo", "lifesteal", "regen", "healing", "shield", "barrier", "slow", "stun", "silence", "root", "disarm", "knockback", "pull", "push", "teleport", "invis", "stealth", "vision", "ward", "orb", "neutral", "boss", "walker", "barrack", "base", "patron", "rejuv", "rejuvenator", "urn", "golden", "statue", "idol", "depot", "shop", "secret", "stairs", "zipline", "rope", "transit", "trooper", "sinner", "sacrifice", "dash", "level", "levels", "xp", "experience"}
    # hero names from heroes_raw.json if available
    try:
        import json as _j, pathlib as _p
        for fname in ("heroes_raw.json", "items_raw.json"):
            fp = DATA / fname
            if fp.exists():
                try:
                    data = _j.loads(fp.read_text(encoding="utf-8"))
                except Exception:
                    data = []
                for e in data:
                    nm = (e.get("name") or e.get("item_name") or e.get("hero_name") or "").lower()
                    if nm:
                        terms.add(nm)
                        for part in nm.split():
                            if part not in {"the", "of", "and", "a", "an", "in", "on", "at", "to", "for", "with", "by", "speed", "light"}:
                                terms.add(part)
        # mechanic file stems
        mech_dir = MARKLOCK / "organized" / "mechanics"
        if mech_dir.exists():
            for p in mech_dir.glob("*.md"):
                for part in _tokenize(p.stem):
                    if len(part) > 3 and part not in {"the", "and", "for", "speed", "light"}:
                        terms.add(part)
    except Exception:
        pass
    toks = set(_tokenize(q))
    return bool(toks & terms)


def _visible(text: str) -> str:
    return re.sub(r"^\s*---\s*\n.*?\n---\s*\n", "", text or "", flags=re.S)


def query(index_path, question: str, top_k: int = 5, filters: Dict[str, Any] = None, history: List[str] = None, rewrite = False, min_score: float = None, as_json: bool = False, mmr_lambda: float = 0.7, current_only: bool = False, generate: bool = True) -> str:
    _METRICS["queries"] += 1
    question = " ".join((question or "").split())[:500]
    if not _in_scope(question):
        if as_json:
            return "[]"
        return "Out of scope: this oracle only answers questions about Deadlock."
    top_k = max(1, min(int(top_k or 5), 20))
    question = " ".join((question or "").split())[:500]
    if not question:
        return "No question provided."
    records = load_index(index_path)
    if not records:
        return "No index found. Run: python rag.py sync"
    if filters:
        cand = []
        for r in records:
            md = r.get("metadata") or {}
            if all(md.get(k) == v or r.get(k) == v for k, v in filters.items()):
                cand.append(r)
        records = cand or records
    if current_only:
        cp = current_patch(index_path)
        cand = [r for r in records if (r.get("metadata") or {}).get("patch_version") in ("current", cp)]
        records = cand or records

    hist = history or []
    # dedup consecutive duplicates
    _dedup = []
    for h in hist:
        if not _dedup or _dedup[-1] != h:
            _dedup.append(h)
    hist = _dedup
    retrieval_question = question
    if hist:
        retrieval_question = "\n".join(hist[-3:] + [question])
    if rewrite or os.getenv("RAG_REWRITE") == "1":
        retrieval_question = _opencode_rewrite(retrieval_question)
    qe = embed(retrieval_question)
    qn = _vec_norm(qe) or 1.0
    qe_hash = _hash_embed(retrieval_question)
    hash_embs = None
    if any(len(r.get("embedding") or []) != len(qe) for r in records):
        hash_embs = [_hash_embed(_chunk_embed_text(r)) for r in records]
    qtoks = set(_tokenize(retrieval_question))
    _expanded = set()
    for t in list(qtoks):
        if t in SYNONYMS:
            _expanded.update(_tokenize(SYNONYMS[t]))
    qtoks = qtoks | _expanded

    # precompute hero slugs mentioned in the query (for hero-name boost)
    _hero_slugs_in_q = []
    try:
        for hp in (MARKLOCK / "organized" / "heroes").glob("*.md"):
            htoks = set(_tokenize(hp.stem))
            if htoks and htoks.issubset(qtoks):
                _hero_slugs_in_q.append(hp.stem.lower())
    except Exception:
        pass

    # BM25 over corpus
    tokenized = [_tokenize(r.get("content", "") + " " + (r.get("section") or "")) for r in records]
    df = {}
    for toks in tokenized:
        for t in set(toks):
            df[t] = df.get(t, 0) + 1
    N = max(len(records), 1)
    avgdl = sum(len(t) for t in tokenized) / N if N else 1.0
    k1, b = 1.5, 0.75

    def _bm25(r, toks):
        score = 0.0
        dl = len(toks) or 1
        tf = {}
        for t in toks:
            tf[t] = tf.get(t, 0) + 1
        for t in qtoks:
            if t not in df:
                continue
            idf = (N - df[t] + 0.5) / (df[t] + 0.5)
            idf = (idf + 1)  # bm25+ style
            import math
            idf = math.log(1 + (N - df[t] + 0.5) / (df[t] + 0.5))
            f = tf.get(t, 0)
            denom = f + k1 * (1 - b + b * dl / (avgdl or 1))
            if denom:
                score += idf * (f * (k1 + 1)) / denom
        return score

    _index_of = {id(r): i for i, r in enumerate(records)}
    bm25_scores = [_bm25(r, tokenized[i]) for i, r in enumerate(records)]
    max_bm = max(bm25_scores) if bm25_scores else 1.0
    if max_bm <= 0:
        max_bm = 1.0

    def _score(r):
        idx = _index_of.get(id(r), 0)
        emb = r.get("embedding") or []
        dense = 0.0
        if len(emb) == len(qe):
            dot = sum(a * b for a, b in zip(qe, emb))
            en = r.get("norm") or _vec_norm(emb) or 1.0
            denom = qn * en
            dense = (dot / denom) if denom else 0.0
        elif hash_embs is not None:
            dense = cosine(qe_hash, hash_embs[idx])
        toks = tokenized[idx]
        tset = set(toks)
        overlap = len(qtoks & tset)
        lex = overlap / (len(qtoks) or 1)
        path_tokens = set(_tokenize(r.get("source_path", "") + " " + (r.get("section") or "")))
        if qtoks and qtoks.issubset(path_tokens):
            path_boost = 1.0
        elif qtoks & path_tokens:
            path_boost = 0.4
        else:
            path_boost = 0.0
        _file_stem = r.get("source_path", "").split("/")[-1]
        if "." in _file_stem:
            _file_stem = _file_stem.rsplit(".", 1)[0]
        file_tokens = set(_tokenize(_file_stem))
        file_boost = 1.0 if (qtoks and qtoks.issubset(file_tokens)) else 0.0
        # hero-name boost: prefer the specific hero's page when a hero is named
        hero_boost = 0.0
        if _hero_slugs_in_q:
            sp = r.get("source_path", "").lower()
            if any(slug in sp for slug in _hero_slugs_in_q):
                hero_boost = 1.0
        bm = bm25_scores[idx] / max_bm
        combined = 0.45 * dense + 0.15 * bm + 0.1 * lex + 0.3 * path_boost + 0.25 * file_boost + 0.1 * hero_boost
        return combined

    # MMR selection
    def _cos(a, b):
        ea = a.get("embedding") or []
        eb = b.get("embedding") or []
        if len(ea) == len(eb) and ea:
            return cosine(ea, eb)
        if hash_embs is not None:
            ia = _index_of.get(id(a))
            ib = _index_of.get(id(b))
            if ia is not None and ib is not None:
                return cosine(hash_embs[ia], hash_embs[ib])
        return 0.0

    selected = []
    candidates = list(records)
    while len(selected) < top_k and candidates:
        if not selected:
            best = max(candidates, key=_score)
        else:
            best = max(candidates, key=lambda r: mmr_lambda * _score(r) - (1 - mmr_lambda) * max((_cos(r, s) for s in selected), default=0.0))
        selected.append(best)
        candidates.remove(best)

    # score threshold
    if min_score is None:
        min_score = 0.05
    filtered = [r for r in selected if _score(r) >= min_score]
    top = filtered if filtered else selected[:1]
    _STOP = {"what", "is", "the", "a", "an", "of", "to", "for", "and", "in", "on", "at", "how", "many", "does", "do", "me", "build", "are", "was", "were", "be", "been", "this", "that", "it", "with", "by", "from", "or", "as", "if", "can", "could"}
    _qtoks = [t for t in _tokenize(question) if t not in _STOP]
    _content = " ".join((r.get("content", "") + " " + (r.get("section") or "") + " " + r.get("source_path", "")) for r in top).lower()
    _cov = (sum(1 for t in _qtoks if t in _content) / len(_qtoks)) if _qtoks else 1.0
    if _cov < 0.5 or any(t.isdigit() and t not in _content for t in _qtoks) or any(vt not in _content for vt in re.findall(r"\d+\.\d+(?:\.\d+)?", question)):
        _maybe_log_query(question, top, True)
        if as_json:
            return "[]"
        return "Insufficient data: I cannot answer this from the retrieved Deadlock sources."
    context = "\n\n".join(f"[{r.get('citation', r.get('source_path'))}] {_visible(r.get('content',''))}" for r in top)
    if as_json:
        _maybe_log_query(question, top, False)
        payload = []
        for r in top:
            payload.append({
                "citation": r.get("citation", r.get("source_path")),
                "score": round(_score(r), 4),
                "snippet": " ".join(_visible(r["content"]).split())[:400],
            })
        return json.dumps(payload, ensure_ascii=False, indent=2)
    generated = _opencode_generate(question, context) if generate and opencode_available() else ""

    lines = []
    if generated:
        lines.append(generated)
        lines.append("")
    lines.append(f"Retrieved (top {len(top)}):")
    for i, r in enumerate(top, 1):
        snippet = " ".join(_visible(r["content"]).split())[:400]
        md = r.get("metadata") or {}
        meta = []
        if md.get("patch_version"):
            meta.append(f"patch {md['patch_version']}")
        if md.get("trust_level"):
            meta.append(f"trust {md['trust_level']}")
        suffix = f" ({', '.join(meta)})" if meta else ""
        lines.append(f"{i}. {snippet}")
        lines.append(f"   [source: {r.get('citation', r.get('source_path'))}{suffix}]")
    srcs = sorted({r.get("citation", r.get("source_path")) for r in top})
    lines.append("")
    lines.append("Sources: " + ", ".join(srcs))
    if not _ollama_available():
        lines.append("[note: ollama DOWN - hash embeddings only]")
    if generate and not opencode_available():
        lines.append("[note: no OpenCode credentials - no generated answer]")
    _maybe_log_query(question, top, False)
    return "\n".join(lines)


def sync_if_stale(index_path=DEFAULT_INDEX, max_age_hours: float = 24.0) -> bool:
    index_path = pathlib.Path(index_path)
    if not index_path.exists():
        sync(index_path)
        return True
    age = time.time() - index_path.stat().st_mtime
    if age > max_age_hours * 3600:
        sync(index_path)
        return True
    return False


def current_patch(index_path=DEFAULT_INDEX) -> str:
    try:
        recs = load_index(index_path)
    except Exception:
        return "current"
    vals = sorted({(r.get("metadata") or {}).get("patch_version") for r in recs if (r.get("metadata") or {}).get("patch_version") and (r.get("metadata") or {}).get("patch_version") != "current"})
    return vals[-1] if vals else "current"


def health(index_path=DEFAULT_INDEX) -> str:
    lines = []
    p = pathlib.Path(index_path)
    lines.append(f"index: {'OK' if p.exists() else 'MISSING'} ({p})")
    if p.exists():
        try:
            age_h = (time.time() - p.stat().st_mtime) / 3600.0
            lines.append(f"index_age_hours: {age_h:.2f}")
            lines.append(f"index_size_bytes: {p.stat().st_size}")
        except OSError:
            pass
    try:
        recs = load_index(p) if p.exists() else []
        lines.append(f"records: {len(recs)}")
        from collections import Counter
        c = Counter(r.get("source_type", "?") for r in recs)
        lines.append(f"by_source_type: {dict(c)}")
        pv = len({(r.get("metadata") or {}).get("patch_version") for r in recs if (r.get("metadata") or {}).get("patch_version")})
        lines.append(f"distinct_patch_versions: {pv}")
    except Exception as e:
        lines.append(f"records: ERROR {e}")
    lines.append(f"ollama: {'UP' if _ollama_available() else 'DOWN'} ({OLLAMA_URL})")
    lines.append(f"circuit_open: {_ollama_circuit_open()}")
    lines.append(f"opencode: {'KEY OK' if opencode_available() else 'NO KEY'} ({OPENCODE_MODEL} via {OPENCODE_BASE_URL})")
    lines.append(f"metrics: {_METRICS}")
    return "\n".join(lines)


def main(argv=None):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass
    parser = argparse.ArgumentParser(description="Deadlock RAG (local, free)")
    parser.add_argument("--version", action="version", version="rag 1.0")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_build = sub.add_parser("build", help="Build index")
    p_build.add_argument("--index", default=str(DEFAULT_INDEX))
    p_query = sub.add_parser("query", help="Query index")
    p_query.add_argument("question")
    p_query.add_argument("--index", default=str(DEFAULT_INDEX))
    p_query.add_argument("--top-k", type=int, default=5)
    p_query.add_argument("--rewrite", action="store_true", help="Rewrite query via OpenCode before retrieval")
    p_query.add_argument("--filter-source-type", default=None)
    p_query.add_argument("--filter-entity-type", default=None)
    p_query.add_argument("--filter-patch", default=None)
    p_query.add_argument("--current-only", action="store_true", help="Filter to current/latest patch records")
    p_query.add_argument("--no-generate", action="store_true", help="Skip OpenCode answer generation")
    p_query.add_argument("--min-score", type=float, default=None)
    p_query.add_argument("--json", action="store_true", dest="as_json")
    p_sync = sub.add_parser("sync", help="Sync/rebuild index")
    p_sync.add_argument("--index", default=str(DEFAULT_INDEX))
    p_sync.add_argument("--watch", action="store_true", help="Loop every 24h")
    p_health = sub.add_parser("health", help="Health check")
    p_health.add_argument("--index", default=str(DEFAULT_INDEX))
    p_health.add_argument("--json", action="store_true", dest="as_json")
    parser.add_argument("--quiet", action="store_true", help="Suppress progress logs")
    args = parser.parse_args(argv)

    if getattr(args, "quiet", False):
        os.environ["RAG_QUIET"] = "1"
    if args.cmd == "build":
        n = build_index(args.index)
        print(f"INDEX_OK: {n} chunks")
    elif args.cmd == "query":
        filters = {}
        if args.filter_source_type:
            filters["source_type"] = args.filter_source_type
        if args.filter_entity_type:
            filters["entity_type"] = args.filter_entity_type
        if args.filter_patch:
            filters["patch_version"] = args.filter_patch
        print(query(args.index, args.question, args.top_k, min_score=args.min_score, as_json=args.as_json, rewrite=args.rewrite, filters=filters or None, current_only=getattr(args, "current_only", False), generate=not getattr(args, "no_generate", False)))
    elif args.cmd == "sync":
        if args.watch:
            while True:
                n = sync(args.index)
                print(f"SYNC_OK: {n} chunks at {time.strftime('%Y-%m-%dT%H:%M:%S')}")
                time.sleep(24 * 3600)
        else:
            n = sync(args.index)
            print(f"SYNC_OK: {n} chunks")
    elif args.cmd == "health":
        if getattr(args, "as_json", False):
            import json as _j
            p = pathlib.Path(args.index)
            recs = load_index(p) if p.exists() else []
            print(_j.dumps({"index": str(p), "exists": p.exists(), "records": len(recs), "distinct_patch_versions": len({(r.get("metadata") or {}).get("patch_version") for r in recs if (r.get("metadata") or {}).get("patch_version")}), "ollama_up": _ollama_available(), "opencode_key": opencode_available(), "opencode_model": OPENCODE_MODEL}, indent=2))
        else:
            print(health(args.index))


if __name__ == "__main__":
    main()
