---
title: "Walker"
pageid: 729
source: wiki-md
---

- name: Walker

- max_health: / /

- attack_range: m

## Overview

Walkers are the second line of defense in each lane, and can only be damaged after their corresponding Guardian has been destroyed. In total, there are 3 Walkers on each team with one individual in each lane. Walkers start with - npc_boss_tier2 MaxHealth HP. As each Walker dies, the remaining Walkers have increased HP, with - npc_boss_tier2 EmpoweredModifierLevel1 MaxHealth for two remaining Walkers and - npc_boss_tier2 EmpoweredModifierLevel2 MaxHealth for one remaining Walker (the Walkers get a flat `-` HP increase and heal when the other Walkers die). They also increase in size.

Walkers provide nearby allied heroes (

- npc_boss_tier2 FriendlyAuraModifier AuraRadius m)

- npc_boss_tier2 FriendlyAuraModifier

- modifierProvidedByAura BULLET_ARMOR_DAMAGE_RESIST % Bullet and - npc_boss_tier2 FriendlyAuraModifier

- modifierProvidedByAura TECH_RESIST % Spirit Resistance. Walkers currently do not take headshot damage anywhere on their bodies.

The Walker is surrounded by two white circles on the ground. The smaller circle indicates the Walker's stomp range, and the larger circle indicates the Walker's range to take damage and to use their fireballs.

Like Guardians, Walkers are immune to all damage when no enemies are within

- npc_boss_tier2 InvulModifierRange m. When an enemy enters this range, the Walker becomes vulnerable, prioritizing the closest target to it.

When attacking, a Walker has three attacks it can use. All the attacks deal [Spirit Damage](Spirit Damage.md) and can be mitigated by [Spirit Resist](Spirit Resist.md).

Several abilities are capable of disabling Walkers, such as - Dynamo's Singularity and - Kelvin's Frozen Shelter.

1. Fire Beam Channels a constantly damaging beam onto the nearest target. Deals

- npc_boss_tier2 BoundAbilities ESlot_Signature_2 AbilityProperties MaxHPDPS % Max HP per second as Spirit Damage.

1. Stomp The Walker stomps the ground, dealing Spirit Damage and stunning enemies for - npc_boss_tier2 StunDuration seconds in a - npc_boss_tier2 StompImpactRadius

- 2 m radius. Deals

- npc_boss_tier2 StompDamage damage as well as - npc_boss_tier2 StompDamageMaxHealthPercent % Max HP as damage. A Walker will only ever use this attack if an enemy gets within

- npc_boss_tier2 MeleeAttemptRange

- 2 m of it. The Walker cannot use Fire Beam or Fireballs when stomping. The Stomp has a 7 second cooldown.

Walkers will not consider players carried by - The Doorman

- l1: Doorman ’s Luggage Cart as valid targets for a stomp until the cart expires or hits a wall.

1. Fireballs The Walker's

- npc_boss_tier2 BoundAbilities ESlot_Signature_1 Name (also known as Fireball Spray) launches a volley of - npc_boss_tier2 BoundAbilities ESlot_Signature_1 AbilityProperties GrenadesInVolley projectiles. Each projectile deals

- npc_boss_tier2 BoundAbilities ESlot_Signature_1 AbilityProperties Damage Spirit Damage on impact and leaves a patch of fire on the ground. The fire lasts for - npc_boss_tier2 BoundAbilities ESlot_Signature_1 AbilityProperties FireDuration seconds and deals

- npc_boss_tier2 BoundAbilities ESlot_Signature_1 AbilityProperties FireDPS damage per second to enemies standing in it. Additionally, the fireballs apply a debuff that reduces Bullet and Spirit resistance by %. This ability has a cooldown of - npc_boss_tier2 BoundAbilities ESlot_Signature_1 AbilityProperties AbilityCooldown seconds.

## Resistances

Walkers possess a high resistance to damage early in the game that degrades over time. They start with 65% [Damage Resistance](Damage Resistance.md), which decays linearly down to -65% Resistance (taking increased damage) over the first 18 minutes of the match (-% resist per second). Additionally, they have

