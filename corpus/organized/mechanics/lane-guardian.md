---
title: "Lane Guardian"
pageid: 647
source: wiki-md
---

- name: Guardian

- spirit_resist: 0

- attack_range: m

## Overview

Lane Guardians are large metal automatons with a fiery brazier as a head. They fight by dealing continuous damage with a laser emitted from their torch, targeting all [Troopers](Trooper.md) and [Heroes](Heroes.md) that enter its radius. There are 3 Lane Guardians per team, one for each lane.

When there are no enemy troopers or players within

- npc_boss_tier1 InvulRange m, the Guardian enters an invulnerable state, where it cannot be damaged by any means. When a trooper or enemy player enters the guardian's range, it will become vulnerable, targeting its laser onto the closest nearby enemy and dealing constant damage over time. However, the Guardian will not take any damage from the player if the player is outside the Guardian's range, even if it is vulnerable to troopers. Guardians take headshot damage to their "head," the brazier on top of their body.

The Guardian's beam deals [Weapon Damage](Weapon Damage.md) and can be mitigated by [Bullet Resist](Bullet Resist.md).

Guardians will target an enemy player if that enemy damages an allied player and is within 15 meters of the Guardian.

When a player or a melee trooper enters close range (

- npc_boss_tier1 MeleeAttemptRange m) of a Guardian, the Guardian will repeatedly use [melee attacks](Melee Attack.md) until the player/trooper is either killed or leaves melee range. The melee attacks can be [parried](Parry.md) by the player. If the Guardian is parried, it will be stunned for 2s, then it will switch to the laser attack and be unable to use melee again for 5s.

When a Guardian is destroyed, its soul bounty is granted to every alive hero on the team that destroyed it.

Lane Guardians don't have [backdoor protection](backdoor protection.md), allowing a player to deal normal damage to a Guardian even if the enemy [zipline](zipline.md) is pushed.

## Resistances

Guardians mitigate incoming damage from players using multiple different modifiers that stack together multiplicatively: Time Scaling [Damage Resist](Damage Resist.md): Lane Guardians have a scaling Damage Resist that applies to all damage types, except [Pure Damage](Pure Damage.md). Starts at 50% and decays linearly down to -50% (taking increased damage) over the first 12 minutes of the match (-% resist per second).

Player Vulnerability: A modifier that gives

- npc_boss_tier1 PlayerDamageResistPct % Bullet Resist against players (taking increased damage).

Bullet Resist: Lane Guardians have

- npc_boss_tier1 IntrinsicModifiers

- 1 BULLET_ARMOR_DAMAGE_RESIST % Bullet Resist.

Because these modifiers stack multiplicatively, players will deal significantly less damage than their base weapon damage in the early game, and significantly more in the late game.

The resists are stacked together in the following formulas: For bullet damage: Damage = Bullet Damage * [(1 - Base Damage Resist) + (time/720)] * (1-Player Resist) * (1-Bullet Resist) For spirit damage: Damage = Spirit Damage * [(1 - Base Damage Resist) + (time/720)] In which "time" is the match time in seconds.

Applying the bullet damage values, we get: Damage = BD * [0.5 + (t / 720)] * `/100)` * `)/100` 1. Ability Damage Reduction The following abilities deal reduced damage to Guardians:
