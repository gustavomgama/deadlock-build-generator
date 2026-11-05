---
title: "Patch/Playtest/2024-05-30"
pageid: 583
source: liquipedia-deadlock-md
---

- name: Playtest - May 30 2024

- version: 2024-05-30

- release: May 30, 2024

- highlight1: Gameplay Updates

- highlight2: Key Updates

- highlight3: Bug Fixes

- highlight4: Item Updates

- highlight5: Hero Updates

- previous: Patch/Playtest/2024-05-242024-05-24

- next: Patch/Playtest/2024-06-012024-06-01

## General

Bots will now replace a human player if the player has been disconnected for more than 30 seconds (hero will retreat home first and then after 30 seconds the bot takes over). After 4 minutes it will start using souls to buy items. During laning phase it will go to its assigned lane, afterwards it will aim to stick near where most allies are located. If the player rejoins the bot will leave. We will work on improving the bot behavior as we get feedback.

Added a temporary matchmaking ban system for people that leave games Reworked the Watch tab to highlight suggested matches to watch. There is currently a limit on the number of people that can watch the same match, so it'll recommend different games if the best suggestions are full. We are working on removing the spectator limit for a future update.

Matches in the watch tab will now indicate if a friend is in that match A paused a game can only be unpaused by the player that paused for the first 30 seconds Once you pause a game, you cannot pause it again within 5 minutes Pause now says the player name pausing it Added a view cone for your player on the minimap to help with finding yourself and the direction you are pointed Added a sound when you receive a chat message Increased the base font size for text chat Increased the duration text chat is visible You can now ping enemy items on the scoreboard to say alert players that the hero has that item.

You can now middle mouse click an ability to say its on cooldown You can now alt click your active items to say if they are ready or not Candle Troopers and other NPCS can no longer see or shoot through Cosmic Veils Changed F1-F5 keys to instantly snap to the team mates rather than move there more slowly

- text: Adjusted the health bar on to be easier to see

- type: fix

- affected1: Walker Match found sound now plays regardless of window focus Added option to give fast stamina regen in Hero Sandbox Minimap player icons now dynamically shrink and adjust positions slightly when there are many overlapping Fixed zooming bypassing the shooting speed penalty Added new effects for Shifting Shroud T1 Boss now has quicker melee animations Fixed Turrets causing backdoor protection to be lost Fixed Guided Owl flying while the game is paused Fixed a bug with using Melee in the air that could cause you to move a lot Fixed some sound issues with Pulse Grenade Added new sprint animations for Abrams Various fixes to Lash's Ground Strike visual effects Fixed various bugs and crashes with hero guides Fixed Turrets not proccing things like Mystic Vulnerability Fixed some outdated details on the minimap Grey Talon's Charged Shot effect matches the damage radius better Added visual tell for when Assassinate is active Fixed some bugs that could cause McGinnis gun to be stuck Updated Zipline Boost hint to say ACTIVE when it is active and only show the cooldown timer when its done Fixed an edge case with Unstoppable and a debuff being applied on the same frame Reduced minimum delay before you can press a button again to cancel a channel/precast from 0.5 to 0.2 Fixed getting stuck going up the ramp on the inner lane street Fixed corner neutral camps not burrowing if they lose line of sight Fixed being able to get on top of the tall border building behind the Chapel and behind the Firehouse

## Gameplay

- text: Lane HP increased from 3750 to 4600

- type: buff

- affected1: Guardian Various adjustments to lane layout to give defenders more options for forward positions near their Guardian

- text: Midlane HP reduced a little bit to match the same HP as the sidelane

- type: nerf

- affected1: Walker

- text: Base moved a little bit further towards the outside of the base

- type: change

- affected1: Guardian Airborne Heavy Melee now triggers when the charge up is complete, rather than waiting for the player to land on the ground (you had to manually release it before) Airborne Heavy Melee distance increased to match ground version Heavy Melee time reduced from 0.6 to 0.55 (same for Air) Crate powerups can now only spawn after 2 minutes (when the small neutrals spawn) Added breakable crates inside each lane's Cosmic Veil Expanded space in some of the lane's Cosmic Veils Audible distance of enemy footsteps is reduced Special 15 minute melee creep now upgrades again at 25 minutes Base zipline speed increased by 10% Extended inner lane urn bridge buildings toward the T1 and added a doorway to allow defenders to shoot down into the canal Removed 3 bush trees on each inner lane near the urn bridge buildings Carved out interior of inner lane tower buildings beside the Guardian and connected to the neutral camp in the underground areas

- text: Moved outer lane on Factory and Mansion sides slightly closer to the stairs

- type: change

