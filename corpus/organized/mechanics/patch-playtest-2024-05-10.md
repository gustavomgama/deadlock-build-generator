---
title: "Patch/Playtest/2024-05-10"
pageid: 588
source: liquipedia-deadlock-md
---

- name: Playtest - May 10 2024

- version: 2024-05-10

- release: May 10, 2024

- highlight1: Gameplay Updates

- highlight2: New Key

- highlight3: Sound Updates

- highlight4: Bug Fixes

- highlight5: Item Updates

- highlight6: Hero Updates

- previous: Patch/Playtest/2024-05-032024-05-03

- next: Patch/Playtest/2024-05-132024-05-13

## General

Sandbox mode now supports entering it with your party Sandbox mode now has troopers spawning on the left side Added Search By Match ID to the Watch Tab Added Filter By Hero to the Watch Tab You can now see an indicator for enemy troopers when near them if they are behind a wall or offscreen (primarly improves tracking their positions during the lane) Map is now precached while in the queue to improve loading times into matches Visual and Audio updates to the shop Added a key for toggling replays being paused (defaults to P) Pocket Affliction visual and sound effects reworked Pocket Enchanter’s Satchel visual effects updated Fixed a bug where Pocket’s briefcase would stop animating when the duration upgrade was taken Updated Divine Barrier sound effects Updated Dynamo VO for Quantum Entanglement and a few other missing lines Hero death voices are now broadcast more widely Fixed being unable to ping while casting or channeling Fixed various issues with hero abilities causing you to be stuck in walls Fixed players being able to kill themselves pre-match and run around in the map Fixed Ice Dome effects disappearing while still active if Kelvin dies during it Simplify some visuals with Seven’s Storm Cloud radius indicator to help clarify the bounds Fixed Stamina not appearing to regenerate while spectating Improve the text display when a replay is still processing after a match

- text: Fixed boss moving around while the game is paused

- type: fix

- affected1: Walker Fixed some controller input issues Fortitude now starts on cooldown to prevent purchasing and selling in the field for significant regen Updated Decay item sound effects Updated Berserker item visuals Fixed visual bug on Spirit Urn when dropping on the ground Fixed Restorative Locket Spirit Resist not working Fixed items not updating in the UI when purchased from the shop while spectating a teammate

## Items

- I Spirit Strike

- text: Buff duration increased from 12s to 18s

- type: buff

- affected1: Spirit Strike

- text: Melee damage bonus increased from 15% to 20%

- type: buff

- affected1: Spirit Strike I Hollow Point Ward

- text: Spirit Shield increased from +70 to +80

- type: buff

- affected1: Hollow Point Ward I Melee Lifesteal

- text: Cooldown reduced from 10s to 8s

- type: buff

- affected1: Melee Lifesteal I Alchemical Fire

- text: Min/Max DPS increased from 30/60 to 40/80

- type: buff

- affected1: Alchemical Fire I Restorative Locket

- text: Max Stacks increased from 12 to 15

- type: buff

- affected1: Restorative Locket

- text: Cooldown increased from 15s to 18s

- type: nerf

- affected1: Restorative Locket I Reactive Barrier

- text: Barrier duration increased from 10s to 13s

- type: buff

- affected1: Reactive Barrier

- text: Cooldown reduced from 60s to 40s

- type: buff

- affected1: Reactive Barrier I Return Fire

- text: No longer has Spirit and Fire Rate bonus during the active

- type: change

- affected1: Return Fire

- text: Now passively always gives +7 Spirit and +7% Fire Rate

- type: change

- affected1: Return Fire I Slowing Hex

- text: Cooldown reduced from 30s to 25s

- type: buff

- affected1: Slowing Hex I Decay

- text: Cooldown reduced from 25s to 22s

- type: buff

- affected1: Decay

- text: Cast range increased from 20m to 30m

- type: buff

- affected1: Decay I Enduring Speed

- text: Movement Speed increased from 1 to 1.25

- type: buff

- affected1: Enduring Speed I Suppressor

- text: Now provides +50 Health

- type: buff

- affected1: Suppressor I Quicksilver Reload

- text: Now passively has a +10% reload time penalty

- type: buff

- affected1: Quicksilver Reload I Divine Barrier

- text: No longer restores any Stamina on the target (previously fully restored it)

- type: nerf

- affected1: Divine Barrier I Warp Stone

- text: No longer slows your hero for 3s

- type: buff

- affected1: Warp Stone

- text: Bullet Resist duration increased from 3s to 5s

- type: buff

