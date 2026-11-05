---
title: "Patch/Playtest/2024-09-12"
pageid: 730
source: liquipedia-deadlock-md
---

- name: Playtest - September 12 2024

- version: 2024-09-12

- release: September 12, 2024

- highlight1: Gameplay Updates

- highlight2: Map Updates

- highlight3: Item Updates

- highlight4: Hero Updates

- previous: Patch/Playtest/2024-09-012024-09-01

- next: Patch/Playtest/2024-09-142024-09-14

## General

Matchmaking is now open 24/7 for all regions Added new minimap Updated base asset and added new unique Hero Icons Neutral Camps are now represented by a highlight glow on the buildings they are located within The Orange Lane (Orchard) is now the Green Lane (Greenwich) Added a new behavior system. Players can temporarily lose access to certain capabilities in the game. The controls include Matchmaking, Voice Chat, Text Chat, Pausing, and Reporting. The system for tracking is active now, however we will wait on most penalties for a few days as we review the results.

There is now a low priority queue. The primary way to enter this is through abandoning games, but it can include other behavior. You must complete the required amount of games (escalates based on low priority frequency) to be able to return to using matchmaking normally.

Regularly misreporting players will result in you losing the reporting function and may in some cases cause you to go into low priority as well.

New players that are queued solo will only match with other new players until they get 4 wins The lane allocation of 1-1-2-2- and 2-2-1-1 will no longer be a possible setup A 6 player party will no longer match against solo players. This may result in longer queue times for 6 stacks.

AFK players will be automatically kicked out after a few minutes Abandon Match dialog is now more clear about consequences of leaving Abandon Match now has a time delay before you can click it to help protect against some accidental cases Added custom hotkeys per hero Bounce Pad visuals have been replaced with a wind fan (no mechanic changes). The effects also indicate the travel path.

Added little spirit frog legs to the Soul Urn Orange zipline is now green Space Bar no longer cancels abilities. Abilities can be pressed again to cancel the ones that have a cancel state.

The Alternate Cast modes "Modifier Button" and "Alternate Cast Button" have had their behaviors merged Added UI button hints when using "Alternate Cast Button" in some extra cases Added a slider for Double Tap Alternate Cast timing Added a slider for Press and Hold Alternate Cast required time Changes to Scoreboard (TAB) and Extra Info (ALT) Previously there was a lot of crossover between the TAB and ALT modes during gameplay. In this update we have separated the behavior of these two modes to better serve different functions. The keys used for each of these modes can be swapped within Keybinds Settings.​ Scoreboard (TAB): Enables cursor mode Displays Scoreboard Displays Damage Summary Allows minimap ping and draw Extra Info (ALT): No longer enables cursor mode​ Quick-upgrade Abilities (ie. ALT+1) each of these can be individually remapped​ Can now more easily map ALT as an Alternate Cast button​ Displays extra information on HUD (ie. Zipline Speed Boost Cooldown) - we plan to expand upon this in future updates​ Client performance improvements Game now automatically starts preloading the map once the client is launched, to help reduce load time for most users Sand Box orb practice area now displays the time in milliseconds that you hit the orb after spawning Added a console command (private_lobby_create) to allow players to create custom lobbies using our servers. This has very temp UI. Once we add a real UI to it along with some misc features, we'll add a non-console way to host custom lobbies.

Upgrade ability keys are now customizable (Current defaults are ALT+1, ALT+2, etc) Adjusted Midboss low health roar sound to be more distinct from spawn sound Added Maximum FPS Sliders for Dashboard and In-Game Removed Pause limit for hero testing, coop bot matches, and the tutorial Added support for launching the game in a secondary monitor properly Fixed friends menu scrolling up automatically when it shouldn't Fixed being unable to invite offline users to a party Fixed invite tooltips on friends menu not being positioned correctly Metal Skin effects revisions Seven's Static Charge effects improvement to make the boundary more clear Updated medic healing beam colors to be consistent with other heals Melee troopers no longer play swipe effect (to reduce some unnecessary noise) Added better indication when all four active slots are full Updated Ice Dome to fix some performance related issues Updated Torment visual effects to reduce some noise Added sound for Tesla Bullets proc Added sound for Toxic Bullets proc Divine Barrier wings no longer fully opaque Reduced intensity of last hit status effect Updated Echo Shard sound effects Added low ammo indication sound Improved clarity for Seven casting and channeling sounds Updated Refresher effects colors from green to purple Minor updates to Abram's Seismic Impact to resolve some states faster to reduce visual noise Updated Lady Geist Blood Bomb, Life Drain, Malice, and Soul Exchange sounds Added Shoulder Charge wall impact effects Changed open mic audio settings to allow open mic to opt in to team chat or party chat Updated effects for the Warp Stone bullet resist buff Added Lucky Shot proc sound effect Updated Berserker buff effects Adjusted Shiv's running reload animation Added wall impact animation for Abram's Shoulder Charge Lowered gun arm during Abram's jump animation to not obscure reticle Soul Jar return location effects will change color based on the captured state of the Soul Jar Lady Geist Blood bomb revisions to improve visibility in team fights Improved visibility of heroes caught in the Singularity Distance field shadows and AO no longer visible behind cosmic veils Added sliders for FSR and FSR2 sharpness Updated Wraith, Grey Talon, and Infernus VO

