---
title: "Trooper"
pageid: 577
source: wiki-md
---

|-|Ranged Trooper =

- can_move: true

- name: Ranged Trooper

- bullet_resist: 0

- spirit_resist: 0%→70

- attack_range: m

- melee_damage: 25

- soul_orbs: 1 |-|Melee Trooper =

- name: Melee Trooper

- can_move: true

- bullet_resist: 0

- spirit_resist: 0%→70

- attack_range: m

- soul_orbs: 1 |-|Medic Trooper =

- name: Medic Trooper

- bullet_resist: 0

- spirit_resist: 0%→70

- attack_range: m

- melee_damage: 25

- soul_orbs: 1

- can_move: true

- [Mirage](Mirage.md)

- Sometimes, the small things make all the difference.

Troopers, also colloquially called Creeps or Minions, are common offensive units coming from each team's ziplines. They are the primary force for pushing lanes and [Soul](Souls.md) farming throughout the game.

## Overview

Troopers appear to be small humanoid puppet-like automata, The Hidden King

- alt_name: Amber Troopers have candles serving as their heads while The Archmother

- alt_name: Sapphire Troopers have lamps as their heads instead. Troopers visually appear to become more damaged depending on their health. There are 3 types of basic troopers: Ranged Troopers, Melee Troopers and Medic Troopers. Each trooper wave has 2 Ranged, 1 Melee and 1 Medic.

Troopers serve as the primary means to pushing lanes. The waves spawn as follows: {| class="wikitable" +Trooper wave spawn rate Match duration Spawn frequency 0 to 20 min 30s 20 to 35 min 25s over 35 min 20s |} Initially the waves consist of 3 Ranged Troopers and 1 Medic Trooper; after 5 minutes they become 2 Ranged, 1 Melee and 1 Medic. Troopers enter lanes by riding [Ziplines](Ziplines.md) in a vessel, which can be shot down to force them to drop early. Once on the ground, Troopers will attempt to move down the lane, attacking other enemy Troopers, [Heroes](Heroes.md) and [structures](structures.md) on the way.

During laning phase, Troopers are also the most reliable source of [Souls](Souls.md). Slain Troopers will drop a [Soul Orb](Soul Orb.md) on the ground that can be picked up by nearby ally players for `*100`% of the soul bounty, and release a floating Soul Orb that can be confirmed or denied by players for the remaining `*100)`% souls. Killing a Trooper with a [melee attack](melee attack.md) prevents orbs from spawning and awards 100% of the value on kill.

Troopers can be [parried](parry.md) and get stunned. However, this doesn't reset the player's parry cooldown and doesn't end the parry early.

1. Combat Stats Troopers have a complex set of resistances and vulnerabilities that change based on the game's state and their opponents.

{| class="wikitable sortable mw-collapsible" +Trooper Combat Stats Enemy Type Damage Output (DPS) Damage Resist (%) Players

- trooper_normal VSPlayer BaseDPS

- trooper_normal VSPlayer DamageResist Troopers

- trooper_normal VSTrooper BaseDPS

- trooper_normal VSTrooper DamageResist Guardians

- trooper_normal VSGuardian BaseDPS 0 Walkers

- trooper_normal VSWalker BaseDPS

- trooper_normal VSWalker DamageResist Base Guardians

- trooper_normal VSWatcher BaseDPS

- trooper_normal VSWatcher DamageResist Shrines

- trooper_normal VSShrine BaseDPS 0 Patron

- trooper_normal VSPatron BaseDPS

- trooper_normal VSPatron DamageResist |} Note: Player damage resist is applied against [Bullet Damage](Bullet Damage.md), but not against [Melee Damage](Melee Damage.md).

Other combat stats They gradually gain spirit resistance over time, reaching 20% at 25 minutes and 70% at 50 minutes.

Troopers gain

- trooper_base EnemyBaseDamageReduction % damage resistance when near/in the enemy base.

At 35 minutes, all Troopers gain +50% HP.

Sight Range Troopers have two different sight ranges: Vs. NPCs:

