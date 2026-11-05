---
title: "Patch/Playtest/2024-06-20"
pageid: 575
source: liquipedia-deadlock-md
---

- name: Playtest - June 20 2024

- version: 2024-06-20

- release: June 20, 2024

- highlight1: Gameplay Updates

- highlight2: Item Updates

- highlight3: New Items

- highlight4: Hero Updates

- previous: Patch/Playtest/2024-06-162024-06-16

- next: Patch/Playtest/2024-06-232024-06-23

## General

Added EU servers and matchmaking region. EU testing times are Mon-Thur 5PM to 3AM and Fri-Sun 3PM to 3AM. Times listed are Central European Summer Time (GMT+2).

Removed the invite requirement of Steam friends having been on your list for a number of days (affected normal user cases often where friends weren't on the Steam list, and we have other metrics and tools on the backend now that we can use to filter for other cases) Added search functionality to the shop. You can now search by item name or by individual stat such as 'Ammo', 'Lifesteal', or 'Spirit Power'.

The game will now let you know when it is safe to abandon (usually if one person has been disconnected for a while) Your personal builds are now always sorted to the top of the in-game Builds dropdown Various network related improvements when there is packet loss Preferred heroes in your roster are now remember on the client across sessions Fixed chat wheel not working during the post-game sequence Updated the entrance to the underground tunnels from the outer lanes to look more like a subway entrance Re-enabled ultra wide UI mode Added street names and symbols to the Zipline UI Updated Sleep Dagger and Silence Glyph tooltips to clarify that they do not cancel channeling abilities Updated reload animations for Warden, Dynamo, and Ivy Improved visibility of Inferno's Concussive Combustion Fixed the unit target UI not showing up for instant-cast abilities (MoKrill ult, Lady Geist ult, Bebop bomb) Fixed the unit target UI not showing the activation button hint Added a Cosmic Veil to the hero demo map Added Ethereal Shift sounds Added wind sound when on the Zipline

## Gameplay

Rejuv buff is now only granted to the players that are alive. Players that are dead will have their respawn times cut in half from their current values.

Footsteps are now quieter when obstructed by level geometry Dash-Down is now double tap CTRL instead of CTRL+SHIFT

- text: bounty increased from 300 to 330

- type: buff

- affected1: Sinner's Sacrifice Fixed various bugs with Headshot Booster and Sharpshooter Added another entrance/exit to the underground tunnels from the warehouse interiors Enclosed the exterior Medium Neutral Camp with fencing in front of the Theater to match the Amber side Cab Stand Added two more veils on each side: Between the Drug Store and the Market on Amber, between the Hotel and Pharmacy on Sapphire Between the exterior Strong Neutral Camps and the outer lane near the T2

## Items

1. New Items I Infuser Added a new T1 Spirit item, Infuser +8% Spirit Resist +10% Ammo Active: Gain 12 Spirit and 20% Spirit Lifesteal for 6 seconds. Cooldown: 35s I Ammo Scavenger Added a new T1 Weapon item, Ammo Scavenger +20% Ammo +50 Health Passive: Anytime you secure or deny a Soul, you get 2 ammo back and have +20% Fire Rate for 4 seconds.

- I Active Reload Added a new T2 Weapon item, Active Reload -20% Reload Time +8% Weapon Damage Passive: Pressing the reload key during the halfway point of a reload will cause you to instantly regain your magazine and grant you +30% Bullet Lifesteal and +15% Fire Rate for 6s. The reload UI has an indicator for the trigger window. Cooldown: 25s Inspired by [None](https://project8.dev/threads/item-idea-trick-reload.2652/) I Veil Walker Added a new T2 Weapon item, Veil Walker +15% Ammo +8% Weapon Damage +200 Bullet Shield

- Passive: Walking through a Cosmic Veil causes you to become invisible with +3 m/s for 4 seconds and grants you +30% Fire Rate for your next magazine. Cosmic Veils regenerate any shields you have. Cooldown: 20s I Melee Charge Added a new T2 Weapon item, Melee Charge +15% Melee Damage +10% Weapon Power +75 Health Passive: Hitting an enemy with a heavy melee reloads your weapon Passive: Increases your heavy melee charge distance by 40% Inspired by [None](https://project8.dev/threads/bayonet.5372/) and [None](https://project8.dev/threads/comple...-category-item-that-buffs-charged-melee.5957/) Added a new T4 Vitality item, Colossus +500 HP +20% Melee Damage +20% Weapon Damage Active: Gain 40% Bullet and Spirit Resist and apply 20% movement slow to enemies within 10m. Your model size grows by 10%. Lasts 7 seconds. Cooldown: 65s 1. Existing Items I Healing Rite

- text: Duration increased from 15s to 17s (total regen increased from 350 to 370)

- type: buff

- affected1: Healing Rite I Extra Spirit

- text: Spirit Power increased from +6 to +7

- type: buff

- affected1: Extra Spirit I Extra Charge

- text: Now grants +7% Cooldown Reduction For Charged Abilities

- type: change

- affected1: Extra Charge

- text: No longer grants +6 Spirit to Charged Abilities

- type: change

- affected1: Extra Charge I Swift Striker

- text: Negative bullet resist reduced from -6% to -5%

- type: nerf

- affected1: Swift Striker I Mystic Shot

- text: Spirit scaling increased from 0.45 to 0.6

- type: buff

- affected1: Mystic Shot I Enduring Speed

- text: Slow resist increased from 35% to 40%

- type: buff

- affected1: Enduring Speed

- text: Now grants +1.5 HP Regen

- type: buff

- affected1: Enduring Speed I Healing Booster

- text: Spirit Resist reduced from 8% to 7%

- type: nerf

- affected1: Healing Booster

- text: Now provides +7% Bullet Resist

- type: buff

- affected1: Healing Booster I Return Fire

- text: Cooldown reduced from 30s to 24s

- type: buff

- affected1: Return Fire I Restorative Locket

- text: Fixed the max stack limit not being followed

- type: fix

- affected1: Restorative Locket

- text: Max stacks increased from 15 to 18

- type: buff

- affected1: Restorative Locket I Bullet Resist Shredder

- text: Bullet Resist Reduction increased from -10% to -12%

- type: buff

- affected1: Bullet Resist Shredder

- text: Bullet Resist Reduction duration increased from 5s to 6s

- type: buff

- affected1: Bullet Resist Shredder I Decay

- text: Cooldown reduced from 27s to 25s

- type: buff

- affected1: Decay I Suppressor

- text: Duration reduced from 4s to 2.5s

- type: nerf

- affected1: Suppressor I Mystic Slow

- text: Duration increased from 2s to 2.5s

- type: buff

- affected1: Mystic Slow I Titanic Magazine

- text: Ammo increased from 65% to 75%

- type: buff

- affected1: Titanic Magazine I Ethereal Shift

- text: Cooldown reduced from 35s to 30s

- type: buff

- affected1: Ethereal Shift I Rescue Beam

- text: Cast range increased from 40m to 45m

- type: buff

- affected1: Rescue Beam

- text: Cooldown reduced from 45s to 40s

- type: buff

- affected1: Rescue Beam I Silence Glyph

- text: Cooldown reduced from 35s to 30s

- type: buff

- affected1: Silence Glyph I Superior Stamina

- text: Stamina increased from +2 to +3

- type: buff

- affected1: Superior Stamina

- text: Fire Rate increased from +12% to +15%

- type: buff

- affected1: Superior Stamina

- text: Spirit Bonus after 2nd jump/dash increased from +20 to +25

- type: buff

- affected1: Superior Stamina I Lifestrike

- text: Slow duration increased from 1.5s to 2s

- type: buff

- affected1: Lifestrike

- text: Heal increased from 40% of damage to 45%

- type: buff

- affected1: Lifestrike I Majestic Leap

- text: Cooldown increased from 20s to 26s

- type: nerf

- affected1: Majestic Leap

- text: Damage cooldown window increased from 4s to 5s

- type: change

- affected1: Majestic Leap

- text: Fixed cooldown reduction affecting the damage cooldown

- type: fix

- affected1: Majestic Leap I Knockdown

- text: Cooldown reduced from 40s to 30s

- type: buff

- affected1: Knockdown I Improved Spirit

- text: Spirit Power increased from +15 to +18

- type: buff

- affected1: Improved Spirit I Tesla Bullets

- text: Bounce radius increased from 7m to 9m

- type: buff

- affected1: Tesla Bullets I Burst Fire

- text: Now increases your slide distance and duration by 25%

- type: buff

- affected1: Burst Fire I Metal Skin

- text: Now prevents all weapon damage instead of blocking bullets (this allows procs to go through)

- type: change

- affected1: Metal Skin I Inhibitor

- text: Moved from Weapon tree to Vitality

- type: change

- affected1: Inhibitor

- text: No longer requires the component Slowing Bullets

- type: change

- affected1: Inhibitor

- text: Now has +175 Health

- type: change

- affected1: Inhibitor

- text: Weapon Damage reduced from 30% to 20%

- type: change

- affected1: Inhibitor I Crippling Headshot

- text: Bullet and Spirit Lifesteal reduced from 15% to 10%

- type: nerf

- affected1: Crippling Headshot I Unstoppable

- text: Active Spirit Resistance reduced from 40% to 20%

- type: nerf

- affected1: Unstoppable I Ricochet

- text: Ricochet Damage increased from 40% to 45%

- type: buff

- affected1: Ricochet

- text: Ammo increased from 30% to 35%

- type: buff

- affected1: Ricochet I Vampiric Burst

- text: Now grants +150 Health

- type: buff

- affected1: Vampiric Burst

- text: Weapon Damage increased from 20% to 25%

- type: buff

- affected1: Vampiric Burst

- text: Can now be cast while busy (such as while you are shooting)

- type: buff

- affected1: Vampiric Burst I Siphon Bullets

- text: Max HP Steal increased from 40 to 45

- type: buff

- affected1: Siphon Bullets I Spiritual Overflow

- text: Cooldown reduction increased from 10% to 15%

- type: buff

- affected1: Spiritual Overflow

- text: Bonus Spirit Power increased from +35 to +40

- type: buff

- affected1: Spiritual Overflow I Frenzy

- text: Low HP Spirit Resist increased from +25% to +30%

- type: buff

- affected1: Frenzy

- text: Fixed tooltip on Spirit Resist missing the %

- type: fix

- affected1: Frenzy I Shadow Weave

- text: Now grants +30% Ammo

- type: buff

- affected1: Shadow Weave

- text: Ambush Fire Rate increased from +50% to +60%

- type: buff

- affected1: Shadow Weave

- text: Ambush Spirit Power increased from +40 to +55

- type: buff

- affected1: Shadow Weave

- text: Invisibility no longer plays footstep sounds (general change)

- type: buff

- affected1: Shadow Weave

- text: Casting the item immediately puts you into Sprint mode

- type: buff

- affected1: Shadow Weave I Leech

- text: Now grants +7 Spirit

- type: buff

- affected1: Leech I Mystic Reverb

- text: Delayed damage increased from 30% to 40%

- type: buff

- affected1: Mystic Reverb I Boundless Spirit

- text: Spirit Power increased from +55 to +60

- type: buff

- affected1: Boundless Spirit

- text: Bonus Health increased from +175 to +200

- type: buff

- affected1: Boundless Spirit

## Heroes

- H Abrams

- text: Improved misc issues with collision

- type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text: can be held for up to 3 seconds. Press the ability again anytime to land.

- type: change

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: hitbox reduced from 36 inches to 33

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: cooldown increased from 100s to 110s

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: move speed increased from 3.8 to 4.2

- type: buff

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text: T1 radius reduced from +3m to +2m

- type: nerf

- affected1: Dynamo

- affected2: Singularity

- text: falls 70% slower when [Majestic Leap](Majestic Leap.md)} down is used (similar to the hero falling slower normally when casting the ability from an elevation)

- type: change

- affected1: Dynamo

- affected2: Singularity H Grey Talon

- text: Fixed being evaded by's

- type: fix

- affected1: Grey Talon

- affected2: Charged Shot

- text: cooldown increased from 30s to 33s

- type: nerf

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: can now explode in the air by pressing the release key

- type: change

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: cooldown reduced from 29s to 27s

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: T2 cooldown changed from -15s to -13s

- type: nerf

- affected1: Haze

- affected2: Sleep Dagger

- text: T2 changed to "Replenishes stamina on cast and grants +40% Stamina Regen"

- type: change

- affected1: Haze

- affected2: Smoke Bomb

- text: bonus damage no longer ignores bullet falloff

- type: nerf

- affected1: Haze

- affected2: Fixation

- text: cast point reduced from 0.8s to 0.4s

- type: buff

- affected1: Haze

- affected2: Bullet Dance

- text: move speed increased from 3.5 to 4

- type: buff

- affected1: Haze

- affected2: Bullet Dance H Infernus

- text: Fixed duration not being affected by duration extender

- type: fix

- affected1: Infernus

- affected2: Flame Dash H Ivy

- text: now does 50% less damage to objectives

- type: nerf

- affected1: Ivy

- affected2: Kudzu Bomb H Kelvin

- text: movespeed limit is now applied via a reduction rather than a speed cap (to allow items to be combined for faster movement like Surge of Power)

- type: change

- affected1: Kelvin

- affected2: Arctic Beam H Lady Geist

- text: no longer starts decaying the arm time while in the air

- type: buff

- affected1: Lady Geist

- affected2: Essence Bomb

- text: arm time reduced from 1s to 0.5s (this is a nerf for long distance bombs)

- type: nerf

- affected1: Lady Geist

- affected2: Essence Bomb

- text: T3 changed to "After swap gain +40% Fire Rate and +40% Spirit Resistance for 8s"

- type: change

- affected1: Lady Geist

- affected2: Soul Exchange H Lash

- text: Fixed it being possible to lose your full lock on with sometimes if you look away

- type: fix

- affected1: Lash

- affected2: Death Slam H McGinnis

- text: Turret range reduced from 30m to 25m

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: Turret HP scaling reduced from 40% to 30% (affects initial HP too)

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: Turret cooldown reduced from 35s to 30s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: Turret Charge Time reduced from 8s to 6s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: Base Spirit Resist increased from 20% to 25%

- type: buff

- affected1: McGinnis

- text: Base Regen increased from 1 to 2

- type: buff

- affected1: McGinnis

- text: cooldown reduced from 35s to 30s

- type: buff

- affected1: McGinnis

- affected2: Spectral Wall

- text: cooldown reduced from 110s to 100s

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage H Mo & Krill

- text: You can now cast items and while spinning out of - type: change

- affected1: Mo & Krill

- affected2: Burrow

- text: bonus health per kill increased from 25 to 30

- type: buff

- affected1: Mo & Krill

- affected2: Combo H Paradox

- text: cooldown increased from 22s to 24s

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: cooldown increased from 35s to 45s

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine H Pocket

- text: base damage reduced from 40 to 35

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: T1 reduced from +20 to +15

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: Fixed a recent change causing to not play damage at the destination when teleporting with - type: fix

- affected1: Pocket

- affected2: Enchanter's Satchel

- affected3: Flying Cloak H Seven

- text: now uses the new instant cast option that Bebop Bomb uses

- type: change

- affected1: Seven

- affected2: Static Charge

- text: spirit scaling increased from 0.1 to 0.2 (new total with T3 is now from 0.5 to 0.6)

- type: buff

- affected1: Seven

- affected2: Power Surge H Vindicta

- text: debuff duration increased from 5s to 6s

- type: buff

- affected1: Vindicta

- affected2: Crow Familiar

- text: bonus damage increased from 130 to 145

- type: buff

- affected1: Vindicta

- affected2: Assassinate H Yamato

- text: now provides 80% Damage Resistance and 80% Debuff Resistance instead of invulnerability during the post-channel buff

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation

- text: cooldown reduced from 110s to 100s

- type: buff

- affected1: Yamato

- affected2: Shadow Transformation

- text: T3 increased from +1s to +1.5s

- type: buff

- affected1: Yamato

- affected2: Shadow Transformation