- text: AoE Stomp has new effects

- type: change

- affected1: Walker Viscous Splatter effects have been adjusted Revised Silencer cast and duration sounds Added Rebirth channel and revive sounds Added Infuser cast sound Audio bug fixes related to switching spectating targets

## Gameplay

Orbs now favor the claimer rather than the denier when both impact within a very narrow window of each other

- text: Flex Slot moved from "First " to "Two

- type: change

- affected1: Walker All ability and item cooldowns increased by 6% globally Max respawn time now happens at 35 minutes rather than 40 minutes T4 Items Cost reduced from 6300 to 6200 Shield regeneration time reduced from 60s to 50s Wall Jump activation has been made more lenient Wall Jump launch angle can now be steered a bit more Jump shooting lockout period reduced from 0.25s to 0.15s Souls from bosses now appear much more spread out Rope climbing speed increased from 13 to 14 Taking non-dot damage while on a rope slows you by 30% Improved Heavy melee hit registration

- text: warning now happens at 60% instead of 50%

- type: buff

- affected1: Mid Boss

- text: beam max range (the sticky portion after being acquired) reduced by 20% (50m to 40m)

- type: nerf

- affected1: Walker Successful Parry CD reduced from 0.5s to 0.25s Fixed Alt Fires not working with conditional bonuses (like Close Range) Melee trooper hitbox improved

- text: Fixed Medic sometimes using their heal on boss

- type: fix

- affected1: Guardian

- affected2: Trooper Fixed multiple heroes getting the power-up bonus by standing on top of it before spawns Fixed your gun reloading down to a smaller magazine when reloading with higher ammo than your max

## Items

1. Weapon I Headshot Booster

- text: Bonus damage reduced from 45 to 40

- type: nerf

- affected1: Headshot Booster I High-Velocity Mag

- text: Weapon Damage reduced from 14% to 12%

- type: nerf

- affected1: High-Velocity Mag I Restorative Shot

- text: Healing from heroes increased from 35 to 40

- type: buff

- affected1: Restorative Shot

- text: Healing from troopers increased from 10 to 15

- type: buff

- affected1: Restorative Shot I Hollow Point Ward

- text: Conditional Weapon Damage increased from 20% to 22%

- type: buff

- affected1: Hollow Point Ward I Rapid Rounds

- text: Fire Rate reduced from 12% to 9%

- type: nerf

- affected1: Rapid Rounds

- text: No longer provides -50 Max Health

- type: nerf

- affected1: Rapid Rounds I Active Reload

- text: Lifesteal reduced from 22% to 20%

- type: nerf

- affected1: Active Reload I Mystic Shot

- text: Spirit damage now considers bullet falloff

- type: nerf

- affected1: Mystic Shot

- text: Cooldown reduced from 6s to 5s

- type: buff

- affected1: Mystic Shot I Berserker

- text: Bullet Resist reduced from 8% to 7%

- type: nerf

- affected1: Berserker I Long Range

- text: Bullet Shield increased from +90 to +140

- type: buff

- affected1: Long Range I Melee Charge

- text: Charge distance bonus is moved to innate section

- type: change

- affected1: Melee Charge

- text: Passive now has a 8s cooldown

- type: change

- affected1: Melee Charge

- text: When passive triggers, you deal bonus +20% Melee Damage

- type: change

- affected1: Melee Charge

- text: Now gives a UI indication when reload procse

