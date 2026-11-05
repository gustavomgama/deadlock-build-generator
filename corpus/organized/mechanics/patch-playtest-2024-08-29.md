---
title: "Patch/Playtest/2024-08-29"
pageid: 557
source: liquipedia-deadlock-md
---

- name: Playtest - August 29 2024

- version: 2024-08-29

- release: August 29, 2024

- highlight1: Balances

- highlight2: Bug fixes

- highlight3: Wall Jumping

- previous: Patch/Playtest/2024-08-232024-08-23

- next: Patch/Playtest/2024-09-012024-09-01

## General

Added a new Profile page that displays a breakdown of recent matches and all-time player and hero statistics (Note: the newly added stats 'Souls Collected' and 'Healing' are starting at 0 for all players) Added Report button to ESC menu player list to allow reporting of teammates in-game Improved visibility of report button on post-game screen You can now drag-and-drop items between categories in Builds Added search to the Public Builds list, you can search by keyword within build names Newly published hero builds now store the language of the build Added 'Show All Languages' checkbox in Public Builds list, can be unchecked to only see builds in your language Fixed issue with builds list not updating when changing between heroes in sandbox Added localization support for German, Polish, and Korean Matchmaking window is now open 1 hour earlier on weekdays and weekends Players can only pause once per game A team can only pause at most 3 times in total amongst all the players The game application now flashes when the game is unpaused Various client and server performance improvements Added streamer setting to the options panel. Causes player names in the game UI panels to be hidden.

Added a Melee Trainer bot in the 'gym' area of hero sandbox Added new "Game out of Date" status message at the top of the hud, so you can quickly know when there is an update rather than finding out at queue time Added a checkbox on the post game survey to make it not show again in the future Items now show their spirit power impact when using alt Fixed profile match history not remembering the history page you were on Added Heal Amp and Debuff Resist to the Vitality stats in the shop Hero details on the dashboard now show spirit information with alt, rather than requiring you to be in-game (this was added in a hotfix patch recently) The game will now prevent any quick ability upgrades for 2 seconds after death, to help prevent against accidental upgrades Can now reliably spectate a friend's game via the Friendlist Miscellaneous fixes to friends and party menus Added unavailable state to Zipline UI when zipline is on damage cooldown Spectating controls now use Left/Right mouse buttons to switch between players on a team and space to switch teams. This now works with free cursor mode, and you can still click on portraits/minimap to spectate individual heroes.

Added new respawn countdown music 5 seconds before respawn Added alternate shop music which plays in the neutral shop Spectator count is now shown in-game Player names are now shown to spectators Added object motion blur Optimized performance of distance field ambient occlusion Fixed selling an item not removing charges correctly. Now you can't buy Extra Charge and immediately sell it and keep that readied charge.

- text: Fixed some tooltips not showing [golden statue](golden statue.md) bonuses if it wasn't the direct stat (i.e. you got fire rate but bullets per second didn't show the golden statue)

- type: fix

- affected1: Golden Statue Fixed Sharpshooter showing up in stats for bullet velocity even though it doesn't increase your bullet velocity Fixed a bug that caused items in the build page to not be dimmed when the shop was out of range Fixed bug with Lash not hearing his own Ground Strike impact explosion sound Added new effects for Withering Whip Updated Ethereal Shift effects Fixed the disarmed spinner not showing up on your crosshair when you get disarmed Fixed parts of Shiv's coat being considered a headshot Build list will now refresh if you change heroes in the sandbox

- text: Fixed Zipline speed from Base killing and Zip booster ability not stacking properly

- type: fix

- affected1: Guardian

- text: Fixed Base boost not properly doing its ramp up and instead instantly being fast

- type: fix

