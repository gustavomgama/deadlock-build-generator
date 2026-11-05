---
title: "Patch/Playtest/2024-08-01"
pageid: 568
source: liquipedia-deadlock-md
---

- name: Playtest - August 01 2024

- version: 2024-08-01

- release: August 01, 2024

- highlight1: Gameplay Updates

- highlight2: Bug Fixes

- highlight3: Item Updates

- highlight4: Hero Updates

- highlight5: New Hero:

- previous: Patch/Playtest/2024-07-232024-07-23

- next: Patch/Playtest/2024-08-062024-08-06

## General

Added a new hero, H Viscous. He's green.

Improved client performance Reworked the Hero Builds system. Browsing and editing builds now happens within the Shop UI (accessible via Sandbox or during a normal game). You can create custom categories for items with unique names and descriptions that can be independently resized and positioned. The interface for browsing builds has also been improved, public builds will now be sorted by popularity (number of favorites). Old builds are incompatible with this system, so they won't be visible in this UI, but we'll have a console command we'll release soon that you can use to print out your older guides if you need them for reference.

North America (NA) servers have been moved from the west coast to closer to the middle of the country to make latency between east and west coast a little more even, as the majority of users are east coast now. The total average ping amongst all players will be lower as a result of this (a little higher for some and a lot lower for others).

NA region testing times now start 1 hour earlier weekdays and weekends Minimum hero roster requirement reduced from 4 to 3 Added Oceanic servers and matchmaking region. Testing times are displayed in the client Added Teleporter icons on the minimap. The icons glow when you get close to them and pulse on the teleporter's exit location to show you the destination when you are about to enter it.

When using the underground tunnels, the primary minimap fades out and an underground map for that area shows you your path and the exit locations.

Reworked the invite system in the client to streamline the process. Emails are no longer required, the users will now receive access directly through Steam and Discord/Forum access will be available through the client. The UI will now also group users into three categories: available to invite, already invited, and already have access. This new system will result in less invitations stuck in limbo, and any previous invites that have not already claimed the game will be granted through this system as well.

Hero Sandbox: Added an orb spawner for practicing last-hitting orbs Hero Sandbox: Added a dummy hero that patrols left and right to practice targeting Added a checkbox on the startup development dialog to be able to choose to not show it again Your vision through a Cosmic Veil is now based on your hero position rather than camera position Adjusted Zipline camera positions for various heroes to help with visibility Double tap threshold increased from 0.2s to 0.3s Fixed Candle Troopers near-death flash sometimes occurring while moving or doing other active animations Candle Trooper behind-wall HUD indicator now also shows near-death state Fixed taking damage not interrupting teleporters Fixed clicking on the top bar or minimap to change spectate targets being unreliable Fixed Function keys (F1-F5) being broken recently and not spectating teammates Fixed various abilities not showing the cast preview correctly on the first use (Mini Turrets, Quantum Entanglement, etc) Fixed Paradox Swap sometimes putting players behind walls Fixed Lash's Ground Strike sometimes causing the hero to be stuck for the rest of the match Fixed Abrams' Charge and Siphon pings not playing the correct VO

- text: Fixed having a pause at the end of their Rocket Barrage

- type: fix

- affected1: Walker Fixed multiple instances of "Killing Blow" in the Damage Report Temporarily disabled the audio reminder on being unable to damage the patron while the shrines are alive Fixed Spectral Wall forcing itself into the first ability slot if its cooldown is refreshed Changed camera to more closely track the followed hero angles when watching replays Player names no longer show up above hero's heads when in replay free-cam mode Increased post-game time by 1s Fixed upgrading abilities via hotkeys not working while dead Fixed dead player minimap icons showing over enemy players who are below street level and over shop icons Fixed various bugs with Infernus that caused significant lag Fixed Shrines not having collision Fixed crosshair sometimes being stuck hidden for Yamato after Flying Strike was interrupted Added a bunch of new Ivy lines including updated pings, kill lines, etc Improved mix clarity for game dialog Improved distinction between orb collect and orb deny sounds Fixed various cheat/debug commands being accessible Updated Pocket animations: New crouch walk and aim, updated slide animation, and new firing from slide animation.

