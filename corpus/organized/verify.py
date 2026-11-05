#!/usr/bin/env python3
import os, json, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
MANIFEST = os.path.join(ROOT, "manifest.json")

HERO_KEYS = ("api_id:", "api_class_name:", "api_name:")
CORPUS_KEYS = ("title:", "pageid:", "source:")


def keys_for(rel):
    return HERO_KEYS if rel.startswith(("heroes/", "items/")) else CORPUS_KEYS


def kebab(name):
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*\.md", name))


def corpus_files():
    out = []
    for dp, dn, fns in os.walk(ROOT):
        for fn in fns:
            if fn.endswith(".md") and fn != "TEMPLATE.md":
                out.append(os.path.relpath(os.path.join(dp, fn), ROOT).replace(os.sep, "/"))
    return sorted(out)


def write_manifest(files):
    with open(MANIFEST, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"files": files}, f, indent=2, ensure_ascii=False)
        f.write("\n")


def main():
    actual = corpus_files()
    listed = []
    if os.path.exists(MANIFEST):
        with open(MANIFEST, encoding="utf-8") as f:
            manifest = json.load(f)
        listed = manifest.get("files") if isinstance(manifest, dict) else manifest
    assert isinstance(listed, list), "manifest must list files"
    if "--sync" in sys.argv:
        write_manifest(actual)
    else:
        deleted = sorted(set(listed) - set(actual))
        assert not deleted, f"corpus files removed: {deleted[:5]}"
        if sorted(listed) != actual:
            write_manifest(actual)
            print(f"SYNCED manifest to {len(actual)} files", file=sys.stderr)
    for rel in actual:
        full = os.path.join(ROOT, rel)
        assert os.path.getsize(full) > 0, f"empty file: {rel}"
        raw = open(full, "rb").read()
        assert b"\r\n" not in raw, f"CRLF line endings: {rel}"
        assert raw.startswith(b"---\n"), f"missing frontmatter: {rel}"
        end = raw.find(b"\n---\n", 3)
        assert end != -1, f"unterminated frontmatter: {rel}"
        assert kebab(os.path.basename(rel)), f"bad filename: {rel}"
        fm = raw[4:end].decode("utf-8")
        for key in keys_for(rel):
            assert key in fm, f"missing {key} in {rel}"
    assert not os.path.exists(os.path.join(ROOT, "liquipedia")), "liquipedia folder present"
    for c in ("heroes", "items", "mechanics"):
        assert os.path.isdir(os.path.join(ROOT, c)), f"missing folder {c}"
    for name in os.listdir(os.path.join(ROOT, "heroes")):
        assert not os.path.isdir(os.path.join(ROOT, "heroes", name)), f"hero subfolder: {name}"
    print("VERIFY_OK")


if __name__ == "__main__":
    main()
