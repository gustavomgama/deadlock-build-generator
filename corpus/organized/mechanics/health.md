---
title: "Health"
pageid: 829
source: wiki-md
---

Health measures the amount of [damage](damage.md) that can be taken before [dying](Death.md), and is fundamental to all [heroes](heroes.md) and units. Units and players with health are allowed to interact with the game, and consequently when your health drops to zero you are disabled from playing until respawning.

## Maximum Health

Max health is calculated as follows: \text{Max HP} = (\text{Base HP} + \text{Boons Earned} \times \text{HP per Boon}) \times (1 + \text{Vitality Bonuses}) + \text{Bonus HP} Where: Base HP is the hero's starting health value.

Boons Earned is the number of [Boons](Boons.md) the hero has earned, multiplied by the hero's hero-specific HP gained per Boon.

Vitality Bonuses are the percentage-based health increases from [Vitality](Vitality.md) items, starting at 8% and increasing with further Vitality investment.

Bonus HP is flat health added from items, map pickups, and other sources, applied after the Vitality multiplier.

Note that the max health presented in-game is rounded up to the nearest integer.

1. Base Health Base health is the sum of starting base health and added base health from boons. It is scaled by the inherent increased base health stats of Vitality items. Different heroes have different amounts of starting base health and added base health from boons.

1. Health scaling To see all [Heroes](Heroes.md) health scaling by [Boon](Boon.md) please visit the [Hero Comparison Table](Hero Comparison Table.md).

- heroHealthTable 1. Bonus Health Bonus health comes from a variety of sources: Items are the most common source of added bonus health. Bonus health can be found on all three item types, but Vitality items tend to provide the largest amounts.

[Golden statues](Golden Statue.md) occasionally drop small but permanent added bonus health buffs: +

- hp_permanent_pickup Modifer ScriptValues

- 1

- value before 10 minutes, +

- hp_permanent_pickup_lv2 Modifer ScriptValues

- 1

- value between 10 and 30 minutes, or +

- hp_permanent_pickup_lv3 Modifer ScriptValues

- 1

- value after 30 minutes.

The [Survival Powerup](Powerup.md) immediately grants +

- survival_powerup_pickup Modifer ModifierValues

- 1

- valueMin to +

- survival_powerup_pickup Modifer ModifierValues

- 1

- valueMax bonus health (scales as game goes on), but only for 160 seconds or until death.

Bonus Health is not scaled by increased base health. Bonus health is added after the increased base health multiplier has been applied to base health.

1. Example [Kelvin](Kelvin.md) begins the game with 600 Base HP. If Kelvin purchases two tier 1 vitality items, one of which grants 100 bonus health, his max health becomes: \text{Max HP} = 600 \times (1 + 0.10 + 0.10) + 100 = 820 If Kelvin then earns a power increase, his base health increases by 50, and his max health becomes: \text{Max HP} = (600 + 50) \times (1 + 0.10 + 0.10) + 100 = 880

## Regaining Health

- Healing Health Regen From the start of the match, heroes will regenerate health slowly over time, typically 2 HP per second. This rate can be increased by purchasing items such as Extra Regen and Fortitude. Health can be regained quickly by returning to the spawn room of the team's base. Various hero abilities can heal, such as Dynamo's Rejuvenating Aurora. Sources of [spirit](Spirit Lifesteal.md) and [bullet lifesteal](Bullet Lifesteal.md) grant heroes the opportunity to regain health by dealing the respective damage type.

## Health Bars

Health Bars are visual indicators of a hero's current health, located just above each hero. Health bars consist of filled rectangles, arranged in rows of up to ten. Enemy heroes are displayed with orange rectangles, while allied heroes use an off-white color. As the hero loses health, the rectangles deplete horizontally. Each full rectangle represents 100 health, and each full row represents 1000 health.

The small yellow and blue bars above the health bar represent bullet [shields](Damage Shield.md) and spirit shields, respectively.

When the player goes below 50% health, their health bar will enlarge, begin pulsating, and the text will turn sickly green until their health is restored above 50%.

1. Command Line Alternate health bar The alternate health bar is an experimental bar that can be tested by players. This bar always has the same size, and the health count is displayed as markings instead of rectangles. One marking represents 100 health, and a line represents 500 health (from left to right).

1. Gameinfo.gi Alternate health Bar There is another experimental health bar accessible to players. Inside the gameinfo.gi in the game's files, under the ConVars block, adding the 2 lines "citadel_unit_status_use_v2" "true" and "citadel_unit_status_use_v2_for_nonplayers" "true" applies this health bar. When at critical health, the 'critical' text will appear above the hero.

The healthbar scales on the heroes maximum health, with 1 segment for every 1000 health points. A segment that does not represent 1000 health will be shorter than other segments. If a hero uses stamina bar, a stamina pool appears over their head, represented by dots. A filled dot is stamina the hero can use, and an empty dot is stamina that has to be regenerated.

If this health bar is enabled, the health bar given by citadel_unit_status_use_new true will be overridden.