Updated Mo & Krill Burrow start, duration, and end sounds Updated Mo & Krill Combo sound Updated Mo & Krill Sand Blast cast sound mix Updated Warden Alchemical Flask impact sounds Updated Warden Binding Word sound mix for teammates Updated Pocket Enchanted Satchel cast and delay sounds Added sleep status sound Updated Wraith zipline animations Fixed a bug with Urn that could cause you to be permanently silenced Fixed shop close sounds playing whenever the player enters the radius of a closed shop Added new visual effects for Lash's Ground Strike Improved ground impact effects for Ivy's True Form The client now culls more sounds when they are below a volume threshold The server no longer tells clients to play certain sounds when players and spectators are outside of audible range Shortened weapons and abilities volume attenuation over distance Fixed the console command zoom_sensitivity_ratio affecting both zoomed in and out Replaced two oil trucks with a new vehicle prop Improved visibility of low health state on troopers about to die Fixed Pocket's Cloak being able to tunnel through some ceilings and out of the world

## Gameplay

- text: Reworked the location of the on Amber Yellow and Sapphire Purple lanes. They are a little further towards the map edges. Nearby terrain has been reworked as well.

- type: change

- affected1: Walker The shooting experience near corners has been improved. Previously if your hero's eyes were obstructed at all, you would be unable to shoot altogether even if a large portion of your body was clearly visible. The check will now be a little more sophisticated and custom per hero, to allow you to shoot if your body is reasonably exposed. A part of this will also involve your hero leaning out a bit if not enough of your model is exposed to enemies.

Soul Orbs now fly out in different initial directions before floating up. There is a 1/3rd chance it goes left, 1/3rd chance it goes right, and 1/3rd chance it goes up.

Teleporters are now in pairs that send you between them to traverse the map horizontally Removed outer lane teleporters Added teleporters to areas between lanes (one in each quadrant). Total of 6 teleporters.

Old teleport exit location changed to a connection to the street that slopes down to Mid Added connection from the underground teleport station to the outer lane Guardian (previously a juke spot) Added steam tunnel connection from Amber Blue Guardian and Sapphire Orange Guardian to Mid (one-way) Each trooper you shoot at will now consider you a higher priority than Guardians/Walkers; that trooper will stop shooting the Guardians/Walkers and consider you its target for a few seconds

- text: laser DPS vs troopers increased from 150 to 190

- type: buff

- affected1: Walker

- text: Parrying a attack will no longer cause the Guardian to be stunned

- type: buff

- affected1: Guardian When Shrines are destroyed the Patron gets more aggressive, moves faster, and does more damage Weakened Patron HP regen increased from 80 to 120 Weakened Patron out of combat delay reduced from 30s to 20s Rejuv bonus reduced from 75% to 50% respawn time reduction

- text: health gained per minute increased from 350 to 425

- type: buff

- affected1: Mid Boss Urn now gives the team that is behind +2 more sprint when carrying it Bullet damage falloff now maxes out at ~60m instead of ~65m Movement Powerup: Stamina regen increased from 20% to 30% Movement Powerup: Sprint speed increased from +2 to +3 Movement Powerup: Zipline bonus increased from 30% to 50% Gun Powerup: Ammo increased from +30% to +40% Powerup durations increased from 150s to 160s Reworked the climb-up exit from the Cosmic Veil space on the outer lanes Moved kiosk cover prop in the outer lanes to space out trooper paths Moved delivery truck out from the street curb near the underground shop Moved breakable idols from the street level juke spots to other locations Removed the tree in front of the Walkers on Amber Orange and Sapphire Blue Replaced some trees on the Amber side with steam vents Moved barrel cover barrier to block the Guardian shop opening on Amber Purple and Sapphire Yellow Raised the sign on the roof of the garage Removed the smoke wall from the end of the alleys

## Items

1. Weapon I Hollow Point Ward

