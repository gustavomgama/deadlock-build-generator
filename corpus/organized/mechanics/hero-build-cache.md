---
title: "Hero Build Cache (cached_hero_builds.kv3)"
pageid: 0
source: steam-cfg
---

The Deadlock client keeps every build the player has saved, favourited or published in one file:

```text
C:/Program Files (x86)/Steam/userdata/85560017/1422450/remote/cfg/cached_hero_builds.kv3
```

It is Valve **binary KeyValues3 version 5** (magic `0x4B563305`, file bytes `05 33 56 4b`), LZ4 block compressed, 37 355 bytes. It is the game's own saved data, so it is the ground truth for what the client stores: which category names it recognises, how a build is laid out and how an ability order is encoded. The file is read-only; everything below was copied into this repository, nothing was written back.

The same build payload travels inside build codes as `base64(zstd(protobuf))`, so the rules recovered here are the rules the client applies to an imported code. The build-code format itself is documented in [build-codes.md](build-codes.md); this page is the ground truth behind it.

## Snapshot provenance

The client rewrites this file every time the player saves, favourites or deletes a build, so **the counts on this page are a dated snapshot of one player's own library, not properties of the game**. They were measured from the file version recorded here:

| field | value |
| --- | --- |
| captured at | 2026-10-20T17:19:35-03:00 |
| file size | 37 355 bytes |
| sha256 | `6c68cd639fed949056cedb546c985e17d9d61ce87e1ee7b54cc61a43999259e3` |

The **format** rules - the category names the client recognises, the ability-order delta ladder, the meaning of every payload field - do not change when the file is rewritten, and those are what the corpus, the oracle agent and the /build command rely on. Re-run the commands below to refresh the counts after a client update.

The same numbers in machine readable form, so a tool can check the document against them:

```json
{
  "source": "C:/Program Files (x86)/Steam/userdata/85560017/1422450/remote/cfg/cached_hero_builds.kv3",
  "captured_at": "2026-10-20T17:19:35-03:00",
  "source_size": 37355,
  "source_sha256": "6c68cd639fed949056cedb546c985e17d9d61ce87e1ee7b54cc61a43999259e3",
  "facts": {
    "file_size": 37355,
    "version": 5,
    "compression": 1,
    "strings": 71,
    "hero_class_strings": 67,
    "buffer1": [
      888,
      585
    ],
    "buffer2": [
      773,
      716
    ],
    "types": 75,
    "nodes": 72,
    "blobs": 37,
    "blob_bytes": 89629,
    "favorites": 15,
    "unpublished": 11,
    "saved_last_used": 11,
    "builds": 37,
    "local_account_builds": 11,
    "other_account_ids": 17,
    "last_used_entries": 67,
    "last_used_zero": 23,
    "last_used_build_id": 44,
    "last_used_in_file": 17,
    "last_used_not_in_file": 27,
    "categories": 242,
    "distinct_names": 128,
    "free_names": 113,
    "empty_names": 13,
    "token_occurrences": {
      "#Citadel_HeroBuilds_Lane": 3,
      "#Citadel_HeroBuilds_EarlyGame": 10,
      "#Citadel_HeroBuilds_Early": 4,
      "#Citadel_HeroBuilds_LateGame": 9,
      "#Citadel_HeroBuilds_MidGame": 8,
      "#Citadel_HeroBuilds_Mid": 3,
      "#Citadel_HeroBuilds_Late": 1
    },
    "plain_occurrences": {
      "early-mid": 3,
      "mid-late": 3,
      "late": 3,
      "late-late": 3,
      "optional spirit-resist": 3,
      "optional general-resist-sustain": 3,
      "early": 1,
      "mid": 1
    },
    "optional_1": 129,
    "optional_0": 5,
    "optional_absent": 108,
    "width_present": 238,
    "mod_entries": 1392,
    "sell_priority_zero": 325,
    "sell_priority_set": 22,
    "order_entries": 649,
    "deltas": {
      "2/-1": 171,
      "1/-1": 164,
      "1/-2": 165,
      "1/-5": 149
    },
    "abilities": 139,
    "ladder_shapes": [
      [
        [
          [
            1,
            -5
          ],
          [
            1,
            -2
          ],
          [
            1,
            -1
          ],
          [
            2,
            -1
          ]
        ],
        135
      ],
      [
        [
          [
            1,
            -2
          ],
          [
            1,
            -1
          ],
          [
            2,
            -1
          ]
        ],
        2
      ],
      [
        [
          [
            2,
            -1
          ]
        ],
        2
      ]
    ],
    "full_ladder": 135,
    "partial_ladder": 4,
    "builds_with_order": 34,
    "hero_owned": 33,
    "mixed_builds": [
      "Dew"
    ],
    "without_order": 3,
    "no_order_heroes": [
      50,
      86,
      88
    ],
    "field13_eq_field4": 26,
    "tags_total": 93,
    "tags_distinct": 37,
    "tags_resolved": 27,
    "tags_missing": 10,
    "f9_local_hero": [
      2,
      1041,
      13,
      2,
      1,
      1001,
      10,
      11
    ],
    "f9_local_without": 3
  }
}
```