- affected1: Guardian Added custom effects for Abram's Seismic Impact T3 buff Fixed a bug where someone could be holding down M1 and still be attacking when the magic carpet arrives Updated Lash Grapple cast sound Added Decay impact sound Removed wind and city ambient looping sounds Volume and playback tweaks to one shot ambient sounds Removed vent sounds in places where vents had been removed Fixed some spectator music bugs Updated negative feedback sound for clarity Added hit confirm audio functionality to Warden's Alchemical Flask Updated bounce pad sound Improved some Binding Word effects to be less noisy Increased charged melee volume and falloff for victims Reduced likelihood of irrelevant announcer and hero dialog lines playing during combat exchanges Improved clarity of Dynamo Singularity sound for team and opponents Updated Viscous primary fire sound Soul jar return effect tinted red like minimap to make it more clear it's the return location Player's low health screen effect more visible for longer if you're below 20% of your max HP Teleporter model and effect updated Updated Alchemical Flask projectile effect Fixed Bebop being able to sprint while his gun is spun up Added new voice content for Seven and Lash Added Shadow Weave cast and ambush sounds Fixed bullets hitting the world immediately when looking sharply upward Fixed M Sinner's Sacrifice not always correctly animating Fixed an issue where some kill lines that were only intended for the killer were playing for the victim as well (killstreak taunts still play for everyone) Some heroes can now comment on being alone in enemy territory, losing sight of an injured enemy, or leaving their teammates alone in a lane Fixed a bunch of minor typos / grammar errors in various texts

- text: Added 'Express' state to zipline indicators when speed had increased from defeating Enemy Base

- type: change

- affected1: Guardian

## Gameplay

Added wall jumping (does not consume stamina, requires input direction away from the wall, can be done once)

- text: Moved a flex slot from "Set of enemy Base " to "All Enemy Lane "

- type: change

- affected1: Guardian Added ropes to some buildings to let you climb up (hold jump key to latch onto them). Can shoot while hanging on them.

A pair of teleporters has been added to the outer lanes at the midpoint (near the three red neutral creeps) Four teleporters have changed locations The upper floor teleporters have moved to the street level The interior teleporters have moved to the Bodega building and the Theater Teleporters are closed for the first 10 minutes (they look visually closed)

- text: no longer give 1 AP

- type: change

- affected1: Guardian AP is now added to the following Soul levels: 3500, 5200, 8000, 9700 Parry cooldown reduced from 6s to 5s Urn delivery sprint bonus increased from +2 to +3

- text: The minimum range the player must be to attack a is increased from 30m to 32m

- type: change

- affected1: Walker Golden Statues drop rate increased by 6% Replaced some bounce pads with ropes if the purpose was to go straight up Added two bounce pads next to sidelane walkers at cultural center and courthouse Added bounce pad from the Amber Orange/Sapphire Blue Walker walkway to the low roofs toward the Walker.

Removed some rooftop zap volumes that damage players Several buildings have been made taller to make their rooftops out of bounds Several buildings have been made shorter to make them more accessible A few of the buildings have new passageways at higher floors that are along the way to the rooftop Breakable containers have been added to the new playable rooftops Juke closets have replaced the previous location of the upper floor teleporters The half of the underground tunnel towards the outer lanes has been made wider Tunnel walls now have the color of the lane that the exit is closest to Removed the archway leading to the underground shop Placed temporary signage for interior buildings and storefronts for future reference Two upper floor juke spots have been converted to passages through buildings Added a new upper floor juke spot to each side Stairwell from Amber Orange/Sapphire Blue Walker catwalk to the courtyard now less cramped Lowered the statue pedestals in the inner lanes outside of Mid

## Items

1. Weapon I Monster Rounds

- text: Bullet Resist vs NPC increased from 30% to 35%

- type: buff

- affected1: Monster Rounds I Hollow Point Ward

- text: Spirit Shield increased from +80 to +85

- type: buff

- affected1: Hollow Point Ward I Restorative Shot

- text: Heal from heroes increased from 30 to 35

- type: buff

- affected1: Restorative Shot I High-Velocity Mag

- text: Bullet Velocity reduced from +35% to +30% (now has an upgrade)

- type: nerf

- affected1: High-Velocity Mag I Active Reload

- text: Lifesteal reduced from 30% to 22%

- type: nerf

- affected1: Active Reload

- text: Buff duration reduced from 8s to 7s

- type: nerf

- affected1: Active Reload I Kinetic Dash

- text: Active Fire Rate reduced from 30% to 25%

- type: nerf

- affected1: Kinetic Dash I Long Range

- text: Now grants +90 Bullet Shield

