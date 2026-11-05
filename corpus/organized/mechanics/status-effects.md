---
title: "Status Effects"
pageid: 943
source: wiki-md
---

See also [Crowd Control](Crowd Control.md) for a list of all Crowd Control effects.

Status Effects are modifiers or effects applied to units or players after certain conditions have been met. Buffs are positive status effects, while debuffs are negative. They will last for a set duration unless cleared through certain items or abilities. Status effects can be displayed over an entity's health bar, as a transparent overlay on the entity's body, or not displayed at all.

## Buffs

- isBuff: true

- status: Barrier

- status icon: Barrier Damage Barrier 1. Barrier A temporary shield that absorbs a set amount of incoming damage before breaking.

Sources: The Doorman's Doorway (Tier 2) Ivy's Air Drop (Tier 1) Paige's Plot Armor Rat King's Royal Pestments Vyper's Slither (Tier 3) Warden's Willpower Wraith's Project Mind (Tier 2) Divine Barrier (Active) Diviner's Kevlar Grit Guardian Ward (Active) Indomitable Majestic Leap (Active) Reactive Barrier Spirit Shielding Weapon Shielding

- isBuff: true

- status: Fire Rate Buff

- status icon: Fire Rate Fire Rate 1. Fire Rate Buff A temporary buff that increases the weapon's rate of fire.

Sources: [Gun Powerup](Powerup.md) Paige's Plot Armor (Tier 1) Wraith's Full Auto Ivy's Kudzu Connection Mina's Sanguine Retreat (Tier 1) Mirage's Traveler (Tier 1) Sinclair's Spectral Assistant (Tier 3) Silver's Lycan Curse Silver's Slam Fire Victor's Shocking Reanimation (Tier 1) Active Reload Blood Tribute Burst Fire Cultist Sacrifice Frenzy Fury Trance Healing Tempo Heroic Aura Kinetic Dash Mercurial Magnum Quicksilver Reload Shadow Weave Spellslinger Spiritual Overflow Surge of Power Vampiric Burst

- isBuff: true

- status: Health Regeneration

- status icon: Healing Health Regen 1. Health Regeneration A temporary buff that restores health over time (HoT). This does not include instant heals or lifesteal.

Sources: [Survival Powerup](Powerup.md) Abrams ' Infernal Resilience (conditional) Dynamo's Rejuvenating Aurora Kelvin's Frozen Shelter McGinnis's Medicinal Specter Victor's Jumpstart Fortitude (conditional) Healing Rite Healing Nova Mystic Regeneration Radiant Regeneration

- isBuff: true

- status: Invincibility

- status icon: Metal Skin Old 1. Invincibility The user cannot be damaged or targeted by hostile effects for a short duration.

Sources: Apollo's Riposte Calico's Return to Shadows Dynamo's Quantum Entanglement Ivy's Stone Form Pocket's Enchanter's Satchel Mina's Sanguine Retreat Mirage's Tornado Victor's Shocking Reanimation Yamato's Shadow Transformation (While transforming) Ethereal Shift

- isBuff: true

- status: Lifesteal

- status icon: Healing Lifesteal 1. Lifesteal A temporary buff that causes the user to heal for a percentage of the damage they deal.

Sources: Haze's Smoke Bomb (Tier 3) (Bullet Lifesteal) Ivy's Kudzu Connection (Bullet Lifesteal) Active Reload (Bullet Lifesteal) Fury Trance (Bullet Lifesteal) Infuser (Spirit Lifesteal) Vampiric Burst (Bullet Lifesteal) Leech (Bullet and Spirit Lifesteal)

- isBuff: true

- status: Movement Speed Buff

- status icon: Move speed sprint Move Speed 1. Movement Speed Buff A temporary increase to movement speed.

Sources: [Movement Powerup](Powerup.md) Calico's Ava Drifter's Bloodscent (Tier 1 Upgrade and have an isolated enemy hero around) Dynamo's Rejuvenating Aurora Haze's Smoke Bomb Kelvin's Ice Path Rat King's Rule, Ratannia!