- type: change

- affected1: Melee Charge I Soul Shredder Bullets

- text: Weapon Damage increased from 6% to 7%

- type: buff

- affected1: Soul Shredder Bullets I Fleetfoot

- text: Active move speed reduced from 4 to 3

- type: nerf

- affected1: Fleetfoot

- text: Cooldown reduced from 22s to 18s

- type: nerf

- affected1: Fleetfoot

- text: Health increased from +75 to +90

- type: buff

- affected1: Fleetfoot I Warp Stone

- text: Range reduced from 13m to 11m

- type: nerf

- affected1: Warp Stone I Heroic Aura

- text: Active movement speed bonus reduced from 3 to 2

- type: nerf

- affected1: Heroic Aura I Sharpshooter

- text: Bullet Health increased from +175 to +200

- type: buff

- affected1: Sharpshooter I Hunter's Aura

- text: Bullet Resist reduction reduced from -10% to -9%

- type: buff

- affected1: Hunter's Aura I Titanic Magazine

- text: Bullet Resist increased from 15% to 18%

- type: buff

- affected1: Titanic Magazine I Alchemical Fire

- text: Spirit Power increased from +7 to +11

- type: buff

- affected1: Alchemical Fire I Crippling Headshot

- text: Debuff duration reduced from 5s to 4s

- type: nerf

- affected1: Crippling Headshot I Lucky Shot

- text: Bonus Damage increased from 80% to 90%

- type: buff

- affected1: Lucky Shot I Glass Cannon

- text: Max stacks increased from 5 to 7

- type: buff

- affected1: Glass Cannon I Silencer

- text: Damage increased from 15% to 20%

- type: buff

- affected1: Silencer I Frenzy

- text: Linger duration increased from 4s to 6s

- type: buff

- affected1: Frenzy 1. Vitality I Healing Rite

- text: Now grants +3 Spirit Power

- type: buff

- affected1: Healing Rite I Enduring Spirit

- text: Spirit Lifesteal increased from 8% to 10%

- type: buff

- affected1: Enduring Spirit I Melee Lifesteal

- text: Melee damage reduced from 15% to 13%

- type: nerf

- affected1: Melee Lifesteal I Healing Nova

- text: Now requires

- type: change

- affected1: Health Nova

- text: Now grants +4 Spirit Power

- type: change

- affected1: Health Nova

- text: Range reduced from 18m to 15m

- type: nerf

- affected1: Health Nova I Divine Barrier

- text: Bullet Shield shield reduced from 300 to 260

- type: nerf

- affected1: Divine Barrier

- text: Spirit Shield shield reduced from 300 to 260

- type: nerf

- affected1: Divine Barrier I Rescue Beam

- text: Heal reduced from 30% to 26%

- type: nerf

- affected1: Rescue Beam

- text: Cast range reduced from 45m to 36m

- type: nerf

- affected1: Rescue Beam

- text: No longer requires Healing Rite

- type: change

- affected1: Rescue Beam I Fortitude

- text: Lane troopers do not reset the passive regen timer

- type: change

- affected1: Fortitude I Lifestrike

- text: Melee damage reduced from 40% to 35%

- type: nerf

- affected1: Lifestrike I Majestic Leap

- text: Cooldown reduced from 24s to 22s

- type: buff

- affected1: Majestic Leap I Metal Skin

- text: Cooldown reduced from 22s to 20s

- type: buff

- affected1: Metal Skin I Inhibitor

- text: Fixed damage reduction on bullets not being reduced by a percentage properly

- type: fix

- affected1: Inhibitor I Colossus

- text: Radius increased from 10m to 12m

- type: buff

- affected1: Colossus

- text: Cooldown reduced from 45s to 35s

- type: buff

- affected1: Colossus I Phantom Strike

- text: Damage reduced from 150 to 75

- type: nerf

- affected1: Phantom Strike

- text: Spirit Power scaling reduced from 2 to 1

- type: nerf

- affected1: Phantom Strike I Soul Rebirth

- text: No longer grants 20% Weapon Damage

- type: nerf

- affected1: Soul Rebirth

- text: Cooldown Reduction reduced from 18% to 15%

- type: nerf

- affected1: Soul Rebirth 1. Spirit I Spirit Strike

- text: Melee damage reduced from 15% to 12%

- type: nerf

- affected1: Spirit Strike