- affected1: Walker Carved out interior of outer lane wall buildings beside the Walker to allow forward position for defenders Reduced width of forward base lookout bridges

## Items

- I Basic Magazine

- text: Ammo reduced from +16% to +15%

- type: nerf

- affected1: Basic Magazine

- text: Weapon Damage reduced from +16% to +15%

- type: nerf

- affected1: Basic Magazine I Headshot Booster

- text: Cooldown reduced from 9s to 5s

- type: buff

- affected1: Headshot Booster I Spirit Strike

- text: Health Regen increased from 0.7 to 1

- type: buff

- affected1: Spirit Strike I Enduring Spirit

- text: No longer provides +1 Sprint

- type: nerf

- affected1: Enduring Spirit

- text: +10% Spirit Lifesteal

- type: buff

- affected1: Enduring Spirit I Soul Shredder Bullets

- text: Spirit Amp reduced from 14% to 12%

- type: nerf

- affected1: Soul Shredder Bullets I Slowing Hex

- text: Cooldown increased from 25 to 27

- type: nerf

- affected1: Slowing Hex I Restorative Locket

- text: Spirit increased from +4 to +5

- type: buff

- affected1: Restorative Locket I Decay

- text: Cast range now scales with Spirit (0.2 factor)

- type: buff

- affected1: Decay I Suppressor

- text: Fire rate slow increased from 30% to 35%

- type: buff

- affected1: Suppressor I Enduring Speed

- text: Move Speed increased from +1.25 to +1.4

- type: buff

- affected1: Enduring Speed I Swift Striker

- text: Bullet Resist penalty reduced from -8% to -7%

- type: buff

- affected1: Swift Striker I Alchemical Fire

- text: Now grants +5 Spirit

- type: buff

- affected1: Alchemical Fire

- text: Bullet Shield Health increased from +150 to +175

- type: buff

- affected1: Alchemical Fire

- text: Cooldown reduced from 37 to 34

- type: buff

- affected1: Alchemical Fire I Ethereal Shift (Then called Shifting Shroud)

- text: Duration increased from 2.75 to 3

- type: buff

- affected1: Ethereal Shift

- text: Can now be canceled early

- type: buff

- affected1: Ethereal Shift

- text: Cooldown reduced from 55s to 45s

- type: buff

- affected1: Ethereal Shift I Knockdown

- text: Cooldown reduced from 50s to 40s

- type: buff

- affected1: Knockdown I Superior Stamina

- text: Spirit buff duration increased from 8s to 12s

- type: buff

- affected1: Superior Stamina I Lifestrike

- text: Melee damage increased from +35% to +40%

- type: buff

- affected1: Lifestrike I Toxic Bullets

- text: Now deals half damage against troopers and neutrals

- type: buff

- affected1: Toxic Bullets I Leech

- text: No longer gives +8 Spirit

- type: nerf

- affected1: Leech I Glass Cannon

- text: Weapon Damage reduced from +70% to +65%

- type: nerf

- affected1: Glass Cannon I Mystic Reverb

- text: No longer stops the echo if the target dies

- type: buff

- affected1: Mystic Reverb I Vampiric Burst

- text: Duration reduced from 5s to 4.5s

- type: nerf

- affected1: Vampiric Burst

- text: Lifesteal increased from 60% to 70%

- type: buff

- affected1: Vampiric Burst I Shadow Weave

- text: Invis Sprint increased from +3 to +5

- type: buff

- affected1: Shadow Weave I Curse

- text: Now grants +8 Spirit

- type: buff

- affected1: Curse I Refresher

- text: Spirit Resist increased from +10% to +12%

- type: buff

- affected1: Refresher I Silencer

- text: Ammo increased from +15% to +20%

- type: buff

- affected1: Silencer I Spiritual Overflow

- text: Spirit bonus increased from 30 to 35

- type: buff

- affected1: Spiritual Overflow I Boundless Spirit

- text: Spirit increased from +40 to +45

- type: buff

- affected1: Boundless Spirit

## Heroes

- H Abrams

- text: is now faster to play out

- type: buff

- affected1: Abrams

- affected2: Seismic Impact

- text: now has a very brief busy state upon landing

- type: change

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: width increased from 2.7m to 2.9m

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: Base bullet armor increased from 20% to 24%

- type: buff

- affected1: Bebop H Dynamo

- text: fire rate bonus reduced from 35% to 30%

- type: nerf

- affected1: Dynamo

- affected2: Quantum Entanglement

- text: T1 range increased from +2m to +3m

- type: buff

- affected1: Dynamo

- affected2: Singularity H Grey Talon

- text: spirit scaling improved from 1 to 1.3

- type: buff

- affected1: Grey Talon