- Silver's Lycan Curse Victor's Jumpstart Warden's Willpower Yamato's Shadow Transformation (Tier 2 Upgrade) Active Reload Backstabber (conditional) Blood Tribute Burst Fire (conditional) Counterspell Dispel Magic (Active) Divine Barrier (Active) Ethereal Shift Fleetfoot Fortitude Frenzy Guardian Ward Healing Rite Healing Tempo Headhunter Heroic Aura (Active) Magic Carpet Radiant Regeneration Surge of Power (Conditional) Spirit Shielding Veil Walker Weapon Shielding

- isBuff: true

- status: Resistance Buff

- status icon: Bullet Armor Damage Resistance 1. Resistance Buff A temporary buff that reduces incoming damage from a specific source.

Sources: Billy's Chain Gang (during cast time) McGinnis ’s Medicinal Specter (Tier 3 Upgrade - Spirit) Rat King's Rule, Ratannia!

(Reduces incoming damage via [Damage Reduction](Damage Reduction.md)) Yamato's Power Slash (Tier 1 Upgrade - Bullet) Yamato's Shadow Transformation (Bullet and Spirit) Blood Tribute (Debuff Resistance) Colossus (Bullet and Spirit) Escalating Resilience (stacking Bullet Resist on hit) Frenzy (Debuff, when below 50% health) Fury Trance (Spirit) Metal Skin (Bullet Immunity) Spirit Snatch (steals Spirit Resist on melee hit) Warp Stone (Bullet)

- isBuff: true

- status: Spirit Power Buff

- status icon: Spirit icon Spirit Power 1. Spirit Power Buff A temporary increase to Spirit Power.

Sources: [Casting Powerup](Powerup.md) Arcane Surge Counterspell Diviner's Kevlar Enchanter's Emblem Ethereal Shift Infuser Shadow Weave Spirit Snatch Spiritual Overflow

- isBuff: true

- status: Stealth

- status icon: Invisible 1. Stealth A temporary buff that renders the user invisible.

All steath sources share some common properties: Being close to any enemy reveals a silhouette of the player.

Attacking or casting an ability breaks the stealth.

Receiving damage temporarily reveals the player with stealth.

The specific numbers (e.g. distance to being revealed) are unique for each Stealth source and can be found on appropriate pages.

Sources: Haze's Smoke Bomb Shadow Weave Veil Walker Shadow Strike 1. Abilities that don't break stealth

- dontbreakstealth 1. Items that don't break Stealth {| class="wikitable" Item Notes

- fleetfoot Blood Tribute Only when untoggling its active.

- Heroic Aura Restorative Locket |}

- isBuff: true

- status: Hidden on Minimap

- status icon: Invisible 1. Hidden on minimap A temporary buff that renders the user unable to be seen on the minimap.

- Calico's Ava

- isBuff: true

- status: Unstoppable

- status icon: Unstoppable Symbol 1. Unstoppable A powerful buff that grants immunity to crowd control effects like Stun, Silence, Sleep, and Immobilize. The user can still take damage while Unstoppable.

Sources: Abrams ' Seismic Impact (Tier 3) Billy's Chain Gang (Tier 3) The Doorman's Hotel Guest (Tier 3) Warden's Last Stand (Tier 3) (While channeling) Rem's Naptime (Tier 3) (While channeling) Yamato's Shadow Transformation Unstoppable (Active)

- isBuff: true

- status: Weapon Damage Buff

- status icon: Bullet Damage Damage Amplification 1. Weapon Damage Buff A temporary increase to weapon damage output.

Sources: Paige's Plot Armor Abrams's Shoulder Charge (Tier 1) Bebop's Exploding Uppercut (Tier 2) Billy's Rising Ram (Tier 2) Lash's Grapple (Tier 2) Berserker Split Shot

## Debuffs

- isBuff: false

- status: Bleed 1. Bleed A negative status effect that deals damage equal to a percentage of a unit's health over time.

Sources: Drifter's Stalker's Mark Vindicta's Crow Familiar Shiv's Serrated Knives Decay Toxic Bullets Note: Serrated Knives applies a unique variant of bleed that deals flat damage rather than percent health damage.

