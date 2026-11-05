---
title: "Spirit Power"
pageid: 674
source: wiki-md
---

Spirit Power is a [stat](stats.md) that increases the effectiveness of [abilities](Ability.md) and [items](items.md). In addition to increasing Spirit Damage, Spirit Power can also increase miscellaneous ability attributes that are not otherwise broadly covered by [spirit stats](spirit.md). Spirit Power is generally useful on all heroes, but some will benefit much more than others due to better scaling coefficients.

- lLwVMFC-nhQ

- 360

- description: Video explaining Spirit Power and Spirit Damage

## Spirit Power Scaling

When an ability or item can be [scaled](Scaling.md) by spirit power it will be indicated with a purple upward trending arrow and the spirit star icon. The effectiveness of spirit power on a given ability is based on its spirit power coefficient shown after the spirit scaling icon e.g.

- 0.5. Using that spirit power coefficient, spirit damage can be represented with the formula: \mathit{Spirit Damage} = \mathit{Base Damage} + (\mathit{Spirit Power} * \mathit{Spirit Power Coefficient}) For example, Lash's Flog ability deals 65 base damage and has a spirit power coefficient of - 0.8. In a case where it was being buffed by 20 spirit power, the calculation would be as follows: \mathit{Spirit Damage} = 65 + (20 * 0.8) = 81 The same principle applies to items. For instance, [Tesla Bullets](Tesla Bullets.md) deals 33 base damage with a coefficient of - 0.19. If you have 76 spirit power, its damage becomes: \mathit{Spirit Damage} = 33 + (76 * 0.19) = 47.44 In general this represents linear scaling, with the rate of increase being determined by the spirit power coefficient. In most cases, the spirit power coefficient can be obtained by hovering over the skill while pressing the Extra Info hotkey.

Note: Obtaining exact calculations can be difficult because the spirit scaling values are rounded to the nearest tenth. This can lead to inaccurate calculations when trying to apply the above formula. In general, it is possible to obtain good approximations of spirit power's affect on damage but exact calculations often require sandbox testing to obtain the un-rounded scaling values.

1. Abilities that scale with Spirit Power

- scalingspirit

- collapsed: yes 1. Items that scale with Spirit Power Alchemical Fire deals up to - get_prop Alchemical Fire DPSMax Value Spirit Damage per second in an area.

- Mystic Shot makes the player's bullet deal

- get_prop Mystic Shot ProcBonusMagicDamage Value Spirit Damage every

- get_prop Mystic Shot AbilityCooldown seconds.

- Tesla Bullets deals

- get_prop Tesla Bullets DamagePerChain Shock Damage on hit and on jump (reduced by [Damage Falloff](Damage Falloff.md)).

- Torment Pulse deals

- get_prop Torment Pulse DamagePulseAmount Pulse Damage every

- get_prop Torment Pulse AbilityCooldown s.

- Toxic Bullets deals

- get_prop Toxic Bullets DotHealthPercent Bleed Damage based on current health per second.

## Bonus Spirit Power

Flat bonus spirit power from all sources is added equally to the player's current spirit power (unlike [Weapon Damage](Weapon Damage.md) and [Health](Health.md), in which the bonus values are calculated separately from the base values).

Sources of bonus percent (%) spirit power, such as - Boundless Spirit, stack multiplicatively with other bonus % sources, and apply to the player's current spirit power at all times.

## Spirit Damage

Spirit Damage is a form of damage dealt by most [abilities](Ability.md) and some [items](items.md). It is modifiable by obtaining Spirit Power, and scales with the respective ability or item's Spirit [Scaling](Scaling.md). Certain items will deal additional Spirit Damage if a condition is met.

1. Spirit Resistance Damage Resistance Incoming damage is reduced by the target's Spirit Resist and increased by the attacker's Spirit Resist Reduction. These stats stack multiplicatively. For a detailed breakdown on how multiple items stack, see the main page.

1. NPCs Attacks from [Walkers](Walkers.md), [Shrines](Shrines.md) and [Patrons](Patrons.md) deal Spirit Damage.

## Spirit Scaling by Hero

- heroSpiritTable The following heroes have base stats that scale with Spirit Power.

- write_spirit_scaling_table TechPower

- title: Base Spirit Power based on Boons
