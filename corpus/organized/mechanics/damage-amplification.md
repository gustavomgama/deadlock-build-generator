---
title: "Damage Amplification"
pageid: 4756
source: wiki-md
---

Damage Amplification or Damage Amp is a stat that multiplies the damage caused by the player to affected enemies and NPCs. It can be both positive and negative. In latter case it reduces damage and is also known as Damage Reduction.

- apzBQPZyW_w

- 360

- description: Video explaining Damage Amplification

## Calculation

Contrary to what the percentages might suggest, multiple sources of damage amplification do not all stack in the same way. There are three distinct categories of Damage Amplification, each interacting with the damage formula differently: Additive Amps: These add together with each other (including additive Damage Reductions) into a single pool.

Multiplicative Amps: These multiply the total damage one by one.

Instance Amps: These are nearly identical to multiplicative amps, main exception being they create a new instance of damage.

1. The Damage Formula Based on testing, the generalized formula for how these amps apply to weapon damage is as follows: \text{Damage} = [(\text{Base Bullet Damage} \times \text{Weapon Multiplier}) \times (1 + \text{Total Additive Amps}) + \text{Flat Bonus}] \times \text{Multiplicative Amp}_1 \times \text{Multiplicative Amp}_2 \dots \times \text{Instance Amp Damage}_1 \times \text{Instance Amp Damage}_2 Example: A hero has a base bullet damage of 100 and 0 flat weapon damage for simplicity.

The hero is affected by - Inhibitor (an Additive Damage Reduction of -30%). Their damage drops to 70 (100 * 0.70 = 70).

- Ivy casts Air Drop on the hero (an Additive Amp of +20%). The additive pool is now -30% + 20% = -10%. The hero deals 90 damage (100 * 0.90 = 90).

The hero parries an enemy hero (Multiplicative Amp of +25% against parried target). This is applied after the additive pool. The hero now deals 112.5 damage (90 * 1.25 = 112.5).

## Damage Amplification

1. Sources of Damage Amplification 1. Additive Amplifiers {| class="wikitable sortable" +List of heroes Hero Ability Tier Stat change Calico Ava 3 +

- get_ability_upgrade_prop Ava

- 3 OutgoingDamagePercent % Ramping Damage Amp Ivy Air Drop 0 +20% Damage Amp on Ivy and carried ally Shiv Killing Blow 0 +

- get_ability_prop Killing Blow BuffDamage % Damage Amp 2 +

- get_ability_upgrade_prop Killing Blow

- 2 BuffDamage % Damage Amp Rebuttal + Rebuttal BonusDamagePercent Damage Amp |} 1. Multiplicative Amplifiers {| class="wikitable sortable" +List of heroes Hero Ability Tier Stat change Infernus Napalm 0 +

- get_ability_prop Napalm IncomingDamagePercentFromCaster % Damage Amp 3 +

- get_ability_upgrade_prop Napalm

- 3 IncomingDamagePercentFromCaster % Damage Amp McGinnis Spectral Wall 1 +

- get_ability_upgrade_prop Spectral Wall

- 1 BonusDamagePercent % Damage Amp Mo & Krill Scorn 3 +

- get_ability_upgrade_prop Scorn

- 3 DamageBonus % Damage Amp per Stack Victor Aura of Suffering 3 +

- get_ability_upgrade_prop Aura of Suffering

- 3 IncomingDamagePercent % Damage Amp Bebop Hook 1 +

- get_ability_upgrade_prop Grapple Arm

- 1 BulletAmp % Weapon Damage Amp against hooked targets All Heroes [Parry](Parry.md) 0 +25% Damage Amp (Parried target takes 25% increased damage from all sources) |} 1. Instance Amplifiers {| class="wikitable sortable" +List of heroes and items Hero / Item Ability Tier Stat change Drifter Bloodscent 0 +

- get_ability_prop Bloodscent AmpDamagePercent % Damage Amp on Isolated Heroes 3 +

- get_ability_upgrade_prop Bloodscent

- 3 AmpDamagePercent % Damage Amp on Isolated Heroes Lady Geist Malice 0 +

- get_ability_prop Malice VulnerabilityPerStack % Damage Amp per Stack 3 +

- get_ability_upgrade_prop Malice

- 3 VulnerabilityPerStack % Damage Amp per Stack Paradox Pulse Grenade 0 +

- get_ability_prop Pulse Grenade DamageAmplificationPerStack % Damage Amp per Stack 3 +

- get_ability_upgrade_prop Pulse Grenade

- 3 DamageAmplificationPerStack % Damage Amp per Stack Pocket Barrage 0 +

- get_ability_prop Barrage AmpPercentPerStack % Damage Amp per Stack 3 +

- get_ability_upgrade_prop Barrage

- 3 AmpPercentPerStack % Damage Amp per Stack Sinclair Rabbit Hex 0 +

- get_ability_prop

- ability_magician_animalhexarea DamageAmpPercentage % Damage Amp 3 +

- get_ability_upgrade_prop

- ability_magician_animalhexarea

- 3 DamageAmpPercentage % Damage Amp Escalating Exposure + Escalating Exposure MagicIncreasePerStack Spirit Damage Amp per Stack |} 1. Unique Amplifiers These amplifiers have unique mechanics that do not cleanly fit into the Additive, Multiplicative, or Instance categories.

