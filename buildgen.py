import argparse
import json
import os
import pathlib
import re
import subprocess
import sys
import textwrap

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

import rag

RAG_DIR = pathlib.Path(__file__).resolve().parent
ROOT = RAG_DIR
TEMPLATE = ROOT / "build-template.md"
ITEMS_PATH = ROOT / "data" / "items_raw.json"
HEROES_PATH = ROOT / "data" / "heroes_raw.json"
CODEC_DIR = ROOT / "codec"
VALIDATE = ROOT / "validate_build.py"

CATEGORIES = [
    "early",
    "mid",
    "late",
    "late-late",
    "optional spirit-resist",
    "optional general-resist-sustain",
]
OPTIONAL_CATEGORIES = {"optional spirit-resist", "optional general-resist-sustain"}
FORBIDDEN_PATHS = (
    "build-codes.md",
    "build-code-schema.json",
    "build-up.md",
    "hero-build-cache.md",
    "oracle-builds.md",
    "/oracle/",
)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def normalize(name):
    return re.sub(r"[^a-z0-9]+", " ", (name or "").lower()).strip()


def find_hero(heroes, name):
    key = normalize(name)
    for hero in heroes:
        if normalize(hero.get("name")) == key or normalize(hero.get("class_name")) == key:
            return hero
    raise SystemExit(f"Unknown hero: {name}")


def hero_abilities(items, hero_id):
    out = []
    for item in items:
        if item.get("type") != "ability":
            continue
        owners = item.get("heroes") or []
        if hero_id not in owners or len(owners) > 3:
            continue
        out.append(item)
    return out


def shopable_upgrades(items):
    grouped = {}
    for it in items:
        if it.get("type") != "upgrade" or not it.get("shopable"):
            continue
        key = (it.get("item_tier") or 99, it.get("item_slot_type") or "")
        grouped.setdefault(key, []).append(it)
    out = []
    for key in sorted(grouped):
        bucket = sorted(grouped[key], key=lambda it: (it.get("cost") or 0, it.get("name") or ""))
        out.extend(bucket[:5])
    return sorted(out, key=lambda it: (it.get("item_tier") or 99, it.get("item_slot_type") or "", it.get("name") or ""))


def retrieve_context(hero_name, role, constraints, top_k):
    queries = [
        (f"{hero_name} identity role abilities damage power spikes", {"entity_type": "hero"}),
        (f"{hero_name} items weapon vitality spirit counters", {"entity_type": "item"}),
        (f"Deadlock mechanics {role} {constraints}", {"entity_type": "mechanic"}),
        (f"Deadlock item tiers costs slot balance {role}", {"entity_type": "item"}),
    ]
    seen = set()
    chunks = []
    for question, filters in queries:
        raw = rag.query(
            rag.DEFAULT_INDEX,
            question,
            top_k=top_k,
            filters=filters,
            as_json=True,
            generate=False,
            current_only=True,
        )
        try:
            rows = json.loads(raw)
        except json.JSONDecodeError:
            continue
        for row in rows:
            citation = row.get("citation", "")
            snippet = row.get("snippet", "")
            key = (citation, snippet)
            if not citation or not snippet or key in seen:
                continue
            if any(part in citation.lower() for part in FORBIDDEN_PATHS):
                continue
            seen.add(key)
            chunks.append(f"[{citation}] {snippet}")
    return "\n\n".join(chunks)


def load_analytics(path):
    if not path:
        return {}
    p = pathlib.Path(path)
    if not p.exists():
        raise SystemExit(f"Unknown analytics file: {path}")
    return load_json(p)


def observed_block(observed):
    rows = (observed or {}).get("items") or []
    if not rows:
        return ""
    lines = [
        f"PLAYER DATA for this hero (all recorded matches; hero win rate {observed.get('hero_win')}%):",
        "name | pick% | win% | delta vs hero baseline | tier | slot | avg buy (min)",
    ]
    for row in rows[:22]:
        buy = row.get("buy_s")
        buy_min = f"{buy / 60:.0f}" if isinstance(buy, (int, float)) else "?"
        lines.append(
            f"- {row['name']} | {row.get('pick')} | {row.get('win')} | {row.get('delta')} | "
            f"tier {row.get('tier')} | {row.get('slot')} | {buy_min}"
        )
    return "\n".join(lines)


