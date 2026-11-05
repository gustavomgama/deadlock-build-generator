---
title: "Fire Rate"
pageid: 836
source: wiki-md
---

, also known as Bullets Per Second, is a stat that determines the amount of [ammo](ammo.md) that will be fired by the weapon per second.

Its inverse is called gun cycle time, which instead measures seconds per bullet.

Several heroes have [abilities](abilities.md) that increase their Fire Rate to shoot faster, and it can also be decreased, primarily through enemy [items](items.md). All bonuses and slows are combined into a single total modifier, which is then applied to the hero's base Fire Rate.

## Calculation

1. Total modifier Bonuses and slows are combined under separate rules: positive bonuses are additive, while slows are multiplicative.

\text{Total Modifier} = (\text{Sum of Bonuses}) - (\text{Total Slows}) Where: Sum of Bonuses = all positive bonuses added together (e.g.,

- /100 + /100 ) Total Slows = the result of multiplying the remaining values of each slow: (1 - \text{Slow}_1) \times (1 - \text{Slow}_2) \times \dots Any total modifier lower than -50% is capped at that value.

1. Applying the modifier The total modifier is not applied the same way in both directions. Its effect depends on its sign: If the total modifier is positive, it increases Fire Rate directly: \text{Final Fire Rate} = \text{Base Fire Rate} \times (1 + \text{Total Modifier}) If the total modifier is negative, it instead increases the gun cycle time, the interval between shots: \text{Final Fire Rate} = \frac{\text{Base Fire Rate{1 + |\text{Total Modifier}|} Because a negative modifier lengthens the interval rather than shortening the rate, it reduces the number of bullets fired per second by less than its stated value: A -10% modifier leaves % of base Fire Rate.

A -25% modifier leaves % of base Fire Rate.

A -50% modifier, the maximum, leaves % of base Fire Rate, a reduction of only % in bullets per second.

Positive modifiers have no equivalent discrepancy: a +50% modifier grants a full 50% more bullets per second. The in-game UI reports the total modifier itself, not the resulting change in bullets per second.

1. Examples 1. Combined bonuses and slows For an example with multiple sources: + Ricochet BonusFireRate % Fire Rate from Ricochet + Swift Striker BonusFireRate % Fire Rate from Swift Striker Vexing Bolt

- Upgrades.1.FireRateSlow % Fire Rate Slow from Sinclair's Vexing Bolt Suppressor FireRateSlow % Fire Rate Slow from an enemy's Suppressor First, the groups are calculated separately: Bonuses:

- /100 + /100 + )/100 Slows:

- (1 - /100 ) \times (1 - /100 ) /100 \times /100 /100) * (1 - /100) They are then combined into the total modifier:

- \text{Total Modifier} + )/100 - (1 - /100) * (1 - /100) ) + )/100 - /100) * (1 - /100) + )/100 - (1 - (1 - /100) * (1 - /100))) round 4 Because the total modifier is negative, it is applied to the gun cycle time:

- \text{Final Fire Rate} \frac{\text{Base Fire Rate} }{1 + + )/100 - (1 - (1 - /100) * (1 - /100))) round 4 } + )/100 - (1 - (1 - /100) * (1 - /100))))) round 3 \times \text{Base Fire Rate} The hero therefore fires ` + )/100 - (1 - (1 - /100) * (1 - /100))))) * 100) round 1`% fewer bullets per second, while the in-game UI displays the total modifier of ` + )/100 - (1 - (1 - /100) * (1 - /100))) * 100 round 0`%, rounded to the nearest whole number.

1. Maximum slow reduction For an example with only slows applied: No positive Fire Rate bonuses (0) Vexing Bolt

- Upgrades.1.FireRateSlow % Fire Rate Slow from Sinclair's Vexing Bolt Suppressor FireRateSlow % Fire Rate Slow from an enemy's Suppressor Rusted Barrel FireRateSlow % Fire Rate Slow from an enemy's Rusted Barrel The calculation is:

- 0 - (1 - (/100 \times /100 \times /100 ))

- 0 - (1 - /100) * (1 - /100) * (1 - /100) ) /100) * (1 - /100) * (1 - /100))) round 4 This results in a calculated modifier of `/100) * (1 - /100) * (1 - /100))) * 100 round 2`%. Due to the cap, the value is raised to the maximum of -50%, which is then applied to the gun cycle time:

- \text{Final Fire Rate} \frac{\text{Base Fire Rate} }{1 + 0.5} \times \text{Base Fire Rate} Even under the maximum possible slow, the hero still fires two thirds of the bullets per second of an unslowed hero.

## Base Fire Rate

Values referenced from [Hero Comparison Table](Hero Comparison Table.md).

- heroRoundsPerSecondTable Notes: Due to a bug, The Doorman's and Paige's weapons have incorrect fire rate values listed in the game UI. The values listed here are accurate.

- McGinnis ' and Victor's weapons have a wind-up time before reaching maximum fire rate.
