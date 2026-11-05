---
title: "Patch/Playtest/2024-08-15"
pageid: 566
source: liquipedia-deadlock-md
---

- name: Playtest - August 15 2024

- version: 2024-08-15

- release: August 15, 2024

- highlight1: Gameplay Updates

- highlight2: Bug Fixes

- highlight3: Item Updates

- highlight4: New Item:

- highlight5: Hero Updates

- highlight6: New Hero:

- previous: Patch/Playtest/2024-08-062024-08-06

- next: Patch/Playtest/2024-08-162024-08-16

## General

Added a new hero, H Shiv Games can now be watched by an unlimited number of spectators Spectator games now have 1 minute delay Added localization for Simplified Chinese, Russian, Brazilian Portuguese, Spanish (Spain), Spanish (Latin America), Turkish, Ukrainian, Czech, and French. These are currently a work-in-progress.

Language can be selected from the settings menu Matchmaking windows are now open 1 hour earlier in all regions You can now prioritize your roster into three groups to indicate your preference ordering to the matchmaker: Selected, Priority, High Priority Added customization options for your crosshair Builds: You can now author a suggested ordering of Ability Upgrades Builds: You can now add per-item author comments by right clicking on items while editing builds that will show up in the item tooltip for users of the build Fixed a bug that allowed published build data to overwrite local changes to a published build Fixed a bug that prevented the last used hero build from loading when it was not a favorited build Hovering items in the shop will now highlight their components, or which item they are components of Reworked the Hero Stats UI in the shop Hero Stats in the shop have been expanded and are now broken up by Weapon, Vitality, and Spirit. Various additional stats that were previously hidden have been added here.