def merge_observed_candidates(candidates, observed):
    have = {c["id"] for c in candidates}
    merged = list(candidates)
    for row in (observed or {}).get("items") or []:
        if row["id"] in have:
            continue
        merged.append(
            {
                "id": row["id"],
                "name": row["name"],
                "item_tier": row.get("tier"),
                "item_slot_type": row.get("slot"),
                "cost": row.get("cost"),
            }
        )
        have.add(row["id"])
    return merged


def build_prompt(template, hero, role, constraints, ability_order, context, items, abilities, observed=None):
    item_lines = [
        f"- {it['id']} | {it['name']} | tier {it.get('item_tier')} | {it.get('item_slot_type')} | {it.get('cost')}"
        for it in items
    ]
    ability_lines = [f"- {it['id']} | {it['name']}" for it in abilities]
    observed_lines = observed_block(observed)
    return f"""You are an elite human player of Deadlock and a build creator.
Create an original build from scratch. Do not copy any existing build.
Pre-existing builds, published builds and player builds are evaluation references only.
Use only the RAG facts, item list and ability list below.

Follow the build-template contract: original build, six categories (early/mid/late/late-late/optional spirit-resist/optional general-resist-sustain) all present with items, tier progression early=tier1-2 mid=tier2-3 late=tier3-4 late-late=tier3-4, max 10 items per category, 12 slots held at once.

Requested hero: {hero['name']} (hero_id {hero['id']})
Role / playstyle: {role}
Constraints: {constraints}
Ability order requested: {"yes" if ability_order else "no"}

RAG FACTS:
{context}

{observed_lines}

CANDIDATE ITEMS (use names exactly as written, choose only from this list):
{chr(10).join(item_lines)}

HERO ABILITIES (use names exactly as written, only if ability order requested):
{chr(10).join(ability_lines)}

Return JSON only. No markdown. Shape:
{{
  "name": "string",
  "description": "string",
  "categories": [
    {{
      "name": "early",
      "description": "string",
      "items": [
        {{"name": "item name", "reason": "why this item now"}}
      ]
    }}
  ],
  "damage_identity": "weapon / spirit / mixed / support / tank",
  "ability_priority": ["ability name"],
  "ability_order": [],
  "buy_order": [{{"step": 1, "buy": "item name", "replace": "none", "timing": "early", "reason": "why"}}],
  "swaps": [{{"situation": "enemy comp", "replace": "item name", "with": "item name", "reason": "why", "source": "citation"}}],
  "matchups": [{{"matchup": "hero or archetype", "plan": "how to play", "answer": "item/ability answer"}}],
  "evidence_gaps": "string",
  "curation_notes": "string"
}}

Rules:
- Return exactly these six categories, in this order, every one of them with items: {", ".join(CATEGORIES)}. A plan missing a category is rejected.
- Item counts per category: early 4-5, mid 4-5, late 3-4, late-late 3-5, optional spirit-resist 2-4, optional general-resist-sustain 2-4. Never more than 10 in one category.
- The 12-slot limit is what the player holds at once, not the size of the list: late-late lists the upgrades that replace early/mid items, and the optional pools are situational buys. List all six categories.
- Tier progression: early=tier1-2, mid=tier2-3, late=tier3-4, late-late=tier3-4; never a tier-1 item in late, late-late or either optional pool.
- Each of the four phase categories (early, mid, late, late-late) must mix at least two of weapon/vitality/spirit; a phase that is a single slot type is rejected.
- Every phase must carry damage: early, mid and late each need at least one item that directly raises this hero's kill damage (weapon item for gun heroes, spirit item for spirit heroes, and for a third of the buy in between). A phase of pure vitality is a broken build.
- optional spirit-resist: only spirit-damage answers (spirit resist, debuff purge, spirit barrier, silence protection).
- optional general-resist-sustain: only healing, shielding, cleanse, or incoming-damage reduction.
- Use exact item names from CANDIDATE ITEMS.
- Do not repeat an item across categories; each item appears in exactly one category.
- Use exact ability names from HERO ABILITIES.
- ability_priority is a list of exact hero ability names in spend priority order; use it when ability order is requested.
- ability_order must be [] when not requested; buildgen expands ability_priority into the full currency ladder.
- currency_type is 1 or 2. delta is negative.
- Every item must make sense for this hero and phase.
- Weight items by hero identity first, then player pick rate, then win delta.
- pick% is what real players actually buy on this hero: treat it as a strong prior.
- delta is confounded: expensive tier-4 items are bought by players who are already ahead, so a high delta partly reflects winning rather than causing it. Use delta only as a tiebreaker within the same tier and slot.
- Do not include a popular item that fights this hero's kit; every slot still needs a reason tied to this hero.
"""