- text: Bonus damage reduced from 25% to 20%

- type: nerf

- affected1: Hollow Point Ward I Monster Rounds

- text: HP Bonus increased from +50 to +65

- type: buff

- affected1: Monster Rounds I Rapid Rounds

- text: HP Penalty increased from -40 HP to -50 HP

- type: nerf

- affected1: Rapid Rounds I Mystic Shot

- text: Base Spirit Damage reduced from +70 to +65

- type: nerf

- affected1: Mystic Shot I Berserker

- text: Damage required to earn a stack increased from 100 to 110

- type: nerf

- affected1: Berserker I Kinetic Dash

- text: Now gives 1 HP regen

- type: buff

- affected1: Kinetic Dash I Slowing Bullets

- text: Weapon Damage increased from 14% to 16%

- type: buff

- affected1: Slowing Bullets Added a new T3 Weapon Item, I Pristine Emblem: Gives +25% Weapon Damage, +12 Spirit Power, and +12% Spirit Armor. When an enemy is above 50% HP, you deal an additional +25% Weapon Damage.

- I Hunter's Aura

- text: No longer grants +16% Ammo, now grants +150 Health

- type: change

- affected1: Hunter's Aura I Point Blank

- text: Bullet Shield increased from 250 to 300

- type: buff

- affected1: Point Blank

- text: Weapon Damage increased from 40% to 45%

- type: buff

- affected1: Point Blank I Titanic Magazine

- text: Now gives +8% Bullet resistance

- type: buff

- affected1: Titanic Magazine I Heroic Aura

- text: Bonus Health increased from +125 to +150

- type: buff

- affected1: Heroic Aura I Intensifying Magazine

- text: Fixed a bug that allowed you to gain weapon damage without firing

- type: change

- affected1: Heroic Aura I Ricochet

- text: Bonus Health increased from 100 to 125

- type: buff

- affected1: Ricochet

- text: Now gives +8% Fire Rate

- type: buff

- affected1: Ricochet I Glass Cannon

- text: Weapon Damage increased from 70% to 75%

- type: buff

- affected1: Glass Cannon I Silencer

- text: Cooldown increased from 25s to 34s

- type: nerf

- affected1: Silencer I Siphon Bullets

- text: Weapon damage is no longer conditional on 15m, now always gives +40% Weapon Damage (previously gave +45% when close)

- type: change

- affected1: Siphon Bullets I Spiritual Overflow

- text: Now grants +10% Spirit Lifesteal

- type: buff

- affected1: Spiritual Overflow 1. Vitality I Extra Regen

- text: Regen increased from 2.5 to 2.7

- type: buff

- affected1: Extra Regen I Melee Lifesteal

- text: Bonus health increased from +50 to +70

- type: buff

- affected1: Melee Lifesteal I Restorative Locket

- text: When consuming at max stacks, replenishes target's stamina fully

- type: change

- affected1: Restorative Locket I Return Fire

- text: Bullet Damage returned increased from 70% to 80%

- type: buff

- affected1: Return Fire

- text: Bonus HP increased from +100 to +125

- type: buff

- affected1: Return Fire I Divine Barrier

- text: Cast range increased from 30m to 35m

- type: buff

- affected1: Divine Barrier

- text: Now grants +1.5 HP regen

- type: change

- affected1: Divine Barrier I Healing Nova

- text: Bonus HP increased from +50 to +75

- type: buff

- affected1: Health Nova I Reactive Barrier

- text: Now grants +75 HP

- type: change

- affected1: Reactive Barrier I Rescue Beam

- text: Pull speed is now 25% faster

- type: buff

- affected1: Rescue Beam

- text: Now grants +2 Sprint

- type: change

- affected1: Rescue Beam

- text: Bonus HP increased from +100 to +125

- type: buff

- affected1: Rescue Beam I Metal Skin

- text: Duration increased from 3s to 3.5s

- type: buff

- affected1: Metal Skin I Lifestrike

- text: Bullet Resist increased from 6% to 8%

- type: buff

- affected1: Lifestrike I Veil Walker