- affected2: Charged Shot

- text: duration increased from 13s to 14s

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: Owl T3 increased from 20% to 22%

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: player collision sized increased to regular sizes for these kind of projectiles

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: cooldown increased from 27 to 29

- type: nerf

- affected1: Haze

- affected2: Sleep Dagger

- text: spirit scaling increased from 2.2 to 2.5

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: T2 and T3 swapped

- type: change

- affected1: Haze

- affected2: Smoke Bomb

- text: T3 cooldown improved from -20s to -25s

- type: buff

- affected1: Haze

- affected2: Smoke Bomb H Infernus

- text: T3 reduced from +40 dps to +35

- type: nerf

- affected1: Infernus

- affected2: Afterburn

- text: T1 duration reduced from 8s to 7s

- type: nerf

- affected1: Infernus

- affected2: Flame Dash

- text: T1 Fire Rate slow increased from +30% to +35%

- type: buff

- affected1: Infernus

- affected2: Flame Dash

- text: T2 increased from +40 DPS to +45

- type: buff

- affected1: Infernus

- affected2: Flame Dash

- text: T3 increased from -15s to -20s

- type: buff

- affected1: Infernus

- affected2: Flame Dash H Ivy

- text: T3 improved from +50 DPS to +60

- type: buff

- affected1: Ivy

- affected2: Kudzu Bomb H Kelvin

- text: Base health increased from 550 to 600

- type: buff

- affected1: Kelvin

- text: radius increased from 6 to 6.5

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade

- text: charge time reduced from 10s to 8s

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade

- text: Players can now slide down the - type: change

- affected1: Kelvin

- affected2: Ice Path

- text: slow resistance increased from 50% to 60%

- type: buff

- affected1: Kelvin

- affected2: Ice Path

- text: T3 max spirit increased from 40 to 55

- type: buff

- affected1: Kelvin

- affected2: Ice Path H Lady Geist

- text: cast time reduced from 0.5 to 0.2

- type: buff

- affected1: Lady Geist

- affected2: Soul Exchange H McGinnis

- text: now does less damage to objectives similar to other ability damage

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage H Mo & Krill

- text: no longer affects bosses

- type: nerf

- affected1: Mo & Krill

- affected2: Sand Blast H Paradox

- text: Bullet base damage reduced from 8 to 7.2 (indirectly affects )

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: Bullet growth reduced from 0.48 to 0.42 (indirectly affects )

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: damage reduced from +100% to +85%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: range reduced from 40m to 35m

- type: nerf

- affected1: Paradox

- affected2: Paradoxical Swap

- text: Fixed being able to grab multiple heroes if they were really close to each other

- type: fix

- affected1: Paradox

- affected2: Paradoxical Swap H Pocket

- text: radius increased from 5m to 6m

- type: buff

- affected1: Pocket

- affected2: Barrage

- text: cooldown reduced from 35 to 30

- type: buff

- affected1: Pocket

- affected2: Barrage

- text: T3 increased from 100% to 150%

- type: buff

- affected1: Pocket

- affected2: Barrage

- text: speed increased by 7%

- type: buff

- affected1: Pocket

- affected2: Flying Cloak

- text: T3 increased from +5 damage to +7

- type: buff

- affected1: Pocket

- affected2: Flying Cloak H Vindicta

- text: Now has -10% Base Bullet Resist

- type: nerf

- affected1: Vindicta

- text: no longer grants +1 bonus air speed

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: falloff damage increase reduced from +20% to +10%

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: Fixed flight spirit damage being able to pierce Metal Skin

- type: fix

- affected1: Vindicta

- affected2: Flight H Warden

- text: T1 improved from +15% to +20%

- type: buff

- affected1: Warden

- affected2: Willpower

- text: duration increased from 5s to 6s

- type: buff

- affected1: Warden

- affected2: Last Stand H Wraith

- text: cooldown reduced from 50s to 45s

- type: buff

- affected1: Wraith

- affected2: Project Mind H Yamato

- text: spirit scaling improved from 1.6 to 2.0

- type: buff

- affected1: Yamato

- affected2: Power Slash

- text: no longer does a very minor movement on enemies hit

- type: fix

- affected1: Yamato

- affected2: Power Slash

- text: Fixed sometimes not being a full charge when channeled fully during the Shadow Transformation

- type: fix

- affected1: Yamato

- affected2: Power Slash

- text:'s ability speedup now affects the post-cast durations as well

- type: buff

- affected1: Yamato

- affected2: Shadow Transformation

- text:'s ability speedup now improves the visual animations (cosmetic only change)

- type: change

- affected1: Yamato

- affected2: Shadow Transformation