- type: buff

- affected1: Long Range I Melee Charge

- text: Now grants +1 HP regen

- type: buff

- affected1: Melee Charge I Swift Striker

- text: Now grants +10% Ammo

- type: buff

- affected1: Swift Striker I Titanic Magazine

- text: Bullet Armor increased from 10% to 15%

- type: buff

- affected1: Titanic Magazine I Toxic Bullets

- text: Heal Reduction increased from -55% to -65%

- type: buff

- affected1: Toxic Bullets

- text: Bleed damage reduced from 6% to 5%

- type: nerf

- affected1: Toxic Bullets

- text: Now grants +100 Health

- type: buff

- affected1: Toxic Bullets I Intensifying Magazine

- text: Now steadily ramps back down to 0% when you stop shooting rather than instantly emptying

- type: change

- affected1: Intensifying Magazine I Warp Stone

- text: Active Bullet Resistance reduced from 40% to 30%

- type: nerf

- affected1: Warp Stone I Sharpshooter

- text: Now grants +175 Bullet Shield

- type: buff

- affected1: Sharpshooter

- text: No longer provides bonus headshot damage

- type: nerf

- affected1: Sharpshooter

- text: Weapon damage increased from 60% to 70%

- type: buff

- affected1: Sharpshooter I Burst Fire

- text: Active duration increased from 3s to 4s

- type: buff

- affected1: Burst Fire I Escalating Resilience

- text: Max Bullet Resist increased from 36% to 40%

- type: buff

- affected1: Escalating Resilience I Alchemical Fire

- text: Cooldown reduced from 28s to 26s

- type: buff

- affected1: Alchemical Fire I Heroic Aura

- text: Active duration increased from 5s to 6s

- type: buff

- affected1: Heroic Aura I Headhunter

- text: Added new T3 Weapon Item, Headhunter: Requires High-Velocity Mag.

Grants +50% Bullet Velocity, +15% Weapon Damage and +150 Bullet Shield.

Passive cooldown: Landing a headshot on heroes deals bonus +140 Damage, heals you for +8% Max HP and grants +2 m/s for 3 seconds.

Cooldown: 6 seconds.

- type: change

- affected1: Headhunter I Siphon Bullets

- text: Weapon Damage reduced from 40% to 28%

- type: nerf

- affected1: Siphon Bullets I Frenzy

- text: Ammo increased from +9 to +12

- type: buff

- affected1: Frenzy I Lucky Shot

- text: Proc chance increased from 30% to 35%

- type: buff

- affected1: Lucky Shot I Ricochet

- text: Bounce damage increased from 50% to 60%

- type: buff

- affected1: Ricochet

- text: Fixed not applying spirit bonus damage from and abilities

- type: fix

- affected1: Ricochet 1. Vitality I Melee Lifesteal

- text: Effectiveness vs non-heroes increased from 35% to 40%

- type: buff

- affected1: Melee Lifesteal I Healing Rite

- text: Cooldown reduced from 65s to 60s

- type: buff

- affected1: Healing Rite I Divine Barrier

- text: No longer grants +7% Bullet Resist

- type: nerf

- affected1: Divine Barrier

- text: No longer grants +1.5 Health Regen

- type: nerf

- affected1: Divine Barrier

- text: Now grants +1 Sprint

- type: buff

- affected1: Divine Barrier

- text: Now grants +75 Health

- type: buff

- affected1: Divine Barrier

- text: Now grants +8% Ability Range

- type: buff

- affected1: Divine Barrier I Combat Barrier

- text: Now also grants +8% Fire Rate while active

- type: buff

- affected1: Combat Barrier I Enchanter's Barrier

- text: Now also grants +8% Cooldown Reduction while active

- type: buff

- affected1: Enchanter's Barrier I Reactive Barrier

- text: Duration reduced from 13s to 9s

- type: nerf

- affected1: Reactive Barrier I Healing Booster

- text: Now has also 15% Heal Reduction Resist

- type: buff

- affected1: Healing Booster

- text: No longer has +6% Bullet Resist

- type: nerf

- affected1: Healing Booster I Superior Stamina

- text: Air Jump/Dash Distance reduced from +40% to +30%