- affected1: Warp Stone I Withering Whip

- text: Cast range increased from 12m to 20m

- type: buff

- affected1: Withering Whip I Knockdown

- text: Cooldown reduced from 55s to 50s

- type: buff

- affected1: Knockdown

- text: Now provides +200 Spirit Shield

- type: buff

- affected1: Knockdown I Escalating Resilience

- text: Resist per stack increased from 1% to 2%

- type: buff

- affected1: Escalating Resilience I Superior Stamina

- text: Spirit buff duration increased from 5s to 8s

- type: buff

- affected1: Superior Stamina I Lifestrike

- text: Slow duration increased from 1s to 1.5s

- type: buff

- affected1: Lifestrike

- text: Cooldown reduced from 10s to 8s

- type: buff

- affected1: Lifestrike I Heroic Aura

- text: Active radius increased from 20m to 30m

- type: buff

- affected1: Heroic Aura I Curse

- text: Now provides +15% Clip

- type: buff

- affected1: Curse

- text: Duration increased from 3.5s to 3.75s

- type: buff

- affected1: Curse I Shadow Weave

- text: Now provides +15 Health Regen

- type: buff

- affected1: Shadow Weave I Phantom Strike

- text: No longer passively provides +500 Bullet Shield

- type: change

- affected1: Phantom Strike

- text: Now provides +200 Health

- type: change

- affected1: Phantom Strike

- text: When using the active, gain a temporary +500 Bullet Shield for 7 seconds

- type: change

- affected1: Phantom Strike

- text: Now deals 200 damage on impact

- type: change

- affected1: Phantom Strike I Vampiric Burst

- text: Active Bullet Lifesteal increased from 40% to 60%

- type: buff

- affected1: Vampiric Burst I Unstoppable

- text: Movement Speed increased from +1 to +1.25

- type: buff

- affected1: Unstoppable I Mystic Reverb

- text: Spirit Lifesteal increased from +10% to +15%

- type: buff

- affected1: Mystic Reverb

- text: Spirit Resist increased from +10% to +15%

- type: buff

- affected1: Mystic Reverb I Crippling Headshot

- text: Headshot Resistance Reduction increased from 30% to 35%

- type: buff

- affected1: Crippling Headshot I Diviner's Kevlar

- text: Channeling Spirit bonus increased from +40 to +50

- type: buff

- affected1: Diviner's Kevlar

## Gameplay

Sprint is now always considered active as long as you are out of combat (haven’t taken or dealt damage for 5s, healthbar is now a little transparent when out of combat).

Fixed various inconsistencies and scenarios with how Sprint speed was calculated. Previously there were many conditions that could result in you losing the bonus.

Patron (Weakened) now has 40hp/s regen when it has not taken damage for 30s Medic Troopers no longer use their heal on troopers if there is a hero within 30m Zipline Speed Boost cooldown reduced from 420s to 380s Damage over time no longer prevents zipline usage Adjusted how the Anti Backdoor system works. It does a little less % damage reduction now, but it regens “backdoor damage” dealt to it over time. Backdoor damage is defined as any damage taken with no candle troopers within 50m in the last 20 seconds.

Troopers run speed increased from 9.1 m/s to 10 m/s Troopers DPS vs Patrons reduced from 110 DPS to 80 DPS Troopers DPS vs Walkers from 110 DPS to 80 DPS

- text: DPS vs Base from 110 DPS to 80 DPS

- type: nerf

- affected1: Guardian

- affected2: Trooper Crate Powerups: Removed Zipline buff as a potential drop Crate Powerups: Increased Health Regen drop from 1.25% Regen to 1.5% Crate Powerups: Added Fire Rate drop, provides +20% Fire Rate for 25s

- text: [Vaults](Vaults.md) base bounty increased from 200 to 225

- type: buff

- affected1: Sinner's Sacrifice Fixed some issues that allowed players to more easily camp players in the spawn area

## Heroes

- H Abrams

- text: Reduced chances that Leap gets stuck on geometry during the downward phase

- type: fix

- affected1: Abrams

- affected2: Leap H Bebop

- text: No longer has an innate +15% Spirit Resist

- type: nerf

- affected1: Bebop

- text: Now has innate +20% Bullet Resist

- type: buff

- affected1: Bebop

- text: cooldown reduced from 27s to 22s

- type: buff

- affected1: Bebop

- affected2: Hook

- text: T3 reduced from -15s to -12s Cooldown

- type: buff

- affected1: Bebop

- affected2: Hook

- text: Speed increased from 2700 to 3000

- type: buff

