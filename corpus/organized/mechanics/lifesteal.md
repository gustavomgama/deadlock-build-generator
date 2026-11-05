---
title: "Lifesteal"
pageid: 2343
source: wiki-md
---

Lifesteal is a mechanic which heals a player by a portion of the damage they deal to an opponent. There are two main types of lifesteal, each with an associated [stat](stats.md): Bullet Lifesteal

- pic: AttributeIconBulletLifesteal, which returns a portion of the [bullet damage](Bullet Damage.md) dealt, and - Spirit Lifesteal

- pic: AttributeIconSpiritLifesteal, which returns a portion of the [spirit damage](Spirit Damage.md) dealt. Bullet and Spirit Lifesteal are calculated independently, but use the same formula.

## Calculation

While lifesteal is shown as a percentage (like +20%), different sources of lifesteal do not simply add together. Instead, they stack multiplicatively. This means that as you gain more sources of lifesteal, each new item is slightly less effective than the last.

To calculate your final lifesteal, you can use the following formula: \text{Total Lifesteal} = 1 - (1 - L_1) \times (1 - L_2) \times (1 - L_3) \dots (Where L is the lifesteal value of each source expressed as a decimal, e.g., 0.20 for 20%).

1. Example If you have 22% Bullet Lifesteal from - Fury Trance and 30% Bullet Lifesteal from - Leech, your lifesteal is calculated as follows: Convert the percentages to decimals: 0.22 and 0.30.

Subtract each from 1: (1 - 0.22) = 0.78 and (1 - 0.30) = 0.70.

Multiply those results together: 0.78 × 0.70 = 0.546.

Subtract that result from 1: 1 - 0.546 = 0.454.

Your final Bullet Lifesteal is 45.4%.

Note: The in-game user interface is inconsistent with rounding, so it may display as 45% or 46%.

1. Lifesteal vs. Creeps Lifesteal against creeps (non-hero units) is reduced compared to heroes: Bullet Lifesteal vs. creeps: 60% effectiveness (e.g., 10% lifesteal becomes 6%).

Spirit Lifesteal vs. creeps: 40% effectiveness (e.g., 10% lifesteal becomes 4%).

## Lifesteal Effectiveness

Lifesteal Effectiveness is a stat that modifies a hero's bullet and spirit lifesteal effectiveness. Most heroes have 100% effectiveness.

- Rat King has ``% Lifesteal Effectiveness.

## Bullet Lifesteal

Bullet Lifesteal returns a percentage of all outgoing [bullet damage](Bullet Damage.md) to the player as health.

- Graves has

- get_hero_var

- hero_necro BulletLifesteal

- 3 % innate Bullet Lifesteal.

1. Sources 1. Hero Abilities The following abilities provide Lifesteal:

- lifesteal Abilities that deal weapon damage also provide heal from Bullet Lifesteal. Here are all of the relevant abilities:

- weapondamage

## Spirit Lifesteal

Spirit Lifesteal returns a percentage of all outgoing [spirit damage](Spirit Damage.md) to the player as health.

1. Sources

## Melee Lifesteal

- Lifestrike Melee Lifesteal is provided by abilities such as - Abrams ' Infernal Resilience and - Apollo's Riposte, and heals for a percentage of melee damage dealt. It functions the same as other Lifesteal effects and has 40% effectiveness against creeps.

The item and its upgrade Lifestrike both provide a passive ability which heals the user by a percentage of their [melee damage](Melee Damage.md) dealt, but they behave differently from Lifesteal.

These abilities activate for one melee attack, then go on cooldown for several seconds, during which no further health can be regained from melee attacks. In contrast, Bullet and Spirit Lifesteal are always active and have no cooldowns. These items also grant a flat healing bonus on activation, and are less effective against non-[heroes](hero.md).