- type: nerf

- affected1: Superior Stamina I Metal Skin

- text: Cooldown reduced from 25s to 22s

- type: buff

- affected1: Metal Skin I Rescue Beam

- text: Channel duration reduced from 3s to 2.5s

- type: buff

- affected1: Rescue Beam I Lifestrike

- text: Effectiveness vs non-heroes increased from 35% to 40%

- type: buff

- affected1: Lifestrike I Fortitude

- text: Damage taken duration threshold reduced from 12s to 11s

- type: buff

- affected1: Fortitude I Veil Walker

- text: Cooldown reduced from 18s to 17s

- type: buff

- affected1: Veil Walker I Majestic Leap

- text: Cooldown reduced from 26s to 24s

- type: buff

- affected1: Majestic Leap I Leech

- text: No longer has 30% Heal Reduction Resist

- type: nerf

- affected1: Leech I Unstoppable

- text: Can now be cast while channeling

- type: change

- affected1: Unstoppable

- text: Cooldown reduced from 65s to 60s

- type: buff

- affected1: Unstoppable I Soul Rebirth

- text: Cooldown reduction increased from +15% to +18%

- type: buff

- affected1: Soul Rebirth

- text: Now grants +12 Spirit

- type: buff

- affected1: Soul Rebirth

- text: Fixed being able to purchase globally during its brief respawn period

- type: fix

- affected1: Soul Rebirth

- text: Fixed the camera moving away from the player if you will respawn, rather than following the ragdoll

- type: fix

- affected1: Soul Rebirth I Colossus

- text: Slow increased from 25% to 35%

- type: buff

- affected1: Colossus I Shadow Weave

- text: Spirit Shield health increased from +200 to +300

- type: buff

- affected1: Shadow Weave

- text: Spot radius reduced from 20m to 18m

- type: nerf

- affected1: Shadow Weave I Phantom Strike

- text: Cast range reduced from 30m to 25m

- type: nerf

- affected1: Phantom Strike 1. Spirit I Ammo Scavenger

- text: Health increased from +50 to +60

- type: buff

- affected1: Ammo Scavenger I Extra Charge

- text: Cooldown reduction increased from +8% to +10%

- type: buff

- affected1: Extra Charge I Spirit Strike

- text: Debuff duration increased from 8s to 13s

- type: buff

- affected1: Spirit Strike

- text: Spirit Shield increased from +85 to +100

- type: buff

- affected1: Spirit Strike I Extra Spirit

- text: Health increased from +25 to +35

- type: buff

- affected1: Extra Spirit I Withering Whip

- text: No longer grants +20% Ammo

- type: nerf

- affected1: Withering Whip

- text: Now grants +8% Fire Rate

- type: buff

- affected1: Withering Whip

- text: Fire Rate slow reduced from -40% to -30%

- type: buff

- affected1: Withering Whip

- text: Cooldown reduced from 40s to 25s

- type: buff

- affected1: Withering Whip I Quicksilver Reload

- text: No longer has +10% Reload Time

- type: nerf

- affected1: Quicksilver Reload I Suppressor

- text: Health regen reduced from 3 to 2.5

- type: nerf

- affected1: Suppressor

- text: Fire Rate reduction reduced from -30% to -25%

- type: buff

- affected1: Suppressor I Improved Cooldown

- text: Cooldown Reduction increased from 15% to 16%

- type: buff

- affected1: Improved Cooldown I Duration Extender

- text: Health regen increased from 1.5 to 1.75

- type: buff

- affected1: Duration Extender I Slowing Hex

- text: Projectile speed increased by 30%

- type: buff

- affected1: Slowing Hex

- text: Cooldown reduced from 27s to 25s

- type: buff

- affected1: Slowing Hex I Rapid Recharge

- text: Charge count reduced from +3 to +2

- type: nerf

- affected1: Rapid Recharge

- text: Faster Time Between Charges increased from +40% to +55%

- type: buff

- affected1: Rapid Recharge

- text: Cooldown for charged abilities increased from +20% to +25%

- type: nerf

- affected1: Rapid Recharge I Knockdown

- text: Delay reduced from 3s to 2s

- type: buff