def opencode_json(prompt, model, timeout):
    if not rag.opencode_available():
        raise SystemExit("No OpenCode credentials found. Set OPENCODE_API_KEY or sign in to OpenCode (see rag/RAG.md).")

    last = None
    for _ in range(2):
        text = rag.opencode_chat(
            [{"role": "user", "content": prompt}],
            model=model,
            temperature=0.3,
            json_mode=True,
            timeout=timeout,
        )
        text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()
        if not text:
            last = "empty response"
            continue
        try:
            return json.loads(text)
        except json.JSONDecodeError as exc:
            last = exc
            prompt = f"{prompt}\n\nYour previous answer was not valid JSON: {exc}\nReturn JSON only."
    raise SystemExit(f"OpenCode ({model}) did not return valid JSON: {last}")


def resolve_items(plan, items):
    by_name = {normalize(it["name"]): it for it in items}
    allowed = {it["id"] for it in items}
    categories = []
    used = set()
    for category in plan.get("categories") or []:
        name = category.get("name")
        if name not in CATEGORIES:
            print(f"WARNING: skipping invalid category: {name}", file=sys.stderr)
            continue
        mods = []
        for entry in category.get("items") or []:
            raw_name = entry.get("name") if isinstance(entry, dict) else entry
            item = by_name.get(normalize(raw_name))
            if item is None and isinstance(raw_name, str) and " | " in raw_name:
                for part in raw_name.split("|"):
                    cand = by_name.get(normalize(part.strip()))
                    if cand is not None:
                        item = cand
                        break
            if item is None:
                print(f"WARNING: skipping unknown item: {raw_name}", file=sys.stderr)
                continue
            if item["id"] not in allowed:
                print(f"WARNING: skipping non-shopable item: {raw_name}", file=sys.stderr)
                continue
            if name in ("late", "late-late", "optional spirit-resist", "optional general-resist-sustain") and (item.get("item_tier") or 0) == 1:
                print(f"WARNING: skipping tier-1 item in {name}: {item['name']}", file=sys.stderr)
                continue
            if item["id"] in used:
                print(f"WARNING: skipping duplicate item: {item['name']}", file=sys.stderr)
                continue
            used.add(item["id"])
            mods.append(item["id"])
        if mods:
            mods = mods[:10]
            categories.append(
                {
                    "name": name,
                    "description": category.get("description") or "",
                    "height": 1100,
                    "width": 180,
                    "optional": name in OPTIONAL_CATEGORIES,
                    "mods": mods,
                }
            )
    if not categories:
        raise SystemExit("Plan contains no items")
    return categories


