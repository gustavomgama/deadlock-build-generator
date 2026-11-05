"""Evaluation harness for generated Deadlock builds.

Usage:
  python rag\\eval_builds.py [--limit N] [--case NAME] [--timeout S] [--json-out PATH]

Runs buildgen.py for each case, then applies deterministic checks.
"""
import argparse
import json
import pathlib
import subprocess
import sys
import time

RAG_DIR = pathlib.Path(__file__).resolve().parent
ROOT = RAG_DIR
sys.path.insert(0, str(RAG_DIR))
sys.path.insert(0, str(ROOT / "codec"))

import rag  # noqa: E402
import buildgen  # noqa: E402
from decode_build_code import decode_build_code  # noqa: E402

ITEMS = {it["id"]: it for it in json.loads((ROOT / "data" / "items_raw.json").read_text(encoding="utf-8"))}
HEROES = {h["id"]: h for h in json.loads((ROOT / "data" / "heroes_raw.json").read_text(encoding="utf-8"))}
CATEGORIES = set(buildgen.CATEGORIES)
REQUIRED_SECTIONS = [
    "## 1. Inputs",
    "## 2. Generation workflow",
    "## 3. Build identity",
    "## 4. Phase plan",
    "## 5. Item detail",
    "## 6. Ability order",
    "## 7. Situational swaps",
    "## 8. Matchup notes",
    "## 9. Evidence",
    "## 10. Machine payload",
    "## 11. Validation",
    "## 12. Error handling",
    "## 13. Final output",
    "## 14. Curation notes",
]
SHOPABLE = {it["id"] for it in ITEMS.values() if it.get("type") == "upgrade" and it.get("shopable")}

CASES = [
    {"hero": "Infernus", "role": "spirit burn carry", "ability_order": True},
    {"hero": "Haze", "role": "weapon carry", "ability_order": False},
    {"hero": "Abrams", "role": "tank frontline", "ability_order": False},
    {"hero": "Lady Geist", "role": "spirit lifesteal", "ability_order": True},
    {"hero": "Vindicta", "role": "sniper weapon", "ability_order": False},
    {"hero": "McGinnis", "role": "engineer turret", "ability_order": False},
    {"hero": "Dynamo", "role": "support teamfight", "ability_order": True},
    {"hero": "Kelvin", "role": "frost control", "ability_order": False},
    {"hero": "Wraith", "role": "mobility duelist", "ability_order": False},
    {"hero": "Paradox", "role": "time manipulator", "ability_order": True},
    {"hero": "Shiv", "role": "melee assassin", "ability_order": False},
    {"hero": "Ivy", "role": "support tether", "ability_order": False},
]


def run_build(case, timeout):
    cmd = [sys.executable, str(RAG_DIR / "buildgen.py"), case["hero"], "--role", case["role"], "--timeout", str(timeout)]
    if case.get("ability_order"):
        cmd.append("--ability-order")
    t0 = time.time()
    try:
        import os as _os
        env = dict(_os.environ)
        env["PYTHONIOENCODING"] = "utf-8"
        proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, env=env)
    except subprocess.TimeoutExpired:
        return None, f"timeout after {timeout}s", time.time() - t0
    out = (proc.stdout or "") + "\n" + (proc.stderr or "")
    code = None
    for line in reversed((proc.stdout or "").splitlines()):
        s = line.strip()
        if not s:
            continue
        if s.startswith(("Hero:", "Name:", "Categories:", "Ability", "-", "#", "|")):
            continue
        if "VALID" in s:
            continue
        code = s
        break
    return (proc, out, code), None, time.time() - t0