- affected1: Knockdown

- text: Stun reduced from 1.25s to 0.9s

- type: nerf

- affected1: Knockdown

- text: Cast range increased from 35m to 45m

- type: buff

- affected1: Knockdown I Silence Glyph

- text: Duration reduced from 3.5s to 3s

- type: nerf

- affected1: Silence Glyph I Torment Pulse

- text: Spirit damage scaling increased from 0.2 to 0.24

- type: buff

- affected1: Torment Pulse I Surge of Power

- text: Imbued Ability Spirit Power increased from +28 to +34

- type: buff

- affected1: Surge of Power I Superior Duration

- text: Non-Imbued duration increased from +24% to +26%

- type: buff

- affected1: Superior Duration I Improved Spirit

- text: Health Regen increased from 2 to 3

- type: buff

- affected1: Improved Spirit

- text: Health increased from +75 to +100

- type: buff

- affected1: Improved Spirit I Improved Reach

- text: Spirit Resist increased from +10% to +12%

- type: buff

- affected1: Improved Reach I Curse

- text: Duration reduced from 3.5 to 3.25

- type: nerf

- affected1: Curse I Magic Carpet

- text: You are now unslowable while on the Magic Carpet

- type: buff

- affected1: Magic Carpet

- text: Cooldown reduced from 40s to 30s

- type: buff

- affected1: Magic Carpet

- text: Barriers now last for 16s

- type: change

- affected1: Magic Carpet I Echo Shard

- text: Now grants +8 Spirit Power

- type: buff

- affected1: Echo Shard I Escalating Exposure

- text: Base Spirit Resist reduction increased from -12% to -15%

- type: buff

- affected1: Escalating Exposure I Refresher

- text: Now grants +8% Bullet Resist

- type: buff

- affected1: Refresher I Boundless Spirit

- text: Sprint reduced from +4 to +3

- type: nerf

- affected1: Boundless Spirit

- text: Now grants +25% Weapon Damage

- type: change

- affected1: Boundless Spirit

## Heroes

- H Abrams

- text: Regeneration Time increased from 16s to 18s

- type: nerf

- affected1: Abrams

- affected2: Infernal Resilience

- text: Now does pull ups on the zipline once again

- type: buff

- affected1: Abrams

- type: fix

- text: Fixed sometimes not going to the area selected

- affected1: Abrams

- affected2: Seismic Impact

- text: Fixed sometimes stunning enemies on stairs

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge H Bebop

- text: Gun range increased from 30m to 32m

- type: buff

- affected1: Bebop

- text: now only targets enemies when used by default. If you use with alt cast (middle mouse) it will be ally only mode.

- type: change

- affected1: Bebop

- affected2: Hook

- text: can now be canceled by using Parry

- type: change

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: can now be canceled by using Parry

- type: change

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text: Fixed not traveling properly when cast near corners

- type: fix

- affected1: Dynamo

- affected2: Kinetic Pulse

- text: Gun damage reduced from 15 to 13

- type: nerf

- affected1: Dynamo

- text: cast time increased from 0.1 to 0.2

- type: nerf

- affected1: Dynamo

- affected2: Singularity

- text: range reduced from 9m to 8m

- type: nerf

- affected1: Dynamo

- affected2: Singularity H Grey Talon

- text: collision size reduced by 8%

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- text: base damage reduced from 105 to 100

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- text: T2 reduced from +70 to +65

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- text: Fire Rate now scales with Spirit (0.25)

- type: change

- affected1: Grey Talon

- text: Can now use multiple air dashes while using

- type: buff

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: root duration reduced from 2s to 1.25s

- type: nerf

- affected1: Grey Talon

- affected2: Immobilizing Trap

- text: now applies a 50% movement slow for 1 second after the root

- type: change

- affected1: Grey Talon

- affected2: Immobilizing Trap

- text: T2 changed from +1s Root to +2s Slow

- type: change

- affected1: Grey Talon

- affected2: Immobilizing Trap H Haze

- text: Base bullet damage increased from 5.3 to 5.6

- type: buff

- affected1: Haze

- text: impact damage happens immediately, rather than after the brief drowsy period

- type: change

