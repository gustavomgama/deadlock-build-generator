---
title: "Midboss"
pageid: 627
source: wiki-md
---

- name: Midboss

- health_regen: HP/s

- attack_range: m, also colloquially called Mid Boss or Temple Guardian is a powerful [Haunt](Haunt.md) with strong attacks and a regenerating shield to defend itself. [Heroes](Heroes.md) may attempt to kill Midboss which immediately grants [permanent buffs](Permanent Buffs.md) for the team that defeats it, as well as an opportunity to obtain [Rejuvenator](Rejuvenator.md) Credits, allowing heroes to revive upon death.

## Overview

At the beginning of the match, the Midboss will spawn underground in the sewers in the center of the [map](The Cursed Apple.md). While the Midboss is alive, a golden Rejuvenator symbol will appear at its location in the minimap.

The path to the Midboss' pit can be found in entrances marked with the Rejuvenator sign, at the [Broadway](Lanes.md). These entrances will also have a glowing Rejuvenator symbol above them when the Midboss has respawned.

The Midboss is initially dormant and will not attack anyone outside its pit. As soon as a player has entered the pit, the Midboss will attack by channeling a bright purple beam onto them, dealing [Weapon Damage](Weapon Damage.md). If multiple players are inside the pit, it will prioritize the closest one. Additionally, the Midboss can only be damaged by players who are inside its pit, and will be completely invulnerable to outside attacks.

Unlike most units, Midboss has a special shield surrounding it at all times that prevents it from taking health damage. In order to actually harm it, enough damage needs to be dealt to deplete the constantly regenerating shield, which can prove difficult for individual or unprepared players. The damage shield starts at - npc_super_neutral ShieldLogic BaseAbsorptionPerSecond HP and increases at - npc_super_neutral ShieldLogic ScalingAbsorptionPerMinute HP/minute.

Once Midboss has reached 50% Health, it will roar, announcing to both teams that it is close to death.

1. Health Scaling Midboss' Health scales linearly from when it spawns. For every minute that passes after it has spawned, it gains an additional

- npc_super_neutral HealthGainPerMinute Health, which is added to its

- npc_super_neutral StartingHealth Base Health.

## Death

When the Midboss is slain, the killing team gains (+ /min) souls, 2 [permanent buffs](Permanent Buffs.md) per player, and a Rejuvenator crystal spawns above the pit to begin its slow descent, which takes 6 seconds. The descent of the crystal is accompanied by a musical stinger that plays for both teams. The Rejuvenator crystal is not targetable as it descends and cannot be claimed until it has fully landed on the ground.

Once landed, attacking the crystal with a heavy [melee attack](melee attack.md) grants a Rejuvenator Credit to the entire team. Each heavy melee hit on the crystal grants one credit, up to 3 for each Midboss kill. The first credit claimed will also grant a 100% heal to the hero. Either team may take rejuvenator credits regardless of which team kills the Midboss, allowing for players to steal rejuvenators after the Midboss has been slain.

1. Rejuvenator Credit Rejuvenator The Rejuvenator credit grants all team members a buff that allows them to revive with - citadel_item_pickup_rejuv RebirthModifier RespawnLifePct % health in the place of their death after

- citadel_item_pickup_rejuv RebirthModifier RespawnDelay s. When a player dies, they respawn in place, lose the buff, and their team’s Rejuvenator credits are reduced by 1 (each player can consume only one credit).

The Rejuvenator credit lasts 3 minutes. The top UI bar displays the remaining Rejuvenator credits. Once all credits are used, the buff is removed from all team members.

## Respawn

The Midboss respawns `/60` minutes after its first death. Then it respawns 6 minutes after its second death, and 5 minutes after its third and subsequent deaths.

The respawns are announced through a loud roar, followed by the [Patron](Patron.md)'s Herald announcing "Midboss has arrived".

A timer until the Midboss respawn can be seen as its icon fills up in the minimap. Pressing Tab shows players the exact time in minutes/seconds.
