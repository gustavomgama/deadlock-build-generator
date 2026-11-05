---
title: "Ammo"
pageid: 834
source: wiki-md
---

- pic: Clip size icon

- size: 32, also known as Clip Size, is a stat that dictates the maximum number of rounds that can be stored and fired from a weapon. As the weapon is fired, the number of available rounds decreases from the maximum to zero, at which point no more rounds can be fired. Weapons can be [reloaded](Reload Time.md) to regain rounds up to the maximum.

- yu7dzf5ottg

- 360

- description: Video explaining Ammo

## Overview

Ammo is displayed as a number under the [stamina](stamina.md) bars. The left number is the current ammo count, and the right number is the full magazine capacity.

While sliding, the player has infinite ammo, indicated by a light green infinity symbol.

1. Burst fire For burst fire weapons, each shot fired by the player fires more than one bullet in a short burst. The number of bullets fired per shot consumes the equivalent amount of ammo.

1. Alternate fire For heroes who have an alternate fire, shooting with the alt fire consumes more than one ammo round at once. However, the player can still use alt fire with only one round left.

## Base Clip Size

Values referenced from [Hero Comparison Table](Hero Comparison Table.md).

Note: Silver (Transformed) has no ammo count.

- heroClipSizeTable

## Calculation

Ammo is calculated by adding all flat bonuses to your base ammo first, then applying the combined total of all percentage bonuses. Percentage bonuses for ammo are additive, meaning they are added together into a single multiplier.

The formula for Clip Size is: \text{Final Ammo} = (\text{Base Ammo} + \text{Flat Bonuses}) \times (1 + \text{Total Percentage Bonuses}) Note: The final result is always rounded up to the nearest whole number.

1. Example If a hero has 20 Base Ammo and gains the following: +10 Flat Ammo from an item.

+15% Ammo from an item.

+4% Ammo from a [Golden Statue](Golden Statue.md).

The calculation would be: Add the Base and Flat ammo: 20 + 10 = 30.

Add the percentage bonuses together: 15% + 4% = 19% (or 0.19).

Multiply the ammo by the percentage multiplier: 30 × 1.19 = 35.7.

Round up to the nearest whole number: 36.
