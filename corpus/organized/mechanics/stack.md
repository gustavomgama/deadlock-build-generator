---
title: "Stack"
pageid: 1265
source: wiki-md
---

A Stack is a scaling effect or buff that can be increased through specific means or actions. Stacks are most often applied through dealing damage, where one instance applies one stack. Most stacking effects are built up quickly and are only temporary, disappearing all at once after their duration runs out. Additionally, there are stacking bonuses that apply directly to heroes, making them stronger, with a few of these bonuses sometimes being permanent. Only a handful of heroes can infinitely stack, allowing them to constantly scale as a game goes on.

While most stacking items effects are temporary, a few keep their stacks under various conditions.

- Glass Cannon loses a stack upon death.

- Restorative Locket spends its charges to heal the hero.

- Trophy Collector has permanent stacks.

See [Build-Up](Build-Up.md) for abilities and items that trigger an effect after reaching 100% of a damage metric.

## Items with Stacking Effects

{| class="wikitable sortable" Name Cost Category Stat change per stack Max stacks Max stat change Split Shot

- get_cost Split Shot

- get_type Split Shot +

- get_prop Split Shot WeaponDamagePerStack Weapon Damage per stack

- get_prop Split Shot MaxStacks +60% Weapon Damage at max stacks Berserker

- get_cost Berserker

- get_type Berserker +

- get_prop Berserker WeaponPowerPerStack Weapon Damage per stack

- get_prop Berserker MaxStacks +70% Weapon Damage at max stacks Ballistic Enchantment

- get_cost Ballistic Enchantment

- get_type Ballistic Enchantment +

- get_prop Ballistic Enchantment WeaponPowerPerStack Weapon Damage per stack +

- get_prop Ballistic Enchantment WeaponPowerPerStackNonHero % Weapon Damage per stack from non-Hero sources

- get_prop Ballistic Enchantment NonHeroStackLimit (Stacks only capped vs non-Hero sources) +140% Weapon Damage (Theoretical limit if damaging all 6 enemy heroes and 8 non-Hero enemies) Escalating Resilience

- get_cost Escalating Resilience

- get_type Escalating Resilience +

- get_prop Escalating Resilience BulletResistPerStack Bullet Resist per stack 15 +30% Bullet Resist at max stacks Spirit Rend

- get_cost Spirit Rend

- get_type Spirit Rend

- get_prop Spirit Rend MagicResistReduction Spirit Resist on Headshot per stack on target

- get_prop Spirit Rend MaxStacks -28% Spirit Resist at max stacks on target Crushing Fists

- get_cost Crushing Fists

- get_type Crushing Fists

- get_prop Crushing Fists BulletResistReduction Bullet Resist per stack on target

- get_prop Crushing Fists MaxStacks -30% Bullet Resist at max stacks on target Glass Cannon

- get_cost Glass Cannon

- get_type Glass Cannon +

- get_prop Glass Cannon FireRatePerKill Weapon Fire Rate per stack

- get_prop Glass Cannon MaxStacks +56% Fire Rate at max stacks Spellslinger

- get_cost Spellslinger

- get_type Spellslinger +

- get_prop Spellslinger BonusFireRate Weapon Fire Rate and - get_prop Spellslinger ReloadSpeedMultipler Reload Time per stack

- get_prop Spellslinger MaxStacks +66% Fire Rate and -60% Reload Time at max stacks Restorative Locket

- get_cost Restorative Locket

- get_type Restorative Locket +

- get_prop Restorative Locket HealPerStack Heal per stack

- get_prop Restorative Locket MaxStacks +400 Heal at max stacks (before [Boon](Boon.md) Scaling) Trophy Collector

- get_cost Trophy Collector

- get_type Trophy Collector +

- get_prop Trophy Collector StackingBonusSprintSpeed /s Sprint Speed +

- get_prop Trophy Collector StackingTechRangeMultiplier Ability Range +

- get_prop Trophy Collector StackingGoldPerMinute Souls per minute

- get_prop Trophy Collector MaxStacks +2.4m/s Sprint Speed +12% Ability Range +288 Souls per minute at max stacks Mystic Regeneration

- get_cost Mystic Regeneration

- get_type Mystic Regeneration

- get_prop Mystic Regeneration Regeneration HP/s Health Regeneration per stack 6 24HP/s Health Regeneration at max stacks Radiant Regeneration

- get_cost Radiant Regeneration

- get_type Radiant Regeneration

- get_prop Radiant Regeneration Regeneration HP/s Health Regeneration per stack 6 24HP/s Health Regeneration at max stacks (before [Spirit Scaling](Spirit_power.md#spirit_power_scaling)) Escalating Exposure

- get_cost Escalating Exposure

- get_type Escalating Exposure +

- get_prop Escalating Exposure MagicIncreasePerStack Spirit Amp per stack

- get_prop Escalating Exposure MaxStacks +54% Spirit Amp at max stacks |}

## Heroes with Stacking Effects

{| class="wikitable sortable" Hero Ability Effect Billy

- size: 30px Blasted Billy gains bonus health and increases Blasted duration for dealing melee attacks while Blasted Celeste

- size: 30px Radiant Daggers Celeste gains increased spirit damage when the beam hits an enemy hero Graves

- size: 30px Essence Theft (passive) Graves gradually steals Weapon Damage and Spirit Resist from shooting a target Haze

- size: 30px Fixation (passive) Haze gains increased bullet damage to targets the more stacks they have Kelvin

- size: 30px Arctic Beam Gradually applies increasing Movement and Fire Rate Slow on enemies Lady Geist

- size: 30px Malice Causes targets to take increased damage from Lady Geist Paradox

- size: 30px Pulse Grenade Applies stacking damage amp to targets, granting increased damage against them Pocket

- size: 30px Barrage Gradually increases Pocket's overall damage as it hits targets Shiv

- size: 30px Serrated Knives Increases the bleed's damage over time and refreshes its duration Mirage

- size: 30px Djinn's Mark (passive) Builds up stacking spirit damage that can be triggered automatically or by Mirage Mo & Krill

- size: 30px Scorn (T3) Applies stacking damage amp to targets, granting increased damage against them Vyper

- size: 30px Screwjab Dagger Applies a stacking movement slow, with the T2 upgrade also applying a stacking bullet resist shred.

|}

## Heroes with Permanent Stack Bonuses

{| class="wikitable sortable" Hero Ability Bonus per Stack Max Stacks Bebop

- size: 30px Sticky Bomb +

- get_ability_prop Sticky Bomb BonusDamagePctPerPlayerKilled % bonus damage per enemy killed, +

- get_ability_prop Sticky Bomb BonusDamagePctPerPlayerHit % per enemy hurt Infinite Drifter

- size: 30px Bloodscent +

- get_ability_prop Bloodscent WeaponDmgPerIsolationKill % Weapon Damage per isolation kill, +`*( / 100)`% per assist Infinite Grey Talon

- size: 30px Guided Owl +

- get_ability_prop Guided Owl BonusTechPowerPerKill Permanent Spirit Power per enemy killed Infinite Mina

- size: 30px Nox Nostra +2 bats released during Nox Nostra per

- love bites trigger against heroes Infinite Mo & Krill

- size: 30px Combo +

- get_ability_prop Combo BonusHealthOnKill Bonus Max Health per enemy killed during or within 3s of Combo ending Infinite Vindicta

- size: 30px Assassinate +6% weapon damage per enemy killed with or within 4s of being hit with Assassinate, increased to +10% with T3 upgrade Infinite |}
