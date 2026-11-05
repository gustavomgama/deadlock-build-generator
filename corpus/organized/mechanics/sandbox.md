---
title: "Sandbox"
pageid: 62299
source: wiki-md
---

- Need to add new settings from City Never Sleeps

- Ready to do some field testing.

- Mcginnis_select_06.mp3 The Sandbox is a map in [Deadlock](Deadlock.md) in which players can test the various [mechanics](mechanics.md) of the game.

## Overview

Players can access the Sandbox from the Play menu or by entering the [Teleporter](Teleporter.md) in the [Hideout](Hideout.md)'s Atrium. Once in the Sandbox, entering the Teleporter will bring them back to the Atrium.

Players spawn in front of a [Curiosity Shop](Curiosity Shop.md) (though they can buy [items](items.md) anywhere on the map). The spawn area heals the player. There is a yellow [Zipline](Zipline.md) circling the building behind the shop.

To the left, there is a small garden with an ally and enemy [Lane Guardian](Lane Guardian.md) on each side, and an area with an enemy [Walker](Walker.md) further to the left. [Trooper](Trooper.md)s will spawn behind each Guardian and fight each other.

To the right, there is an ally and enemy Test Dummy hero next to a shooting range. In the front behind the truck, another Test Dummy runs left to right. There's a [Cosmic Veil](Cosmic Veil.md), a [Rope](Rope.md), a [Jump Pad](Jump Pad.md), two [Powerups](Powerups.md), a [Rejuvenator](Rejuvenator.md), and a pair of [Teleporter](Teleporter.md)s. Further to the right, the Gym has a Dummy that will [melee](melee.md) players to train [parry](parry.md) timing. In the room labeled "Storage" in the back, there is a [Neutral](Neutral.md) camp with a small, medium and large Neutral.

## Settings

These settings are also used in the "Explore NYC" mode.

1. Hero Tools Note: All hero tool settings also apply to the mimic/puppet if the player is controlling one.

Change Hero: change the player's hero Change Team: change to enemy team and choose hero Reset Hero (resetme): reset to level 0 with no ability upgrades Level Up (givelevelupgold 1): level the player up by 1 Max Level (givelevelupgold ): set level to Half Health (healthpct 50): set the player to half health Full Health (healthpct 100): set the player to full health Kill Hero (lethaldamageme): kill the player All Perks (giveallupgrades): unlock all ability upgrades Spawn Camp (citadel_spawn_nearby_neutrals): spawn jungle camp 1. Game Rules No Death: heroes can't die (NPCs can still die) No Reload: weapons have infinite ammo No Cooldown: set all cooldowns to 1s (not actually instant) Fast Stamina: make stamina cooldown faster Speed- (host_timescale_dec): slow game time Speed= (host_timescale 1.0): reset to default speed Speed+ (host_timescale_inc): speed up game time 1. Hero Control Take Control (citadel_assume_pawn_control): take control of the target hero Remove Bots (bot_kick_all): remove all bot heroes from the map, including Dummies Hero to spawn (hero portrait): select which hero will be spawned as enemy or friendly As Enemy: spawn enemy hero based on the player's crosshair As Friendly: spawn friendly hero based on the player's crosshair Make Mimic (bot_mimic_target): make target hero mimic the player Make Puppet (bot_puppet_target): switch control to the target hero from the current hero's perspective Clear Follow (bot_mimic 0; bot_puppet 0): reset mimic or puppet

## Known Bugs

If the player goes back to the Hideout via the menu while in puppet mode, they won't be able to move their hero in the Hideout. This can only be fixed by using "Clear Follow" in [console](Console commands.md) (bot_puppet 0), or by closing and re-opening the game.