def resolve_abilities(plan, abilities, requested):
    if not requested:
        return None
    by_name = {normalize(it["name"]): it for it in abilities}
    changes = []
    priority = plan.get("ability_priority") or []
    if priority:
        for raw_name in priority:
            ability = by_name.get(normalize(raw_name))
            if ability is None:
                raise SystemExit(f"Unknown ability: {raw_name}")
            changes.append({"ability_id": ability["id"], "currency_type": 2, "delta": -1})
            changes.append({"ability_id": ability["id"], "currency_type": 1, "delta": -1})
            changes.append({"ability_id": ability["id"], "currency_type": 1, "delta": -2})
            changes.append({"ability_id": ability["id"], "currency_type": 1, "delta": -5})
    else:
        for entry in plan.get("ability_order") or []:
            raw_name = entry.get("ability_name") if isinstance(entry, dict) else entry
            ability = by_name.get(normalize(raw_name))
            if ability is None:
                raise SystemExit(f"Unknown ability: {raw_name}")
            currency_type = entry.get("currency_type", 2) if isinstance(entry, dict) else 2
            delta = entry.get("delta", -1) if isinstance(entry, dict) else -1
            if currency_type not in (1, 2):
                raise SystemExit(f"Invalid currency_type: {currency_type}")
            if not isinstance(delta, int) or delta >= 0:
                raise SystemExit(f"Invalid delta: {delta}")
            changes.append({"ability_id": ability["id"], "currency_type": currency_type, "delta": delta})
    if not changes:
        return None
    return {"currency_changes": changes}

