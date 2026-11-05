---
title: "Reload Time"
pageid: 1449
source: wiki-md
---

Reload Time is the time it takes for a [hero](hero.md) to reload their [weapon's](Weapon.md) [ammo](ammo.md) count.

## Overview

Each weapon has either a full or single reload type. Using a [Melee Attack](Melee Attack.md) or [Dashing](Mechanics.md#Movement) will interrupt the reload until the melee or dash animation is finished.

A notable exception is Billy, whose reload is not interrupted when performing a light melee attack.

1. Full Reload and Single Reload Most heroes will reload their weapon's entire magazine at once, with a consistent reload time regardless of ammo left.

- Abrams ' and Silver's weapons are reloaded one shell at a time, and the reload can be interrupted by firing their weapon before it's finished. For these weapons, the time to reload a full magazine depends on how much ammo was left before reloading. These heroes also have a short delay to start reloading after firing their weapon.

- heroReloadDelayTable 1. Base Reload Time Values referenced from [Hero Comparison Table](Hero Comparison Table.md).

Notes: Abrams and Silver take `*round2`s and `*`s to reload a full starting ammo clip, respectively (not counting reload delay).

- Silver (Transformed)'s reload is incorrect, since she has no reload.

- heroReloadTable

## Items

- Reload Time There are several items that bypass reloading completely, and will instantly reload the player's weapon.

- Active Reload allows the player to skip 50% of the reload by adding a quick-time event in the reload bar. Active Reload's activation window lasts 0.3s.

- Crushing Fists will restore

- get_prop Crushing Fists LightMeleeAmmo ammo on a light melee and 30% ammo on a heavy melee.

- Quicksilver Reload and Mercurial Magnum will reload the player's weapon when using the ability imbued by this item.

- Vampiric Burst will cancel reloading and add

- get_prop Vampiric Burst ActiveReloadPercent base ammo to the player's clip, adding bonus ammo to any amount over the clip capacity.
