---
title: "Patch/Playtest/2025-07-29"
pageid: 2359
source: liquipedia-deadlock-md
---

- name: Patch - July 29, 2025

- version: 2025-07-29

- highlight1: General, Gameplay, Items and Heroes improvements

- release: July 29, 2025

- previous: Patch/Playtest/2025-07-042025-07-04

- next: Patch/Playtest/2025-08-012025-08-01

- footnotes: Source: [07-29-2025 Update](https://forums.playdeadlock.com/threads/07-29-2025-update.72760/)

## General

Mid Boss HP is now fixed at the spawn time. Base HP increased from 6725 to 12500 and growth reduced from 470 to 200.

Reworked Rejuv reward from Mid Boss. No longer buffs troopers, reduces respawn time and buffs various stats.

Upon death, 3 rejuv crystals fall to the ground (4 for subsequent midboss kills).

Claiming one now grants you in place revive after 3s.

If you already claimed one and claim another, it'll go to an ally (priority is closest allies first, then most recent dead allies).

Dying with Rejuv no longer counts as a kill/death nor gives out bounties.

While you have the Rejuv buff, you gain the following: +20% Max HP, +20% Fire Rate, and +15% Spirit Damage.

Gaining the buff heals you to full and lasts up to 7 minutes.

Meleeing a mantling enemy no longer cancels their mantle, instead it applies 80% movement slow that ramps down to 20% over 2s.

Adding a debuff that makes you climb ropes 40% slower for 4s after you've taken player damage. This debuff only exists when you're on a rope, and tapers off to 0% in the last 1s of the damage window.

Slight reduction to the amount of turning you can do while performing a heavy melee.

Light melee base damage reduced by 20% (except for - H Viscous, H Calico and - H Bebop ).

Heavy Melee cooldown increased from 0.9s to 1.0s.

Heavy Melee cooldown when missing increased from 0.9s to 1.3s.

Parried stun duration is no longer reduced by debuff resistance.

Parry bonus damage is no longer melee specific, now affects all damage types (reduced from 35% to 30%).

Heroes now have different dash speeds (same distance, slower to get there). They are placed into 3 buckets to start: Bucket 1: +5% - H Ivy, H Haze, H Holliday, H Calico, H Grey Talon, H Paradox Bucket 2: -5% - H Seven, H Mirage, H Lash, H Yamato, H Pocket, H Viscous, H Vyper, H Warden, H Vindicta, H Sinclair, H Wraith, H Infernus, H Lady Geist Bucket 3: -15% - H Mo & Krill, H Abrams, H Shiv, H Dynamo, H Bebop, H Kelvin, H McGinnis Removed the teleporters behind the Walkers.

After 20 minutes, trooper spawn time is reduced from 30s to 25s.

Trooper bounty growth reduced from 1.5 to 1.2.

Removed the bounce pads on top of the Nursery/Fish Market rooftop leading back to Mid.

Trooper ally split updated from 100/65/30/20/15/11% to 100/65/28/15/12/8%.

Breakables souls growth per minute reduced from 2.6 to 2.0.

Reduced comeback multipliers a bit.

Neutrals bounty increased by 15% (strong neutrals +25%).

Medium Neutrals respawn rate increased from 360s to 420s (+17%).

Strong Neutrals respawn rate increased from 480s to 600s (+25%).

- M Sinner's Sacrifice: Retaliate damage increased from 40 to 60.

- M Sinner's Sacrifice: Heavy melee end success bonus now grants 4 buffs rather than 3 (these also take a little longer to kill now due to the melee timing changes).

Hero bounties are now reduced based on the amount of players, similar to the trooper mechanic. (Means kills are less efficient/rewarding when its a big group, 1/2/3/4/5/6 players are 100/100/90/85/80/75% efficient).

Movespeed Slow when shooting reduced from -30% to -25%.

Side Walkers HP increased by 10%.

Objectives no longer have 20-25% Spirit Resistance.

The following abilities now do 50% damage to objectives: M Last Stand, M Storm Cloud, M Hyper Beam, M Heavy Barrage.

Trooper: Walk speed increased from 6.1 to 6.3.

Trooper: Run speed increased from 11 to 13.

Minor respawn curve reductions (19 min from 40s to 35s, 30 min from 80s to 75s, 40 min is still 85s).

Update the Zipline Knockdown to make the players go straight down and not start the stun timer until they hit the ground.

Zipline knockoff stun duration reduced from 3s to 2.5s.

Added new UI indicator on HP for showing pending heal (affects things like H Abrams's passive).

## Heroes

- H Bebop

- text: No longer has +10% Base Bullet Resistance

- type: change

- affected1: Bebop

- text: Now has +0.3% Bullet Resistance per Boon

- type: change

- affected1: Bebop

- text: T2 reduced from +50% Weapon Damage to +40%

- type: nerf

- affected1: Bebop

- text: T2 duration reduced from 12s to 9s

- type: nerf

- affected1: Bebop

- text: T1 reduced from +25% Weapon Damage to +20%

- type: nerf

- affected1: Bebop

- text: T1 duration reduced from 10s to 6s

- type: nerf

- affected1: Bebop H Dynamo

- text: damage height increased from 0.5m to 0.7m

- type: buff

- affected1: Dynamo H Grey Talon

- text: Curse duration increased from 1.75s to 2s

- type: buff

- affected1: Grey Talon

- text: cooldown reduced from 135s to 120s

- type: buff

- affected1: Grey Talon H Kelvin

- text: T3 no longer bounces off of objectives

- type: change

- affected1: Kelvin H Lady Geist

- text: no longer sticks to units

- type: change

- affected1: Lady Geist

- text: cooldown increased from 10.5 to 14.5

- type: nerf

- affected1: Lady Geist

- text: radius increased from 7m to 9m

- type: buff

- affected1: Lady Geist

- text: T1 changed from "+2m Radius" to "-4s Cooldown"

- type: change

- affected1: Lady Geist

- text: projectile speed increased by 25%

- type: buff

- affected1: Lady Geist H McGinnis

- text: Health per boon reduced from 56 to 52

- type: nerf

- affected1: McGinnis

- text: fixed a bug where aiming at long stairs would sometimes cause the preview to go through it

- type: fix

- affected1: McGinnis

- text: change the preview particle

- type: change

- affected1: McGinnis

- text: now supports Lag Compensation

- type: change

- affected1: McGinnis

- text: will now erupt where the preview Particle is displaying when manually triggering the Eruption

- type: change

- affected1: McGinnis

- text: health per boon reduced from 12 to 10

- type: nerf

- affected1: McGinnis H Mirage

- text: Base bullet damage reduced by 10%

- type: nerf

- affected1: Mirage H Paradox

- text: Bullet damage scaling increased by 10%

- type: buff

- affected1: Paradox H Pocket

- text: initial Current HP % damage increased from 10% to 12%

- type: buff

- affected1: Pocket H Shiv

- text: now only builds up from damaging players

- type: change

- affected1: Shiv

- text: buildup for all damage types increased by 20% (easier to build up)

- type: buff

- affected1: Shiv

- text: decay duration increased from 9s to 12s

- type: buff

- affected1: Shiv

- text: duration reduced from 12s to 6s

- type: nerf

- affected1: Shiv

- text: cooldown reduced from 60s to 45s

- type: buff

- affected1: Shiv

- text: damage clear increased from 30% to 40%

- type: buff

- affected1: Shiv

- text: T1 and T2 swapped

- type: change

- affected1: Shiv

- text: T3 increased from +20% to +35%

- type: buff

- affected1: Shiv H Seven

- text: Base movement speed reduced from 7.1 to 6.9

- type: nerf

- affected1: Seven

- text: Move Speed spirit scaling reduced from 0.023 to 0.02

- type: nerf

- affected1: Seven

- text: T1 and T2 swapped

- type: change

- affected1: Seven

- text: cooldown increased from 170s to 180s

- type: nerf

- affected1: Seven

- text: Spirit Power scaling reduced from 0.7 to 0.65

- type: nerf

- affected1: Seven

- text: DPS reduced from 95 to 90

- type: nerf

- affected1: Seven

- text: T3 reduced from +65 to +60

- type: nerf

- affected1: Seven H Vindicta

- text: T1 bounce no longer bounces off of objectives

- type: change

- affected1: Vindicta

- text: T3 reduced from +2m to +1m

- type: nerf

- affected1: Vindicta H Viscous

- text: cooldown reduced from 30s to 24s

- type: buff

- affected1: Viscous

- text: T3 increased from -11.5s Cooldown to -12s

- type: nerf

- affected1: Viscous H Warden

- text: Bullet base damage reduced from 17 to 15

- type: nerf

- affected1: Warden

- text: Bullet damage growth increased from 0.38 to 0.44

- type: buff

- affected1: Warden

- text: DPS reduced from 74 to 70

- type: nerf

- affected1: Warden

- text: lifesteal vs non-heroes reduced from 15% to 10%

- type: nerf

- affected1: Warden H Wraith

- text: Bullet damage increased from 4.95 to 5.115

- type: buff

- affected1: Wraith

- text: Bullet damage growth reduced from 0.18 to 0.175 (same overall peak damage)

- type: nerf

- affected1: Wraith H Yamato

- text: Alt Fire base damage reduced from 63.36 to 50

- type: nerf

- affected1: Yamato

- text: Alt Fire base damage now grows per boon (+0.7)

- type: change

- affected1: Yamato

## Items

- M Weapon I Restorative Shot

- text: Heal from NPC reduced from 20 to 15

- type: nerf

- affected1: Restorative Shot

- text: Weapon damage reduced from 8% to 6%

- type: nerf

- affected1: Restorative Shot I Fleetfoot

- text: Bullet Resistance reduced from 10% to 6%

- type: nerf

- affected1: Fleetfoot I Melee Charge

- text: Bullet Resistance reduced from 10% to 6%

- type: nerf

- affected1: Melee Charge I Spirit Shredder Bullets

- text: Spirit Resist Reduction increased from -7% to -8%

- type: buff

- affected1: Spirit Shredder Bullets I Slowing Bullets

- text: After buildup is achieved, debuff duration is refreshed rather than starting buildup again

- type: change

- affected1: Slowing Bullets I Swift Striker

- text: Fire Rate increased from 18% to 20%

- type: buff

- affected1: Swift Striker I Express Shot

- text: Primary weapon damage increased from 165% to 185%

- type: buff

- affected1: Express Shot I Toxic Bullets

- text: Damage reduced from 2.5% Max HP to 2.1%

- type: nerf

- affected1: Toxic Bullets

- text: Now scales with Spirit Power (0.005%)

- type: change

- affected1: Toxic Bullets I Berserker

- text: Bullet Resistance reduced from 16% to 8%

- type: nerf

- affected1: Berserker I Blood Tribute

- text: Healing Reduction reduced from -50% to -40%

- type: nerf

- affected1: Blood Tribute

- text: Now grants +4 Out of Combat Regen

- type: change

- affected1: Blood Tribute

- text: Active Move Speed increased from 1.75 to 2

- type: buff

- affected1: Blood Tribute I Weighted Shots

- text: Bullet Velocity reduced from -25% to -30%

- type: nerf

- affected1: Weighted Shots

- text: Stamina Recovery reduced from -10% to -20%

- type: nerf

- affected1: Weighted Shots I Hunter's Aura

- text: Now grants +1 Sprint

- type: change

- affected1: Hunter's Aura I Spirit Rend

- text: Spirit Resist Reduction increased from -7% to -8%

- type: buff

- affected1: Spirit Rend I Crushing Fists

- text: Bullet Resistance reduced from 20% to 12%

- type: nerf

- affected1: Crushing Fists

- text: Heavy Melee Distance reduced from +70% to +60%

- type: nerf

- affected1: Crushing Fists I Armor Piercing Rounds

- text: Chance reduced from 60% to 50%

- type: nerf

- affected1: Armor Piercing Rounds I Shadow Weave

- text: Duration reduced from 25s to 18s

- type: nerf

- affected1: Shadow Weave

- text: Cooldown reduced from 40s to 32s

- type: buff

- affected1: Shadow Weave

- text: Now grants +25% Melee Damage on Ambush reveal

- type: change

- affected1: Shadow Weave I Capacitor

- text: Damage increased from 45 to 50

- type: buff

- affected1: Capacitor I Spellslinger

- text: Buff duration increased from 10s to 14s

- type: buff

- affected1: Spellslinger M Vitality I Guardian Ward

- text: Cooldown reduced from 45s to 40s

- type: buff

- affected1: Guardian Ward I Weapon Shielding

- text: Barrier reduced from 400 to 325

- type: nerf

- affected1: Weapon Shielding

- text: Barrier no longer scales with Spirit Power (1.116)

- type: change

- affected1: Weapon Shielding

- text: Barrier now scales with Boons (+4)

- type: change

- affected1: Weapon Shielding I Spirit Shielding

- text: Barrier reduced from 400 to 325

- type: nerf

- affected1: Spirit Shielding

- text: Barrier no longer scales with Spirit Power (1.116)

- type: change

- affected1: Spirit Shielding

- text: Barrier now scales with Boons (+4)

- type: change

- affected1: Spirit Shielding I Return Fire

- text: Bullet Resistance reduced from 10% to 6%

- type: nerf

- affected1: Return Fire

- text: Bullet Damage Returned reduced from 60% to 50%

- type: nerf

- affected1: Return Fire

- text: Spirit Damage return from 30% to 25%

- type: nerf

- affected1: Return Fire I Veil Walker

- text: Cooldown reduced from 14s to 12s

- type: buff

- affected1: Veil Walker I Metal Skin

- text: Cooldown reduced from 24s to 20s

- type: buff

- affected1: Metal Skin I Debuff Remover

- text: Bonus Health reduced from 125 to 100

- type: nerf

- affected1: Debuff Remover

- text: Cooldown increased from 45s to 50s

- type: nerf

- affected1: Debuff Remover I Trophy Collector

- text: Out of Combat regen increased from 2 to 3.5

- type: buff

- affected1: Trophy Collector I Spirit Resilience

- text: Spirit Resistance reduced from 30% to 25%

- type: nerf

- affected1: Spirit Resilience I Divine Barrier

- text: Cooldown reduced from 45s to 40s

- type: buff

- affected1: Divine Barrier I Cheat Death

- text: Effect no longer gets pierced by kill events like Killing Blow or Guided Owl

- type: change

- affected1: Cheat Death M Spirit I Rusted Barrel

- text: Now reduces Bullet Resistance by 5%

- type: change

- affected1: Rusted Barrel

- text: Cooldown reduced from 25s to 20s

- type: buff

- affected1: Rusted Barrel I Suppressor

- text: Fire Rate reduction reduced from -35% to -30%

- type: nerf

- affected1: Suppressor I Cold Front

- text: Spirit Resistance reduced from 10% to 6%

- type: nerf

- affected1: Cold Front I Slowing Hex

- text: Duration increased from 3s to 3.5s

- type: buff

- affected1: Slowing Hex I Bullet Resist Shredder

- text: Bullet Resistance Reduction increased from -12% to -13%

- type: buff

- affected1: Bullet Resist Shredder I Spirit Sap

- text: Spirit Power reduction increased from -15 to -18

- type: buff

- affected1: Spirit Sap

- text: Cast Range increased from 30m to 40m

- type: buff

- affected1: Spirit Sap

- text: Bonus Health increased from 50 to 75

- type: buff

- affected1: Spirit Sap I Disarming Hex

- text: Cooldown reduced from 25s to 20s

- type: buff

- affected1: Disarming Hex I Surge of Power

- text: Cooldown increased from 8s to 14s

- type: nerf

- affected1: Surge of Power

- text: Duration increased from 6s to 8s

- type: buff

- affected1: Surge of Power

- text: Fire Rate increased from 20% to 22%

- type: buff

- affected1: Surge of Power

- text: Spirit Power increased from 25 to 28

- type: buff

- affected1: Surge of Power I Tankbuster

- text: Now ignores enemy Spirit Resistance

- type: change

- affected1: Tankbuster

- text: Damage reduced from 6% to 5%

- type: nerf

- affected1: Tankbuster I Decay

- text: Damage increased from 2.4% to 2.6%

- type: buff

- affected1: Decay I Scourge

- text: Projectile speed increased from 800 to 1600

- type: buff

- affected1: Scourge I Focus Lens

- text: Cooldown reduced from 28s to 25s

- type: buff

- affected1: Focus Lens I Vortex Web

- text: Projectile Speed increased from 1800 to 2400

- type: buff

- affected1: Vortex Web