- npc_boss_tier2 IntrinsicModifiers

- 1 BULLET_ARMOR_DAMAGE_RESIST % Bullet Resist.

Walkers also take less weapon damage for each additional enemy within

- npc_boss_tier2 NearbyEnemyResist NearbyEnemyResistRange

- 2 m, from - npc_boss_tier2 NearbyEnemyResist ResistValues

- 4 % (3 enemies) to - npc_boss_tier2 NearbyEnemyResist ResistValues

- 7 % (6 enemies). If there's only one or two enemies nearby, it has no additional resistance.

The different resist types are stacked multiplicatively. So for example, a Walker being attacked by 3 enemies at minute 18 receives 86% bullet damage: Damage = Bullet Damage * [1 - (-0.65)] * (1 - `/100`) * (1 - `/100`) 1. Ability Damage Reduction The following abilities deal reduced damage to Walkers: 1. Backdoor protection Like [Shrines](Shrine.md) and [Base Guardians](Guardian.md), the Walker has a [Backdoor Protection](Backdoor Protection.md) represented by a green circular effect around them, if the player attacks the Walker while their lane hasn't been [pushed up](Strategy.md#Pushing-Lanes) to its position. When backdoor protection is active, the Walker gains

- npc_boss_tier2 BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers % damage reduction from players and regenerates

- npc_boss_tier2 BackdoorProtectionModifier HealthPerSecondRegen health per second.

Since the lane progress depends on the position of the last trooper wave, the Walker still has backdoor protection until the active enemy trooper wave reaches the Walker's position.

Because resistances are multiplicative, the 65% Damage Resistance from backdoor protection and -65% Damage Resistance after 18 minutes do not cancel out. Instead, they multiply out to 1 - (1 - 0.65) \times (1 + 0.65) = 42.25% damage resistance.

## Destruction

When a team destroys a Walker, it awards a total of. The bounty is divided among attackers in two parts: First, 40% (

- *0.4 round0 ) is split between all nearby attacking players (including those that did damage to the walker in the last 20 seconds). The remaining 60% (

- *0.6 round0 ) is then distributed equally among all six members of the attacking team, regardless of their location.

1. Extra Slots Each Walker destroyed unlocks one [Extra Slot](Extra Slots.md) for the entire team.

## Liquipedia

Walkers is the other type of defence other than the - M Guardian present in the lanes. Comperable to Towers in other MOBA's, they are static in their location, and need to be destroyed to progress further into the lane to reach the - M Patron.

## Walker Locations

There are a total of four Walkers on the Map, with one in each lane. They are the second structure in the lane, and can be attacked once the first M Guardian in the lane is destroyed.

## Walker Combat

Walkers are immune to damage until a - M Trooper or Hero (from it's opposing team) is nearby. Once vulnerable you can damage it. The Walkers have a total of 5,800 health.

The Walkers attack Heroes and Troopers through 3 various attacks. A Fire Beam that targets a specific target, a ground stomp that stuns enemies for 2 seconds in a radius around the Walker, and Fireballs, which deal damage upon landing, and leave behind a pool of fire which deals damage if you are standing in it.

## Souls & Ability Points

Walkers contain a total of 700 M Souls (for a player) Once a Walker is destroyed. It immediatly grants 250 M Souls to all alive heroes on the team that destroyed the walker. Another 450 M Souls spawn in 12 Soul Orbs, these are also awarded to all alive heroes on the team. The enemies can however steal/deny these orbs, and then grant the Souls to everyone on their team.

If all players on the team are alive, and all souls would be secured, this grants the team a total of 4,200 M Souls.

In addition, each hero on the team is granted an - M Ability Point.

## Flex Slots

Once two Walkers are destroyed, every hero on the team unlocks a [Flex Slot](Flex Slot.md). After all of the four Walkers are destroyed, another Flex Slot is unlocked.
