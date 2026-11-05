---
title: "Move Speed"
pageid: 831
source: wiki-md
---

Move Speed is a stat that [heroes](heroes.md) start with and can obtain more through [items](items.md). Move speed dictates how many meters per second the hero will move.

## Overview

Heroes will accelerate up to base movement speed velocity from a standstill. Move Speed bonuses from items and abilities stack diminishingly, meaning adding more speed provides progressively less value.

While firing, a hero's movement speed is reduced to 75% of its normal value (with the exception of Rem and Silver (Transformed) ), which can be mitigated by Fleetfoot. This is calculated based on Move Speed + Sprint Speed. There is no penalty while zooming in. While crouched, all heroes have 4.8 m/s crouch speed not affected by the movement speed penalty, except for Grey Talon and Warden, whose movement speed penalty while firing applies while crouched, becoming 4.4 m/s.

Some heroes have [Spirit Scaling](Spirit Scaling.md) affecting their Move Speed and Sprint Speed. See "Base Move and Sprint Speed" table below.

1. Sprint Speed Sprint Speed is a related stat that is conditionally added to a hero's move speed when a hero is out of combat for five seconds, and persists until entering combat or zooming in. Zooming in while sprinting resets the player's speed back to base move speed.

If the hero has more than 2.5m/s Sprint Speed, the rest of the sprint speed will be added to the hero's movement at a rate of 0.6m/s/s as the player moves. While capped at the hero's Sprint Speed stat, sprinting will continue building up past its current max value, meaning bonuses applied while sprinting (e.g.

- Healing Rite ) will instantly increase current Move Speed. Taking damage, shooting enemy [Heroes](Heroes.md), getting [Stunned](Crowd Control.md#Stun), [Immobilized](Crowd Control.md#Immobilize), [Displaced](Crowd Control.md#Displace) or [Slept](Crowd Control.md#Sleep), using a [Zipline](Ziplines.md), [Crouching](Crouching.md), or stopping movement input will reset this counter. Holding two opposing inputs, such as forward and back while trying to turn around, counts as stopping movement unless left or right are also held.

Performing a [light melee](light melee.md), [heavy melee](heavy melee.md), shooting [Haunt](Haunt.md) camps (as long as no damage is taken) or [Breakables](Breakables.md), [Sliding](Sliding.md), using a [Teleporter](Teleporter.md), flying on the Magic Carpet, or walking into walls or corners does not interrupt sprinting. Because sliding can transition to crouching, it can interrupt sprinting if held until a full stop or while sliding into a wall. Sprint speed can be built up in a teleporter by walking into a wall and maintained after teleporting.

1. Slide Heroes moving above 8.9 m/s can slide on a flat horizontal surface by crouching.

Due to Fleetfoot's move speed increase, all heroes can "perma-slide" with Fleetfoot's active effect by repeatedly crouching on flat surfaces.

## Calculation

1. Calculating Move Speed While items often display movement speed bonuses as flat values (e.g., +2 m/s), multiple sources of move speed do not simply add together. Instead, they stack multiplicatively using a similar formula to [resistance](Damage Resistance.md), meaning each additional source provides diminishing returns.

To find your effective move speed bonus, use the following formula: \text{Effective Move Bonus} = 12 \times (1 - (1 - \frac{B_1}{12}) \times (1 - \frac{B_2}{12}) \dots) Where B_1, B_2, etc. are individual move speed bonuses.

Then calculate your total speed: \text{Total Speed} = \text{Base Move Speed} + \text{Effective Move Bonus} + \text{Base Sprint Speed} + \text{Sprint Bonus}_1 + \text{Sprint Bonus}_2 \dots Example: If you have two sources of move speed, one providing +2 m/s and another providing +3 m/s: Divide each bonus by 12: {\approx}0.167 and 0.25.

Subtract from 1: (1 - 0.167) = \textbf{0.833} and (1 - 0.25) = \textbf{0.75}.

Multiply the remainders: 0.833 \times 0.75 = \textbf{0.625}.

Subtract from 1: 1 - 0.625 = \textbf{0.375}.

Multiply by 12: 0.375 \times 12 = \textbf{4.5 m/s}.

Your Effective Move Bonus is 4.5 m/s (not 5 m/s).

If your hero has 6.5 base move speed, 1.6 base sprint speed, and no sprint bonuses: 6.5 + 4.5 + 1.6 = \mathbf{12.6 m/s} 1. Sprint Speed Stacking Unlike move speed, sprint speed stacks additively with no diminishing returns. If you have base 1.6 sprint speed and get items with +2 and +5 sprint speed, you simply have 8.6 sprint speed.

\text{Total Sprint} = \text{Base Sprint} + \text{Bonus}_1 + \text{Bonus}_2 \dots 1. Combined Example A hero with: 6.4 base move speed 1.6 base sprint speed +2 and +3 move speed bonuses +2 and +1.5 sprint speed bonuses Step 1: Calculate Move Speed 12 \times (1 - (1 - \frac{2}{12}) \times (1 - \frac{3}{12})) = 4.5 \text{ m/s effective} 6.4 + 4.5 = \mathbf{10.9 \text{ m/s Step 2: Calculate Sprint Speed 1.6 + 2 + 1.5 = \mathbf{5.1 \text{ m/s Step 3: Add Together 10.9 + 5.1 = \mathbf{16.0 \text{ m/s

## Base Move and Sprint Speed

Values referenced from [Hero Comparison Table](Hero Comparison Table.md).

"Total Speed" is the sum of Move Speed and Sprint Speed. "Shooting Speed" is Total Speed multiplied by Shooting Mult.

- heroMoveSpeedTable