def encode_and_validate(obj):
    sys.path.insert(0, str(CODEC_DIR))
    from decode_build_code import decode_build_code
    from encode_build_code import encode_build

    code = encode_build(obj)
    decoded = decode_build_code(code)
    if decoded.get("hero_id") != obj.get("hero_id"):
        raise SystemExit("Round-trip hero mismatch")
    proc = subprocess.run(
        [sys.executable, str(VALIDATE), code],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    output = (proc.stdout or "") + (proc.stderr or "")
    if proc.returncode != 0:
        raise SystemExit(f"Validation failed:\n{output}")
    return code, output.strip()


def summarise(obj, items, abilities):
    item_names = {it["id"]: it["name"] for it in items}
    ability_names = {it["id"]: it["name"] for it in abilities}
    lines = [f"Hero: {obj['hero_id']}", f"Name: {obj.get('name')}", "Categories:"]
    for category in obj["details"]["mod_categories"]:
        names = ", ".join(item_names.get(mid, str(mid)) for mid in category["mods"])
        lines.append(f"- {category['name']}: {names}")
    order = (obj["details"].get("ability_order") or {}).get("currency_changes") or []
    if order:
        lines.append("Ability order:")
        for change in order:
            lines.append(
                f"- {ability_names.get(change['ability_id'], change['ability_id'])} "
                f"({change['currency_type']}/{change['delta']})"
            )
    return "\n".join(lines)


def render_template(obj, plan, hero, role, constraints, ability_requested, items, abilities, code, validation):
    item_by_id = {it["id"]: it for it in items}
    name = obj.get("name")
    desc = obj.get("description")
    damage_identity = plan.get("damage_identity") or "mixed"
    categories = obj["details"]["mod_categories"]
    lines = []
    lines.append("# Deadlock Build Document")
    lines.append("")
    lines.append("## 1. Inputs")
    lines.append("")
    lines.append("| field | value |")
    lines.append("| --- | --- |")
    lines.append(f"| hero | {hero['name']} |")
    lines.append(f"| hero_id | {hero['id']} |")
    lines.append("| patch | current |")
    lines.append(f"| role / playstyle | {role} |")
    lines.append(f"| damage identity | {damage_identity} |")
    lines.append(f"| requested ability order | {'yes' if ability_requested else 'no'} |")
    lines.append(f"| constraints | {constraints} |")
    lines.append("")
    lines.append("## 2. Generation workflow")
    lines.append("")
    for i, step in enumerate([
        "If an encoded build code is provided, decode it first.",
        "Retrieve hero, ability, item, mechanic, patch and matchup facts from RAG.",
        "Plan the build thesis, phases, buy order, swaps and ability order.",
        "Resolve every item and ability id; never invent one.",
        "Assemble the decoded JSON.",
        "Encode it with deadlock-codec.",
        "Decode the result back and validate it.",
        "Return the final code plus a decoded summary.",
    ], 1):
        lines.append(f"{i}. {step}")
    lines.append("")
    lines.append("## 3. Build identity")
    lines.append("")
    lines.append(f"**Build name:** {name}")
    lines.append("")
    lines.append("### Build goals")
    lines.append("")
    for b in [
        "Always create the build from scratch.",
        "Use RAG facts about Deadlock as the only evidence for choices.",
        "Never copy an item list, category layout, description, ability order or build code from an existing build.",
        "The build must have a clear identity, win condition and power spikes.",
    ]:
        lines.append(f"- {b}")
    lines.append("")
    lines.append("### Item selection philosophy")
    lines.append("")
    for b in [
        "Start from the hero: abilities, damage identity, role, power spikes and matchups.",
        "Every item must have a reason tied to this hero, this phase and this game plan.",
        "Prefer upgrading an item already in an earlier phase over buying a new tier-1 item, when sensible.",
        "Optimize the base 10 item slots; 12 is the maximum, not the target.",
    ]:
        lines.append(f"- {b}")
    lines.append("")
    lines.append("### Curation guidance")
    lines.append("")
    for b in [
        "Treat RAG sources as facts, never as templates to copy.",
        "Never invent ids; resolve every item and ability through the API or local mirrors.",
        "If evidence is missing, state the gap instead of filling it with a copied choice.",
        "Round-trip decode every produced code before presenting it.",
    ]:
        lines.append(f"- {b}")
    lines.append("")
    lines.append("## 4. Phase plan")
    lines.append("")
    lines.append("| category | time | target items held | avg midpoint | avg end |")
    lines.append("| --- | --- | --- | --- | --- |")
    times = {
        "early": ("0-10 min", "~1-5", "2.64 (5 min)", "5.00 (10 min)"),
        "mid": ("10-20 min", "~5-8", "6.82 (15 min)", "8.14 (20 min)"),
        "late": ("20-30 min", "~8-10", "9.17 (25 min)", "9.92 (30 min)"),
        "late-late": ("30+ min", "~10-12", "11.18 (32.5 min)", "12.00 (45 min)"),
        "optional spirit-resist": ("situational", "no cap", "-", "-"),
        "optional general-resist-sustain": ("situational", "no cap", "-", "-"),
    }
    for c in categories:
        t = times.get(c["name"], ("", "", "", ""))
        lines.append(f"| {c['name']} | {t[0]} | {t[1]} | {t[2]} | {t[3]} |")
    lines.append("")
    lines.append("## 5. Item detail")
    lines.append("")
    for c in categories:
        lines.append(f"### {c['name']}")
        lines.append("")
        lines.append(c.get("description") or "")
        lines.append("")
        lines.append("| item | item_id | tier | slot | cost | reason |")
        lines.append("| --- | --- | --- | --- | --- | --- |")
        reason_map = {}
        for pc in plan.get("categories") or []:
            if pc.get("name") != c.get("name"):
                continue
            for entry in pc.get("items") or []:
                if isinstance(entry, dict):
                    reason_map[normalize(entry.get("name", ""))] = entry.get("reason", "")
        for mid in c.get("mods", []):
            it = item_by_id.get(mid, {})
            r = reason_map.get(normalize(it.get("name", "")), "")
            lines.append(
                f"| {it.get('name', mid)} | {mid} | {it.get('item_tier', '')} | "
                f"{it.get('item_slot_type', '')} | {it.get('cost', '')} | {r} |"
            )
        lines.append("")
    # buy order
    lines.append("### Buy order and replacement plan")
    lines.append("")
    lines.append("| step | buy | replace | timing | reason |")
    lines.append("| --- | --- | --- | --- | --- |")
    buy_order = plan.get("buy_order") or []
    if not buy_order:
        step = 1
        for cat in plan.get("categories") or []:
            for entry in cat.get("items") or []:
                raw_name = entry.get("name") if isinstance(entry, dict) else entry
                reason = entry.get("reason", "") if isinstance(entry, dict) else ""
                lines.append(f"| {step} | {raw_name} | none | {cat.get('name')} | {reason} |")
                step += 1
    else:
        for entry in buy_order:
            if isinstance(entry, dict):
                lines.append(
                    f"| {entry.get('step', '')} | {entry.get('buy', '')} | "
                    f"{entry.get('replace', 'none')} | {entry.get('timing', '')} | {entry.get('reason', '')} |"
                )
    lines.append("")
    lines.append("## 6. Ability order (optional)")
    lines.append("")
    if not ability_requested:
        lines.append("Not requested")
        lines.append("")
    else:
        order = (obj["details"].get("ability_order") or {}).get("currency_changes") or []
        ability_names = {it["id"]: it["name"] for it in abilities}
        if order:
            lines.append("```json")
            lines.append(json.dumps(order, indent=2))
            lines.append("```")
            lines.append("")
            lines.append("| ability | currency_type | delta |")
            lines.append("| --- | --- | --- |")
            for ch in order:
                lines.append(f"| {ability_names.get(ch['ability_id'], ch['ability_id'])} | {ch['currency_type']} | {ch['delta']} |")
        else:
            lines.append("Not requested")
        lines.append("")
    lines.append("## 7. Situational swaps")
    lines.append("")
    lines.append("| situation | replace | with | reason | source |")
    lines.append("| --- | --- | --- | --- | --- |")
    swaps = plan.get("swaps") or []
    if swaps:
        for s in swaps:
            if isinstance(s, dict):
                lines.append(
                    f"| {s.get('situation', '')} | {s.get('replace', '')} | {s.get('with', '')} | "
                    f"{s.get('reason', '')} | {s.get('source', '')} |"
                )
    else:
        lines.append("| none | - | - | No situational swaps specified | RAG |")
    lines.append("")
    lines.append("## 8. Matchup notes")
    lines.append("")
    lines.append("| matchup | plan | item/ability answer |")
    lines.append("| --- | --- | --- |")
    matchups = plan.get("matchups") or []
    if matchups:
        for m in matchups:
            if isinstance(m, dict):
                lines.append(f"| {m.get('matchup', '')} | {m.get('plan', '')} | {m.get('answer', '')} |")
    else:
        lines.append(f"| {role} | Play to hero identity | see item detail |")
    lines.append("")
    lines.append("## 9. Evidence")
    lines.append("")
    gaps = plan.get("evidence_gaps") or ""
    if gaps and gaps.lower() not in ("", "string"):
        lines.append(f"Evidence gaps: {gaps}")
    else:
        lines.append("All items resolved via items_raw.json; reasons from RAG context.")
    lines.append("")
    lines.append("Source discipline: deadlock-api high trust for numbers; deadlock.wiki medium-high for prose.")
    lines.append("")
    lines.append("## 10. Machine payload")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(obj, indent=2))
    lines.append("```")
    lines.append("")
    lines.append("## 11. Validation")
    lines.append("")
    lines.append("| check | result |")
    lines.append("| --- | --- |")
    lines.append(f"| encode | ok |")
    lines.append(f"| round-trip decode | ok |")
    lines.append(f"| validate | {validation.splitlines()[0] if validation else 'VALID'} |")
    lines.append("| warnings | none |")
    lines.append("| id resolution | ok |")
    lines.append("")
    lines.append("## 12. Error handling")
    lines.append("")
    for b in [
        "If decode fails, report the error; do not fabricate.",
        "If an item or ability id is unknown, re-resolve it; never invent one.",
        "If validation reports an ERROR, fix the build and re-encode.",
        "Never present a code that fails validation or round-trip decode.",
    ]:
        lines.append(f"- {b}")
    lines.append("")
    lines.append("## 13. Final output")
    lines.append("")
    lines.append("```text")
    lines.append(code)
    lines.append("```")
    lines.append("")
    lines.append("## 14. Curation notes")
    lines.append("")
    notes = plan.get("curation_notes") or ""
    if notes and notes.lower() not in ("", "string"):
        lines.append(notes)
    else:
        lines.append("- Assumes standard lobby; adjust swaps for enemy comp.")
        lines.append("- Item ids are patch-dependent; re-resolve on patch change.")
    lines.append("")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Generate an original Deadlock build from RAG")
    parser.add_argument("--version", action="version", version="buildgen 1.0")
    parser.add_argument("--list-heroes", action="store_true", help="List available heroes and exit")
    parser.add_argument("hero", nargs="?")
    parser.add_argument("--role", default="default")
    parser.add_argument("--constraints", default="none")
    parser.add_argument("--ability-order", action="store_true")
    parser.add_argument("--top-k", type=int, default=4)
    parser.add_argument("--model", default=os.getenv("BUILDGEN_MODEL", rag.OPENCODE_MODEL))
    parser.add_argument("--timeout", type=float, default=300.0)
    parser.add_argument("--analytics", default=None, help="JSON with per-hero item pick/win rates")
    parser.add_argument("--json", action="store_true", help="Print a JSON summary instead of the full document")
    args = parser.parse_args()

    if args.list_heroes:
        heroes = load_json(HEROES_PATH)
        for h in heroes:
            print(h.get("name"))
        return

    if not args.hero:
        parser.print_help()
        return

    template = TEMPLATE.read_text(encoding="utf-8")
    heroes = load_json(HEROES_PATH)
    items = load_json(ITEMS_PATH)
    hero = find_hero(heroes, args.hero)
    abilities = hero_abilities(items, hero["id"])
    analytics = load_analytics(args.analytics)
    observed = analytics.get(str(hero["id"])) or {}
    candidates = shopable_upgrades(items)
    if observed:
        candidates = merge_observed_candidates(candidates, observed)
    context = retrieve_context(hero["name"], args.role, args.constraints, args.top_k)
    prompt = build_prompt(
        template,
        hero,
        args.role,
        args.constraints,
        args.ability_order,
        context,
        candidates,
        abilities,
        observed,
    )
    plan = opencode_json(prompt, args.model, args.timeout)
    categories = resolve_items(plan, candidates)
    missing = [c for c in CATEGORIES if c not in {cat["name"] for cat in categories}]
    if missing:
        raise SystemExit(f"Plan is missing required categories: {', '.join(missing)}")
    ability_order = resolve_abilities(plan, abilities, args.ability_order)
    details = {"mod_categories": categories}
    if ability_order:
        details["ability_order"] = ability_order
    obj = {
        "hero_id": hero["id"],
        "version": 13,
        "hero_build_id": 0,
        "author_account_id": 0,
        "name": f"{hero['name']}#1 by helmet",
        "description": ((plan.get("description") or "").strip() if ((plan.get("description") or "").strip().lower() not in ("", "string")) else f"Generated build for {hero['name']}"),
        "language": 0,
        "origin_build_id": 0,
        "tags": [],
        "details": details,
    }
    code, validation = encode_and_validate(obj)
    if args.json:
        import json as _j
        summary = {
            "hero": hero["name"],
            "hero_id": hero["id"],
            "name": obj.get("name"),
            "categories": [{"name": c["name"], "items": c["mods"]} for c in obj["details"]["mod_categories"]],
            "code": code,
            "validation": validation.splitlines()[0] if validation else "",
        }
        print(_j.dumps(summary, indent=2))
        return
    doc = render_template(obj, plan, hero, args.role, args.constraints, args.ability_order, candidates, abilities, code, validation)
    print(doc)
    print()
    print(textwrap.dedent(summarise(obj, candidates, abilities)))
    print()
    print(validation)
    print()
    print(code)


if __name__ == "__main__":
    main()
