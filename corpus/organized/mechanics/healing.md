---
title: "Healing"
pageid: 2124
source: wiki-md
---

Healing is the act of recovering a unit's current [health](health.md), which includes various methods such as [Lifesteal](Lifesteal.md), [Health Regen](Health Regen.md), and [Item](Item.md) effects.

## Overview

The most reliable way for a player to heal themselves is by killing a [Medic Trooper](Trooper.md) and picking up their Medic Pack, collecting [Healing Snacks](Healing Snacks.md) around the map, or by going back to their team's base, which has a constant source of healing. Alternatively, they can buy Healing or [Lifesteal](Lifesteal.md) items. Some heroes also have healing abilities. See a full list of healing sources below.

Besides direct healing, players passively recover health at all times through [Health Regen](Health Regen.md).

## Healing Amp

Healing Amp, also known as Healing Effectiveness, is a [stat](Stats.md) which increases the amount of healing a hero does with their [abilities](abilities.md) and [items](items.md). This affects both healing to themselves and to their allies. Healing Amp affects healing-over-time buffs, such as Healing Rite's active effect.

This [stat](Stats.md) is represented as a percentage. For example, a 25% gain would increase a heal of 100 to 125.

## Healing Reduction

Healing Reduction is a negative effect which reduces the effectiveness of healing on the unit it is applied to.

Healing Reduction is represented as a percentage and stacks multiplicatively.

If a player is hit by the same source of Healing Reduction before its effect has worn off (e.g. two or more enemy players with Healbane ), only the first source is applied.

## Calculation

1. Calculating Healing Reduction Multiple sources of Healing Reduction stack multiplicatively: \text{Total Reduction} = 1 - (1 - R_1) \times (1 - R_2) \dots Example: If two sources of Healing Reduction are applied, one providing 40% and another providing 40%: Convert percentages to decimals: 0.40 and 0.40.

Subtract from 1: (1 - 0.40) = 0.60 and (1 - 0.40) = 0.60.

Multiply the remainders: 0.60 × 0.60 = 0.36.

Subtract from 1: 1 - 0.36 = 0.64.

Total Healing Reduction is 64%, not 80%.

1. Calculating Final Healing \text{Final Healing} = \text{Initial Healing} \times (1 - \text{Total Reduction}) \times (1 + \text{Healing Amp}) Example: A heal of 200 HP is applied to a target with 64% Total Healing Reduction. The healer has 25% Healing Amp.

Apply Reduction: 200 × (1 - 0.64) = 200 × 0.36 = 72 HP.

Apply Amp: 72 × (1 + 0.25) = 72 × 1.25 = 90 HP.

Final Healing received is 90 HP.

Note: Healing that recovers health from self-damage sources such as Victor's Jumpstart and Aura of Suffering isn't counted in the endgame hero stats screen, but it does appear in the healing sources graph.