## How to reproduce everything on this page

```powershell
# decode the whole file to JSON
python C:\Users\helmet\dev\deadlock\decode_kv3.py "C:\Program Files (x86)\Steam\userdata\85560017\1422450\remote\cfg\cached_hero_builds.kv3" --out build_cache.json

# just the string table (71 entries)
python C:\Users\helmet\dev\deadlock\decode_kv3.py "C:\Program Files (x86)\Steam\userdata\85560017\1422450\remote\cfg\cached_hero_builds.kv3" --strings-only

# every saved build with resolved item names, category names and the ability ladder
python C:\Users\helmet\dev\deadlock\decode_kv3.py "C:\Program Files (x86)\Steam\userdata\85560017\1422450\remote\cfg\cached_hero_builds.kv3" --builds --out build_cache_builds.json

# check the decoder against the structure of this file (prints SELF_TEST_OK)
python C:\Users\helmet\dev\deadlock\decode_kv3.py "C:\Program Files (x86)\Steam\userdata\85560017\1422450\remote\cfg\cached_hero_builds.kv3" --self-test
```

`decode_kv3.py` is the parser this repository now has for binary KV3; it implements the layout ValveResourceFormat's `BinaryKV3` reader documents (magic, LZ4 buffers, value lanes, type bytes, chained binary blobs). `--builds` reuses the protobuf schema of `decode_build_code.py` for the build payload, so the two tools agree on the field numbers.

## File structure (verified)

| part | value | meaning |
| --- | --- | --- |
| magic | `0x4B563305` | binary KeyValues3, version 5 |
| format GUID | `7c161274-e906-9846-aff2-e63eb59037e7` | the KV3 format the file was written with |
| compression | `1` | LZ4 block compression |
| strings | 71 | `LastUsedBuilds`, 67 hero class names, `Favorites`, `Unpublished`, `SavedLastUsed` |
| buffer 1 | 888 bytes uncompressed (585 compressed) | the string table |
| buffer 2 | 773 bytes uncompressed (716 compressed) | object lengths, value lanes, 75 type bytes, blob lengths |
| binary blobs | 37 blobs, 89 629 bytes | the saved builds themselves |
| nodes | 72 | tree size hint |

The root object has exactly four members:

| key | type | content |
| --- | --- | --- |
| `LastUsedBuilds` | object | 67 entries, `hero_<class_name>` -> build id. 23 heroes map to `0` (never played); 44 map to a build id. |
| `Favorites` | array | 15 builds |
| `Unpublished` | array | 11 builds |
| `SavedLastUsed` | array | 11 builds |

15 + 11 + 11 = 37 builds in total. Every one of them is a binary blob holding the same protobuf payload that a build code carries.

