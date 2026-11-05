import json
import sys
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "codec"))

HEROES = {h.get("id"): h for h in json.loads((ROOT / "data" / "heroes_raw.json").read_text(encoding="utf-8"))}
ITEMS = {it.get("id"): it for it in json.loads((ROOT / "data" / "items_raw.json").read_text(encoding="utf-8"))}


def resolve_hero(obj):
    raw = obj.get("hero_id")
    if isinstance(raw, int) and raw >= 1000:
        return raw - 1000
    details = obj.get("details") or {}
    ao = details.get("ability_order") or {}
    changes = ao.get("currency_changes") or []
    heroes = set()
    for e in changes:
        if not isinstance(e, dict):
            continue
        it = ITEMS.get(e.get("ability_id"))
        if it and it.get("type") == "ability":
            for h in (it.get("heroes") or []):
                heroes.add(h)
    if len(heroes) == 1:
        return next(iter(heroes))
    return raw

VALID_CATEGORIES = {
    "early", "early-mid", "mid", "mid-late", "late", "late-late",
    "optional spirit-resist", "optional general-resist-sustain",
}


def _load(path_or_code):
    p = pathlib.Path(path_or_code)
    if p.exists():
        text = p.read_text(encoding="utf-8")
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            pass
        import decode_build_code
        return decode_build_code.decode_build_code(text.strip())
    import decode_build_code
    return decode_build_code.decode_build_code(path_or_code)


def validate(obj):
    errors = []
    warnings = []
    hero_id = resolve_hero(obj)
    if hero_id not in HEROES:
        errors.append(f"unknown hero_id: {hero_id}")
    details = obj.get("details") or {}
    seen = set()
    for cat in details.get("mod_categories") or []:
        name = cat.get("name", "")
        if name not in VALID_CATEGORIES:
            warnings.append(f"unknown category name: {name}")
        mods = cat.get("mods") or []
        if len(mods) > 12:
            warnings.append("more than 12 mods in a category")
        for m in mods:
            mid = m if not isinstance(m, dict) else m.get("id", m.get("mod_id"))
            if mid not in ITEMS:
                errors.append(f"unknown item id: {mid}")
            elif mid in seen:
                warnings.append(f"duplicate item id: {mid}")
            else:
                seen.add(mid)
    ao = details.get("ability_order") or {}
    for e in (ao.get("currency_changes") or []):
        if not isinstance(e, dict):
            continue
        ct = e.get("currency_type")
        if ct not in (1, 2):
            errors.append(f"invalid currency_type: {ct}")
        delta = e.get("delta")
        if not isinstance(delta, int) or delta >= 0:
            errors.append("delta must be negative")
        aid = e.get("ability_id")
        it = ITEMS.get(aid)
        if it is None or it.get("type") != "ability":
            warnings.append(f"unknown ability id: {aid}")
    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("usage: validate_build.py <file-or-code>", file=sys.stderr)
        sys.exit(2)
    obj = _load(sys.argv[1])
    errors, warnings = validate(obj)
    for w in warnings:
        print(f"WARN: {w}")
    if errors:
        for e in errors:
            print(f"ERROR: {e}")
        print("INVALID")
        sys.exit(1)
    print("VALID:")
    sys.exit(0)


if __name__ == "__main__":
    main()
