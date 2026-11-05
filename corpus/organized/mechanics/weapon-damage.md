---
title: "Weapon Damage"
pageid: 850
source: wiki-md
---

Weapon Damage is a stat that determines the player's [Bullet Damage](Bullet Damage.md), and also increases their [Melee Damage](Melee Damage.md). Some [abilities](abilities.md) can deal Weapon Damage.

- xGTD-bBA57M

- 360

- description: Video explaining Weapon Damage

## Base Weapon Properties

1. Base Bullet Damage Base Bullet Damage is the amount of damage your Hero deals with no items. This value is unique to each hero and increases automatically as you level up through [Boons](Boons.md).

1. Spreadshots Spreadshots allow certain weapons to fire multiple bullets at once (such as shotguns or shurikens). In these cases, all calculation rules apply to every individual bullet.

- Drifter, Grey Talon with - Rain of Arrows active, and - Split Shot are exceptions to this, where the same amount of bullet damage is dealt to a target regardless of how many pellets hit per shot.

1. Piercing shots Paige's weapon's shots pierce through enemies and can hit multiple enemies per projectile, disappearing only when they hit a map surface. However, they do not deal headshot bonus damage, but can proc headshot items.

- Doorman's weapon's shots also pierce enemies. Unlike Paige's, they can deal headshot damage but deal half damage to all enemies hit after the first.

1. Melee Damage [Melee Damage](Melee Damage.md) is considered a source of Weapon Damage and scales with the Weapon Damage stat by 50%. Items and abilities that trigger from "dealing weapon damage" or "weapon damage hits" (e.g.

- Stalker, Card Trick, etc.) include Melee Damage. Some effects that specify "bullets", such as - Metal Skin and - Toxic Bullets, have no effect with Melee Damage, but others do (such as - Slowing Bullets and - Weighted Shots ).

In addition to Melee Resist gained from items, [Bullet Resist](Damage Resistance.md#Bullet-Resist) affects all Weapon Damage, granting another source of resistance against Melee Damage. The only exception is - Venator's innate Spirit-scaled Bullet Resist, although this is likely a bug.

## Combat Modifiers

1. Damage Falloff Damage Falloff reduces damage based on distance. All heroes have a Falloff Range in which damage is linearly reduced from 100% to 10%.

When aiming at an enemy hero, a dot on their health bar indicates the percentage of damage you will deal: {| class="wikitable" Dot Color Damage Percentage Red 10% - 20% Orange 20% - 35% Yellow 35% - 75% Transparent 75% - 100% |} 1. Crit Multiplier Aiming for the head deals increased damage. [Troopers](Troopers.md), [Neutrals](Neutrals.md), [Lane Guardians](Lane Guardians.md) and [Heroes](Heroes.md) have a weakpoint hitbox that receives 1.65x bullet damage when hit.

\text{Crit Multiplier} = 1 + [(0.65 + \text{Crit Bonus Scale}) \times \text{Crit Resist}] The following heroes cannot deal critical damage: Deadman Danny Graves Paige (though she can proc headshot item effects) Viscous ' alt-fire Yamato's alt-fire Crit Bonus Scale is a stat that modifies critical damage dealt by certain heroes.

- heroCritTable Abilities that can deal critical damage have different critical modifiers. This replaces the +65% multiplier of base weapons.

{| class="wikitable sortable mw-collapsible" +Ability Crit Damage Stats Hero Ability Crit Damage (%) Paradox Kinetic Carbine

- get_ability_prop Kinetic Carbine HeadshotBonus Venator Ira Domini 30 Vindicta Assassinate

- get_ability_prop Assassinate HeadshotBonus |}

## Target Modifiers

1. Bullet Resistance Damage Resistance Incoming damage is reduced by the target's Bullet Resist and increased by the attacker's Bullet Resist Reduction. These stats stack multiplicatively. For a detailed breakdown on how multiple items stack, see the main page.

1. Increased Bullet Damage Increased Bullet Damage is a debuff inflicted on enemies. It multiplies the total amount of damage they take from you. Because this is applied at the end of the calculation, it also increases the effectiveness of your Flat Weapon Damage.

## Flat Weapon Damage

Flat Weapon Damage is an extra amount of damage obtained through certain hero abilities and items.

Flat Weapon Damage is not increased by your "Weapon Damage %" multiplier. It is an additive source added to your total after the percentage multiplier is applied to your base. However, it is still affected by Damage Falloff, Bullet Resist, and Crit Multipliers.

## Weapon Damage Formula

The final damage dealt by a bullet is determined by multiplying your base stats, your item bonuses, and various situational modifiers.

\begin{array}{c} \text{Final Damage} = \\ [(\text{Base DMG} \times \text{DMG Multiplier}) + \text{Flat Bonus}] \\ \times \text{Falloff} \times \text{Resistances} \times \text{Crit Multiplier} \end{array}

## Weapon Damage Scaling

Some abilities scale with Weapon Damage.

For most Weapon Damage scaling abilities, they only scale based on the "Bonus Weapon Damage" stat, which is granted by items and Weapon shop investments (see list below).

- Paradox's Kinetic Carbine is an exception, since it scales with her Base Weapon Damage (counting as a full burst shot), and thus increases with [Boons](Boon.md). [Melee Damage](Melee Damage.md) scaling abilities also scale with Weapon Damage, since Melee Damage scales with Weapon Damage (by 50%).

1. Abilities that scale with weapon damage

- weaponscaling

## NPCs

Attacks from [Troopers](Troopers.md), [Guardians](Guardians.md), [Neutrals](Neutrals.md), [Base Turrets](Base Turrets.md) and the [Mid-Boss](Mid-Boss.md) deal weapon damage.