- affected1: Haze

- affected2: Sleep Dagger

- text: drowsy period before sleep kicks in increased from 0.25 to 0.35

- type: nerf

- affected1: Haze

- affected2: Sleep Dagger

- text: cooldown reduced from 27s to 25s

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: radius reduced from 20m to 18m

- type: nerf

- affected1: Haze

- affected2: Smoke Bomb

- text: T2 max stacks increased from +30 to +40

- type: buff

- affected1: Haze

- affected2: Fixation

- text: now provides +2 Weapon Damage in the base ability (similar to the T1)

- type: change

- affected1: Haze

- affected2: Bullet Dance H Infernus

- text: Reduced vertical reach on dps

- type: nerf

- affected1: Infernus

- affected2: Flame Dash

- text: speed is now affected by slows

- type: change

- affected1: Infernus

- affected2: Flame Dash

- text: trail now gets wider with Ability Range bonus

- type: buff

- affected1: Infernus

- affected2: Flame Dash

- text: T1 duration reduced from 7s to 6s

- type: nerf

- affected1: Infernus

- affected2: Flame Dash

- text: Damage Amplification reduced from 30% to 25%

- type: nerf

- affected1: Infernus

- affected2: Catalyst

- text: T3 Damage Amplification increased from +10% to +15%

- type: buff

- affected1: Infernus

- affected2: Catalyst

- text: T2 reduced from +20% Lifesteal to +15%

- type: nerf

- affected1: Infernus

- affected2: Catalyst H Ivy

- text: Bullet damage growth per boon reduced from 0.55 to 0.5

- type: nerf

- affected1: Ivy

- text: Health growth per boon reduced from +41 to +35

- type: nerf

- affected1: Ivy

- text: T2 reduced from +3 m/s to +2

- type: nerf

- affected1: Ivy

- affected2: Watcher's Covenant

- text: no longer silences allies

- type: buff

- affected1: Ivy

- affected2: Air Drop

- text: now causes allies to deal 50% less damage while being carried

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text: movement adjusted to be a little less frantic

- type: change

- affected1: Ivy

- affected2: Air Drop

- text: Fixed bomb disappearing if you cancel your ultimate after dropping it but before it lands

- type: fix

- affected1: Ivy

- affected2: Air Drop

- text: self cast cast time increased from 1s to 2s

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text: max move speed reduced from 20 to 18

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text: During flight you can pitch up and down with Dash/Crouch buttons

- type: change

- affected1: Ivy

- affected2: Air Drop

- text: Fixed getting stuck under bridges and in buildings while flying

- type: fix

- affected1: Ivy

- affected2: Air Drop H Kelvin

- text: Bullet radius increased from 5 to 6

- type: buff

- affected1: Kelvin

- text: Base health growth per boon increased from +45 to +50

- type: buff

- affected1: Kelvin

- text: max slow increased from 60% to 80%

- type: buff

- affected1: Kelvin

- affected2: Arctic Beam

- text: now affects soul orbs (secures/denies them)

- type: change

- affected1: Kelvin

- affected2: Arctic Beam

- text: T3 range reduced from 15m to 13m

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: Fixed jitter

- type: fix

- affected1: Kelvin

- affected2: Ice Path

- text: T2 Heal increased from 135 to 145

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade H Lash

- text: Improved firing arm position to be a little bit more out of the way from the reticle

- type: change

- affected1: Lash

- text: no longer gives a stamina charge on use

- type: nerf

- affected1: Lash

- affected2: Grapple H Paradox

- text: Fixed still going through even if Paradox dies during it

- type: fix

- affected1: Paradox

- affected2: Paradoxical Swap H Pocket

- text: amp reduced from 8% to 7% per stack

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: Fixed amp visual not showing properly

- type: fix

- affected1: Pocket

- affected2: Barrage H Seven

- text: radius increased from 5m to 6m

- type: buff

- affected1: Seven

- affected2: Static Charge

- text: T2 radius increased from +7m to +8m

- type: buff

- affected1: Seven

- affected2: Static Charge

- text: spirit power scaling reduced from 1.1 to 0.8

- type: nerf

- affected1: Seven

- affected2: Storm Cloud

