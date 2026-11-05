---
title: "Walking/Sprinting"
pageid: 21131
source: wiki-md
---

- Walking Overview,Sprinting

- name: Sprinting

- file: sprinting.mp4

- tech_type: Universal Tech

- difficulty: Basic Mechanics

- character_dependent: No

- inputs: Move (WASD) All characters have the ability to Sprint. Sprinting in [Deadlock](Deadlock.md) is a passive action - no further action is required to sprint. When sprinting, you instantly accelerate up to +2.5 m/s of your base sprint speed, then gain 0.6 m/s every second above that threshold. Sprinting characters can be identified by the grey speed lines coming off them.

Every character has a base sprint speed of 1.6 m/s except: Bebop –

- get_hero_var Bebop SprintSpeed m/s Kelvin –

- get_hero_var Kelvin SprintSpeed m/s Lady Geist –

- get_hero_var Lady Geist SprintSpeed m/s Lash –

- get_hero_var Lash SprintSpeed m/s Paige –

- get_hero_var Paige SprintSpeed m/s Victor –

- get_hero_var Victor SprintSpeed m/s When damaged by an enemy hero or non-hero, sprint will be disabled for 3 seconds.

You cannot sprint while firing or zooming with alt-fire. Upon firing, the character will slow to around ~70% of their base walk speed until the character stops firing.

With the - Weapon Fleetfoot, they will move at their base walk speed if they are firing.

- Ivy ’s Kudzu Connection, provides Fleetfoot's passive to both her and the tethered teammate.

1. Gaining Sprint Speed from Runes Runes Sprint speed can be obtained by picking up the Movement Rune above the bridges between the inner and outer lanes. The Movement Rune grants a temporary base +3 m/s sprint speed buff for 160 seconds, that scales with time.

1. Characters with Sprint Scaling from Spirit Power Certain characters have their sprint speed scale with [Spirit Power](Spirit Power.md); this is indicated with the symbol. The equation for sprint speed scaling with Spirit Power is \text{FinalSprintSpeed} = \text{BaseSprintSpeed} + (\text{Spirit Power} \times \text{Coefficient}) {| class="wikitable" Character Base Sprint Speed (m/s) Scaling Coefficient Wraith

- get_hero_var Wraith SprintSpeed

- get_hero_scalar Wraith Spirit SprintSpeed |} 1. Abilities that Increase Sprint Speed {| class="wikitable" Character Ability Upgrade Type Amount Notes Drifter Eternal Night Base Flat +

- get_ability_prop Eternal Night BonusSprintSpeed m/s Entire duration

- 2 Flat +

- get_ability_upgrade_prop Eternal Night

- 2 BonusSprintSpeed m/s (6.00 m/s) Haze Smoke Bomb Base Flat +

- get_ability_prop Smoke Bomb InvisMoveSpeedMod m/s While invisible

- 1 Flat +

- get_ability_upgrade_prop Smoke Bomb

- 1 InvisMoveSpeedMod m/s (+7.00 m/s) Kelvin Ice Path Base Flat +

- get_ability_prop Ice Path SprintSpeedBonus m/s While on Ice Path

- 1 Flat +

- get_ability_upgrade_prop Ice Path

- 1 SprintSpeedBonus m/s (+6.00 m/s) |} 1. Items that increase Sprint Speed Certain items that have the +Sprint Speed stat increase sprint speed: Sprint Speed 1. Base Walk and Sprint Speed per Character Total Sprint Speed is the sum of Move Speed and Sprint Speed.

- heroMoveSpeedTable
