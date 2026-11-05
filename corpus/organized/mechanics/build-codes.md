---
title: "Deadlock Build Codes"
pageid: 0
source: deadlock-api
---

A Deadlock build code is the game's own build payload: `base64(zstd(protobuf))`. The JSON below is the shape that the game client accepts, that `decode_build_code.py` produces and that `encode_build_code.py` writes back. This page is the canonical copy of those rules; the Deadlock-Oracle agent file (`.opencode/agents/deadlock-oracle.md`) and the `/build` command (`.opencode/commands/build.md`) carry the same rules inline and cite this path. The machine-readable companion of this page is [build-code-schema.json](build-code-schema.json): a JSON Schema for the decoded build object, so a tool can validate a build without parsing prose.

Every rule on this page is backed by a file, a script run, or an API response. The [Claims and evidence](#claims-and-evidence) table lists each one with its confidence, and [Unverified and inferred](#unverified-and-inferred) lists what could not be proven. Discovered 2026-10-20.

Sources used:

- `decode_build_code.py` - decoder; defines the JSON field names and the protobuf field numbers.
- `encode_build_code.py` - encoder; writes the same field numbers.
- `validate_build.py` - validator; defines the accepted category names, the `currency_type` set and the `delta` rule.
- `codec-site/lib/deadlock_codec.rb` - independent Ruby implementation of the same codec.
- `C:/Program Files (x86)/Steam/userdata/85560017/1422450/remote/cfg/cached_hero_builds.kv3` - the client's own build cache (read-only, never written to).
- `build.bin`, `build2.bin`, `user_build.bin` - build payloads produced by the local game client.
- deadlock-api REST `/v1/builds` and the deadlock-api MCP (`list_items`, `list_heroes`) - published builds and item/ability id tables.

## What a build code is

1. `base64` decode the code. Published codes decode to bytes starting with `28 b5 2f fd` - the zstd frame magic (verified on the codes in `codec-site/test/fixtures/files/builds_all_heroes.md`).
2. If the zstd magic is present, decompress it. `decode_build_code.py` does this with `zstandard`; `codec-site/lib/deadlock_codec.rb` does it with `zstd-ruby` (`ZSTD_MAGIC`).
3. Parse the result as a protobuf. Raw, uncompressed protobuf payloads are also accepted: `build.bin` starts with `08 06 10 0d` (field 1 = hero_id 6, field 2 = version 13).

`encode_build_code.py` always writes `base64(zstd(protobuf))`, which is what the client produces.

## Top-level JSON schema (decoded build)

| JSON key | protobuf field | type | meaning |
| --- | --- | --- | --- |
| `hero_id` | 1 | varint | Hero the build is for. Resolve with `list_heroes`; `validate_build.py` errors on an unknown id. |
| `version` | 2 | varint | Edit counter of the build. The local client files use `13`; published builds use 90-94. |
| `hero_build_id` | 3 | varint | Id of this build itself. In all three local client files it equals the local Steam account id (`85560017`); in published builds it is the per-hero build number (for example `1007`). |
| `author_account_id` | 4 | varint | Steam account that owns the build (`85560017`'s build files carry `1792216466`). |
| `name` | 5 | string | Build title. `validate_build.py` warns when it is empty. |
| `description` | 6 | string | Free-text description. |
| `language` | 7 | varint | `0` (English) in every sample seen. |
| `origin_build_id` | 8 | varint | Build this one was copied from. |
| `field_9` | 9 | varint | Meaning unknown in normal builds (0 or 2 in this repo's builds). On copies of other builds it holds the raw `hero_id` (field 1) of the build this one was copied from: `1` for a copy of an Infernus build, `1001` for a copy of the Default Infernus Build, `10` for a copy of build 10. `origin_build_id` (field 8) stays `0` on these copies, so field 9 is a separate "source build id" used to track the copy chain. Not tested in-game. |
| `details` | 10 | message | Holds `mod_categories` and `ability_order`. |
| `tags` | 11 | repeated varint | Ability ids tagged on the build (a published Seven build carries `539192269, 2061574352, 1074714947`). |
| `field_13` | 13 | varint | Meaning unknown; not set by this repo. |

Field numbers come from `decode_build_code.py` (`get_int`/`get_str` on the parsed message) and `encode_build_code.py` (`encode_field`), and are mirrored by `codec-site/lib/deadlock_codec.rb` (`build_hash`, `encode_top`).

```json
{
  "hero_id": 2,
  "version": 91,
  "hero_build_id": 1007,
  "author_account_id": 464664477,
  "name": "Seven Ultimate Build V1.5 02.05",
  "description": "",
  "language": 0,
  "origin_build_id": 1007,
  "tags": [],
  "details": {
    "mod_categories": [],
    "ability_order": { "currency_changes": [] }
  }
}
```

## details.mod_categories (item categories)

`details.mod_categories` is an ordered list of categories. Each category is one object; the codec reads it as protobuf field 1 of `details`.

| Key | protobuf field | type | meaning |
| --- | --- | --- | --- |
| `mods` | 1 (repeated) | message | One entry per item: field 1 is the **item id**. |
| `name` | 2 | string | Category label shown in the client. |
| `description` | 3 | string | Optional note shown under the label. |
| `height` | 4 | float32 | Cosmetic layout height. |
| `width` | 5 | float32 | Cosmetic layout width. |
| `optional` | 6 | varint (bool) | Marks the category as optional in the client. |

```json
{
  "name": "early",
  "description": "",
  "height": 1100.0,
  "width": 180.0,
  "optional": false,
  "mods": [668299740, 4104549924, 1548066885]
}
```

`mods` entries carry more fields in the live game (`annotation`, `required_flex_slots`, `sell_priority`, `imbue_target_ability_id`, per the `BuildHeroDetailsCategoryAbility` schema in `deadlock-api/api-1.json`). The local codec only writes field 1, so those extras are dropped on a round trip through `encode_build_code.py`.

`height` and `width` are cosmetic: 40 published builds contain 171 different `(height, width)` pairs, and the client's own files use `861.75 x 172.5`, `807.0 x 205.5` and `840.75 x 192.0`. The value `1100 x 180` used by this repo's generated builds is a convention, not a client requirement.

`validate_build.py` rules: unknown hero id, unknown item id, non-int mod id, or more than 12 mods in a category are errors or warnings as coded there; a category with more than 12 mods warns, an item repeated across categories warns.

## Category names the client accepts

- **The client's own defaults** are localisation keys: `#Citadel_HeroBuilds_EarlyGame`, `#Citadel_HeroBuilds_MidGame`, `#Citadel_HeroBuilds_LateGame`, and a fourth default category literally named `Category 4`. Verified by decoding the three client-produced payloads `build.bin`, `build2.bin` and `user_build.bin` in this repo.
- **Names are otherwise free-form labels.** 40 published builds (REST `/v1/builds?limit=40`) use `Optional`, `Laning`, `Jungling`, `Late`, `Farm`, `Mid - Late`, `500 Weapon`, `500 Vitality`, `500 Spirit`, `1250 Weapon`, `1250 Vitality`, `1250 Spirit`, `3000 Weapon`, `3000 Vitality`, `3000 Spirit`, `6200 Weapon`, `6200 Vitality`, `6200 Spirit`, `Super Early Game`, `Early Game`, `Mid Game`, `Priority Late Game Picks`, `Spirit Armors`, `Check Out The Annotations!`, `Active play`. None of them uses the `#Citadel_HeroBuilds_*` key form, so a plain label imports.
- **The client's own category names** live in `cached_hero_builds.kv3`, which `decode_kv3.py` now parses: the client ships the localisation keys `#Citadel_HeroBuilds_Early`, `#Citadel_HeroBuilds_Mid`, `#Citadel_HeroBuilds_Late`, `#Citadel_HeroBuilds_EarlyGame`, `#Citadel_HeroBuilds_MidGame`, `#Citadel_HeroBuilds_LateGame` and `#Citadel_HeroBuilds_Lane`, plus the plain phase names `early`, `early-mid`, `mid`, `mid-late`, `late`, `late-late`, `optional spirit-resist`, `optional general-resist-sustain`. See [hero-build-cache.md](hero-build-cache.md) for the recovered structure.
- **This repo's validator** accepts a fixed set (`validate_build.py`): `early`, `early-mid`, `mid`, `mid-late`, `late`, `late-late`, `optional spirit-resist`, `optional general-resist-sustain`. A name outside that set is a **warning**, never an error.

Rule for generated builds: use a label from the validator's list so the code validates cleanly, and use the client's `#Citadel_HeroBuilds_EarlyGame` / `_MidGame` / `_LateGame` keys only when the build should line up with the panels the client creates by default. The 43 generated builds in `codec-site/test/fixtures/files/builds_all_heroes.md` currently use `early`, `early-mid`, `#Citadel_HeroBuilds_Mid`, `mid-late`, `late`, `late-late`, `optional spirit-resist`, `optional general-resist-sustain` - a mix of both forms, which the client accepts but which is not symmetric.

## details.ability_order and the currency_type delta ladder

`details.ability_order` (protobuf field 2 of `details`) holds `currency_changes`, a repeated list of entries. Each entry is one action in the order the player takes it.

| Key | protobuf field | type | meaning |
| --- | --- | --- | --- |
| `ability_id` | 1 | varint | Ability id (from the `type: ability` items). |
| `currency_type` | 2 | varint | `1` = ability points, `2` = ability unlock. |
| `delta` | 3 | varint | Negative amount spent; `1` is stored as `-1`. |
| `annotation` | 4 | string | Optional label shown in the client (for example `3rd skill`). |

**The ladder (verified).** Every build with an ability order carries exactly 16 entries with this multiset:

| Entry | `currency_type` | `delta` | Meaning |
| --- | --- | --- | --- |
| 4x unlock | `2` | `-1` | Spend one Ability Unlock, one per ability. |
| 4x tier 1 | `1` | `-1` | First upgrade of an ability: 1 Ability Point. |
| 4x tier 2 | `1` | `-2` | Second upgrade of an ability: 2 Ability Points. |
| 4x tier 3 | `1` | `-5` | Third upgrade of an ability: 5 Ability Points. |

Evidence:

- 40 published builds fetched from `https://api.deadlock-api.com/v1/builds?limit=40`: all 40 have an ability order, and the counts of `(currency_type, delta)` pairs are exactly 160 each for `(2, -1)`, `(1, -1)`, `(1, -2)` and `(1, -5)`.
- The same shape appears in the local client payloads' sibling data and in all 43 generated builds in `codec-site/test/fixtures/files/builds_all_heroes.md` (16 entries each: 4 unlocks, then 4 x `-1`, 4 x `-2`, 4 x `-5`).
- The tier costs match the game economy: `mechanics/ability-points.md` records "Each ability has 3 upgrade tiers costing 1, 2, and then 5 Ability Points (8 points to fully max one ability)" and "One ability fully maxed: unlock + 8 Ability Points".

**Order within the spend phase.** The multiset is fixed, but the sequence of the twelve `currency_type: 1` entries varies in the wild: most published builds group them tier by tier (all four `-1` entries, then all four `-2`, then all four `-5`), while the published "Seven Ultimate Build V1.5" groups them per ability (`539192269` -1/-2/-5, then `1074714947` -1, `2061574352` -1/-2/-5, ...). Both import; the client reads the list as a timeline of spends.

**Validator rules** (`validate_build.py`): `currency_type` must be `1` or `2` (error otherwise); `delta` must be a negative integer (error otherwise, so `0` and positive values are rejected); an `ability_id` that is not an item of `type: ability` is a warning.

```json
"ability_order": {
  "currency_changes": [
    { "ability_id": 1074714947, "currency_type": 2, "delta": -1 },
    { "ability_id": 539192269, "currency_type": 2, "delta": -1 },
    { "ability_id": 1065103387, "currency_type": 2, "delta": -1 },
    { "ability_id": 2061574352, "currency_type": 2, "delta": -1 },
    { "ability_id": 539192269, "currency_type": 1, "delta": -1 },
    { "ability_id": 539192269, "currency_type": 1, "delta": -2 },
    { "ability_id": 539192269, "currency_type": 1, "delta": -5 }
  ]
}
```

## Resolving item, ability and hero ids

Never invent an id. Two authoritative lookups:

- **deadlock-api MCP**: `list_heroes` for `hero_id`, `list_items` for item and ability ids (`list_items` with `type=ability` returns 431 entries).
- **Local mirrors**: `items_raw.json` (774 items, of which 431 have `type: ability`) and `heroes_raw.json`. `validate_build.py` resolves against these, so a code that validates locally used ids the game still knows.

Item ids change with patches, so the lookup is the procedure, not a stored table. Worked example - the ids in the client's own `build.bin` resolved through `items_raw.json`:

| id | name | type |
| --- | --- | --- |
| 668299740 | Rapid Rounds | upgrade |
| 968099481 | Extra Spirit | upgrade |
| 1292979587 | Surge of Power | upgrade |
| 2037039379 | Inhibitor | upgrade |

Ability ids for Seven, resolved through `list_items(type=ability)`:

| id | name | class name |
| --- | --- | --- |
| 539192269 | Power Surge | `ability_power_surge` |
| 1074714947 | Static Charge | `citadel_ability_static_charge` |
| 1065103387 | Lightning Ball | `citadel_ability_lightning_ball` |
| 2061574352 | Storm Cloud | `citadel_ability_storm_cloud` |

Note the two id spaces: `mods` entries are **item** ids (`type: upgrade`), while `ability_order.ability_id` entries are **ability** ids (`type: ability`).

**Hero id.** The decoder reads protobuf field 1 as `hero_id` and also reports `hero` (the resolved hero) and `is_default_build`. Three cases:

- Normal builds: field 1 = `hero_id` (1-88), and `hero` = `hero_id`.
- Default (Valve-provided) builds: field 1 = `1000 + hero` (e.g. `1001` = Default Infernus Build), and `hero` = `hero_id - 1000`, `is_default_build` = `True`.
- Builds whose field 1 is not the real hero (e.g. a build index such as `9`-`12`, or a `1000 + hero` default id): the hero is recovered from the ability ids in `ability_order`, which each resolve to exactly one hero through `items_raw.json`. `hero` is then that hero and `hero_id` stays the raw field-1 value. This is necessary because the client's own `cached_hero_builds.kv3` stores the hero id in field 2 (not field 1), and copies of default builds carry their build index in field 1. The ability ids are the reliable hero identifier.

## Encoding, decoding and validating a build

```powershell
# decode
python C:\Users\helmet\dev\deadlock\decode_build_code.py "<base64-code>"

# encode
python C:\Users\helmet\dev\deadlock\encode_build_code.py <build.json>

# validate (exits 1 on any error)
python C:\Users\helmet\dev\deadlock\validate_build.py <build.json-or-code>
```

`validate_build.py` accepts either a JSON file or a raw build code, so a produced code can be checked without a separate decode step. The pass bar for "imports in-game" is: decode the code back, run `validate_build.py` on it (0 errors), and resolve every item and ability id against the game's own data.

## Claims and evidence

| claim | evidence | confidence |
| --- | --- | --- |
| A build code is `base64(zstd(protobuf))`; raw protobuf is also accepted | `decode_build_code.py` (zstd magic check), `codec-site/lib/deadlock_codec.rb` (`ZSTD_MAGIC`, `zstd_frame?`), `build.bin` vs `build.zst` headers, published codes from `/v1/builds` | verified |
| Top-level JSON keys map to protobuf fields 1-13 as listed above | `decode_build_code.py`, `encode_build_code.py`, `deadlock_codec.rb` (`build_hash` / `encode_top`) | verified |
| `mod_categories` entries use fields 1-6 (`mods`, `name`, `description`, `height`, `width`, `optional`) | `decode_build_code.py` (`mod_categories` parsing), `encode_build_code.py` (`encode_category`), `deadlock_codec.rb` (`parse_category`), `BuildHeroDetailsCategory` in `deadlock-api/api-1.json` | verified |
| `mods` entries hold item ids | `items_raw.json` resolves every id in `build.bin` to an item of `type: upgrade` | verified |
| The client's default categories are `#Citadel_HeroBuilds_EarlyGame`, `#Citadel_HeroBuilds_MidGame`, `#Citadel_HeroBuilds_LateGame` plus `Category 4` | decoded `build.bin`, `build2.bin`, `user_build.bin` | verified |
| Category names are free-form labels | 40 published builds use 25+ different labels | verified |
| The validator's category set is `early`, `early-mid`, `mid`, `mid-late`, `late`, `late-late`, `optional spirit-resist`, `optional general-resist-sustain`; others only warn | `validate_build.py` (`VALID_CATEGORIES`) | verified |
| `height`/`width` are cosmetic, not fixed | 171 distinct pairs across 40 published builds; the client's own files use three more | verified |
| An ability order carries 4 unlocks (`currency_type` 2, `delta` -1) plus 4 x -1, 4 x -2, 4 x -5 spends (`currency_type` 1) | 40 published builds from `/v1/builds` (160 of each pair), the 43 generated builds in `codec-site/test/fixtures/files/builds_all_heroes.md` | verified |
| The tier costs 1 / 2 / 5 are the game's Ability Point costs | `mechanics/ability-points.md` | verified |
| `currency_type` 1 = ability points, 2 = ability unlock | unlocks precede the point spends in every sample; the tier costs match the Ability Point tiers in `mechanics/ability-points.md` | verified |
| `delta` must be a negative integer and `currency_type` must be 1 or 2 | `validate_build.py` | verified |
| The order of the twelve spend entries may be tier-by-tier or per ability | 40 published builds (mostly tier-by-tier) vs the published "Seven Ultimate Build V1.5" (per ability) | verified |
| `tags` holds ability ids | one published build (`539192269, 2061574352, 1074714947` = Three of Seven's abilities) | inferred |
| `hero_build_id` is the id of the build; locally it equals the account id | `build.bin` / `build2.bin` / `user_build.bin` (`hero_build_id` 85560017 = local Steam account id) vs published builds (`hero_build_id` 1007 with a separate `author_account_id`) | verified for the samples |
| The client's own category names are the seven `#Citadel_HeroBuilds_*` keys and the eight plain phase names listed above | `decode_kv3.py --builds` on the client's cache file; see [hero-build-cache.md](hero-build-cache.md) | verified |

## Default (Valve-provided) builds

The client ships a "Default {hero_name} Build" ("Valve-provided default recommended items for this hero.") for every hero, reachable through the "Default Suggested Build" picker. A copy of one (`Copy of [Default Infernus Build]`) decodes to:

- `hero_id` (raw field 1) = `1001` = `1000 + 1`, where `1` is Infernus's hero id. The same offset applies to every hero: `1000 + hero_id`. The resolved hero is `hero_id - 1000`.
- `version` = `1`, `hero_build_id` = `0`, `origin_build_id` = `0`, `field_9` = `0`.
- `name` = `Copy of [Default {hero_name} Build]`, `description` = `#Citadel_HeroBuilds_DefaultHeroBuildDesc`.
- Categories use the client's default template names `#Citadel_HeroBuilds_EarlyGame`, `#Citadel_HeroBuilds_MidGame`, `#Citadel_HeroBuilds_LateGame` with the client's own box sizes (`836.4 x 171.0`, `658.8 x 171.0`, `837.6 x 171.0`) and 9 / 7 / 9 items.
- `ability_order` carries the full 16-entry ladder for that hero's four abilities.
- `tags` holds ability ids.

`decode_build_code.py` reports both `hero_id` (the raw field-1 value, `1001`) and `hero` (the resolved hero, `1`), plus `is_default_build` (`True` when `hero_id >= 1000`). To produce a default build, set `hero_id` to `1000 + hero` in the JSON before encoding.

## Unverified and inferred

- `cached_hero_builds.kv3` is Valve binary KV3 (magic `05 33 56 4b`); `decode_kv3.py` parses it and [hero-build-cache.md](hero-build-cache.md) records the recovered structure, the category names and the ability-order ladder. The cached payload numbers the hero id in field 2 while this page labels field 1 `hero_id` and field 2 `version`; that difference is documented there and was not tested in-game.
- `field_9` and `field_13` have unknown semantics; they are copied through untouched and never set by this repo.
- `language` is `0` in every sample; other values were never observed.
- The `height`/`width` pair `1100 x 180` used by this repo's generated builds is a convention of this repo, not a client requirement.
- The `mod` sub-fields `annotation`, `required_flex_slots`, `sell_priority` and `imbue_target_ability_id` exist in the live schema but are not encoded by the local codec, so they do not survive a round trip through `encode_build_code.py`.
- Whether the client rejects a build whose category names are unknown was not tested in-game; the published builds show unknown-to-the-validator names importing fine.