- affected1: Bebop

- affected2: Hook

- text: Return Speed increased from 1800 to 2200

- type: buff

- affected1: Bebop

- affected2: Hook

- text: DPS increased from 180 to 210

- type: buff

- affected1: Bebop

- affected2: Hook H Grey Talon

- text: damage increased from 105 to 115

- type: buff

- affected1: Grey Talon

- affected2: Charged Shot

- text: Multishot increased from 3 to 5

- type: buff

- affected1: Grey Talon

- affected2: Rain of Arrows H Kelvin

- text: cooldown reduced from 30s to 26s

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade H Infernus

- text: Fixed refreshing from item damage

- type: fix

- affected1: Infernus

- affected2: Afterburn H Ivy

- text: Base stamina increased from 3 to 4

- type: buff

- affected1: Ivy H Lash

- text: now additionally damages enemies within 2m of Lash on impact

- type: buff

- affected1: Lash

- affected2: Ground Strike

- text: radius reduced from 16m to 14m

- type: nerf

- affected1: Lash

- affected2: Ground Strike

- text:'s ground preview now lines up under Lash when cast on the ground

- type: fix

- affected1: Lash

- affected2: Ground Strike

- text: T3 reduced from +100% to +85%

- type: fix

- affected1: Lash

- affected2: Ground Strike

- text: Bullet Damage growth increased from 0.76 to 1.0

- type: buff

- affected1: Lash

- text: tether visuals now improved to communicate the different phases its in - type: fix

- affected1: Lash

- affected2: Death Slam H Lady Geist

- text: now comes out quicker and no longer slows you

- type: buff

- affected1: Lady Geist

- affected2: Malice H McGinnis

- text: Spirit Resistance increased 50% to 60%

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: Mini Turret Health increased from 30% to 40%

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: T2 increased from +5m Range to +10m

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: Fixed issues with not damaging units within the target area

- type: fix

- affected1: McGinnis

- affected2: Heavy Barrage H Mo & Krill

- text: Base HP increased from 650 to 700

- type: buff

- affected1: Mo & Krill

- affected2: Mini Turret

- text: damage increased from 40 to 50

- type: buff

- affected1: Mo & Krill

- affected2: Scorn

- text: debuff duration increased from 10s to 16s

- type: buff

- affected1: Mo & Krill

- affected2: Scorn

- text: duration increased from 3.5s to 4s

- type: buff

- affected1: Mo & Krill

- affected2: Sand Blast

- text: T3 DPS increased from +30 to +40

- type: buff

- affected1: Mo & Krill

- affected2: Combo H Paradox

- text: bullet freeze duration no longer increases with Spirit or Duration Extender

- type: nerf

- affected1: Paradox

- affected2: Time Wall

- text: bullet freeze base duration reduced from 1.5 to 1.25

- type: nerf

- affected1: Paradox

- affected2: Time Wall

- text: no longer deals damage to Mid Boss

- type: nerf

- affected1: Paradox

- affected2: Time Wall

- affected3: Mid Boss

- text: Max Damage Amp reduced from 150% to 125%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: T3 no longer provides +50% Min Damage Amp

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: T3 reduced from +125% Max Damage to +75%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine H Pocket

- text: Gun damage per bullet reduced from 6 to 5.6

- type: nerf

- affected1: Pocket

- text: DPS reduced from 30 to 26

- type: nerf

- affected1: Pocket

- affected2: Affliction H Seven

- text: rebalanced around no longer reducing fire rate (similar shock value effectiveness as before)

- type: change

- affected1: Seven

- affected2: Power Surge H Warden

- text: damage increased from 48 to 55

- type: buff

- affected1: Warden

- affected2: Alchemical Flask H Yamato

- text: cooldown reduced from 13s to 11s

- type: buff

- affected1: Yamato

- affected2: Crimson Slash

- text: physics/world collision reduced from 15 to 4 (allowing it to be more easily used near objects)

- type: buff

- affected1: Yamato

- affected2: Power Slash

- text: radius increased from 14m to 16m

- type: buff

- affected1: Yamato

- affected2: Shadow Explosion

- text: Fire Rate and Spirit buff duration increased from 15s to 20s

- type: buff

- affected1: Yamato

- affected2: Shadow Explosion

- text: T3 Spirit bonus increased from +10% to +15%

- type: buff

- affected1: Yamato

- affected2: Shadow Explosion

- text: T3 Fire Rate bonus increased from +5% to +10%

- type: buff

- affected1: Yamato

- affected2: Shadow Explosion
