---
title: "Ability Cooldown"
pageid: 1445
source: wiki-md
---

Ability Cooldown is the time it takes for an [Ability](Ability.md) to be usable again.

## Overview

Cooldowns range from a few seconds, as in Lady Geist's Malice, to a few minutes, as in Dynamo's Singularity. Ability cooldowns can be reduced by acquiring the Cooldown Reduction stat, which reduces the cooldown by a percentage of base [ability](ability.md) time.

In the in-game HUD, ability cooldowns only show decimal values below 2s.

Unlike [Ability Range](Ability Range.md) and [Ability Duration](Ability Duration.md), ability cooldown does not affect items. Items are only affected by a separate stat called [Item Cooldown Reduction](Ability Cooldown.md#Item-Cooldown) which is granted by Transcendent Cooldown.

1. Charged Abilities Some abilities can acquire multiple charges. In those cases, the ability cooldown represents the time for a charge to become available again after being used. This should not be confused with the time between charges, which describes the delay after using a charge that a different charge can be used.

## Calculation

1. Calculating Cooldown Reduction Despite being presented in-game as +X% Cooldown Reduction, multiple sources stack multiplicatively, not additively: \text{Total Cooldown Reduction} = 1 - (1 - CR_1) \times (1 - CR_2) \dots Example: With CooldownReduction % from and CooldownReduction % from: Convert percentages to decimals: CooldownReduction % to

- |CooldownReduction / 100 and CooldownReduction % to

- |CooldownReduction / 100.

Subtract from 1: (1 - ) = `` and (1 - ) = ``.

Multiply the remainders: `` × `` =

- ) * (1 - ) round 4.

Subtract from 1: 1 - = ` round 4`.

Total Cooldown Reduction is `) * 100 round 1`%, not ` + ) * 100 round 1`%.

## Item Cooldown

Item Cooldown is the time it takes for an [Item](Item.md) to be usable again. This includes both [Active](Active.md) and Passive items.

[Charge-Up](Charge-Up.md) items such as Tankbuster and Mercurial Magnum are not affected by Item Cooldown Reduction.

1. Sources of Item Cooldown Reduction Item Cooldown Reduction
