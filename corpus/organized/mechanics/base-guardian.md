---
title: "Base Guardian"
pageid: 7236
source: wiki-md
---

- name: Base Guardian

- attack_range: m

## Overview

Each team has 3 sets of 2 Base Guardians at the team's base entrances, one set for each lane. They fight by dealing continuous damage with a laser emitted from their head, targeting all [Troopers](Trooper.md) and [Heroes](Heroes.md) that enter its radius. The Guardians have a different model for each team: [The Archmother](The Archmother.md)'s Guardians are stone statues with a small obelisk inside and a spiked crown, and [the Hidden King](the Hidden King.md)'s Guardians are wicker men with a single large eye for a head and candles at their fingertips.

The Base Guardian's beam deals [Weapon Damage](Weapon Damage.md) and can be mitigated by [Bullet Resist](Bullet Resist.md). Guardians will use a melee attack on enemies within

- npc_barrack_boss MeleeAttemptRange m.

Unlike [Lane Guardians](Lane Guardians.md), Base Guardians don't take [Headshot](Headshot.md) Damage and their melee attacks cannot be parried.

Once the Base Guardians have been killed, a permanent speed boost is applied to the attacking team's zipline in that lane.

[Shrines](Shrines.md) are invulnerable until at least one set of Base Guardians has been destroyed.

## Resistances

Base Guardians mitigate incoming damage from players using multiple different modifiers that stack together multiplicatively: Enemy Scaling [Bullet Resist](Bullet Resist.md): Base Guardians have a scaling Bullet Resist, similar to [Shrines](Shrines.md), that starts at - npc_barrack_boss BackdoorBulletResistModifier BulletResist %, losing

- npc_barrack_boss BackdoorBulletResistModifier BulletResistReductionPerHero % per enemy hero nearby, up to 0% minimum for 2 or more enemies.

Player Vulnerability: A modifier that gives

- npc_boss_tier1 PlayerDamageResistPct % Bullet Resist against players (taking increased damage).

Bullet Resist: Base Guardians have

- npc_barrack_boss IntrinsicModifiers

- 1 BULLET_ARMOR_DAMAGE_RESIST % Bullet Resist.

Because these modifiers stack multiplicatively, players will deal significantly less damage than their base weapon damage in the early game, and significantly more in the late game.

For bullet damage, the resists are stacked together in the following formula: Damage = Bullet Damage * (1-Enemy Resist) * (1-Player Resist) * (1-Bullet Resist) 1. Ability Damage Reduction The following abilities deal reduced damage to Guardians:

## Protection

When [Backdoor Protection](Backdoor Protection.md) is active, Base Guardians have

- npc_barrack_boss BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers % [Damage Resist](Damage Resist.md) and - npc_barrack_boss BackdoorProtectionModifier HealthPerSecondRegen [Health Regen](Health Regen.md) per second.
