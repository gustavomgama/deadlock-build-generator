---
title: "Patch/Playtest/2024-06-13"
pageid: 578
source: liquipedia-deadlock-md
---

- name: Playtest - June 13 2024

- version: 2024-06-13

- release: June 13, 2024

- highlight1: Gameplay Updates

- highlight2: HUD Updates

- highlight3: Bug Fixes

- highlight4: Item Updates

- highlight5: Hero Updates

- previous: Patch/Playtest/2024-06-072024-06-07

- next: Patch/Playtest/2024-06-142024-06-14

## General

Voice/Text chat is now opt-in. There is a prompt pre-match for joining the chat, or you can control it at any time from the ESC menu during a match.

You can now press ESC to mute individual players. Muted accounts will not be alerted, and mutes will persist across games.

Parties can now set their in-game chat mode to be Party-only, All Team or Chat Disabled (if using discord or other programs) Spirit stat has now been renamed to Spirit Power with updated icon Top bar now highlights your lane partner and lane enemies during the laning phase Increased difficulty for hard mode bots Added sandbox option for spawning neutrals Improved the camera when using Dynamo's Quantum Entanglement Added overhead number counter effect for opponents to see the stacks of Berserker Increased the range the enemy-candle-behind-wall indicator shows up from 25m to 35m Fixed ping wheel randomly coming up instantly instead of doing an in-world ping Added ping indicator on the HUD indicating the direction the ping came from (enabled by default in settings) Ping Wheel context slot will now show nothing if there is no context currently Added new UI indicating how many friends you have that are in the game Improved visibility of the edge of Dynamo's Singularity Fixed various issues with bots getting stuck Fixed Build descriptions not showing up properly with the in-game tooltip version Moved HUD elements closer to center for ultra wide monitors Added heal and kill events to the contextual ping wheel slot Fixed AP not showing when you have your hero selected Fixed TAB/ALT not bringing up your abilities when spectating the Patron Added indicator for burrow damage radius for the local player Fixed Affliction sometimes becoming lethal when combined with Escalating Exposure Fixed Yamato's Crimson Slash visual direction being wrong sometimes

- text: Added Patron VO for when allied or enemy base are destroyed

- type: fix

- affected1: Guardian Adjusted the builds drop down in-game to be more clear it can be changed there

- text: Fixed's moving the - type: fix

- affected1: Mid Boss