def validate_code(code):
    proc = subprocess.run(
        [sys.executable, str(ROOT / "validate_build.py"), code],
        capture_output=True, text=True, encoding="utf-8",
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    return proc.returncode == 0 and "VALID" in out, out


def check_case(case, timeout):
    result = {"case": f"{case['hero']} ({case['role']})", "hero": case["hero"]}
    run, err, dur = run_build(case, timeout)
    result["duration_s"] = round(dur, 1)
    if err:
        result["error"] = err
        result["score"] = 0.0
        return result
    proc, out, code = run
    result["exit_code"] = proc.returncode
    result["code"] = code
    if proc.returncode != 0:
        result["error"] = (out or "")[:500]
        result["score"] = 0.0
        return result
    if not code:
        result["error"] = "no code parsed"
        result["score"] = 0.0
        return result

    valid, vout = validate_code(code)
    result["validity"] = bool(valid)
    try:
        obj = decode_build_code(code)
    except Exception as e:
        result["error"] = f"decode: {e}"
        result["score"] = 0.0
        return result

    hero = buildgen.find_hero(json.loads((ROOT / "data" / "heroes_raw.json").read_text(encoding="utf-8")), case["hero"])
    hero_id = hero["id"]
    # resolve hero via validate logic
    cats = obj.get("details", {}).get("mod_categories", [])
    cat_names = [c.get("name") for c in cats]
    result["category_validity"] = all(n in CATEGORIES for n in cat_names) and len(cat_names) > 0
    item_ids = [m for c in cats for m in (c.get("mods") or [])]
    result["item_validity"] = all(
        (isinstance(mid, int) and mid in ITEMS and ITEMS[mid].get("type") == "upgrade" and ITEMS[mid].get("shopable"))
        for mid in item_ids
    ) and len(item_ids) > 0
    # ability
    ao = (obj.get("details") or {}).get("ability_order") or {}
    changes = ao.get("currency_changes") or []
    abilities_ok = True
    if changes:
        for e in changes:
            aid = e.get("ability_id")
            it = ITEMS.get(aid)
            if not (it and it.get("type") == "ability"):
                abilities_ok = False
                break
            if hero_id not in (it.get("heroes") or []):
                abilities_ok = False
                break
            if e.get("currency_type") not in (1, 2) or not isinstance(e.get("delta"), int) or e.get("delta", 0) >= 0:
                abilities_ok = False
                break
    result["ability_validity"] = abilities_ok
    # ability order requested handling
    if case.get("ability_order"):
        result["ability_order_present"] = len(changes) > 0
    else:
        result["ability_order_present"] = (len(changes) == 0)
    # template compliance: required payload fields plus every required template section in output
    sections_ok = all(s in (out or "") for s in REQUIRED_SECTIONS)
    result["template_compliance"] = bool(obj.get("name")) and bool(obj.get("description")) and len(cats) > 0 and sections_ok
    # coherence: no tier-1 in late/late-late, <=12 per cat
    coh = True
    for c in cats:
        name = c.get("name")
        if name in ("late", "late-late", "optional spirit-resist", "optional general-resist-sustain"):
            for mid in c.get("mods") or []:
                if ITEMS.get(mid, {}).get("item_tier") == 1:
                    coh = False
        if len(c.get("mods") or []) > 12:
            coh = False
    # duplicate items
    if len(item_ids) != len(set(item_ids)):
        coh = False
    # phase distribution: at least 2 categories
    if len(cats) < 2:
        coh = False
    result["coherence"] = coh

    checks = [
        result["validity"],
        result["category_validity"],
        result["item_validity"],
        result["ability_validity"],
        result["template_compliance"],
        result["coherence"],
    ]
    if case.get("ability_order"):
        checks.append(result["ability_order_present"])
    else:
        checks.append(result["ability_order_present"])
    result["score"] = sum(1 for c in checks if c) / len(checks)
    result["checks"] = {
        "validity": result["validity"],
        "category_validity": result["category_validity"],
        "item_validity": result["item_validity"],
        "ability_validity": result["ability_validity"],
        "template_compliance": result["template_compliance"],
        "coherence": result["coherence"],
        "ability_order": result["ability_order_present"],
    }
    # rubric placeholders
    result["grounding"] = None
    result["originality"] = None
    return result


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--case", default=None)
    ap.add_argument("--timeout", type=float, default=600.0)
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    cases = CASES
    if args.case:
        cases = [c for c in CASES if c["hero"].lower() == args.case.lower()]
    if args.limit:
        cases = cases[: args.limit]

    results = []
    for c in cases:
        print(f"=== {c['hero']} ({c['role']}) ===", flush=True)
        r = check_case(c, args.timeout)
        results.append(r)
        print(f"score={r.get('score')} validity={r.get('validity')} items={r.get('item_validity')} cats={r.get('category_validity')}", flush=True)
        if r.get("error"):
            print(f"ERROR: {r['error']}", flush=True)

    # failure handling check
    try:
        proc = subprocess.run(
            [sys.executable, str(RAG_DIR / "buildgen.py"), "NonexistentHeroXYZ", "--role", "default"],
            capture_output=True, text=True, encoding="utf-8", timeout=60,
        )
        fh_ok = proc.returncode != 0 and bool((proc.stderr or proc.stdout or "").strip())
    except Exception:
        fh_ok = False
    print(f"Failure handling check: {'PASS' if fh_ok else 'FAIL'}")

    total = sum(r.get("score", 0) or 0 for r in results) / max(len(results), 1)
    print(f"\nAverage score: {total:.3f} over {len(results)} cases")
    summary = {"average_score": total, "cases": results, "failure_handling": fh_ok}
    if args.json_out:
        pathlib.Path(args.json_out).write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print(f"Wrote {args.json_out}")
    # also write default
    (RAG_DIR / "eval_builds_scores.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()
