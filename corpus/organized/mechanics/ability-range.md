---
title: "Ability Range"
pageid: 1495
source: wiki-md
---

[Ability Range](Ability Range.md) determines the effective distance and cast range of hero abilities and items. It is measured in a distance of meters, and stat gains are measured in percentages.

For example, [Shiv](Shiv.md)'s Slice and Dice ability has a dash range of 12 meters. Purchasing [Mystic Expansion](Mystic Expansion.md) improves this by 35%, making the new effective dash range of the ability 16.2 meters.

The range of [Active Items](Active Items.md) does not consider height and their cast range is shaped like a cylinder. This means their range can be greater than expected when targeting heroes above or below the player. For example, a Seven casting Storm Cloud directly above a group of enemies will always be within range of Phantom Strike or Cursed Relic no matter how high up he is. Likewise, jumping does not make it easier to target flying enemies, and being on top of a rooftop or vantage point does not hinder the range of items.

## Calculation

1. Calculating Ability Range Multiple sources of Ability Range stack multiplicatively, not additively: \text{Total Ability Range} = 1 - (1 - R_1) \times (1 - R_2) \dots Example: With TechRangeMultiplier % from and TechRangeMultiplier % from: Convert percentages to decimals: TechRangeMultiplier % to

- |TechRangeMultiplier / 100 and TechRangeMultiplier % to

- |TechRangeMultiplier / 100.

Subtract from 1: (1 - ) = `` and (1 - ) = ``.

Multiply the differences: `` × `` =

- ) * (1 - ) round 4.

Subtract from 1: 1 - = ` round 4`.

Total Ability Range bonus is `) * 100`%, not ` + ) * 100 round 1`%.