- text: Debuff duration reduced from 13s to 11s

- type: nerf

- affected1: Spirit Strike

- text: Spirit Shield reduced from 100 to 80

- type: nerf

- affected1: Spirit Strike

- text: Regen reduced from 1 to 0.8

- type: nerf

- affected1: Spirit Strike I Mystic Reach

- text: Spirit Resist increased from 5% to 6%

- type: buff

- affected1: Mystic Reach

- text: Ability Range increased from 15% to 16%

- type: buff

- affected1: Mystic Reach I Extra Spirit

- text: Spirit increased from 8 to 9

- type: buff

- affected1: Extra Spirit I Ammo Scavenger

- text: Neutral kills now count as a soul capture

- type: buff

- affected1: Ammo Scavenger

- text: Buff duration increased from 35s to 40s

- type: buff

- affected1: Ammo Scavenger I Withering Whip

- text: Fire Rate slow increased from 30% to 40%

- type: buff

- affected1: Withering Whip I Slowing Hex

- text: Projectile speed increased by 20%

- type: buff

- affected1: Slowing Hex I Quicksilver Reload

- text: Damage increased from 50 to 65

- type: buff

- affected1: Quicksilver Reload I Surge of Power

- text: Imbued ability now grants +10% Fire Rate when used (same 6s duration as the movespeed buff)

- type: buff

- affected1: Surge of Power I Rapid Recharge

- text: Now gains +12% Weapon Damage (T1 Extra Charge gives +6%)

- type: buff

- affected1: Rapid Recharge I Improved Burst

- text: Damage reduced from 10% of Max HP to 9%

- type: nerf

- affected1: Improved Burst I Improved Reach

- text: Spirit Power increased from +6 to +8

- type: buff

- affected1: Improved Reach I Torment Pulse

- text: Health increased from +125 to +140

- type: buff

- affected1: Torment Pulse I Silence Glyph

- text: Spirit Shield reduced from +200 to +150

- type: nerf

- affected1: Silence Glyph I Echo Shard

- text: Spirit Power increased from +8 to +12

- type: buff

- affected1: Echo Shard

## Heroes

- H Abrams

- text: Fixed getting stuck on ceilings like in the mid boss room

- type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text: turn rate reduced a bit

- type: buff

- affected1: Abrams

- affected2: Shoulder Charge

- text: reduced from 17% to 16%

- type: nerf

- affected1: Abrams

- affected2: Infernal Resilience

- text: stun time reduced from 1s to 0.85s

- type: nerf

- affected1: Abrams

- affected2: Shoulder Charge H Bebop

- text: no longer roots your hero during cast time

- type: buff

- affected1: Bebop

- affected2: Uppercut

- text: Can now keep firing if he jumps and his laser is already warmed up

- type: buff

- affected1: Bebop

- text: Reverted recent change to make have an alternate cast mode to pierce through allies/enemies

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: range reduced from 35m to 30m

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: now does splash damage around a 5m area the beam connects to on the ground (can be used to fish heroes out of cover in some areas)

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: no longer gets canceled when stamina is used

- type: buff

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text: T3 reduced from 4% to 3.8%

- type: nerf

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text: T1 reduced from 40% slow to 35%

- type: nerf

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: cooldown increased from 11s to 12s

- type: nerf

- affected1: Dynamo

- affected2: Quantum Entanglement H Grey Talon

- text: Fixed issues with hitting targets behind walls

- type: fix

- affected1: Grey Talon

- affected2: Charged Shot

- text: Fixed doing damage through buildings

- type: fix

- affected1: Grey Talon

- affected2: Guided Owl

- text: Weapon Damage reduced from +7 to +4

- type: nerf

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: T2 Weapon Damage reduced from +7 to +5

- type: nerf

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: Bullet damage growth per boon increased from +1.46 to +1.8

- type: nerf

- affected1: Grey Talon

- text: cooldown increased from 110s to 120s

- type: nerf

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: Fixed issues with hitting targets behind walls

- type: fix

- affected1: Haze

- affected2: Sleep Dagger H Infernus

- text: Base health reduced from 625 to 600

- type: fix

- affected1: Infernus

- text: slow resistance increased from 30% to 50%

- type: fix

- affected1: Infernus

- affected2: Flame Dash H Ivy

- text: Fixed some control issues when flying near a wall

- type: fix

- affected1: Ivy