- affected2: Dynamo Fixed various bugs with Shifting Shroud Added a new "major damage" sound effect to indicate large instances of damage to the local player Fixed Lash's Ground Strike T3 not being accurate in the tooltip Fixed Diviner's Kevlar gaining the Bullet Shield buff if the ultimate was manually cancelled Updated effects for Unstoppable Minor improvements to visibility of Pocket's Affliction cast Updated effects to Alchemical Fire to make it less noisy Reload anims now play correctly in relation to the reload timer. Previously they would end prematurely if reloads were paused during dash/melee/abilities Fixed some bugs with Pocket/channeling A few buildings are 2-3 stories taller Added new effects for Knockdown Added new effects for Vampiric Burst Fixed Mo & Krill gaining Reactive Barrier buff while channeling the ultimate Added instructional text to the bottom of the ping wheel container reminding that they can customize it in settings Changed Ivy's True Form ability name to Stone Form Fixed bugs that were keeping some heroes desperation ability use lines from playing correctly (casting an ability when you're below 10% should play different VO) Fixed several instances of ability use VO getting swallowed up by SFX Boosted volume of ult cast VO Added various ambient sounds - walla, birds, drones - and overall mix tweaks Iterated on binding word sound effects Added Curse item selection start, loop, and end sounds The Patrons no longer care about the well being of the Urn Runner, and so they will stop asking you to protect them (patrons will no longer call out the urn being picked up)

## Gameplay

Added two new underground tunnels, one on each side of the map. The tunnels connect the underground shop to the Bodega area on Amber and the Theater area on Sapphire.

Added two new teleporters, one on each outer lane (behind the Chapel and behind the Firehouse) Urn reward now has a comeback component where it gives extra gold for the team that is behind based on the magnitude A small share of the comeback portion of hero kill bounty is now given to each other player outside of just the kill/assist players. This also makes the amount the killer gets be more consistent, previously the amount could vary significantly based on how many people were involved. The killer and assist players still get the bigger shares.

Kill assist window increased from 7s to 10s

- text: is no longer area pick up and now requires someone to heavy melee it to pick it up after it's dropped to the round

- type: change

- affected1: Rejuvenator

- text: will no longer stop dropping if it touches player created geometry (like Ice Dome) and always goes down to the target position

- type: change

- affected1: Rejuvenator You can air-dash downward by pressing CTRL+SHIFT while in the air Successful parry reduces the cooldown from 1s to 0.5s (unsuccessful parry cd is still 6s) Heroes HP growth per boon increased by +5 (there are 11 instances of these). This is not done for Abrams or Dynamo.

Post lane medic troopers will heal other troopers if a hero within range is full hp Post lane medic troopers' hero heal increased from 40 to 80 Base zipline speed increased by 5% If the Soul Urn is dropped it goes back to its original spot a little bit faster Healing/Spawn area in the base now has its defense damage go up over time Carrying the Soul Urn no longer causes you to get slowed briefly by 50% when you get shot Carrying the Soul Urn now always slows you by 15% Carrying the Soul Urn now also silences your items The silence effect for Soul Urn now applies as you start channeling to pick it up (0.5s after touching it, to prevent accidental walk overs) Base side doors near the healing area now open a lot faster

## Items

- I Mystic Burst

- text: No longer grants +3 Spirit Power

- type: change

- affected1: Mystic Burst

- text: No longer grants +1 Sprint

- type: change

- affected1: Mystic Burst

- text: Now grants +40 Spirit Shield

- type: change

- affected1: Mystic Burst

- text: Now grants +6% Weapon Power

- type: change

- affected1: Mystic Burst I Headshot Booster

- text: Bonus headshot damage reduced from 50 to 45

- type: nerf

- affected1: Headshot Booster I Restorative Shot (Then called Medic Bullets)

- text: Healing from heroes increased from 25 to 30

- type: buff

- affected1: Restorative Shot I Extra Health

- text: Health increased from 125 to 135

- type: buff

- affected1: Extra Health I Divine Barrier

- text: No longer grants +2 Sprint

- type: change

- affected1: Divine Barrier

- text: Bullet Resist reduced from 10% to 7%

- type: nerf

- affected1: Divine Barrier

- text: Cooldown increased from 20 to 30

- type: nerf

- affected1: Divine Barrier

- text: Active Move Speed reduced from 3 to 2

- type: nerf

- affected1: Divine Barrier I Enchanter's Barrier

- text: Shield increased from 275 to 300

- type: buff

- affected1: Enchanter's Barrier I Bullet Resist Shredder

- text: Debuff duration increased from 4s to 5s

- type: buff

- affected1: Bullet Resist Shredder I Healbane

- text: Bonus HP increased from 50 to 75

- type: buff

- affected1: Healbane I Healing Booster

- text: No longer grants +50 HP

- type: change

- affected1: Healing Booster

- text: Now grants +8% Spirit Resist

- type: change

- affected1: Healing Booster I Swift Striker

- text: Armor penalty reduced from -7% to -6%

- type: nerf

- affected1: Swift Striker I Fleetfoot

- text: Cooldown increased from 20s to 22s

- type: nerf

- affected1: Fleetfoot I Reactive Barrier

- text: Cooldown reduced from 25s to 20s

- type: buff

- affected1: Reactive Barrier I Cold Front

- text: Time to expand reduced from 1.5s to 0.75s

- type: buff

- affected1: Cold Front I Majestic Leap

- text: Cooldown increased from 15s to 20s

- type: nerf

- affected1: Majestic Leap

- text: Drop down speed reduced from 51 to 36

- type: nerf

- affected1: Majestic Leap I Burst Fire

- text: Cooldown reduced from 10s to 9s

- type: buff

- affected1: Burst Fire I Rescue Beam

- text: No longer grants movement speed

- type: nerf

- affected1: Rescue Beam

- text: Active has been reworked. Now channels for 3 seconds, healing you and the target for up to 25% of Max HP. If you click the ally again during that time, you will pull them to you. Has 40m cast range and 45s cooldown. Can be self cast.

- type: change

- affected1: Rescue Beam I Tesla Bullets

- text: Internal cooldown reduced from 0.4s to 0.35s

- type: buff

- affected1: Tesla Bullets I Mystic Slow

- text: Bonus HP increased from +75 to +100

- type: buff

- affected1: Mystic Slow I Ethereal Shift

- text: Shifting Shroud renamed to Ethereal Shift

- type: buff

- affected1: Shifting Shroud

- affected2: Ethereal Shift I Warp Stone

- text: Fixed some cases where it would fail to cast near objects

- type: fix

- affected1: Warp Stone I Escalating Resilience

- text: Stacks share a duration now and each new stack refreshes it

- type: change

- affected1: Escalating Resilience

- text: Duration reduced from 15s to 10s

- type: nerf

- affected1: Escalating Resilience

- text: Max resistance reduced from 36% to 30%

- type: nerf

- affected1: Escalating Resilience I Alchemical Fire

- text: Cooldown reduced from 34s to 30s

- type: buff

- affected1: Alchemical Fire I Crippling Headshot

- text: Bullet and Spirit resistance reduction reduced from 35% to 30%

- type: nerf

- affected1: Crippling Headshot I Boundless Spirit

- text: Spirit Power increased from +50 to +55

- type: buff

- affected1: Boundless Spirit

- text: Now grants +175 Health

- type: buff

- affected1: Boundless Spirit I Ricochet

- text: Ammo increased from +25% to +30%

- type: buff

- affected1: Ricochet I Vampiric Burst

- text: Lifesteal increased from 70% to 80%

- type: buff

- affected1: Vampiric Burst I Refresher

- text: Now has a 0.3s cast time

- type: nerf

- affected1: Refresher

## Heroes

- H Abrams

- text: Base health regen reduced from 2 to 1

- type: nerf

- affected1: Abrams

- text: T1 reduced from +2 HP Regen to +1.5

- type: nerf

- affected1: Abrams

- affected2: Infernal Resilience H Bebop

- text: base damage reduced from 130 to 120

- type: nerf

- affected1: Bebop

- affected2: Sticky Bomb

- text: grab radius reduced from 40 inches to 36

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: movement and dash slow increased from 30% to 40%

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: DPS increased from 210 to 220

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: tracking speed increased by 10%

- type: buff

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: radius reduced from 10m to 9m

- type: nerf

- affected1: Dynamo

- affected2: Singularity H Grey Talon

- text: cooldown reduced from 130s to 120s

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: damage Spirit growth increased from 2.5 to 2.8

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: T3 is now -12% Bullet Resistance for 6 seconds

- type: change

- affected1: Haze

- affected2: Sleep Dagger

- text: T1 increased from +4 m/s Invis Sprint Speed to +5

- type: buff

- affected1: Haze

- affected2: Smoke Bomb

- text: causes your footsteps to be silent

- type: buff

- affected1: Haze

- affected2: Smoke Bomb H Ivy

- text: replicated healing reduced from 55% to 45%

- type: nerf

- affected1: Ivy

- affected2: Watcher's Covenant

- text: no longer provides +2 m/s in the base ability

- type: nerf

- affected1: Ivy

- affected2: Watcher's Covenant

- text: T2 movement bonus increased from +2 m/s to +3

- type: buff

- affected1: Ivy

- affected2: Watcher's Covenant H Kelvin

- text: movement speed slow increased from 25% to 35%

- type: buff

- affected1: Kelvin

- affected2: Frozen Shelter

- text: Can now dismiss while channeling other abilities ()

- type: change

- affected1: Kelvin

- affected2: Frozen Shelter H Lash

- text: base damage reduced from 110 to 90

- type: nerf

- affected1: Lash

- affected2: Ground Strike

- text: damage per meter increased from 6 to 6.75

- type: buff

- affected1: Lash

- affected2: Ground Strike

- text: now reduced scaling after 25m height to 4.5

- type: nerf

- affected1: Lash

- affected2: Ground Strike H McGinnis

- text: charge delay reduced from 10s to 8s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: Fixed to be compatible with again (Activating echo shard resets the ability so you can cast it again and not have to cancel your first one. After casting the 2nd, using cancel will remove the first wall first)

- type: fix

- affected1: McGinnis

- affected2: Echo Shard

- affected3: Spectral Wall

- text: Can now dismiss while channeling other abilities (Heavy Barrage)

- type: change

- affected1: McGinnis

- affected2: Spectral Wall H Mo & Krill

- text: HP Growth per boon reduced from 48 to 42

- type: nerf

- affected1: Mo & Krill

- text: now grants 25 max hp each time a target dies during it

- type: buff

- affected1: Mo & Krill

- affected2: Combo H Seven

- text: initial radius increased from 10m to 12m

- type: buff

- affected1: Seven

- affected2: Storm Cloud

- text: T2 bonus radius reduced from 12m to 10m

- type: nerf

- affected1: Seven

- affected2: Storm Cloud H Yamato

- text: T3 bonus damage reduced from +210 to +200

- type: nerf

- affected1: Yamato

- affected2: Power Slash

- text: cooldown increased from 100 to 110

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation
