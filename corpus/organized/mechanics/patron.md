---
title: "Patron"
pageid: 622
source: wiki-md
---

- The Patrons must be stopped. No matter the cost.

- Warden select 01.mp3 |-|Patron=

- name: Patron

- health_regen: /s

- bullet_resist: 0

- dps: 440 + 5% HP

- attack_range: m

- voice_actor: Debra Wilson (Archmother)

- information: true |-|Weakened Patron=

- name: Weakened Patron

- health_regen: /s

- bullet_resist: 0

- bullet_damage: + % HP

- dps: (Damage Pulse)

- attack_range: m

- voice_actor: Debra Wilson (Archmother)

- information: true A is a deity which takes the form of a large extraplanar entity. Each team’s base houses a Patron,

- name: The Hidden King and - name: The Archmother, and victory is secured by defeating the opposing team's Patron, completing the ritual.

[The Hidden King](The Hidden King.md) appears as a shadowy figure with antlers and glowing yellow eyes, bound to a burning [wicker man](wikipedia_Wicker_man.md) effigy. Long, claw-like yellow hands extend from the shadows. His base is a factory filled with large speakers and microphones, and his side of the map features working-class red brick buildings labeled "Downtown". [The Archmother](The Archmother.md) wears a broken mask resembling the head of the [Statue of Liberty](wikipedia_Statue_of_Liberty.md), her form bound to a crystalline effigy burning with blue flames. Her base is a museum with a [Neoclassic](wikipedia_Neoclassicism.md) aesthetic, and her side of the map features upper-class white brick buildings labeled "Uptown".

During gameplay, a herald speaks on behalf of the Patrons to their teams, commenting on player performance, announcing major events, and offering boons that allow players to [level up](Level.md).

## Overview

The Patron is a formidable unit found at the back of each team's base. In its first phase, the Patron is completely unkillable until both [Shrines](Shrine.md) are destroyed.

The Patron has two methods of attack in Phase 1: Laser Beam: Fires a slow-moving beam dealing 440 + 5% HP [Spirit Damage](Spirit Damage.md) per second, targeting enemy players and [Troopers](Troopers.md) and reducing their bullet and spirit resistance by %. The beam leaves behind burning ground that deals damage over time to those who remain in it.

Shrine Defense: Creates a large explosion at a Shrine platform after a - npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties AbilityCastDelay s delay, dealing

- npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties Damage +

- npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties DamageHealthPercent % HP [Spirit Damage](Spirit Damage.md) and [cursing](Status Effects.md#Curse) any enemies caught in the blast, forcing them to retreat or be damaged.

After the first half of its health bar is depleted, the Patron enters its second phase. It becomes invulnerable again for a short period as its shadowy form collapses into its structure. The structure then explodes and reforms into an orb that hovers in the pit. Once the transformation completes, it becomes vulnerable again as a Weakened Patron.

Defeating the Patron's first phase shortens the remaining respawn time of any dead players on the defending team by up to 20s (see [Last Stand Buff](Death.md#Last-Stand-Buff)).

The Patron is the only structure that regenerates health out of combat, restoring

- npc_boss_tier3 ObjectiveRegen OutOfCombatHealthRegen health/s. It is also protected by [Backdoor Protection](Backdoor Protection.md), which increases this regeneration by - npc_boss_tier3 BackdoorProtection HealthPerSecondRegen health/s when no enemy Troopers are nearby.

1. Ability Damage Reduction The following abilities deal reduced damage to the Patron:

## Weakened Patron

In its second phase, the Patron enters its Weakened form, compressing into a spherical orb that hovers inside the pit of its team's base. The Hidden King's orb appears as a cracked sphere of charred wood and burning debris, with a glowing ember core visible through the fissures, surrounded by jagged wooden spikes. The Archmother's orb appears as a crystalline blue sphere surrounded by jagged rock shards arranged to form a face-like structure, with glowing cyan energy emanating from within.

In this state, it has two attacks: Damage Pulse: Constantly emits

- npc_boss_tier3 Phase2DamagePulseModifier DamagePerPulse damage every second to up to - npc_boss_tier3 Phase2DamagePulseModifier MaxTargets nearby enemies within a - npc_boss_tier3 Phase2DamagePulseModifier Radius

- 2 m radius.

Pit Explosion: Unleashes a large expanding wave inside the pit after a - npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties AbilityCastDelay s delay, dealing

- npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties Damage +

- npc_boss_tier3 BoundAbilities ESlot_Signature_2 AbilityProperties DamageHealthPercent % HP damage and [cursing](Status Effects.md#Curse) enemies, similar to the Shrine Defense attack. The explosion has a 15s cooldown.

Similar to [Mid Boss](Mid-Boss.md), the Patron is immune to all incoming damage from outside the pit once weakened, forcing players to get in close if they want to damage it. The Weakened Patron has the same starting HP as the first phase but gains more HP per minute than phase one.

The Weakened Patron has 50% damage resistance when an ally has been in the pit for more than 2s, and 100% damage resistance when two or more allies are in the pit.

1. Health Scaling The Patron's maximum health is not static and increases as the match progresses, starting at specific times during each phase.

{| class="wikitable" Phase Scaling Starts At Max Health Gained per Minute Phase 1

- npc_boss_tier3 ObjectiveHealthGrowthPhase1 GrowthStartTimeInMinutes minutes

- npc_boss_tier3 ObjectiveHealthGrowthPhase1 GrowthPerMinute Phase 2

- npc_boss_tier3 ObjectiveHealthGrowthPhase2 GrowthStartTimeInMinutes minute

- npc_boss_tier3 ObjectiveHealthGrowthPhase2 GrowthPerMinute |}
