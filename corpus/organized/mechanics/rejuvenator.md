---
title: "Rejuvenator"
pageid: 732
source: wiki-md
---

- Get ready to defend the base, they'll be coming for us.

- reacting to the enemy team claiming the Rejuvenator

- Bookworm_enemy_gets_rejuv_03.mp3 The Rejuvenator, also colloquially called Rejuv or Rejuve is a single rune that spawns above the Midboss pit after it is slain. It appears as a large, green crystal.

## Overview

After the Midboss is killed, the Rejuvenator descends over

- get_rejuv_param RejuvinatorDropDuration seconds and cannot be claimed until it fully touches the ground. Once it lands, any player in the match can hit it with a heavy [melee attack](melee attack.md), granting the Rejuvenation Credit buff to their entire team. Each heavy melee hit grants one Rejuvenator Credit to the team, up to 3. Hitting the Rejuvenator also heals the first player who punched it to full health.

## Rejuvenation Credit

The Rejuvenation Credit is a team-wide buff granted to all allies when a Rejuvenator crystal is claimed. The buff lasts 3 minutes or until all credits are consumed, whichever comes first.

When there are

- get_rejuv_param RejuvinatorExpirationWarningTiming seconds left on the buff duration, Heroes are warned that it will expire soon.

The buff allows each player to revive with

- citadel_item_pickup_rejuv RebirthModifier RespawnLifePct % of their health in the place of their death after

- citadel_item_pickup_rejuv RebirthModifier RespawnDelay seconds. Upon [death](death.md), the player respawns in place (and on the ground below them if they died mid-air), loses the buff, and their team's Rejuvenation Credits are reduced by 1 (each player can only consume one credit). The top UI bar displays the remaining Rejuvenation Credits, and players who haven't consumed a credit have a highlight below their net worth. When all credits are used, the buff is removed from all team members.

Killing a player with a Rejuvenation credit does not appear as a kill in the HUD and does not grant any [souls](souls.md), but it does trigger "on hero kill" effects such as the cooldown reset of Shiv's Killing Blow or the [stack](stack.md) buildup of Grey Talon's, Mo & Krill's and Vindicta's ultimates, and of Drifter's Bloodscent. The player is effectively "dead" during the revive countdown, meaning they do not share ally presence-based effects and do not contest the [Unstable Rift](Unstable Rift.md).
