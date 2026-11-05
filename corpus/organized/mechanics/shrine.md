---
title: "Shrine"
pageid: 730
source: wiki-md
---

- name: Shrine

- max_health: /

## Overview

The [Hidden King](Hidden King.md) shrine resembles a speaker tower with three large loudspeakers and three smaller ones, all mounted on an inscribed hexagonal platform with a candle placed at each point. A glowing magical symbol sits at the center of the speakers. The shrine is primarily colored orange to match the Hidden King’s theme, and it faces the Hidden King patron, appearing to transmit sound waves toward it.

In contrast, the [Archmother](Archmother.md) shrine takes the form of a blue-lit platform, fitting the Archmother theme, topped by a book stand holding a magical tome. A hexagon is also inscribed on the platform, surrounded by magical sigils and inscriptions. The book periodically flips open and appears to emit magical energy directed toward the Archmother patron.

Shrines are found in pairs within each team's base, located on opposite sides to each other. The Patron will defend any that are under attack with a beam that deals damage and [curses](Status Effects.md#Curse) players in or near the Shrine platform. Shrines start with - destroyable_building MaxHealthGenerator HP. When one shrine is destroyed, the other shrine's HP is increased to - destroyable_building MaxHealthGeneratorSecond.

## Resistances

Shrines are completely invulnerable to damage until at least one pair of [Base Guardians](Base Guardians.md) has been destroyed, and are also immune to damage from any source outside their platform.

Shrines have

- destroyable_building IntrinsicModifiers

- 1 BULLET_ARMOR_DAMAGE_RESIST % [Bullet Resist](Bullet Resist.md).

Additionally, like [Base Guardians](Base Guardians.md), Shrines have enemy scaling Bullet Resist. It starts at - destroyable_building BackdoorBulletResistModifier BulletResist %, losing

- destroyable_building BackdoorBulletResistModifier BulletResistReductionPerHero % per enemy hero nearby, up to 0% minimum for 3 or more heroes. This is added multiplicatively to the base Bullet Resist.

When [Backdoor Protection](Backdoor Protection.md) is active, they have

- npc_barrack_boss BackdoorProtectionModifier BackdoorProtectionDamageMitigationFromPlayers % [Damage Resist](Damage Resist.md) and - npc_barrack_boss BackdoorProtectionModifier HealthPerSecondRegen [Health Regen](Health Regen.md) per second.

1. Ability Damage Reduction The following abilities deal reduced damage to Shrines:

## Destruction

Once a shrine is destroyed, [Troopers](Troopers.md) allied to the team that destroyed the shrine become Super Troopers for that shrine's lane. Blue lane only gets Super Troopers when both shrines are destroyed. Super Troopers gain

- trooper_base ShrinesDownBuffModifier DamageScale % damage, ` - 1) * 100`% health, and yield 15% less souls when killed. Once both Shrines have been destroyed, the enemy Patron will become vulnerable to damage.