- text: silence and slow debuff duration reduced from 4.5s to 4s

- type: nerf

- affected1: Ivy

- affected2: Air Drop H Kelvin

- text: fire rate slow reduced from 80% to 40%

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: movement slow reduced from 80% to 70%

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: Objectives and are now frozen and invulnerable when under frozen shelter

- type: buff

- affected1: Kelvin

- text: and can now also be cancelled by hitting the ability key again

- type: change

- affected1: Kelvin

- affected2: Arctic Beam

- affected3: Ice Path H Lady Geist

- text: T3 damage increased from 22% to 26%

- type: buff

- affected1: Lady Geist

- affected2: Essence Bomb

- text: spirit scaling increased from 1.05 to 1.15

- type: buff

- affected1: Lady Geist

- affected2: Essence Bomb

- text: Fixed a recent bug with that caused multiple blood shards to be absorbed by 1 hero rather than pass through and hit others (it didn't stack that way in any case)

- type: fix

- affected1: Lady Geist

- affected2: Malice

- text: Self Damage no longer consumes shields (general change)

- type: change

- affected1: Lady Geist H Lash

- text: now allows you to turn during the descent

- type: buff

- affected1: Lash

- affected2: Ground Slam

- text: Bullet growth from 1.15 to 0.9

- type: nerf

- affected1: Lash

- text: Damage spirit scaling increased from 0.78 to 0.85

- type: buff

- affected1: Lash

- affected2: Ground Slam

- text: Damage Per Meter Spirit scaling increased from 0.045 to 0.05

- type: buff

- affected1: Lash

- affected2: Ground Slam H McGinnis

- text: radius reduced from 6m to 5m

- type: nerf

- affected1: McGinnis

- affected2: Medicinal Specter

- text: radius now grows with Spirit Power (0.07)

- type: buff

- affected1: McGinnis

- affected2: Medicinal Spectre

- text: Can no longer wall jump from - type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text: min range reduced from 7m to 6m

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text: duration reduced from 6s to 5s

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text: spirit scaling increased from 0.3 to 0.35

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage

- text: min range reduced from 7m to 6m

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:'s bullet travel speed increased

- type: buff

- affected1: McGinnis

- affected2: Mini Turret H Mo & Krill

- text: Camera zooms out a little bit more when un-burrowing

- type: fix

- affected1: Mo & Krill

- text: Can cast Scorn while using Combo

- type: change

- affected1: Mo & Krill

- affected2: Scorn

- affected3: Combo

- text: T2 reduced from +1s to +0.75s

- type: nerf

- affected1: Mo & Krill

- affected2: Combo H Paradox

- text: Fixed issues with hitting targets behind walls

- type: fix

- affected1: Paradox H Pocket

- text: amp per stack reduced from 7% to 6%

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: slow reduced from 40% to 30%

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: Added a brief lockout period on to prevent accidental double clicks

- type: fix

- affected1: Pocket

- affected2: Flying Cloak H Seven

- text: Base bullet resist reduced from 8% to 0%

- type: nerf

- affected1: Seven

- text: Bullet resist no longer scales with Boons

- type: nerf

- affected1: Seven

- text: Headshot reduction increased from 25% to 35%

- type: nerf

- affected1: Seven

- text: damage reduced from 124 to 110

- type: nerf

- affected1: Seven

- affected2: Storm Cloud

- text: max radius reduced from 30m to 25m

- type: nerf

- affected1: Seven

- affected2: Storm Cloud

- text: cooldown reduced from 180s to 140s

- type: buff

- affected1: Seven

- affected2: Storm Cloud

- text: audio is now a little clearer when it's cast

- type: fix

- affected1: Seven

- affected2: Storm Cloud H Shiv

- text: Fixed issues with hitting targets behind walls

- type: fix

- affected1: Shiv

- affected2: Serrated Knives

- text: damage reduced from 125 to 105

- type: nerf

- affected1: Shiv

- affected2: Slice and Dice

- text: Deferred Damage Cleared reduced from 50% to 40%

- type: nerf

- affected1: Shiv

- affected2: Bloodletting

- text: Bonus Damage from Full Rage reduced from +25% to +20%

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text: T2 now also increases Rage Amp by +5%

- type: buff

- affected1: Shiv

- affected2: Killing Blow H Vindicta

- text: Base bullet damage reduced from 14 to 13

- type: nerf

- affected1: Vindicta

- text: T1 duration reduced from +0.75s to +0.5s

- type: nerf

- affected1: Vindicta

- affected2: Stake

- text: bonus gold is now shared with assisters

- type: buff

- affected1: Vindicta

- affected2: Assassinate

- text: now reduces bullet armor by 6%

- type: buff

- affected1: Vindicta

- affected2: Crow Familiar

- text: impact damage reduced from 50 to 40

- type: nerf

- affected1: Vindicta

- affected2: Crow Familiar

- text: impact damage spirit scaling reduced from 1 to 0.8

- type: nerf

- affected1: Vindicta

- affected2: Crow Familiar

- text: spirit power duration scaling reduced from 0.04 to 0.03

- type: nerf

- affected1: Vindicta

- affected2: Crow Familiar

- text: You can now use stamina while flying to get an impulse in the facing direction

- type: buff

- affected1: Vindicta

- affected2: Flight

- text: Space bar no longer exists the ability, you have to press the key again

- type: change

- affected1: Vindicta

- affected2: Flight

- text: now does 20% more damage when getting a headshot

- type: buff

- affected1: Vindicta

- affected2: Assassinate

- text: scope ends when you are stunned

- type: nerf

- affected1: Vindicta

- affected2: Assassinate H Viscous

- text: now correctly knocks people in up in the air

- type: fix

- affected1: Viscous

- affected2: Puddle Punch

- affected3: The Cube

- text: Improved various issues with the camera

- type: fix

- affected1: Viscous

- text: now telegraphs an effect before it forms

- type: change

- affected1: Viscous

- affected2: Puddle Punch

- text: Base bullet damage reduced from 14 to 13

- type: nerf

- affected1: Viscous

- text: damage reduced from 110 to 100

- type: nerf

- affected1: Viscous

- affected2: Splatter

- text: turn rate improved a bit

- type: buff

- affected1: Viscous

- affected2: Goo Ball

- text: stun frequency cooldown improved from 1.5s to 1.25s

- type: buff

- affected1: Viscous

- affected2: Goo Ball

- text: Fixed piercing Unstoppable

- type: fix

- affected1: Viscous

- affected2: Puddle Punch

- affected3: Unstoppable H Warden

- text: Bullet growth reduced from 1.31 to 1.2

- type: nerf

- affected1: Warden

- text: debuff duration reduced from 7s to 6s

- type: nerf

- affected1: Warden

- affected2: Alchemical Flask

- text: radius reduced from 7m to 6.5m

- type: nerf

- affected1: Warden

- affected2: Alchemical Flask

- text: You gain 50% bullet resistance during the 2s ult channel ()

- type: nerf

- affected1: Warden

- affected2: Last Stand H Wraith

- text: damage reduced from 100 to 80

- type: nerf

- affected1: Wraith

- affected2: Card Trick

- text: spirit scaling increased from 1.2 to 1.5

- type: buff

- affected1: Wraith

- affected2: Card Trick

- text: card projectiles spawn above the reticle rather than on the left side

- type: change

- affected1: Wraith

- affected2: Card Trick

## Map

Inner Lane Changes: Added connections from the Shop to the front of the Department Store and the New York Oracle buildings Added veil in the opening at the front looking out toward the opposing side Added a cover barrier in front of the opening with the veil Moved the catwalk stair in front of the Department Store and New York Oracle closer to the Mid Base Changes: Angled the walkway connection from the outer lane exits to the inner lane exits Added an overhang below the Patron position Added two juke closets facing the Patron Rope Changes: Removed the exterior ropes from the Garage and Nightclub Replaced interior stairwells with ropes inside the Garage and the Nightclub that give access to the 2nd floor and roof Rooftop Changes: Raised Apothecary and Imports rooftops to match heights of the Record Store and the Comedy Club Removed rooftop details from roofs that are not safe Added rooftop details to new valid rooftops Miscellaneous: Changed collision on the shelves inside the Armory and Warehouse to improve shooting through them Replaced wall landing in front of the Nursery and the Market with an electrical box Bug Fixes: Fixed breakable items outside the underground tunnel Removed some duplicate models, lights and geometry Fixed bug where the Hotel sign was replacing billboards on other rooftops Fixed rooftop details not aligned to the new height of the rooftops Fixed enemy team from being able to enter the base side passages
