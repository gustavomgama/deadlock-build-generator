---
title: "Damage Resistance"
pageid: 922
source: wiki-md
---

Damage Resistance refers to the [Bullet](Weapon Damage.md), [Melee](Melee Attack.md), and [Spirit](Spirit Power.md) Resist statistics which reduce incoming damage taken. Bullet Resist reduces all weapon and melee damage, Melee Resist reduces only melee damage, while Spirit Resist reduces all spirit damage. [Unit](Unit.md)s have a unique "Damage Resistance" stat that is applied to all sources of damage, including [Trooper](Trooper.md)s.

Most resistances stack multiplicatively; they are not added together. Sources of Resistance Reduction are multiplied together separately first. The total reduction is then subtracted from the total resistance. This has the consequence of resistance reduction being more effective on targets with higher resistance.

- kOg7Q-OLwwQ

- 360

- description: Video explaining Damage Resistance

## Resistance types

1. Bullet Resist Bullet Resist reduces all incoming [Weapon Damage](Weapon Damage.md), including from abilities. [Troopers](Troopers.md), [Guardians](Guardians.md), [Neutrals](Neutrals.md) and the [Mid-Boss](Mid-Boss.md) deal weapon damage.

List of abilities that deal weapon damage:

- weapondamage 1. Spirit Resist Spirit Resist reduces all incoming [Spirit Damage](Spirit Damage.md). Most abilities and items deal spirit damage, as well as [Walkers](Walkers.md), [Shrines](Shrines.md), and the [Patron](Patron.md).

1. Melee Resist Melee Resist reduces all incoming [Melee Damage](Melee Damage.md), including from abilities.

In addition to Melee Resist gained from items, Bullet Resist affects all Weapon Damage, granting another source of resistance against Melee Damage. The only exception is - Venator's innate Spirit-scaled Bullet Resist, although this is likely a bug.

List of abilities that deal melee damage: Melee 1. Crit Reduction Crit Reduction is a stat that reduces the critical damage (headshots) received by the hero. Not to be confused with [Crit Bonus Scale](Weapon Damage.md#Crit-Multiplier), a stat that reduces the critical damage dealt by the hero to other targets.

Crit Reduction is an innate stat to balance heroes with large head hitboxes, and cannot be modified by items or abilities.

## Starting Damage Resistance

The following [Heroes](Hero.md) either have starting Damage Resistance values or gain resistance with [Boons](Boon.md) or [Spirit Power](Spirit Power.md). Boon and Spirit scaling resistances stack additively.

Note: Negative values indicate that the hero receives increased damage.

- heroDamageResistTable

## Calculation

While items often display resistance as a flat percentage (e.g., +20% Resist), multiple sources of resistance do not simply add together. Instead, they stack multiplicatively.

1. Calculating Resistance To find your total resistance, use the following formula: \text{Total Resist} = 1 - (1 - R_1) \times (1 - R_2) \dots Example: If you have two sources of resistance, one providing 40% and another providing 20%: Convert percentages to decimals: 0.40 and 0.20.

Subtract from 1: (1 - 0.40) = 0.60 and (1 - 0.20) = 0.80.

Multiply the remainders: 0.60 × 0.80 = 0.48.

Subtract from 1: 1 - 0.48 = 0.52.

Your Total Resist is 52%.

1. Calculating Resistance Reduction Resistance Reduction (often called "shred") acts as a counter to resistance. It is calculated separately using the same multiplicative formula, and then subtracted from the target's resistance.

\text{Final Resist} = \text{Total Resistance} - \text{Total Reduction} Example: A target has 52% Total Resistance (as calculated above). You attack them with two sources of Reduction: one providing 25% and another providing 20%.

Step 1: Calculate Total Reduction 1 - (1 - 0.25) \times (1 - 0.20) = 0.40 \rightarrow \mathbf{40\%} Step 2: Subtract Reduction from Resistance 52\% - 40\% = \mathbf{12\%} The target has a final effective Resist of only 12%.

1. Negative Resistance If the Total Reduction is higher than the Total Resistance, the final value will be negative. This acts as a damage amplifier.

30% Resist: You take 70% of incoming damage.

0% Resist: You take 100% of incoming damage (True Damage).

-30% Resist: You take 130% of incoming damage.

## Effective Health

Include graph of effective health as a function of Damage Reduction. In the mean time, feel free to refer to this [Desmos graph](https://www.desmos.com/calculator/97vhqmutyz).

Include graph of effective damage increase from using 15%, 30%, and 45% Resistance Reduction as a function of the target's original Damage Reduction. In the mean time, feel free to refer to this [Desmos graph](https://www.desmos.com/calculator/u7dkpebmm7).