- isBuff: false

- status: Burn 1. Burn A negative status effect that deals [Spirit Damage](Spirit Damage.md) over time.

Sources: Holliday's

- powder keg Infernus ' Afterburn Venator's Consecrating Grenade (deals [Weapon Damage](Weapon Damage.md) and [Pure Damage](Pure Damage.md) instead of Spirit) Spirit Burn

- isBuff: false

- status: Curse

- status icon: Curse icon 1. Curse A negative status effect that interrupts, [disarms](Status Effects.md#Disarm), and [silences](Status Effects.md#Silence) abilities and active items.

Sources: Grey Talon's Spirit Snare Cursed Relic (also removes non-ultimate buffs) Mystical Piano (also applies movement slow) [Patron](Patron.md) and [Shrine](Shrine.md)s defensive attack Adjacent Effects: Apollo's Itani Lo Sahn applies an effect similar to Curse, but it also applies [Slow Motion](Slow Motion.md) and does not interrupt abilities.

- status icon: Damage heart

- status: Damage Output Reduction

- isBuff: false Damage Amplification#Damage Reduction 1. Damage Output Reduction A negative status effect that reduces the damage output of the afflicted target. Some sources can reduce all damage types outputted, and others may only reduce a specific type.

Sources: Infernus ' Afterburn (Tier 2) - Decreases spirit damage output (Built-Up from Bullets) Mirage's Fire Scarabs (Base and Tier 3) - Decreases all damage outputs Silver's Boot Kick (Tier 3) - Decreases all damage outputs Warden's Alchemical Flask (Base and Tier 2) - Decreases weapon damage output Graves ' Essence Theft (Base and Tier 2) - Decreases weapon damage output (Built-Up from Bullets) Inhibitor Decreases all damage outputs (Built-Up from Bullets) Silencer Decreases spirit damage outputs (Built-Up from Bullets)

- isBuff: false

- status: Disarm 1. Disarm A negative status effect that prevents the afflicted target from firing their weapon. They are still capable of casting abilities and using melee attacks.

Disarm affects abilities that modify the player's primary fire, such as - Venator's Ira Domini and - Paradox's Kinetic Carbine. However, it does not affect abilities that deal [Weapon Damage](Weapon Damage.md) without primary fire, such as - Haze's Bullet Dance or - Venator's Consecrating Grenade and - Gutshot. It also doesn't affect Vindicta's Assassinate.

Sources: Apollo's Itani Lo Sahn Grey Talon's Spirit Snare Mo & Krill's Sand Blast Silver (Transformed)'s Tail Whack Cursed Relic Disarming Hex Mystical Piano Phantom Strike [Patron](Patron.md) and [Shrine](Shrine.md)s defensive attack

- isBuff: false

- status: Displace

- status icon: Status Displacement 1. Displace A negative status effect that changes the direction and acceleration of the target's movement. Pull, knockup and knockback are types of displace.

Sources: Abrams ' Shoulder Charge Abrams ' Seismic Impact Baba's Granny Long Legs Bebop's Exploding Uppercut Bebop's Grapple Arm Billy's Bashdown Billy's Rising Ram Billy's Chain Gang The Doorman's Luggage Cart Dynamo's Kinetic Pulse Dynamo's Singularity Holliday's Powder Keg Holliday's Spirit Lasso Ivy's Air Drop Lash's Ground Strike (Tier 2) McGinnis's Spectral Wall Mirage's Tornado Mo & Krill's Burrow Mo & Krill's Combo Paige's Rallying Charge Paradox's Paradoxical Swap Rat King's Rule, Ratannia!

- Rem's Pillow Toss Silver's Boot Kick Venator's Gutshot and - Ira Domini Viscous ' Puddle Punch Viscous ' Goo Ball Wraith's Telekinesis Knockdown (If the target is not on the ground) Phantom Strike (If the target is not on the ground) Rescue Beam Vortex Web

- isBuff: false

- status: Healing Reduction

- status icon: Damage heart Healing#Healing_Reduction

- l1: Healing Reduction 1. Healing Reduction A negative status effect that reduces the target's healing from all sources.

Sources: Drifter's Stalker's Mark (Tier 3) Pocket's Affliction (Tier 3) Infernus ' Napalm (Tier 3) Venator's Consecrating Grenade Vindicta's Crow Familiar (Tier 1) Vyper's Lethal Venom (Tier 2) Cheat Death (Self) Crippling Headshot Decay Healbane Inhibitor Spirit Burn Toxic Bullets

- isBuff: false

- status: Immobilized

- status icon: Immobilize 1. Immobilized A negative status effect that prevents the target from moving. While rooted in place, the target is free to use abilities and fire their weapon.

Sources: Billy's Bashdown (when pulling an enemy downwards) Graves ' Grasping Hands Lash's Ground Strike (when dragging an enemy to the ground) Paige's Captivating Read Silver's Boot Kick (when kick connects to the target) Venator's Hex-Lined Snap Trap Warden's Binding Word Arctic Blast

- isBuff: false

- status: Movement Silence

- status icon: MoveSlow 1. Movement Silence A negative status effect that applies [Movement Slow](Movement Slow.md) and prevents the target from casting movement-related abilities and active items, and in some cases further restricts movement. See Slowing Hex for a list of abilities and items affected.

Sources: Silver's Entangling Bola (also prevents stamina use) Wraith's Telekinesis (also prevents stamina use) Capacitor (also prevents stamina use) Slowing Hex Vortex Web

- isBuff: false

- status: Movement Slow Movement Slow 1. Movement Slow A negative status effect that reduces the movement speed of the target, including sprint speed. Its effectiveness can be reduced through the use of items such as - Enduring Speed.

For a comprehensive list of sources, see [Movement Slow](Movement Slow.md).

- isBuff: false

- status: Silence 1. Silence A negative status effect that prevents the target from casting abilities, but they can still use active items (with the exception of sources of [curse](Status Effects.md#Curse)). It does not disable passive abilities.

Sources: Apollo's Itani Lo Sahn Baba's Baba's Brew (Silencing) Celeste's Dazzling Trick Drifter's Rend (Tier 3) Grey Talon's Spirit Snare Ivy's Air Drop (Tier 3) Lady Geist's Soul Exchange (Tier 2) Paradox's Time Wall (Tier 2) Warden's Binding Word (Tier 3) Mina's Nox Nostra Cursed Relic (also silences active items) Focus Lens Fury Trance (Self, also silences stamina) Mystical Piano Silence Wave Silencer

- isBuff: false

- status: Sleep 1. Sleep A negative status effect that prevents the target from taking actions, but they may wake up upon taking damage. While sleeping, targets can move but extremely slowly.

Sources: Haze's Sleep Dagger Rem's Naptime

- isBuff: false

- status: Stun 1. Stun A negative status effect that completely immobilizes the target and prevents them from taking any actions until the effect expires.

Sources: [Parry](Parry.md) Getting knocked off a [zipline](Ziplines.md) Getting knocked off a [rope](Ropes.md) [Walker](Walker.md)'s Stomp Abrams ' Shoulder Charge Abrams ' Seismic Impact Apollo's Riposte The Doorman's Luggage Cart (Tier 3) Dynamo's Singularity Grey Talon's Guided Owl Holliday's Spirit Lasso Infernus ' Concussive Combustion Ivy's Stone Form Lash's Death Slam (Tier 3 unlocks additional stun on hit) Mo & Krill's Combo Paige's Rallying Charge Seven's Static Charge Venator's Gutshot (If target hits a wall) Victor's Shocking Reanimation Viscous ' Goo Ball Wraith's Telekinesis Crushing Fists Knockdown Lightning Scroll Mystical Piano

- isBuff: false

- status: Time Stop

- status icon: Kinetic Carbine 1. Time Stop A negative status effect that slows the speed of the player's actions, including the effects of inertia and gravity. Also known as Time Slow or Slow Motion.

Sources: Apollo's Itani Lo Sahn Paradox's Kinetic Carbine (also applies to self when aiming in the air) The Doorman's Hotel Guest (on return) Note: Paradox's Pulse Grenade is listed as applying a "time slow" in the description, but it actually applies a Movement Slow.

## Hero Specific Effects

The following Status Effects are either exclusively relevant to or only applied by a specific Hero.

- isBuff: false

- status: Affliction

- status icon: Affliction 1. Affliction A negative status effect applied by - Pocket's Affliction ability. It deals constant damage over time for a long duration, however it is non-lethal and cannot reduce a target's health below 1. It also does not apply item procs.

- isBuff: false

- status: Eternal Night

- status icon: Eternal Night 1. Eternal Night A negative status effect applied by - Drifter's ability of the same name. Inflicted heroes have their vision severely limited.

- isBuff: false

- status: Fixation

- status icon: Fixation 1. Fixation A negative status effect that increases the target's damage received from - Haze. It is unique to her, applied through her ability of the same name.

- isBuff: false

- status: Hotel Guest

- status icon: Hotel Guest 1. Hotel Guest A negative status effect applied by - The Doorman's ability of the same name. The target is sent to the [Baroness Hotel](Baroness Hotel.md) and has to make their way to the elevator to escape.

- isBuff: false

- status icon: Lethal Venom

- status: Lethal Venom 1. Lethal Venom A negative status effect applied exclusively by - Vyper's ability of the same name. After a short delay, it deals Spirit Damage to the target. The max damage depends on the target's missing health.

- isBuff: false

- status: Malice

- status icon: Malice 1. Malice A negative status effect applied exclusively by - Lady Geist's ability of the same name. It inflicts a decaying Movement Slow on the target and increases the amount of damage Lady Geist deals to them. It can be stacked up to 5 times and refreshed.

- isBuff: false

- status icon: Petrifying Bola

- status: Petrified 1. Petrified A negative status effect applied by - Vyper's Petrifying Bola. Inflicted heroes are interrupted, unable to move and perform actions, but block all incoming damage, with the exception of - Vyper's Lethal Venom (both the buildup and damage).

- isBuff: false

- status: Rabbit Hex

- status icon: Rabbit Hex 1. Rabbit Hex A negative status effect applied by - Sinclair's ability of the same name. Inflicted heroes change shape into a rabbit, with its corresponding hitbox, and move faster but have amplified received damage. The hero cannot perform any actions and abilities in rabbit form besides walking and jumping, but any actions and abilities initiated before the transformation are not interrupted.

- isBuff: false

- status: Tether 1. Tether A negative status effect applied by - Vindicta's Stake ability. It binds all nearby targets to a central point, forcing them to stay within a short radius of the center.

- status icon: Blasted

- status: Wrecked 1. Wrecked A negative status effect applied by the passive of - Billy's Blasted ability. Melee hits will inflict wrecked on enemies. When Blasted is activated, Billy will gain additional bullet damage against Wrecked enemies.

## Countering Debuffs

Certain abilities and items can be used to mitigate or remove negative status effects.

1. Temporary Buffs These effects grant a short-term immunity to certain debuffs. For a full list of sources, see the main entry for each buff.

[Invincibility](untitled.md#Invincibility): Grants temporary immunity to all damage and hostile effects.

[Unstoppable](untitled.md#Unstoppable): Grants temporary immunity to crowd control effects.

- Indomitable: Grants immunity to a single crowd control effect.

1. Purge These effects instantly remove currently active debuffs.

{| class="wikitable" Name Removes debuffs from Ultimates?

- Dynamo's Quantum Entanglement (Tier 3) No Haze's Smoke Bomb (Tier 3) No Kelvin's Frozen Shelter (Tier 3) No Victor's Shocking Reanimation Yes Viscous ' The Cube (Tier 3) No Yamato's Shadow Transformation Yes Dispel Magic No Divine Barrier Yes |} 1. Debuff Resistance (Stat) The following effects grant a [Debuff Resistance](Debuff Resist.md) stat, which reduces the duration of debuffs. Except for - Willpower, this is a character stat, not a temporary buff.

- Abrams's Infernal Resilience (Tier 3) Warden's Willpower (Tier 3) Debuff Resist