`LastUsedBuilds` points into the same id space as the stored builds. Verified examples: `hero_inferno` -> `12` -> the build `Copy of [Copy of [Copy of [Default Infernus Build]`; `hero_gigawatt` -> `8` -> `Copy of [Seven #2 - helmet]`; `hero_haze` -> `6` -> `Haze - Oracle Build`; `hero_artist` -> `4` -> `Copy of [Default Violet Build]`; `hero_baba` -> `7` -> `New Baba Build`. 17 of the 44 non-zero ids resolve to a build stored in this file; the other 27 are the client's shipped per-hero default builds, which are stored by the game service and not in this file.

## Build payload structure (verified)

Each blob is a wrapper whose field 1 holds the build payload. The payload uses the same field numbers as `decode_build_code.py`:

| field | value in this cache | meaning |
| --- | --- | --- |
| 1 | `2`-`12`, `1007`, `1013`, `1023`, `207750`, `242723`, `317821`, ... | id of this build |
| 2 | `1`, `2`, `3`, `13`, `17`, `20`, `50`, `58`, `63`, `65`, `72`, `77`, `86`, `88`, ... | **hero id** - the id used by `heroes_raw.json` and `list_heroes` |
| 3 | `85560017` on the 11 builds of the local account, 17 other account ids on published builds | id of the account that owns the build |
| 4 | e.g. `1750107163` | last-updated timestamp (Unix seconds) |
| 5 | text | build name |
| 6 | text | build description |
| 7 | `0` | language |
| 8 | `0` on the 11 locally authored builds, otherwise the id of the build it was copied from (`4`, `10`, `24`, `63`, `66`, `77`, `107`, ...) | origin build id |
| 9 | a second id: the hero id on 8 of the 11 locally authored builds (`2`, `1041`, `13`, `2`, `1`, `1001`, `10`, `11`) and absent on the other 3; `0` or a large id such as `206703`, `247578`, `239350`, `643407` on the imported ones | unknown - see [Unverified](#unverified-and-inferred) |
| 10 | message | `details` |
| 11 | varints | the ids of the abilities and upgrades the build references. 93 entries, 37 distinct; 27 of the 37 resolve through `items_raw.json` (both `ability` and `upgrade` types), 10 no longer exist in the live data |
| 13 | the same value as field 4 | a second copy of the timestamp. Present on 26 of the 37 builds, absent on the 11 locally authored ones |

Field 2 is the hero id, and this is proven from the file itself: for 33 of the 34 builds that carry an ability order, **every** ability id in the build belongs to the hero in field 2 (the 34th, `Dew`, has field 2 `50` = Pocket but its order also lists three Celeste abilities - `Light Eater`, `Dazzling Trick`, `Radiant Daggers`). The three builds without an ability order carry `50` (Pocket), `86` (Violet) and `88` (Baba). Field 1 is therefore the build id, not the hero id: `Haze - Oracle Build` has field 1 `6` and field 2 `13`, and `Haze` is hero `13`, not `6`.

`details` (field 10) holds the two parts that matter for an import:

| part | protobuf | content |
| --- | --- | --- |
| `mod_categories` | field 1, repeated | the item categories, in the order the player wrote them |
| `ability_order` | field 2 | the ability timeline |

A **category** uses fields 1-6:

| field | type | content |
| --- | --- | --- |
| 1 | repeated message | the items in the category |
| 2 | string | the category name |
| 3 | string | the note under the name |
| 4 | float32 | the box height in pixels, e.g. `762`, `285.75` (cosmetic) |
| 5 | float32 | the box width in pixels, e.g. `164.25` (cosmetic). Present on 238 of the 242 categories |
| 6 | varint | optional flag: `1` on 129 of the 242 categories, `0` on 5 more, absent on the other 108 |

An **item entry** (field 1 of a category) uses:

| field | type | content |
| --- | --- | --- |
| 1 | varint | the item id |
| 2 | string | annotation, for example `Pick Rate: 94%\nWR: +0%` |
| 4 | varint | `0` on 325 of 347 entries, otherwise a small number such as `96`, `97`, `99` - the sell priority |
| 5 | varint | an ability id - the target of an imbue upgrade |

Fields 4 and 5 match the `sell_priority` and `imbue_target_ability_id` members of the `BuildHeroDetailsCategoryAbility` schema in `deadlock-api/api-1.json`; the naming is inferred, the values are verified.

The whole cache holds 242 categories, 1 392 item entries and 649 ability-order entries.

## Category names the client uses

### Localisation keys the client ships

Seven distinct `#Citadel_HeroBuilds_*` keys appear in this file:

| key | occurrences | used by |
| --- | --- | --- |
| `#Citadel_HeroBuilds_Early` | 4 | `Seven #2 - helmet`, `Copy of [Seven #2 - helmet]`, `Dew`, `SN|P3R : Emberline [Dash Infernus]` |
| `#Citadel_HeroBuilds_Mid` | 3 | `Seven #2 - helmet`, `Copy of [Seven #2 - helmet]`, `Dew` |
| `#Citadel_HeroBuilds_Late` | 1 | `Dew` |
| `#Citadel_HeroBuilds_EarlyGame` | 10 | `New Pocket Build`, `New Violet Build`, `New Baba Build`, `Renon's Eternus Infernus`, the four `Default ... Build` copies, `xxxxxxxxxxxx`, `Zizis Billy (SEPT 29TH PATCH. PRESS QUICK BUY)` |
| `#Citadel_HeroBuilds_MidGame` | 8 | `Gunfernus Perfected [Lockbuilds.com]`, `GenericEdBoi's - The Only Infernus Build You Need!`, the four `Default ... Build` copies, `xxxxxxxxxxxx`, `Zizis Billy (SEPT 29TH PATCH. PRESS QUICK BUY)` |
| `#Citadel_HeroBuilds_LateGame` | 9 | `Possibly Solved Venator Dopamine Maxxing`, `Gunfernus Perfected [Lockbuilds.com]`, `GenericEdBoi's - The Only Infernus Build You Need!`, `Kari's 1 v 11 Spirit Mina build`, the four `Default ... Build` copies, `xxxxxxxxxxxx` |
| `#Citadel_HeroBuilds_Lane` | 3 | `Parzelion's Seven Build`, `GenericEdBoi's - The Only Infernus Build You Need!` |

The leading `#` marks a localisation key, so the client renders these as the built-in phase headers of the build panel instead of showing the raw token. The seven keys above are the complete set of `#Citadel_HeroBuilds_*` names in the client's own saved data.

### Plain phase names the client ships

The same templates also use the plain phase names, which the client shows literally:

| name | occurrences | used by |
| --- | --- | --- |
| `early` | 1 | `Haze - Oracle Build` |
| `early-mid` | 3 | the three templates `Seven #2 - helmet`, `Haze - Oracle Build`, `Copy of [Seven #2 - helmet]` |
| `mid` | 1 | `Haze - Oracle Build` |
| `mid-late` | 3 | the same three templates |
| `late` | 3 | the same three templates |
| `late-late` | 3 | the same three templates |
| `optional spirit-resist` | 3 | the same three templates |
| `optional general-resist-sustain` | 3 | the same three templates |

The eight names are exactly the set `validate_build.py` accepts as `VALID_CATEGORIES`, and they are the phase names the client itself writes into a new build.

### Free-form labels

113 further free-form names appear in this file - `Core Build`, `Defensives`, `Counter Picks`, `Actives`, `Laning Phase`, `DERP`, `Category 6`, `BELOW THIS CATEGORY IS JUST RANDOM STUFF FOR NOTES AND TESTING`, and so on, 13 of them the empty string. 128 distinct names in total: the 7 localisation keys, the 8 plain phase names and these 113.

**Conclusion (verified):** a category name is a label, not a key. The client stores, renders and re-imports whatever text the author typed. The `#Citadel_HeroBuilds_*` tokens are the client's own phase headers; the plain phase names are the client's default build template. Neither form is required for an import - the items inside the category are what carry the build.

## Ability order: the delta ladder (verified)

`details.ability_order` holds `currency_changes`, one entry per spend, in the order the player made it. Every entry uses fields 1-3: ability id, currency type, delta.

Only four `(currency_type, delta)` pairs exist in this cache, over 649 entries:

| currency_type | delta | occurrences | meaning |
| --- | --- | --- | --- |
| 2 | `-1` | 171 | unlock the ability (one Ability Unlock per ability) |
| 1 | `-1` | 164 | first upgrade tier: 1 Ability Point |
| 1 | `-2` | 165 | second upgrade tier: 2 Ability Points |
| 1 | `-5` | 149 | third upgrade tier: 5 Ability Points |

The tier costs are the game's own: [ability-points.md](ability-points.md) records "Each ability has 3 upgrade tiers costing 1, 2, and then 5 Ability Points (8 points to fully max one ability)" and "One ability fully maxed: unlock + 8 Ability Points".

A fully maxed ability therefore appears in the cache as four entries: `currency_type 2, delta -1` followed by `currency_type 1` with deltas `-1`, `-2`, `-5`. The order of the sixteen spend entries varies: the shipped templates group them tier by tier (all four `-1`, then all four `-2`, then all four `-5`), while player builds interleave them per ability. Both shapes are present in this file, so both are accepted.

The 16 entries of the shipped `Seven #2 - helmet` template, in file order:

```json
[
  { "ability_id": 539192269, "currency_type": 2, "delta": -1 },
  { "ability_id": 1065103387, "currency_type": 2, "delta": -1 },
  { "ability_id": 1074714947, "currency_type": 2, "delta": -1 },
  { "ability_id": 2061574352, "currency_type": 2, "delta": -1 },
  { "ability_id": 539192269, "currency_type": 1, "delta": -1 },
  { "ability_id": 1065103387, "currency_type": 1, "delta": -1 },
  { "ability_id": 1074714947, "currency_type": 1, "delta": -1 },
  { "ability_id": 2061574352, "currency_type": 1, "delta": -1 },
  { "ability_id": 539192269, "currency_type": 1, "delta": -2 },
  { "ability_id": 1065103387, "currency_type": 1, "delta": -2 },
  { "ability_id": 1074714947, "currency_type": 1, "delta": -2 },
  { "ability_id": 2061574352, "currency_type": 1, "delta": -2 },
  { "ability_id": 539192269, "currency_type": 1, "delta": -5 },
  { "ability_id": 1065103387, "currency_type": 1, "delta": -5 },
  { "ability_id": 1074714947, "currency_type": 1, "delta": -5 },
  { "ability_id": 2061574352, "currency_type": 1, "delta": -5 }
]
```

An ability order that only unlocks abilities, or that spends `1` point for every tier, is not what the client writes. 135 of the 139 abilities in this file carry the full `-1 / -2 / -5` ladder; the other 4 are unlocked and upgraded only to tier 1 or tier 2, so a build may stop at any tier - a build code that always maxes every ability is valid, but it is not the only shape the client writes.

## Resolving the ids in this file

Never invent an id. The ids in the cache resolve through the same two lookups the rest of the repository uses:

- **deadlock-api MCP**: `list_items` with an id, or `list_items` with `type=upgrade` / `type=ability` to list them; `list_heroes` for hero ids.
- **Local mirrors**: `items_raw.json` (774 entries: `upgrade`, `ability` and `weapon`) and `heroes_raw.json` (65 heroes).

Worked examples from this cache, resolved through `items_raw.json`:

| id | name | class name | type |
| --- | --- | --- | --- |
| 968099481 | Extra Spirit | `upgrade_improved_spirit` | upgrade |
| 1009965641 | Monster Rounds | `upgrade_non_player_bonus` | upgrade |
| 7409189 | Improved Spirit | `upgrade_soaring_spirit` | upgrade |
| 2163598980 | Spirit Resilience | `upgrade_tech_purge` | upgrade |
| 1593133799 | Afterburn | `ability_afterburn` | ability |
| 539192269 | Power Surge | `ability_power_surge` | ability |

The same ids resolve through the MCP: `list_items({id: 968099481})` returns `Extra Spirit`, `list_items({id: 1593133799})` returns `Afterburn` (`hero: 1`, Infernus), `list_items({id: 539192269})` returns `Power Surge` (`hero: 2`, Seven).

Two id spaces, as in [build-codes.md](build-codes.md): a category `mods` entry is an **item** id (`type: upgrade`), an `ability_order` entry is an **ability** id (`type: ability`), and the payload's field 2 is a **hero** id.

## Claims and evidence

| surface | claim | evidence | confidence | discovered_at |
| --- | --- | --- | --- | --- |
| rag-corpus | `cached_hero_builds.kv3` is binary KeyValues3 version 5 (`0x4B563305`), LZ4 compressed, 37 355 bytes | `decode_kv3.py --strings-only` on the file; header fields read by the parser | verified | 2026-10-20 |
| rag-corpus | The root has exactly `LastUsedBuilds`, `Favorites`, `Unpublished`, `SavedLastUsed`; the three arrays hold 15 + 11 + 11 = 37 builds | `decode_kv3.py --builds` | verified | 2026-10-20 |
| rag-corpus | The client's `#Citadel_HeroBuilds_*` category names are exactly `_Early`, `_Mid`, `_Late`, `_EarlyGame`, `_MidGame`, `_LateGame`, `_Lane` | `decode_kv3.py --builds`, `category_names` (7 keys with the prefix) | verified | 2026-10-20 |
| rag-corpus | The client also ships the plain phase names `early`, `early-mid`, `mid`, `mid-late`, `late`, `late-late`, `optional spirit-resist`, `optional general-resist-sustain` | `decode_kv3.py --builds` (each occurs 1-3 times), and the same list in `validate_build.py` `VALID_CATEGORIES` | verified | 2026-10-20 |
| rag-corpus | A category name is a free-form label: 128 distinct names appear, 113 of them player-authored | `decode_kv3.py --builds`; 128 = 7 `#Citadel_HeroBuilds_*` keys + 8 plain phase names + 113 free-form labels (13 of them the empty string) | verified | 2026-10-20 |
| rag-corpus | The build payload's field 2 is the hero id and field 1 is the build id | 33 of 34 builds with an ability order have all ability ids owned by the hero in field 2; `Haze - Oracle Build` has field 1 `6` and field 2 `13`; the three builds without an ability order carry hero ids `50`, `86`, `88` | verified | 2026-10-20 |
| rag-corpus | `LastUsedBuilds` maps a hero class name to a build id in the same id space as the stored builds | `hero_inferno` -> `12`; `hero_gigawatt` -> `8` -> `Copy of [Seven #2 - helmet]`; `hero_haze` -> `6` -> `Haze - Oracle Build` | verified | 2026-10-20 |
| rag-corpus | `LastUsedBuilds` holds 67 heroes: 23 map to `0`, 44 to a build id, 17 of those 44 to a build stored in this file | `decode_kv3.py --builds`, `last_used_builds`; the 17 matches are the `hero_*` keys whose value is one of the 37 stored build ids | verified | 2026-10-20 |
| rag-corpus | An ability order uses only `currency_type` 1 and 2 with deltas -1, -2 and -5; `currency_type 2` is always the unlock | `decode_kv3.py --builds`, `currency_delta_counts`: `2/-1` 171, `1/-1` 164, `1/-2` 165, `1/-5` 149 over 649 entries | verified | 2026-10-20 |
| rag-corpus | The tier costs 1 / 2 / 5 are the game's Ability Point costs | [ability-points.md](ability-points.md) | verified | 2026-10-20 |
| rag-corpus | A maxed ability is one unlock plus the three tier spends; the sixteen spends may be ordered tier by tier or per ability | the shipped `Seven #2 - helmet` template (tier by tier) against the player builds in `Favorites` (per ability) | verified | 2026-10-20 |
| rag-corpus | A build may stop at any tier: 135 of the 139 abilities in the file carry the full `-1 / -2 / -5` ladder, 4 carry a partial one | per-ability ladder shapes over the 34 builds with an ability order: 135 x unlock+1+2+5, 2 x unlock+1+2, 2 x unlock only | verified | 2026-10-20 |
| rag-corpus | Category item entries carry the item id plus an annotation, and sometimes a sell priority and an imbue target ability | 1 392 mod entries: field sets `(1)`, `(1,2)`, `(1,4)`, `(1,2,4)`, `(1,2,4,5)`, `(1,2,5)`, `(1,5)` | verified | 2026-10-20 |
| rag-corpus | Mod field 4 is the sell priority and field 5 the imbue target ability | the values (small integers, ability ids) match `sell_priority` and `imbue_target_ability_id` in the `BuildHeroDetailsCategoryAbility` schema in `deadlock-api/api-1.json` | inferred | 2026-10-20 |
| rag-corpus | The payload's field 8 is the id of the build a build was copied from (`0` on the 11 `Unpublished` builds), field 9 is a second id whose meaning is unknown, field 11 holds the referenced ability and upgrade ids, and field 13 repeats the field 4 timestamp | field 8 is `0` on the 11 `Unpublished` builds and non-zero on the other 26; field 13 equals field 4 on 26 of 37 builds and is absent on the 11 locally authored ones; 27 of the 37 distinct field 11 ids resolve through `items_raw.json` as `ability` or `upgrade` ids | verified | 2026-10-20 |
| rag-corpus | Item and ability ids resolve through `list_items` / `items_raw.json` | `list_items({id: 968099481})` -> `Extra Spirit`; `list_items({id: 1593133799})` -> `Afterburn`; the same ids in `items_raw.json` | verified | 2026-10-20 |
| tooling | `decode_kv3.py` parses binary KV3 v5 (LZ4 buffers, value lanes, chained blobs) | the parser reproduces the client's builds with resolved item names | verified | 2026-10-20 |

## Unverified and inferred

- The build payload in the cache uses field 2 for the hero id, while `decode_build_code.py` labels field 1 `hero_id` and field 2 `version`. The client's own payloads in this repository (`build.bin`, `build2.bin`, `user_build.bin`) show the same layout as the cache: field 1 `6`/`7`, field 2 `13` (Haze), field 3 the account id `85560017`. Whether the client reads a *build code* the same way was not tested in-game, so the field labels used by the local codec are left as they are.
- The meaning of field 9 is unknown. On the locally authored builds it carries the hero id, on the imported ones `0` or a large id; those large ids are neither hero ids, nor item ids, nor build ids stored in this file.
- Field 8 holds the id of the build a build was copied from: `0` on the 11 locally authored builds, another id on the other 26. The copied-from build is not stored in this file, so that id cannot be resolved from here.
- 10 of the 37 distinct field 11 ids no longer exist in the live data - `list_items` reports `Item not found` for each - so the client wrote ids that have since been removed from the game.
- `field_4` of the payload is treated as a Unix timestamp because the values fall in the current year; the API calls the equivalent field `last_updated_timestamp`.
- 27 of the 44 non-zero `LastUsedBuilds` ids have no matching build in this file. They are the client's shipped per-hero defaults, which live in the game service, not in the local cache.
- Whether the client rejects a build whose category names are unknown was not tested in-game. The published builds and this cache show that unknown-to-the-validator names are stored and re-imported.