- text: time to reach maximum radius reduced from 6s to 3s

- type: buff

- affected1: Seven

- affected2: Storm Cloud

- text: Now provides +20% Bullet Resistance in the base ability

- type: buff

- affected1: Seven

- affected2: Storm Cloud H Shiv

- text: Bullet damage growth per boon reduced from 0.5 to 0.4

- type: nerf

- affected1: Shiv

- text: Gun falloff range reduced by 10%

- type: nerf

- affected1: Shiv

- text: Health growth per boon reduced from +41 to +35

- type: nerf

- affected1: Shiv

- text: T2 reduced from +100 to +85

- type: nerf

- affected1: Shiv

- affected2: Slice and Dice

- text: T3 now considers creeps for only half value

- type: nerf

- affected1: Shiv

- affected2: Slice and Dice

- text: deferred damage reduced from 35% to 30%

- type: nerf

- affected1: Shiv

- affected2: Bloodletting

- text: The targeting UI for Shiv's is now more clear about when the target will be killed

- type: change

- affected1: Shiv

- affected2: Killing Blow H Vindicta

- text: duration reduced from 2.25s to 2s

- type: nerf

- affected1: Vindicta

- affected2: Stake

- text: Spirit Power duration scaling reduced from 0.05 to 0.04

- type: nerf

- affected1: Vindicta

- affected2: Crow Familiar

- text: Fixed left clicks sometimes deselecting the ability when charges aren't ready

- type: fix

- affected1: Vindicta H Viscous

- text: Primary Fire redesigned to make it more usable and have improved damage and scaling

- type: change

- affected1: Viscous

- text: Now has an Alt Fire that has limited range, but deals AOE damage that cannot headshot

- type: change

- affected1: Viscous

- text: Spirit Scaling increased from 1.4 to 1.5

- type: buff

- affected1: Viscous

- affected2: Splatter

- text: Damage on 2nd and 3rd hit increased from 66% and 33% to 70% and 50%

- type: buff

- affected1: Viscous

- affected2: Splatter

- text: damage increased from 100% to 110% of Light Melee

- type: buff

- affected1: Viscous

- affected2: Puddle Punch

- text: T2 is now +50 damage and +20% movement slow (was -10s cooldown)

- type: change

- affected1: Viscous

- affected2: Puddle Punch

- text: T3 is now -12s cooldown (was +80 damage and +20% movement slow)

- type: change

- affected1: Viscous

- affected2: Puddle Punch

- text:: delay before punch increased from 0.25s to 0.35s

- type: nerf

- affected1: Viscous

- affected2: Puddle Punch

- text: Spirit Scaling increased from 1.05 to 1.3

- type: buff

- affected1: Viscous

- affected2: Goo Ball

- text: acceleration increased

- type: buff

- affected1: Viscous

- affected2: Goo Ball

- text: base turn radius and turn radius after bouncing has been increased

- type: change

- affected1: Viscous

- affected2: Goo Ball

- text: Fixed a bug where would have the direction and trail particle stuck on - type: fix

- affected1: Viscous

- affected2: Goo Ball H Warden

- text: Base movement speed reduced from 6.5 to 6

- type: nerf

- affected1: Warden

- text: Fire Rate scaling with spirit reduced from 0.375 Fire Rate per Spirit to 0.3

- type: nerf

- affected1: Warden H Yamato

- text: max damage time requirement reduced from 1.5s to 1.4s

- type: buff

- affected1: Yamato

- affected2: Power Slash

- text: collision radius reduced by 8%

- type: nerf

- affected1: Yamato

- affected2: Power Slash

- text: radius increased from 12m to 13m

- type: buff

- affected1: Yamato

- affected2: Crimson Slash

- text: Fixed being able to die during if hit by Grey Talon's Owl

- type: fix

- affected1: Yamato

- affected2: Shadow Transformation

- affected3: Grey Talon

- affected4: Owl

- text: Fixed some cases where could get into a stuck state

- type: fix

- affected1: Yamato

- affected2: Flying Strike

- text: Fixed some cases where would appear to be cast when it wasn't

- type: fix

- affected1: Yamato

- affected2: Crimson Slash
