---
title: "Haunt"
pageid: 46363
source: wiki-md
---

Haunt, also colloquially called Neutral Creep, Jungle Creep or Denizen, is a type of [Unit](Unit.md) that's not aligned with any of the teams, and offer an alternative source of Souls.

## Overview

Haunts appear in small camps scattered in the jungle on both sides of the map, each with different power levels. When killed, they grant a set amount of Souls to every player that damaged it and do not release any Soul Orbs. Shooting Haunts in the eye deals [critical damage](critical damage.md).

Haunts will spawn and respawn at varying times based on the size of the camp. The timer starts when the last creep is killed.

Haunts scale over the course of the match. Their Health increases by Convar

- citadel_neutral_health_growth_pct_per_min % per minute, while their Damage increases by

- neutral_trooper_normal NeutralDamageGrowth DamageGrowthPctPerMin % per minute.

Haunts spawn dormant. Damage against Haunts is ineffective unless the the attacking player is within

- neutral_trooper_normal SightRangePlayers m or the Haunt is already active. A player standing near the camp will also activate all Haunts in the camp, but they will remain neutral unless provoked.

While attacking, Haunts will move around, occasionally approaching a target player if it has a melee attack. The medium and large variants of Haunts have a chance to use a special attack unique to their Haunt family.

Most Haunts deal Bullet [Weapon Damage](Weapon Damage.md) with their basic ranged attacks and [Spirit Damage](Spirit Damage.md) with a special attack (with some exceptions). Some Haunts that have melee attacks can be [parried](Melee_Attack.md#Parry).

## Souls

See: [Souls#Haunts (Jungle Creeps)](Souls.md#Haunts_(Jungle_Creeps)) Haunts drop varying amounts of Souls depending on their size and the overall duration of a match. The larger the Haunt, the higher the total Soul bounty they drop. If multiple players attack a Haunt, the Souls will be split evenly between all allied players who helped kill it. All Souls dropped by Haunts are [Haunted Souls](Souls.md#Haunted-Souls).

The Haunt Soul bounty increase per minute is equal to

- neutral_trooper_weak GoldRewardBonusPercentPerMinute % of the base Soul value. The starting value is from the start of the match, not when the Haunts are spawned.

 {| class="wikitable sortable" Source Soul Value Soul Gain (/min) Notes Small Haunt

- neutral_trooper_weak GoldReward +` * / 100 round 2` Shared baseline for all small-camp Haunts Medium Haunt

- neutral_trooper_normal GoldReward +` * / 100 round 2` Shared baseline for all medium-camp Haunts Large Haunt

- neutral_trooper_strong GoldReward +` * / 100 round 2` Shared baseline for all large-camp Haunts |}
