# Deadlock Build Document Template

> Generated from RAG corpus facts only. Do not retrieve or copy existing builds,
> oracle builds, published builds or player builds. Those are evaluation references,
> never generation sources.

## 1. Inputs

| field | value |
| --- | --- |
| hero | {{hero_name}} |
| hero_id | {{hero_id}} |
| patch | {{patch_version}} |
| role / playstyle | {{role_or_playstyle}} |
| damage identity | {{weapon / spirit / mixed / support / tank}} |
| requested ability order | {{yes / no}} |
| constraints | {{constraints_or_none}} |

## 2. Generation workflow

1. If an encoded build code is provided, decode it first.
2. Retrieve hero, ability, item, mechanic, patch and matchup facts from RAG.
3. Plan the build thesis, phases, buy order, swaps and ability order.
4. Resolve every item and ability id; never invent one.
5. Assemble the decoded JSON.
6. Encode it with `deadlock-codec`.
7. Decode the result back and validate it.
8. Return the final code plus a decoded summary.

## 3. Build identity

**Build name:** {{<hero_name>#build_number by helmet}}

This section is the first thing the RAG reads before creating a build. Follow it before retrieving, planning or writing.

### Build goals

- Always create the build from scratch.
- Use RAG facts about Deadlock as the only evidence for choices.
- Pre-existing builds, oracle builds, published builds and player builds are evaluation references only.
- Never copy an item list, category layout, description, ability order or build code from an existing build.
- Never present an existing build as a new build.
- The build must have a clear identity, win condition and power spikes.
- Buy order, replace order and full-slot replacement matter as much as the final item list.
- The result must be valid, encodable and playable.

### Item selection philosophy

- Start from the hero: abilities, damage identity, role, power spikes and matchups.
- Every item must have a reason tied to this hero, this phase and this game plan.
- Popularity, win rate and meta are weights, not the deciding factor.
- Do not anchor on what other players buy. Build the item path from the hero's needs.
- Prefer upgrading an item already in an earlier phase over buying a new tier-1 item, when sensible.
- Optimize the base 10 item slots; 12 is the maximum, not the target.
- A late-game upgrade can arrive when all 12 slots are full — plan what it replaces.

### Curation guidance

- Treat RAG sources as facts, never as templates to copy.
- Do not retrieve build documents, oracle builds, published builds or player builds during generation.
- Compare against existing builds only after generation, and only as evaluation.
- Weight items by hero identity, then win rate and popularity.
- Balance weapon / vitality / spirit within each phase; avoid single-slot spam.
- Use real analytics for ability order when available.
- Never invent ids; resolve every item and ability through the API or local mirrors.
- If evidence is missing, state the gap instead of filling it with a copied choice.
- Round-trip decode every produced code before presenting it.

## 4. Phase plan

Use only these category names. Only include categories with items.

| category | time | target items held | avg midpoint | avg end |
| --- | --- | --- | --- | --- |
| early | 0-10 min | ~1-5 | 2.64 (5 min) | 5.00 (10 min) |
| mid | 10-20 min | ~5-8 | 6.82 (15 min) | 8.14 (20 min) |
| late | 20-30 min | ~8-10 | 9.17 (25 min) | 9.92 (30 min) |
| late-late | 30+ min | ~10-12 | 11.18 (32.5 min) | 12.00 (45 min) |
| optional spirit-resist | situational | no cap | — | — |
| optional general-resist-sustain | situational | no cap | — | — |

Rules:

- Max 12 items per category; warn above 10.
- Keep weapon / vitality / spirit balance within each phase.
- Prefer upgrades of earlier items over new tier-1 items when sensible.
- The two optional categories are precise situational pools, not fixed buy orders.
- Tier progression: early = tier 1-2; mid = tier 2-3; late = tier 3-4; late-late = tier 3-4.
- Avoid tier-1 items in late and late-late categories.
- Players buy roughly 1 item per minute on average; ten items per category is not ideal.

## 5. Item detail

Repeat this table per category.

### {{category_name}}

{{category_description}}

| item | item_id | tier | slot | cost | upgrade path |
| --- | --- | --- | --- | --- | --- |
| {{item_name}} | {{item_id}} | {{tier}} | {{weapon/vitality/spirit}} | {{cost}} | {{built_from / builds_into}} |

### Buy order and replacement plan

Buy order and replace order are part of the build, not an afterthought.

| step | buy | replace | timing | reason |
| --- | --- | --- | --- | --- |
| {{n}} | {{item_name}} | {{item_name_or_none}} | {{minute_or_phase}} | {{why_this_now}} |

## 6. Ability order (optional)

Include only when requested. If omitted, write: `Not requested`.

`details.ability_order.currency_changes` is one entry per spend, in the order the player makes it.

| `currency_type` | `delta` | meaning |
| --- | --- | --- |
| `2` | `-1` | unlock one ability (one Ability Unlock per ability) |
| `1` | `-1` | first upgrade tier: 1 Ability Point |
| `1` | `-2` | second upgrade tier: 2 Ability Points |
| `1` | `-5` | third upgrade tier: 5 Ability Points |

A fully maxed hero is 16 entries: 4 unlocks plus 4 x `-1`, 4 x `-2` and 4 x `-5`.

Example shape for one fully maxed ability:

```json
[
  { "ability_id": 0, "currency_type": 2, "delta": -1 },
  { "ability_id": 0, "currency_type": 1, "delta": -1 },
  { "ability_id": 0, "currency_type": 1, "delta": -2 },
  { "ability_id": 0, "currency_type": 1, "delta": -5 }
]
```

Ability-order rules:

- `ability_id` is an ability id (`type: ability`), not an item id.
- `currency_type` must be `1` or `2`.
- `delta` must be a negative integer; `0` and positive values are errors.
- Spend order may be grouped per ability or tier by tier; both shapes import.
- A build may stop at any tier; maxing everything is valid but not required.

## 7. Situational swaps

| situation | replace | with | reason | source |
| --- | --- | --- | --- | --- |
| {{enemy_comp_or_state}} | {{item_name}} | {{item_name}} | {{reason}} | {{citation}} |

## 8. Matchup notes

| matchup | plan | item/ability answer |
| --- | --- | --- |
| {{hero_or_archetype}} | {{how_to_play}} | {{answer}} |

## 9. Evidence

Every item, ability and numeric claim needs a source, but the final answer does not need to expose the full evidence table.

If evidence is missing, state the gap. Never invent a fact, item, ability, id or number.

Source discipline:

- deadlock-api: high trust for structured game data and numbers.
- deadlock.wiki: medium-high trust for prose, mechanics and interactions.
- Prefer API data for numeric values. Record discrepancies instead of merging them.
- Do not use existing builds, oracle builds, published builds or player builds as evidence for originality.

## 10. Machine payload

This is the object the codec encodes. Fill it from the validated tables above.

```json
{
  "hero_id": 0,
  "version": 13,
  "hero_build_id": 0,
  "author_account_id": 0,
  "name": "{{build_name}}",
  "description": "{{build_description}}",
  "language": 0,
  "origin_build_id": 0,
  "tags": [],
  "details": {
    "mod_categories": [
      {
        "name": "early",
        "description": "{{description}}",
        "height": 1100,
        "width": 180,
        "optional": false,
        "mods": [0]
      }
    ],
    "ability_order": {
      "currency_changes": [
        {
          "ability_id": 0,
          "currency_type": 2,
          "delta": -1
        }
      ]
    }
  }
}
```

Category object:

```json
{
  "name": "early",
  "description": "string",
  "height": 1100,
  "width": 180,
  "optional": false,
  "mods": [0]
}
```

Payload rules:

- Use only the six category names in section 4.
- `mods` entries are item ids (`type: upgrade`).
- `ability_id` entries are ability ids (`type: ability`).
- `hero_id` is the real hero id for a normal build.
- `version` is the edit counter; local client files use `13`.
- `hero_build_id` and `author_account_id` are build metadata; keep them stable for edits.
- `height` and `width` are cosmetic; this repository uses `1100 x 180`.
- `optional` is cosmetic; set `true` on the two optional categories.
- Omit `ability_order` entirely when not requested.
- Do not set `field_9` or `field_13`; their meaning is unknown.
- Item ids are patch-dependent; resolve them at generation time, never copy an old id.

### ID resolution

- Hero ids: `heroes_raw.json` or `list_heroes`.
- Item ids: `items_raw.json` or `list_items` with `type: upgrade`.
- Ability ids: `items_raw.json` or `list_items` with `type: ability`.

### In-game import rules

- A build code is `base64(zstd(protobuf))`; raw uncompressed protobuf is also accepted.
- The client rebuilds category boxes from the item ids inside each category. The items carry the build.
- Category names are labels; unknown names are stored and re-imported unchanged.
- Ability order is read as a timeline of spends, not as a final skill tree.
- `height`, `width` and `optional` are cosmetic; the client keeps them but does not require specific values.
- The encoder writes category fields 1-6 only. Per-item `annotation`, `sell_priority` and `imbue_target_ability_id` are dropped.
- `field_9` and `field_13` are copied through untouched.

## 11. Validation

Run:

```powershell
python codec\encode_build_code.py <build.json>
python codec\decode_build_code.py "<code>"
python C:\Users\helmet\dev\deadlock\validate_build.py "<code>"
```

Import bar — every produced code must clear all four:

1. Encode the build JSON.
2. Decode the returned code.
3. Validate it; `validate_build.py` must print `VALID` with 0 errors.
4. Resolve every id: each `mods` entry as an item (`type: upgrade`), each `ability_id` as an ability (`type: ability`).

| check | result |
| --- | --- |
| encode | {{ok / error}} |
| round-trip decode | {{ok / error}} |
| validate | {{VALID / errors}} |
| warnings | {{list}} |
| id resolution | {{ok / error}} |

## 12. Error handling

- If decode fails, report the error; do not fabricate.
- If an item or ability id is unknown, re-resolve it; never invent one.
- If validation reports an ERROR, fix the build and re-encode.
- Never present a code that fails validation or round-trip decode.
- If evidence is missing, state the gap instead of filling it.

## 13. Final output

```text
{{encoded_build_code}}
```

Always return the final encoded build code plus a decoded summary: hero, categories with item names, and ability order if present.

## 14. Curation notes

- What this build assumes about the player and the lobby.
- What is still uncertain.
- What changes if the patch changes.