Individual stats can now be hovered over to see a breakdown of all the bonuses contributing to a value, including things like golden statues Added descriptive gun information to each hero Added Spirit Power Impact panel that displays the effect of Spirit Power on your Abilities and Items Added Outgoing Damage as a UI display mode that you can toggle through Added a setting to let you customize the ability cancel hotkey (default is spacebar) Added a "Friends Only" checkbox to filter the watch tab Added an option to control zoom sensitivity Fixed Candle Troopers sometimes instantly disappearing on death rather than going into their death flash state Using an active item or ability removes the undo option for the item/AP Fixed some abuse cases with undoing AP cooldown reductions Added a video setting to reduce flashing effects Unpause hotkey is now displayed when the game is paused Pause cooldown per player increased from 10 minutes to 15 minutes Improved visual clarity of Grey Talon's trap armed state Replaced the Urn drop parachute with new effects Fixed some cases where the comeback souls would be higher than intended in the early game Fixed being unable to ping while dead Fixed Bebop's Sticky Bomb sometimes misfiring Improved smoothing of spectator camera position and angles Fixed a bug that allowed teleporters to be used while carrying the Soul Urn Fixed targeting previews that draw a model (like McGinnis's turrets) to update every frame, instead of being fixed at 60hz Fixed stuns resetting their duration if you were on the ground and became airborne Fixed some cases where Lash's Ground Strike would cause your hero to be stuck Fixed Ricochet sometimes shooting the extra bullet from your gun rather than the target Fixed Arctic Beam T3 range not being calculated correctly when you have range increase items Fixed ESC not working to close Settings popup sometimes Various visual adjustments on highlight and strobe effects being too loud in some cases Holding M1 down while Flame Dash ends will now cause you to fire your gun instead of requiring you to let go and press again Added popup to bot games to indicate that they tend to be much longer games than normal ones Improved Abrams Siphon and Seismic Impact visuals to not obstruct player view as much Added new Silence status effect sound Updated bullet whizby sounds for nearly all characters Updated Haze Sleep Dagger cast, projectile loop and whizby Updated Haze Smoke Bomb sound Removed Haze Smoke Bomb voice line for everyone except the casting player and spectators Fixed some spectator/replay sound and music bugs Various sound related performance improvements More impactful damage indication sound for attackers Remastered Abrams, Pocket, and Dynamo weapon fire sounds Improved lighting performance around shop Improved Wraith tracers to feel more connected to their bullet Improved visibility of AOE around Bebop while casting Hyper Beam Improved effects around Lady Geist Soul Exchange to help with clarity Updated Infernus tracer, muzzle, and impact fx revisions for better performance Fixed Mimic options in sandbox not working properly Added a sound for movement being restricted by Slowing Hex and Vindicta tether Revised sounds for Pocket Flying Cloak duration and warp Clarified Vindicta Flight T1 tooltip Added alternate shop music Added Refresher cast sound

## Gameplay

Teleporter activation no longer gets canceled on incoming damage.

Teleporter channel time increased from 4s to 5s

- text: now require you to be within 30m to deal damage to them

- type: change

- affected1: Walker

- text: Health increased by 15%

- type: buff

- affected1: Walker

- text: Base Health increased by 20%

- type: buff

- affected1: Guardian Patron damage increased by 30% after it is vulnerable Weakened Patron Health increased by 15% Weakened Patron now has a Torment Pulse style effect, hitting up to 2 enemies in the pit for 75 damage per second You can now use melee hotkey while zoomed to exit zoom and perform a melee Added Bounce Pads in various areas of the map that launch you in a defined direction Added one-way defender exits beside each outer lane entrance Added Speed Boost Volumes in the defender passages on the outsides of the base Firehouse (building next to Sapphire Yellow Guardian) has been reworked to match the layout of the Chapel Low roof buildings beside Amber Purple Guardian and Sapphire Yellow Guardian are now valid play spaces Removed zap triggers Added truck on the back side of those buildings to allow climbing up Removed rooftop props for those buildings Added billboards to the edge closest to the lane Low roof buildings between inner lane Walker arenas are now valid play spaces Removed zap triggers Expanded rooftop size Added fire escape stairs to allow access from the upper level from the Mid Walker Arena - Amber Yellow/Sapphire Purple: Added catwalks from high ground defender area to building across the street Added passage through building and stairs up to a peek spot toward the Guardian Replaced upper floor juke spot with a connection through building across from new peek spot Walker Arena - Amber Orange/Sapphire Blue: Added catwalk from the low roof building to the building across the street Replaced juke spot in the courtyard with passage connecting to the new catwalk Widened hallway above Underground Shop Removed railing and added stairs in the passage toward the Guardian Courtyard floor opening to the Underground Shop moved closer to above the shop Bounce Pad added to allow easier navigation from the Underground Shop to the upper courtyard. Replaces a juke spot.

Walker Arena - Amber Blue/Sapphire Orange: Added interior shaft with Bounce Pad to an upper level balcony from defender side to face the Guardian Added a Bounce Pad on the ground floor of the Police Station/Garment Building to the upper floor Added a juke spot inside the Police Station/Garment Building Added a juke spot down the stairs from the Guardian to the left Walker Arena - Amber Purple/Sapphire Yellow: Added an interior corridor through the building between the base and the Walker Added a balcony that borders the arena on the back side of the Walker

## Items

1. Weapon I Headshot Booster

- text: No longer has +40 Bonus Health

- type: nerf

- affected1: Headshot Booster

- text: Now has +40 Bullet Shield

- type: buff

- affected1: Headshot Booster I Monster Rounds

- text: Health reduced from +65 to +50

- type: nerf

- affected1: Monster Rounds

- text: Now grants +30% Bullet Resistance vs NPCs

- type: buff

- affected1: Monster Rounds I Restorative Shot

- text: Weapon Damage increased from 6% to 8%

- type: buff

- affected1: Restorative Shot I Active Reload

- text: Lifesteal reduced from 40% to 30%

- type: nerf

- affected1: Active Reload

- text: Fire Rate reduced from 24% to 20%

- type: nerf

- affected1: Active Reload I Kinetic Dash

- text: HP regen increased from 1 to 1.5

- type: buff

- affected1: Kinetic Dash I Long Range

- text: Min distance reduced from 18m to 15m

- type: nerf

- affected1: Long Range I Mystic Shot

- text: Cooldown increased from 5s to 6s

- type: nerf

- affected1: Mystic Shot I Slowing Bullets

- text: Now grants +5 Spirit

- type: buff

- affected1: Slowing Bullets I Soul Shredder Bullets

- text: Now grants +6% Weapon Damage

- type: buff

- affected1: Soul Shredder Bullets

- text: Debuff duration increased from 5s to 6s

- type: buff

- affected1: Soul Shredder I Berserker

- text: Fixed gaining stacks much faster than intended when taking damage from troopers

- type: fix

- affected1: Berserker I Warp Stone

- text: Active Bullet Resist reduced from +60% to +40%

- type: nerf

- affected1: Warp Stone

- text: No longer grants +2 Sprint

- type: nerf

- affected1: Warp Stone

- text: Now gains +8 Spirit

- type: buff

- affected1: Warp Stone I Point Blank

- text: No longer grants +300 Bullet Shield

- type: nerf

- affected1: Point Blank

- text: Now grants +15% Bullet Armor

- type: buff

- affected1: Point Blank I Escalating Resilience

- text: Max Bullet Resist increased from 30% to 36%

- type: buff

- affected1: Escalating Resilience I Heroic Aura

- text: Lifesteal increased from 18% to 20%

- type: buff

- affected1: Heroic Aura I Alchemical Fire

- text: Bullet Shield increased from 175 to 225

- type: buff

- affected1: Alchemical Fire I Sharpshooter

- text: Min distance reduced from 18m to 15m

- type: buff

- affected1: Sharpshooter I Titanic Magazine

- text: Weapon Damage increased from 16% to 18%

- type: buff

- affected1: Titanic Magazine

- text: Bullet Resist increased from 8% to 10%

- type: buff

- affected1: Titanic Magazine I Intensifying Magazine

- text: Time for Max Damage reduced from 3.5s to 3s

- type: buff

- affected1: Intensifying Magazine I Ricochet

- text: Fire Rate increased from +8% to +12%

- type: buff

- affected1: Ricochet

- text: Health increased from +125 to +150

- type: buff

- affected1: Ricochet I Siphon Bullets

- text: You permanently steal 1 stack (45 HP) from the enemy if they die under the debuff. If an enemy you stole a stack from kills you, they regain 1 stack back.

- type: buff

- affected1: Siphon Bullets I Silencer

- text: Reduced active duration from 6s to 4s

- type: nerf

- affected1: Silencer I Glass Cannon

- text: Now gives +1 Movement Speed

- type: buff

- affected1: Glass Cannon

- text: No longer gives +2 ammo on kill

- type: nerf

- affected1: Glass Cannon

- text: Weapon Damage reduced from +75% to +70%

- type: nerf

- affected1: Glass Cannon

- text: Now gives +10% Weapon Damage per kill (up to +50%)

- type: buff

- affected1: Glass Cannon

- text: When you die you lose a stack

- type: nerf

- affected1: Glass Cannon 1. Vitality I Melee Lifesteal

- text: Heal effectiveness vs non-heroes increased from 25% to 35%

- type: buff

- affected1: Melee Lifesteal

- text: Health increased from +70 to +75

- type: buff

- affected1: Melee Lifesteal I Extra Regen

- text: Regen increased from 2.7 to 2.8

- type: buff

- affected1: Extra Regen I Healing Rite

- text: Cooldown reduced from 75s to 65s

- type: buff

- affected1: Healing Rite

- text: Cast Range increased from 20m to 30m

- type: buff

- affected1: Healing Rite I Healing Booster

- text: Spirit Resist reduced from +7% to +6%

- type: nerf

- affected1: Healing Booster

- text: Bullet Resist reduced from +7% to +6%

- type: nerf

- affected1: Healing Booster I Divine Barrier

- text: Duration increased from 4s to 5s

- type: buff

- affected1: Divine Barrier

- text: Cooldown reduced from 30s to 28s

- type: buff

- affected1: Divine Barrier I Restorative Locket

- text: Max Stacks reduced from 20 to 15

- type: nerf

- affected1: Restorative Locket

- text: Heal per stack increased from 30 to 40

- type: buff

- affected1: Restorative Locket I Healing Nova

- text: Health increased from +75 to +100

- type: buff

- affected1: Health Nova I Combat Barrier

- text: Weapon Damage While Shielded increased from +24% to +28%

- type: buff

- affected1: Combat Barrier I Enchanter's Barrier

- text: Spirit Power while Shielded increased from +17 to +20

- type: buff

- affected1: Enchanter's Barrier I Bullet Lifesteal

- text: Lifesteal increased from +26% to 28%

- type: buff

- affected1: Bullet Lifesteal I Superior Stamina

- text: Air Jump/Dash Distance reduced from +50% to +40%

- type: nerf

- affected1: Superior Stamina

- text: Fire Rate reduced from 10% to 7%

- type: nerf

- affected1: Superior Stamina I Debuff Remover

- text: Debuff resistance reduced from +40% to +35%

- type: nerf

- affected1: Debuff Remover I Lifestrike

- text: Heal effectiveness vs non-heroes increased from 25% to 35%

- type: buff

- affected1: Lifestrike

- text: Heal increased from 45% of melee damage to +55%

- type: buff

- affected1: Lifestrike I Majestic Leap

- text: Health increased from +100 to +125

- type: buff

- affected1: Majestic Leap

- text: Spirit Power increased from +8 to +10

- type: buff

- affected1: Majestic Leap I Metal Skin

- text: Cooldown reduced from 30s to 25s

- type: buff

- affected1: Metal Skin I Fortitude

- text: Out of combat regen timer reduced from 13s to 12s

- type: nerf

- affected1: Fortitude I Rescue Beam

- text: Cooldown reduced from 30s to 25s

- type: buff

- affected1: Rescue Beam I Soul Rebirth

- text: Rebirth Health increased from 40% to 50%

- type: buff

- affected1: Soul Rebirth

- text: Cooldown reduced from 240s to 200s

- type: buff

- affected1: Soul Rebirth I Inhibitor

- text: Weapon Damage increased from 20% to 25%

- type: buff

- affected1: Inhibitor I Colossus

- text: Slow increased from 20% to 25%

- type: buff

- affected1: Colossus

- text: Slow now affects stamina distances

- type: change

- affected1: Colossus I Phantom Strike

- text: Cast range reduced from 35m to 30m

- type: nerf

- affected1: Phantom Strike 1. Spirit I Infuser

- text: No longer gives +7% Spirit Resist

- type: change

- affected1: Infuser

- text: Now gives +50 Health

- type: change

- affected1: Infuser I Spirit Strike

- text: Spirit damage increased from 40 to 50

- type: buff

- affected1: Spirit Strike

- text: Debuff increased from -10% Spirit Resist to -12%

- type: buff

- affected1: Spirit Strike I Mystic Reach

- text: Now gives +5% Spirit Resist

- type: buff

- affected1: Mystic Reach I Ammo Scavenger

- text: Spirit Power Duration increased from 24s to 35s

- type: buff

- affected1: Ammo Scavenger I Cold Front

- text: Damage reduced from 100 to 75

- type: nerf

- affected1: Cold Front

- text: Damage Spirit Power scaling increased from 1.25 to 1.5

- type: buff

- affected1: Cold Front I Decay

- text: Healing Reduction reduced from -70% to -50%

- type: nerf

- affected1: Decay

- text: Bleed increased from 2.8% to 3.1%

- type: buff

- affected1: Decay

- text: Cooldown increased from 25s to 30s

- type: nerf

- affected1: Decay I Slowing Hex

- text: Debuff no longer cancels active mobility spells, it only prevents them from being casted

- type: nerf

- affected1: Slowing Hex

- text: Damage reduced from 100 to 70

- type: nerf

- affected1: Slowing Hex

- text: Cast range reduced from 35m to 25m

- type: nerf

- affected1: Slowing Hex

- text: Now also reduces stamina distance by 30%

- type: buff

- affected1: Slowing Hex

- text: Projectile speed increased from 1200 to 1350

- type: buff

- affected1: Slowing Hex I Withering Whip

- text: Now applies -40% Fire Rate instead of a Disarm

- type: change

- affected1: Withering Whip

- text: Duration increased from 3s to 4.5s

- type: buff

- affected1: Withering Whip

- text: Cast range increased from 18m to 24m

- type: buff

- affected1: Withering Whip I Quicksilver Reload

- text: Infused ability bonus damage increased from +30 to +50

- type: buff

- affected1: Quicksilver Reload I Improved Cooldown

- text: Cooldown reduction increased from 14% to 15%

- type: buff

- affected1: Improved Cooldown I Ethereal Shift

- text: No longer provides +10% Fire Rate

- type: nerf

- affected1: Ethereal Shift

- text: Cooldown increased from 25s to 30s

- type: nerf

- affected1: Ethereal Shift I Improved Burst

- text: Reduced Weapon Damage from +12% to +8%

- type: nerf

- affected1: Improved Burst I Surge of Power

- text: Movespeed duration increased from 5s to 6s

- type: buff

- affected1: Surge of Power

- text: Imbued Spirit increased from +26 to +28

- type: buff

- affected1: Surge of Power

- text: Now grants +75 Health

- type: buff

- affected1: Surge of Power I Improved Reach

- text: Now gives +10% Spirit Resist

- type: buff

- affected1: Improved Reach I Superior Duration

- text: Now provides +15% Weapon Damage

- type: buff

- affected1: Superior Duration I Mystic Slow

- text: Fire Rate reduction increased from -30% to -40%

- type: buff

- affected1: Mystic Slow I Silence Glyph

- text: No longer reduces Spirit Resist

- type: change

- affected1: Silence Glyph

- text: Now deals +150 damage on impact

- type: change

- affected1: Silence Glyph I Superior Cooldown

- text: Non-Imbued ability cd reduction increased from 22% to 24%

- type: buff

- affected1: Superior Cooldown I Escalating Exposure

- text: Max Interval improved from 1s to 0.7s

- type: buff

- affected1: Escalating Exposure I Diviner's Kevlar

- text: Cooldown increased from 30s to 60s

- type: nerf

- affected1: Diviner's Kevlar I Refresher

- text: Spirit Resist increased from 14% to 16%s

- type: buff

- affected1: Refresher I Curse

- text: Cooldown increased from 40s to 50s

- type: nerf

- affected1: Curse 1. New Items

- Added a new T1 Weapon item. Grants +35% Bullet Projectile Speed, +14% Weapon Damage and +50 Bullet Shield.

Added a new T4 Spirit item, I Magic Carpet: Active - After a 1.3s delay, a magic carpet arrives to pick you up. You gain full flight controls and have +6 m/s movement speed. Lasts 7 seconds. If you cast abilities or use your gun, the carpet disappears. While on the Magic Carpet you gain +400 Bullet and +400 Spirit Shields. Passively grants +150 Health, +10% Ability Duration, and +15 Spirit Power. Cooldown: 40s

## Heroes

- H Abrams

- text: Fixed often not dragging enemies in the air along with you when you are slamming down

- type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text: Fixed not always placing enemies in front of you

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge

- text: damage reduced from 175 to 150

- type: nerf

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: Gun range reduced from 50m to 30m + 2.5m/boon (max of 58m)

- type: nerf

- affected1: Bebop

- text: Speed while shooting increased from 55% to 70%

- type: buff

- affected1: Bebop

- text: Base regen increased from 2.5 to 3

- type: buff

- affected1: Bebop

- text: Base Bullet Resist increased from 0% to 10%

- type: buff

- affected1: Bebop

- text: Bullet Resist per boon reduced from 2.5% to 1.6% (same overall bullet resist at max)

- type: nerf

- affected1: Bebop

- text: range reduced from 40m to 35m

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: T2 increased from +25m to +30m

- type: buff

- affected1: Bebop

- affected2: Hook

- text: now has a slight angle limitation to prevent straight-up direction

- type: change

- affected1: Bebop

- affected2: Exploding Uppercut

- text: radius increased from 10m to 14m

- type: buff

- affected1: Bebop

- affected2: Exploding Uppercut

- text: T1 increased from -10s Cooldown to -11s

- type: nerf

- affected1: Bebop

- affected2: Exploding Uppercut

- text: Fixed hooking through veils sometimes not working

- type: fix

- affected1: Bebop

- text: radius increased from 10m to 12m

- type: buff

- affected1: Bebop

- affected2: Sticky Bomb

- text: can now be cast on self using alt cast hotkey

- type: change

- affected1: Bebop

- affected2: Sticky Bomb

- text: T2 reduced from +140 to +100

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam

- text: spirit scaling increased from 2.4 to 3.0

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: turn rate improved by 10%

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: nearby radius increased from 4.5m to 5m

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: nearby damage now does 25% less than the full amount

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: can now be canceled by using stamina instead of needing to manually exit first (pre T3)

- type: change

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text: Fixed sometimes getting caught on stairs

- type: fix

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: now has a 0.1s cast point

- type: change

- affected1: Dynamo

- affected2: Singularity

- text: width increased from 4.5m to 5m

- type: buff

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: T3 increased from +115 Damage to +125

- type: buff

- affected1: Dynamo

- affected2: Kinetic Pulse H Grey Talon

- text: collision radius reduced by 10%

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- text: Fixed T3 not triggering correctly sometimes when the target has Spirit Armor

- type: fix

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: now puts you in a brief drowsy state for 0.25s seconds where you move slowly before falling asleep (you still have the ability to shoot/cast/move/etc during this period)

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: T2 from +6s Duration to +5s

- type: nerf

- affected1: Haze

- affected2: Fixation

- text: T3 reduced from +0.25 to +0.2

- type: nerf

- affected1: Haze

- affected2: Fixation

- text: T1 increased from +6 to +7

- type: buff

- affected1: Haze

- affected2: Bullet Dance H Ivy

- text: Fixed melee still going through when casting after initiating a melee attack

- type: fix

- affected1: Ivy

- affected2: Stone Form

- text: T2 stun reduced from 0.75s to 0.5s

- type: nerf

- affected1: Ivy

- affected2: Stone Form

- text: T1 reduced from +15% Fire Rate to +10%

- type: nerf

- affected1: Ivy

- affected2: Watcher's Covenant

- text: Now has a new ultimate ability,. Take flight with an Ally (or self-cast to carry a bomb). You fly and drop the ally or bomb onto an area, dealing damage, slowing, and silencing enemies. Ivy and the ally gain a bullet shield when they are dropped. Allies can drop by themselves at any time. When using the ability without an ally (carrying a bomb), it has a 1 second cast time.

- type: change

- affected1: Ivy

- affected2: Air Drop H Kelvin

- text: no longer applies a Disarm

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: now slows Fire Rate (same values as slow)

- type: change

- affected1: Kelvin

- affected2: Arctic Beam

- text: max slow reduced from 90% to 60%

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: time to reach max slow increased from 1.2s to 2s

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: can now be cast while using

- type: change

- affected1: Kelvin

- affected2: Frozen Shelter

- affected3: Arctic Beam H Lash

- text: Health per boon increased from 37 to 42

- type: buff

- affected1: Lash

- text: Base spirit resist increased from 8% to 15%

- type: buff

- affected1: Lash

- text: cooldown reduced from 30s to 25s

- type: buff

- affected1: Lash

- affected2: Flog

- text: now also reduces Fire Rate by 35%

- type: buff

- affected1: Lash

- affected2: Flog H McGinnis

- text: Speed while shooting increased from 55% to 70%

- type: buff

- affected1: McGinnis

- text: s now prioritize any heroes McGinnis is shooting at - type: change

- affected1: McGinnis

- affected2: Mini Turret

- text: duration Spirit Power scaling increased from 0.09 to 0.12

- type: buff

- affected1: McGinnis

- affected2: Medicinal Specter

- text: T1 changed to Rockets apply 35% slow

- type: change

- affected1: McGinnis

- affected2: Heavy Barrage H Mo & Krill

- text: T3 now affects all damage types

- type: buff

- affected1: Mo & Krill

- affected2: Scorn H Paradox

- text: Base ammo reduced from 45 to 40

- type: nerf

- affected1: Paradox

- text: projectile size reduced by 10%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: cooldown increased from 24s to 28s

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: speed duration reduced from 4s to 3.5s

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: no longer affects channels, cast times or things like Lash's Death Slam

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: T1 reduced from +0.75s Max Stop duration to +0.5s

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: T2 cd reduction increased from -8s to -10s

- type: buff

- affected1: Paradox

- affected2: Kinetic Carbine

- text: silence duration reduced from 3.5s to 3s

- type: nerf

- affected1: Paradox

- affected2: Time Wall

- text: projectile size reduced by 10%

- type: nerf

- affected1: Paradox

- affected2: Paradoxical Swap H Pocket

- text: now respects line of sight

- type: change

- affected1: Pocket

- affected2: Barrage

- text: amp effect now shows on Pocket

- type: change

- affected1: Pocket

- affected2: Barrage

- text: Base Bullet Resist increased from -15% to 0%

- type: buff

- affected1: Pocket

- text: Base Spirit Resist reduced from 0% to -15%

- type: nerf

- affected1: Pocket

- text: Amp per stack reduced from 10% to 8%

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: T3 changed to +5% Amp Per Stack

- type: change

- affected1: Pocket

- affected2: Barrage

- text: Fixed the camera moving too slowly after teleporting with - type: fix

- affected1: Pocket

- affected2: Flying Cloak H Seven

- text: Fixed multiple instances of not working correctly

- type: fix

- affected1: Seven

- affected2: Static Charge

- text: duration increased from 4s to 5s

- type: buff

- affected1: Seven

- affected2: Lightning Ball

- text: stun delay reduced from 4s to 3.5s

- type: buff

- affected1: Seven

- affected2: Static Charge H Vindicta

- text: base duration reduced from 2.5s to 2.25s

- type: nerf

- affected1: Vindicta

- affected2: Stake

- text: T1 duration reduced from 1s to 0.75s

- type: nerf

- affected1: Vindicta

- affected2: Stake H Viscous

- text: Fixed direct hits counting as the second hit

- type: fix

- affected1: Viscous

- affected2: Splatter

- text: Fix Damage prevention after being hit by Viscous' being reduced by Debuff Reducer

- type: fix

- affected1: Viscous

- affected2: Goo Ball

- text: cast range increased from 25m to 30m

- type: buff

- affected1: Viscous

- affected2: The Cube

- text: T2 cooldown reduced from -25s to -22s

- type: buff

- affected1: Viscous

- affected2: The Cube

- text: now deals light melee damage and is affected by melee items

- type: change

- affected1: Viscous

- affected2: Puddle Punch

- text: Charge Delay increased from 0.5s to 1.5s

- type: nerf

- affected1: Viscous

- affected2: Puddle Punch

- text: duration reduced from 12s to 10s

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: T1 duration reduced from +6s to +5s

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: cooldown increased from 80s to 90s

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: now deals 50% damage to bosses

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: spirit resist reduced from 80% to 70%

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: bullet resist reduced from 70% to 60%

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: can now only stun and damage a target once every 1.5s, up from once every 1.0s

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: acceleration lowered a bit

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: Stunning or immobilizing Viscous now stops the ball from moving, and prevents him from doing damage and stunning

- type: nerf

- affected1: Viscous

- affected2: Goo Ball H Warden

- text: no longer drains 1 stamina

- type: buff

- affected1: Warden

- affected2: Binding Word

- text: cooldown reduced from 16s to 13s

- type: buff

- affected1: Warden

- affected2: Alchemical Flask

- text: T2 changed from -10s Cooldown to Drains 1 Stamina

- type: change

- affected1: Warden

- affected2: Alchemical Flask

- text: T3 now also reduces cooldown by -7s

- type: buff

- affected1: Warden

- affected2: Alchemical Flask

- text: immobilize duration reduced from 2s to 1.75

- type: nerf

- affected1: Warden

- affected2: Binding Word

- text: now has a quick cast behavior (same as Static Charge)

- type: change

- affected1: Warden

- affected2: Binding Word H Wraith

- text: now has 0.5s cd per cast

- type: nerf

- affected1: Wraith

- affected2: Card Trick

- text: T2 duration reduced from +0.75s to +0.5s

- type: nerf

- affected1: Wraith

- affected2: Telekinesis

- text: T2 changed to Imbues Bullets with +5 Spirit Damage (only affects Wraith)

- type: change

- affected1: Wraith

- affected2: Full Auto

- text: Fixed being able to melee and parry while stunned by Wraith's

- type: fix

- affected1: Wraith

- affected2: Telekinesis H Yamato

- text: Base melee damage increased by 10%

- type: buff

- affected1: Yamato

- text: T3 now procs after the ability ends, rather than when connecting to the target

- type: change

- affected1: Yamato

- affected2: Flying Strike