{| class="wikitable sortable" +List of heroes Hero Ability Tier Stat change Notes Billy Blasted 0 +

- get_ability_prop Blasted BulletDamageAmp % Bullet Damage Amp against wrecked enemies Post‑mitigation [true damage](True Damage.md) amp. (See [Bugs section](untitled.md#Bugs,-Quirks,-and-Exceptions).) 2 +

- get_ability_upgrade_prop Blasted

- 2 BulletDamageAmp % Bullet Damage Amp against wrecked enemies Celeste Radiant Daggers 0 +

- get_ability_prop Radiant Daggers MagicIncreasePerStack % Spirit Damage Amp per Stack Functions like a multiplicative amp with additive bugs. (See [Bugs section](untitled.md#Bugs,-Quirks,-and-Exceptions).) 3 +

- get_ability_upgrade_prop Radiant Daggers

- 3 MagicIncreasePerStack % Spirit Damage Amp per Stack |}

## Damage Reduction

Damage Reduction is a negative form of Damage Amplification, reducing the damage output of enemies or its user. Mechanically, standard Damage Reductions are treated as negative Additive Amps (see Calculation section).

1. Damage Reduction Stacking Valve's May 22 patch notes state that Damage Reduction debuffs are intended to stack diminishingly (i.e., multiplicatively, in the same manner as Resistance).

However, live testing confirms that standard Damage Reduction debuffs have not been fully migrated to this new system. Currently, Damage Reductions (such as - Inhibitor or - Fire Scarabs ) simply act as negative Additive Amps. This means they add directly together with other additive amps (positive or negative) rather than multiplying against each other.

1. Sources of Damage Reduction 1. Weapon, Spirit, and Pure Reduction {| class="wikitable sortable" +List of heroes Hero Ability Tier Stat change Mirage Fire Scarabs 0

- get_ability_prop Fire Scarabs OutgoingDamagePenaltyPercent % Outgoing Damage Reduction 3

- get_ability_upgrade_prop Fire Scarabs

- 3 OutgoingDamagePenaltyPercent % Outgoing Damage Reduction Rat King Rule, Ratannia!

0

- get_ability_prop Rule, Ratannia!

- AllyDamageReduction % Incoming Damage Reduction 3

- get_ability_upgrade_prop Rule, Ratannia!

- 3 AllyDamageReduction % Incoming Damage Reduction Silver Boot Kick 3

- get_ability_upgrade_prop Boot Kick

- 3 OutgoingDamagePercent % Damage Reduction |} Cheat Death, Golden Goose Egg and - Cursed Relic reduce damage dealt by its user.

1. Spirit Damage Reduction Spirit Damage Reduction from - Infernus's Afterburn (T2) and - Silencer does not behave like standard Damage Reduction. Multiple sources of Spirit‑specific reduction stack additively with each other (e.g., Afterburn T2 + Silencer = sum of percentages). This combined spirit reduction is then applied as a separate multiplier, multiplicative with all other additive amps such as - Inhibitor.

{| class="wikitable sortable" +List of heroes and items Hero / Item Ability Tier Stat change Infernus Afterburn 2

- get_ability_upgrade_prop Afterburn

- 2 OutgoingTechDamagePercent % Spirit Damage Reduction Note: Additive with itself, but multiplicative with other additive amps.

- Silencer Silencer TechDamageReduction Spirit Damage Reduction Note: Additive with itself, but multiplicative with other additive amps.

|}

## Bugs, Quirks, and Exceptions

Additive Amps do not apply to many flat values, such as flat weapon damage bonuses, base damage for Melee abilities (Such as the bonus +60 damage from - Calico's Leaping Slash T3 upgrade), Capacitor active, Backstabber, etc.

- Headhunter: Multiplicative non-instance amps are the only amps that work correctly with Headhunter damage.

- Return Fire: Because Multiplicative Amps act as defensive stats on the target, if an attacker fires at a target with Return Fire while the attacker has an M-amp active against them, the attacker will take increased reflected damage.

- Billy's Blasted bullet amp is unique as it is a post-mitigation [pure damage](True Damage.md) amp. Because of this, it does not work at all against barriers.

- Silencer and - Infernus's Afterburn Tier 2 Spirit Damage Reduction are exceptions to the standard Damage Reduction rule. They stack additively with themselves, but multiplicatively with other additive amps.

- Celeste's Spirit damage amp from - Radiant Daggers works like a multiplicative amp but is affected by additive amp bugs (see the Additive Amps entry above).

- Unstoppable: Suppresses all sources of Damage Reduction while active, but only for [Spirit Damage](Spirit Damage.md).

Abilities that scale with Bonus Weapon Damage such as - Gutshot, are not impacted at all by Additive Amps or Reductions.

[Pure damage](True Damage.md) from abilities such as - Ira Domini is affected by Additive Amps and Reductions, but not multiplicative ones.
