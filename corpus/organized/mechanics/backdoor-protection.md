---
title: "Backdoor Protection"
pageid: 27948
source: wiki-md
---

Backdoor Protection or "Protected" is a type of [Damage Resistance](Damage Resistance.md) applied to [Structures](Structures.md) when they have no enemy [Troopers](Troopers.md) nearby.

## Overview

Backdoor Protection is indicated by a green circle effect surrounding the structure and the text "Protected" with a green heart icon under its health bar.

Every structure except for [Lane Guardians](Lane Guardians.md) has backdoor protection. Lane Guardians only have protection in the [Street Brawl](Street Brawl.md) mode.

Backdoor Protection can be removed by pushing the trooper wave up to the structure. For base structures, having any [zipline](zipline.md) pushed up to the base will remove protection. Once protection has been removed, it has a 14s buffer before it's applied again.

Destroying a structure with backdoor protection will instantly push the team's zipline up to the destroyed structure, regardless of it's original progress.

The Backdoor health regen only heals the Structure up to the HP it had before it was attacked under protection. The only structure that can heal up to 100% health out of combat is the [Patron](Patron.md), who has

- npc_boss_tier3 ObjectiveRegen OutOfCombatHealthRegen HP/s out of combat regen.

{| class="wikitable" style="text-align:center" +Backdoor Protection stats Structure Damage Resist (%) Health Regen (HP/s) [Walker](Walker.md)

- npc_boss_tier2 BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers

- npc_boss_tier2 BackdoorProtectionModifier HealthPerSecondRegen [Base Guardian](Base Guardian.md)

- npc_barrack_boss BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers

- npc_barrack_boss BackdoorProtectionModifier HealthPerSecondRegen [Shrine](Shrine.md)

- npc_barrack_boss BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers

- npc_barrack_boss BackdoorProtectionModifier HealthPerSecondRegen [Patron](Patron.md)

- npc_boss_tier3 BackdoorProtection BackdoorProtectionDamageMitigationFromPlayers

- npc_boss_tier3 BackdoorProtection HealthPerSecondRegen |} Additionally, Shrines are invulnerable to damage until a pair of Base Guardians has been destroyed.

Base Guardians and Shrines also have a separate Bullet Resist stat that starts at

- npc_barrack_boss BackdoorBulletResistModifier BulletResist % for Base Guardians and

- destroyable_building BackdoorBulletResistModifier BulletResist % for Shrines, decaying by

- npc_barrack_boss BackdoorBulletResistModifier BulletResistReductionPerHero % for each enemy hero nearby, up to 0% minimum.

## DPS calculation

The [DPS](DPS.md) dealt to a structure with backdoor protection can be calculated as follows: \text{Final DPS} = [\text{Base DPS} \times (1 - \text{Backdoor Resist}) \times (1- \text{Additional Resists})] - \text{Health Regen} So for example, in a scenario where the player is attacking a backdoor Walker with no additional resists, they need to deal a minimum of 189 DPS (rounded up) to damage it: 1 = [188,57 \times (1 - 0,65)] - 65