- trooper_normal SightRangeNPCs

- 2 m Vs. Heroes:

- trooper_normal SightRangePlayers

- 2 m 1. Health Regen Troopers have 7 out of combat [health regen](Health Regen.md).

1. Math Trooper bounty is divided by `*100`% in the ground Orb and `*100)`% in the floating Orb, or 100% on death if killed by a melee attack.

The total Soul bounty per Trooper is equal to + ( per min).

- trooper: 1 Additionally, they are divided among nearby ally players at the rates listed in table below: {| class="wikitable" + Players % share to each player Total % 1

- get_trooper_gold_share_frac

- 1 `|0|-1 * 1`% 2

- get_trooper_gold_share_frac

- 2 `|0|-1 * 2`% 3

- get_trooper_gold_share_frac

- 3 `|0|-1 * 3`% 4

- get_trooper_gold_share_frac

- 4 `|0|-1 * 4`% 5

- get_trooper_gold_share_frac

- 5 `|0|-1 * 5`% 6

- get_trooper_gold_share_frac

- 6 `|0|-1 * 6`% |}

## Trooper types

1. Ranged Trooper Ranged Troopers are the most common type of Trooper. They attack with a ranged weapon that has a range of - trooper_normal Weapon FalloffEndRange

- 2 m, resorting to a [melee](Melee attack.md) if enemies get too close.

1. Melee Trooper Melee Troopers are bulkier and tougher units with - trooper_melee MaxHealth health and a faster walk speed of - trooper_melee WalkSpeed

- 2 m/s. They engage enemies with a melee attack within a - trooper_melee MeleeAttemptRange

- 1 m range. Melee Troopers only start spawning after 5 minutes.

1. Medic Trooper Medic Troopers, also known as Banner Troopers, are a special type of Trooper that can heal nearby Heroes and Troopers when they are killed. They are distinguished by carrying a large banner with a health symbol.

Killing a Medic Trooper will drop a Medic Pack that has to be picked up by a player. It heals allies in a 35m radius, based on the following formula: Heal =

- medic_trooper_aoe_health_pickup_amber MissingPctRegen Base % of hero's missing [HP](Health.md) + (

- medic_trooper_aoe_health_pickup_amber RegenFixed Base HP +

- medic_trooper_aoe_health_pickup_amber RegenFixed PerMinuteAfterStart HP per minute) / Number of nearby heroes Medic Packs cannot be picked up by the Trooper's own team.

Medic Packs pickup range increases from 18m at 10 minutes to 30m at 18 minutes.

Troopers are also healed by a small amount when the Medic Pack is picked up by a player.

1. Super Troopers Once an enemy [Shrine](Shrine.md) has been destroyed, allied Troopers from that Shrine's lane (and for the Blue lane once either Shrine has been destroyed) become Super Troopers, gaining

- trooper_base ShrinesDownBuffModifier DamageScale % damage and `-1)*100`% health for the rest of the match. They also yield 15% less bounty when killed by enemies.

In [Street Brawl](Street Brawl.md), normal Troopers become Super Troopers after 3 minutes, when the round goes into Overtime.

1. Rift Troopers When an - Unstable Rift is captured, Rift Troopers spawn in that lane for the winning team. They are larger, black-colored, and do not drop souls when killed. A minimum of 5 troopers spawn. If the trailing team captures the rift, they receive up to 9 additional Rift Troopers (14 total), scaling based on how far behind they are.

On the first rift, they have +100% health and damage compared to normal troopers, as well as - citadel_koth_cashin TrooperModifier MeleeResistPercents

- 1 % [Melee Resist](Melee Resist.md) and - citadel_koth_cashin TrooperModifier SpiritResistPercents

- 1 % [Spirit Resist](Spirit Resist.md). For each consecutive rift, the bonus health and damage increase by an additional `-`%, up to - citadel_koth_cashin TrooperModifier HealthPercents

- 4 %. The bonus spirit resist also increases by `-`% per rift, up to - citadel_koth_cashin TrooperModifier SpiritResistPercents

- 4 %. Melee resist does not increase.
