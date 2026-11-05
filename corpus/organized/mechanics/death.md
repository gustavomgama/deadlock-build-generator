---
title: "Death"
pageid: 1785
source: wiki-md
---

- [The Hidden King](The Hidden King.md)

- During the ritual, death is temporary. You will return, but know this: the more powerful you become, the longer you stay out of action when you die. Perhaps use that time to go shopping for when you return to the mortal coil.

Death occurs when a [hero](hero.md) takes sufficient damage to be reduced to zero health. Upon dying, the player's screen is shaded gray, a death timer is displayed over their hero's icon, [souls](souls.md) are rewarded to heroes who earned a kill or an assist, and other hero or situation-specific events may occur, as detailed below.

## Overview

Upon dying, heroes will drop any of their unsecured souls in a spherical container that can then be picked up by other heroes.

While dead, players can browse the [shop](shop.md), spectate their teammates, use pings and talk in chat. If all allies are dead, only the [Patron](Patron.md)'s perspective can be seen. Clicking an objective on the [Minimap](Minimap.md) allows the player to view the perspective of that objective.

Once the countdown reaches zero, heroes will respawn back in base.

## Respawn Time

As the game progresses, the players will take longer to respawn. The respawn time increases linearly based on the following times: {| class="wikitable" +Respawn time curves Match duration Respawn time `/60` min Convar

- citadel_player_spawn_time_min_ramp_1 s `/60` min Convar

- citadel_player_spawn_time_max_ramp_1 s `/60` min Convar

- citadel_player_spawn_time_max_ramp_2 s `/60` min Convar

- citadel_player_spawn_time_max_ramp_3 s |} The respawn time is capped at Convar

- citadel_player_spawn_time_max_respawn_time s.

Dying to a non-player [Unit](Unit.md) (when there is no bounty/assist from an enemy Hero) will increase the respawn time by Convar

- citadel_player_spawn_time_in_base_penalty s.

1. Comeback kill After `/60` minutes in a match, killing a player whose net worth is above Convar

- citadel_player_spawn_time_rich_nw_penalty_min_ramp_pct % higher than the killer team's average net worth increases that player's respawn time. The increase varies based on the net worth difference and match duration, from + Convar

- citadel_player_spawn_time_rich_nw_penalty_min_ramp_extratime s for Convar

- citadel_player_spawn_time_rich_nw_penalty_min_ramp_pct % net worth at `/60` minutes to + Convar

- citadel_player_spawn_time_rich_nw_penalty_max_ramp_extratime s for Convar

- citadel_player_spawn_time_rich_nw_penalty_max_ramp_pct % net worth at `/60` minutes.

1. Last Stand Buff Killing the first stage of a [Patron](Patron.md) shortens the remaining respawn time of any dead player in the defending team, as follows: If the remaining time is 30s or above, it is shortened by 20s (e.g. 45s shortened to 25s); If it's between 10s and 30s, it is shortened to 10s; At 10s and below, the respawn time is unchanged.

This effect is only applied once, at the moment the Patron is killed. Subsequent deaths will have the regular respawn time.

1. [Rejuvenator](Rejuvenator.md) Crystal Revive Tokens Revive Tokens are obtained from the Crystal that drops upon killing the [Mid-Boss](Mid-Boss.md). The Crystal contains a total of 3 Revive Tokens.

Revive Tokens can only be claimed by a [Heavy Melee](Melee Damage.md), and only 1 is granted per punch.

Revive Tokens are consumed upon a players death, and any further deaths from that player will not consume more. Once all the Tokens are consumed, the entire team will lose access to the mid-boss buff.

Killing a player with a Rejuvenator credit does not appear as a kill in the HUD and does not grant any [souls](souls.md), but it does trigger "on hero kill" effects such as the cooldown reset of Shiv's Killing Blow or the [stack](stack.md) buildup of Grey Talon's, Mo & Krill's and Vindicta's ultimates. The same happens when triggering Victor's Shocking Reanimation.
