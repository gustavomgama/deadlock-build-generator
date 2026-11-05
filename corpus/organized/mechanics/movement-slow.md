---
title: "Movement Slow"
pageid: 1731
source: wiki-md
---

Movement Slow is a status effect applied by many items and abilities that slows [move speed](move speed.md) by a percentage.

Movement Slow cannot reduce a player's speed below 2.0 m/s in-game (or 80 hammer units per second).

## Notes

The displayed speed in-game in m/s is rounded to the nearest decimal for all numbers under 10 m/s.

## Calculation

1. Stacking Multiple Slows While abilities and items display slow percentages (e.g., 30%), multiple sources of movement slow do not simply add together. Instead, they stack multiplicatively.

To find your total slow percentage, use the following formula: \text{Total Slow} = 1 - (1 - \text{Slow}_1) \times (1 - \text{Slow}_2) \times...

Example: If you are affected by two slows, one providing 30% and another providing 25%: Convert percentages to decimals: 0.30 and 0.25.

Subtract from 1: (1 - 0.30) = 0.70 and (1 - 0.25) = 0.75.

Multiply the remainders: 0.70 × 0.75 = 0.525.

Subtract from 1: 1 - 0.525 = 0.475.

Your Total Slow is 47.5%.

1. Calculating Final Speed Once you have the total slow percentage, apply it to your speed. However, movement slow is calculated using 2.0 m/s as a floor - you cannot be slowed below this speed.

\text{Slowed Speed} = ((\text{Current Speed} - 2) \times (1 - \text{Total Slow})) + 2 Example: If you are moving at 10 m/s and have 50% total slow: Subtract the floor: 10 - 2 = 8.

Apply the slow: 8 × (1 - 0.50) = 8 × 0.50 = 4.

Add the floor back: 4 + 2 = 6 m/s.

1. Movement Slow Resist Movement Slow Resist reduces the final calculated slow percentage. Multiple sources of Movement Slow Resist stack additively (not multiplicatively).

\text{Actual Slow} = \text{Total Slow} \times (1 - \text{Resist}_1 - \text{Resist}_2 -...) Example: If you have 47.5% total slow and 30% Movement Slow Resist: 47.5\% \times (1 - 0.30) = 47.5\% \times 0.70 = \mathbf{33.25\%}