- text: Bullet and Spirit Shields increased from 185 to 200

- type: buff

- affected1: Veil Walker

- text: Cooldown reduced from 20s to 18s

- type: buff

- affected1: Veil Walker

- text: Weapon Damage increased from 6% to 10%

- type: buff

- affected1: Veil Walker I Superior Stamina

- text: Fire Rate reduced from 15% to 10%

- type: nerf

- affected1: Superior Stamina I Colossus

- text: Bonus HP increased from 500 to 600

- type: buff

- affected1: Colossus I Soul Rebirth

- text: Cooldown reduction increased from 10% to 15%

- type: buff

- affected1: Soul Rebirth I Phantom Strike

- text: Cast range increased from 30m to 35m

- type: buff

- affected1: Phantom Strike I Inhibitor

- text: Debuff duration increased from 2s to 2.5s

- type: buff

- affected1: Inhibitor I Leech

- text: Now provides +30% Degen Resistance (reduces anti heal effects by 30%)

- type: change

- affected1: Leech 1. Spirit I Spirit Strike

- text: Spirit Damage increased from 30 to 40

- type: buff

- affected1: Spirit Strike I Ammo Scavenger

- text: Spirit Power duration increased from 18s to 24s

- type: buff

- affected1: Ammo Scavenger I Cold Front

- text: Damage reduced from 115 to 100

- type: nerf

- affected1: Cold Front

- text: Spirit Power damage scaling increased from 0.98 to 1.25

- type: buff

- affected1: Cold Front I Duration Extender

- text: Bonus HP increased from 75 to 100

- type: buff

- affected1: Duration Extender I Silence Glyph

- text: Spirit Shield increased from 150 to 225

- type: buff

- affected1: Silence Glyph I Superior Duration

- text: Bonus HP increased from 125 to 175

- type: buff

- affected1: Superior Duration I Surge of Power

- text: Imbued Spirit Power increased from +24 to +26

- type: buff

- affected1: Surge of Power I Torment Pulse

- text: Now has a regular cooldown that is reduced by cooldown reduction

- type: change

- affected1: Torment Pulse I Escalating Exposure

- text: First stack no longer does double amp value

- type: change

- affected1: Escalating Exposure

- text: Now passively applies -12% Spirit Resist when dealing Spirit Damage

- type: change

- affected1: Escalating Exposure I Refresher

- text: Cooldown reduced from 220s to 200s

- type: buff

- affected1: Refresher

- text: Spirit Resist increased from 12% to 14%

- type: buff

- affected1: Refresher I Echo Shard

- text: Bullet Resist increased from 10% to 16%

- type: buff

- affected1: Echo Shard I Diviner's Kevlar

- text: Buff duration increased from 12s to 15s

- type: buff

- affected1: Diviner's Kevlar

## Heroes

- H Abrams

- text: Fixed not stunning the target when colliding with's

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge

- text: Fixed some cases where did not stun when hitting a wall

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge

- text: Fixed enemies being able to double jump out of - type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text: T3 reduced from +6.5 to +5.5 Weapon Damage

- type: nerf

- affected1: Abrams

- affected2: Shoulder Charge

- text: damage reduced from 200 to 175

- type: nerf

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: Bullet Resistance growth per boon increased from 2% to 2.5%

- type: buff

- affected1: Bebop

- text: now prioritizes enemies over allies

- type: change

- affected1: Bebop

- affected2: Sticky Bomb

- text: duration now scales with Spirit (0.08)

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: spirit scaling increased from 2.2 to 2.4

- type: buff

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: width increased from 4m to 4.5m

- type: buff

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: recharge time reduced from 6s to 5s

- type: buff

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: regen Spirit Power scaling increased from 0.4 to 0.5

- type: buff

- affected1: Dynamo

- affected2: Rejuvenating Aurora H Grey Talon

- text: collision size reduced by 10%

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- text: explosion radius increased from 10m to 12m

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: cooldown reduced from 120s to 110s

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: Bullet damage falloff is now 20% more falloff than default

- type: nerf

- affected1: Haze

- text: Can now cast while on zipline

- type: buff

- affected1: Haze

- affected2: Smoke Bomb H Infernus

- text: Fixed Infernus being unable to slide out of - type: fix

- affected1: Infernus

- affected2: Flame Dash

- text: T1 and T2 Swapped

- type: change

- affected1: Infernus

- affected2: Afterburn

- text: base DPS reduced from 18 to 15

- type: nerf

- affected1: Infernus

- affected2: Afterburn

- text: T3 DPS reduced from 33 to 30

- type: nerf

- affected1: Infernus

- affected2: Afterburn

- text: spirit scaling increased from 0.4 to 0.5

- type: nerf

- affected1: Infernus

- affected2: Afterburn H Kelvin

- text: Fixed not having proper lag compensation

- type: fix

- affected1: Kelvin

- affected2: Arctic Beam

- text: Fixed some cases where would explode and not hit anyone

- type: fix

- affected1: Kelvin

- affected2: Frost Grenade

- text: can now be canceled directly by using parry

- type: change

- affected1: Kelvin

- affected2: Arctic Beam

- text: cast time reduced from 0.2s to 0.1s

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade

- text: recharge time reduced from 8s to 7s

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade

- text: sprint is now granted immediately on use

- type: buff

- affected1: Kelvin

- affected2: Ice Path H Lady Geist

- text: Base sprint reduced from 2 to 1

- type: nerf

- affected1: Lady Geist H Lash

- text: Base sprint reduced from 3 to 1

- type: nerf

- affected1: Lash

- text: Damage Per Meter reduced from 6.3 to 6.0

- type: nerf

- affected1: Lash

- affected2: Ground Strike H McGinnis

- text: no longer target immune structures

- type: change

- affected1: McGinnis

- affected2: Mini Turret

- text: cast/aim behavior improved for indoors and close range

- type: fix

- affected1: McGinnis

- affected2: Heavy Barrage

- text: Reverted recent melee damage reduction

- type: buff

- affected1: McGinnis

- text: Fixed [Health Nova](Health Nova.md) not working on (when Health Nova was cast by McGinnis)

- type: fix

- affected1: McGinnis

- affected2: Health Nova

- affected3: Mini Turret

- text: base HP increased from +50 to +75

- type: buff

- affected1: McGinnis

- affected2: Mini Turret H Mo & Krill

- text: Can now reload while burrowed

- type: change

- affected1: Mo & Krill H Paradox

- text: Time Slowed targets that were moving before the time slow will now resume their momentum when time slow wears off

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: Bullet (and ) projectile speed reduced by 10%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: Ammo count reduced from 54 to 45

- type: nerf

- affected1: Paradox H Pocket

- text: damage is dealt over 18s instead of 16s (same total damage, lower DPS)

- type: change

- affected1: Pocket

- affected2: Affliction

- text: T3 changed from Disarms for 2.5s to Applies -40% Fire Rate for 4s

- type: change

- affected1: Pocket

- affected2: Enchanter's Satchel H Seven

- text: stun duration reduced from 1.25s to 1.1s

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: T3 stun duration reduced from 1.25s to 1.1s

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: T2 radius increased from +5m to +7m

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: Headshot damage taken reduced by 25%

- type: buff

- affected1: Seven H Vindicta

- text: cooldown reduced from 45 to 40

- type: buff

- affected1: Vindicta

- affected2: Flight

- text: Gun damage growth increased from 0.85 to 1.0

- type: buff

- affected1: Vindicta H Wraith

- text: post cast time reduced from 0.5s to 0.2s

- type: buff

- affected1: Wraith

- affected2: Card Trick

- text: Fixed some issues tracking that could cause it to orb players or go to the wrong spot

- type: fix

- affected1: Wraith

- affected2: Card Trick H Yamato

- text: collision size reduced by 10%

- type: nerf

- affected1: Yamato

- affected2: Power Slash

- text: Bullet damage growth increased from 0.4 to 0.5

- type: nerf

- affected1: Yamato
