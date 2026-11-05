---
title: "Patch/Playtest/2024-10-10"
pageid: 1090
source: liquipedia-deadlock-md
---

- name: Playtest - October 10 2024

- version: 2024-10-10

- highlight1: Ranked Mode is Released

- highlight2: Gameplay Updates

- highlight3: New Game Mode

- highlight4: New localizations

- highlight5: New Sounds

- highlight6: Item Updates

- highlight7: Hero Updates

- release: October 10, 2024

- previous: Patch/Playtest/2024-10-072024-10-07

- next: Patch/Playtest/2024-10-112024-10-11

## Ranked Mode

- text: Added [Ranked mode](Ranked mode.md)

- type: change

- affected1: Ranked_mode We are experimenting with a different approach to Ranked during early development, we expect to iterate on it in the future. The focus of this mode will be on concentrating players into specific time windows where they can opt into games where the primary focus is on game quality.

You must have 50 games played in order to enter this mode. If you have any behavior related restrictions (voice/text bans, report misuse, etc), you will be unable to queue into this mode.

The queue will be solo only at the moment and will be open from 1pm-4pm and 7pm-10pm in the respective time zones every day. Each region will have multiple time zones you can select from to find what best fits your schedule (you can only change your selection once per week). Players will be automatically assigned the server in that region that provides the best ping for the players in the match.

When in this mode, you will only be matched with players that have the same medal as you. There are 11 medals in total with 6 levels in each. Everyone's medal and levels will be displayed in these ranked games.

Every Tuesday at 8PM GMT we will run an algorithm that calculates everyone's performance together at the same time based on the games you've played, how the opponents you played against ended up faring in subsequent games, etc. As such, medals will only be updated once per week, to allow for analysis of a wide set of match data together at once for a more accurate review of your skill (rather than a fixed numerical addition/subtraction on a per game basis).

In order to make sure there are enough data to cross reference with other players, you must play at least 7 games in order to be eligible to receive a rank for that week. If at any time you didn't have 7 games played in the previous week, your medal will be marked as undefined until you play enough and earn a new medal the following Tuesday.

The ranked queue will first open next Tuesday, October 15th at 8PM GMT. The first medals will be granted globally the following Tuesday, October 22nd 8PM GMT. You'll have a panel that shows you the history of your previous medals.

## General

Added a 3rd casting mode, Quick Cast (shows range/radius/etc on key down, then on key up acts like Instant Cast). The three casting modes are now Instant Cast, Quick Cast, and Confirm Cast.

Added input buffering for ability usage (so if you cast an ability and then quickly cast another ability during its cast time, the next one will fire instead of the input being dropped) Now displaying a unique ID for builds in the description section of the build browser. You can click on it to copy the Build ID to the clipboard to share specific builds with friends.

If you enter a Build ID in the search box of the build browser, it will show all of the builds for the current hero by the author of that build.

For private lobbies, added the ability to swap players on both teams with a button press. In addition players can be randomly shuffled across the two teams, and if lanes are being assigned, can be shuffled within the teams.

Added "Allow Duplicate Heroes" setting in Private Lobbies Certain heroes now have a higher priority at being in dual lanes (Ivy and Dynamo atm) Added per-player voice volume slider (accessible by clicking on a player via the ESC menu) Pausing is no longer allowed in the first three minutes of the game Added

- th Thai and - id Indonesian localization

- text: Replaced the temp VO with a new translation spoken by a native actress

- type: change

- affected1: Yamato

- text: Added Stomp AoE range indication as the is about to use the ability

- type: change

- affected1: Walker Updated the way status effects are shown above the healthbar Fixed troopers being unreliable to shoot while on the zipline Fixed an Unsecured Souls bug where it gave extra bounty directly to the dying hero carrying unsecured souls Fixed AFK kick detection not working properly Added Crit Bonus Scale tooltip to the Weapon stats in the shop Fixed ESC key not working on the private lobbies page Fixed respawn music not playing while spectating another player Fixed a bug where the bot that would pick up the Urn was not the closest one, just the one that was in the highest player slot Fixed Streamer mode not persisting between game relaunches Keybinds in settings now selects the hero you're playing when you navigate to the Keybinds tab Rescue beam now shows heal indicator if you heal someone with it Fixed Debuff Reducer causing Teleporters to be faster Steam notifications moved to the top-left from the bottom-right, to avoid minimap overlap Continue to have mouse look enabled while M3 is pressed but before the ping wheel shows up Enabled Middle Mouse for "pinging" minimap Enabled the ability to middle mouse click players on the top bar

- text: Fixed's sometimes sending him into orbit

- type: fix

- affected1: Shiv

- text: Fixed's continuing to do damage while being teleported by Quantum Entanglement

- type: fix

- affected1: Shiv Fixed Quantum Entanglement's camera position anims not being smooth

- text:'s now also cancels when the target is out of world (like with Quantum Entanglement)

- type: fix

- affected1: Shiv Fixed Pausing not working when using hero specific key binds

- text:'s now has clearer visual states to indicate when someone is successfully locked in - type: fix

- affected1: Shiv

- text: Fixed some cases where's trap effects would be stuck in the world

- type: fix

- affected1: Grey Talon Updated ground strike preview cone to have a little more information on shape & outer bounds Abandon Match is now only an available option once you have disconnected from the game server. Bringing up the menu while connected to a game now gives you the option to Disconnect rather than Abandon immediately Fixed issues with Bots not using ziplines properly Added Return Fire proc sound Added Metal Skin proc sound

- text: Updated's sound

- type: fix

- affected1: McGinnis

- text: Added and death notification sound for all players

- type: fix

- affected1: Guardian

- affected2: Walker Improved panning resolution of bullet whizby sounds and shortened the max play distance to the local player Fixed hero death UI sound playing inconsistently Added bullet evasion sound effects

- text: Updated weapon fire audio

- type: fix

- affected1: Kelvin

- text: Updated weapon fire audio

- type: fix

- affected1: Infernus Improved clarity for hero roster selection VO

- text: laser animation updated slightly, raising the forearms to better reveal the eye socket weakpoint to players on the ground

- type: fix

- affected1: Wa;ler Re-enabled weapon-specific reload sounds

- text: fades to 50% opacity after initial start to improve visibility

- type: fix

- affected1: Abrams Added [Healing Rite](Healing Rite.md) cast sound Added [Rescue Beam](Rescue Beam.md) heal and pull loop sounds Added [Health Nova](Health Nova.md) cast sound Added [Return Fire](Return Fire.md) cast sound Revised [Metal Skin](Metal Skin.md) cast sound Added [Colossus](Colossus.md) cast and loop sounds Added echo to [Echo Shard](Echo Shard.md) cast sound Added [Silence Glyph](Silence Glyph.md) cast and hit sounds Added [Ammo Scavenger](Ammo Scavenger.md) proc sound Added [Restorative Shot](Restorative Shot.md) proc sound Added [Toxic Bullets](Toxic Bullets.md) proc variations Added a distance fade to [Soul Shredder Bullets](Soul Shredder Bullets.md) debuff effect and tweaked colors to reduce visual noise Improved visibility on [Spiritual Overflow](Spiritual Overflow.md) effects when heroes are airborne

- text: Reworked visual effects for - type: fix

- affected1: Viscous Updated "getting started" VO for the ability points tab to match the text Fixed a bunch of bugs that were impacting how VO was playing in a match. Now a bunch of hero VO that was previously getting squashed/cut off should play properly (for instance certain lines where allies commented on ability usage, the patrons giving compliments for assists/team healing, etc).

The patron once again will warn you when your Walkers are under attack The patron now will sometimes offer words of encouragement when you level up instead of when you destroy a Guardian or Walker Increased the time you need to carry the urn before the urn nags about not being delivered Fixed more instances of the wrong name for a hero being called out

- text: If you're or you can now ping during your ult to alert your allies

- type: fix

- affected1: Dynamo

- affected2: Mo & Krill

- text: still loves the Djinn, but he yells about them less frequently

- type: fix

- affected1: Mirage Added new custom charge and light melee and parry animations for Bebop Added improvements for meleeing while using Siphon Life (book now floats and hand makes a fist)

- text: Updated root effect for - type: fix

- affected1: Grey Talon

- text: Updated updated firing, projectile, impact effects

- type: fix

- affected1: Grey Talon

- text: Updated effects

- type: fix

- affected1: Grey Talon

- text: New heavy melee anims added to and - type: fix

- affected1: Mo & Krill

- affected2: Ivy Adjusted Trooper tracer and muzzle effects for better alignment and lower visual noise

- text: Adjusted to lower visual obstruction but increase awareness when it first latches

- type: fix

- affected1: Lady Geist

- text: effect revisions to help show range better

- type: fix

- affected1: Infernus

- text: death effects resolve quicker and more cleanly

- type: fix

- affected1: Trooper

- text: effects revisions to reduce noise on the victim and appear more clearly for Mirage

- type: fix

- affected1: Mirage Soul jar effect carry and dropoff revisions to reduce visual noise for carrier New Imports Building New Taxi Stand building Replaced old retaining wall Replaced block-in park bridges

## Gameplay

- text: attack range vs Lane reduced from 13.5m to 12m (they get closer to it)

- type: fix

- affected1: Trooper

- affected2: Guardian

- text: Players now need to be within 19m (above the ramp) to attack a Lane

- type: fix

- affected1: Guardian

- text: now take 70% less damage from at the start of the game; this reduces by 10% per minute (max at +30% increased damage at 10 min)

- type: fix

- affected1: Guardian

- affected2: Trooper

- text: damage vs players increased by 20%

- type: fix

- affected1: Guardian

- text: spawn time changed from 7 min to 5 min

- type: fix

- affected1: Denizen

- text: spawn time changed from 7 min to 8 min

- type: fix

- affected1: Denizen Teleporters open time changed from 10 min to 8 min

- text: pawn/bounty lane end time changed from 10 min to 8 min

- type: fix

- affected1: Trooper

- text: spawn time/interval changed from 10/5 to 8/4

- type: fix

- affected1: Sinner's Sacrifice

- text: [Golden Statues](Golden Statues.md) and [Breakables](Breakables.md) spawn time changed from 3 min to 2 min

- type: buff

- affected1: Golden Statue

- affected2: Breakables

- text: [Golden Statues](Golden Statues.md) bonuses upgrade time changed from 15 min to 10 min

- type: buff

- affected1: Golden Statue

- text: [Golden Statues](Golden Statues.md) Health buff increased from 15/20 to 20/30

- type: fix

- affected1: Golden Statue

- text: [Golden Statues](Golden Statues.md) now have a tier 3 upgrade at 25 minutes (+2.5% Fire Rate, +8% Ammo, 1.5% CD Reduction, +7% Weapon Damage, 40 Health, +5 Spirit Power)

- type: buff

- affected1: Golden Statue

- text: now has 15 regen

- type: fix

- affected1: Mid Boss

- text: creep buff rescaled from 70% to 50/70/90% for the 1/2/3rd mid boss death (further deaths don't increase)

- type: fix

- affected1: Mid Boss

- affected2: Rejuvenator

- text: rejuv respawn rescaled from 50% to 40/50/60% for the 1/2/3rd mid boss death (further deaths don't increase)

- type: fix

- affected1: Mid Boss

- affected2: Rejuvenator Urn now causes the runner to be revealed on the minimap Heavy Melee against the urn runner now causes them to drop the urn Urn delivery now gives each player on your team a Golden Statue permanent buff Urn bounty increased by 15% Urn now falls down from the sky a little bit faster Comeback formula weighted a bit less on team vs team net worth calculation and more on the strength of the dying hero (regardless of lead)

- text: Percentage of deniable orbs from objectives for /// rescaled from 54.55/66.67/100/0% to 35%

- type: buff

- affected1: Guardian

- affected2: Walker

- affected3: Patron

- affected4: Shrine Shields no longer reduce damage or get depleted by NPC units (Troopers, Bosses etc, but still takes damage from player summoned units) All heroes' movespeed increased by 0.3 (Enduring Speed reduced by 0.3) Bullet and Spirit Lifesteal now stack diminishingly Teleporters now grant +3 m/s for 5s after arriving at the other side Updated teleporter locations Moved teleporters to travel between outer lane Walkers Added teleporters in the underground tunnels Changed underground teleporters to go between Subway and Tunnel on the same side of the map Widened stairs from Shrines back to the player spawn area Added ledge to mantle back up to the player spawn area from the pit Added bridge and stair to the upper level of the Subway Entrance building from the outer lane Walker arenas Added upper level connection through the Subway Entrance building

- text: Moved back slightly further from stairs down to the canal

- type: change

- affected1: Guardian Widened channels surrounding Mid Temple slightly Widened archways between Mid Temple channels Garage and Night Club: Changed ropes so that they take you to the second floor and added back stairs to take you to the roof

## Items

- M Weapon I Monster Rounds

- text: Weapon Damage vs NPCs reduced from 35% to 30%

- type: nerf

- affected1: Monster Rounds I Restorative Shot

- text: Weapon Damage reduced from 8% to 7%

- type: nerf

- affected1: Restorative Shot I Basic Magazine

- text: Ammo increased from 24% to 26%

- type: buff

- affected1: Basic Magazine I Melee Charge

- text: Cooldown increased from 10.5s to 16s

- type: nerf

- affected1: Melee Charge I Long Range

- text: Ammo increase from 20% to 25%

- type: buff

- affected1: Long Range I Tesla Bullets

- text: Spirit scaling increased from 0.13 to 0.16

- type: buff

- affected1: Tesla Bullets I Alchemical Fire

- text: Now behaves like other grenades and does not bounce off walls

- type: change

- affected1: Alchemical Fire

- text: Base DPS increased from 45 to 55

- type: buff

- affected1: Alchemical Fire I Toxic Bullets

- text: Buildup is now 15% slower

- type: nerf

- affected1: Toxic Bullets I Frenzy

- text: Low HP threshold increased from 40% to 50%

- type: buff

- affected1: Frenzy I Ricochet

- text: Range reduced from 14m to 11m

- type: nerf

- affected1: Ricochet I Silencer

- text: Spirit Power increased from 12 to 18

- type: buff

- affected1: Silencer I Vampiric Burst

- text: Added ammo on active increased from +50% to +75%

- type: buff

- affected1: Vampiric Burst

- text: Cooldown reduced from 37s to 34s

- type: buff

- affected1: Vampiric Burst I Spiritual Overflow

- text: No longer grants +20% Fire Rate

- type: nerf

- affected1: Spiritual Overflow

- text: Upon full build-up, grants +35% Fire Rate

- type: buff

- affected1: Spiritual Overflow

- text: Activated Spirit Power increased from +45 to +50

- type: buff

- affected1: Spiritual Overflow M Spirit I Extra Spirit

- text: Spirit Power increased from 9 to 10

- type: buff

- affected1: Extra Spirit I Ammo Scavenger

- text: Spirit Power Per Soul reduced from 2 to 1

- type: nerf

- affected1: Ammo Scavenger

- text: Max Stacks increased from 10 to 20

- type: buff

- affected1: Ammo Scavenger I Withering Whip

- text: No longer grants +50 Health

- type: nerf

- affected1: Withering Whip

- text: Now grants +100 Bullet Shield

- type: buff

- affected1: Withering Whip

- text: Cooldown reduced from 26s to 22s

- type: buff

- affected1: Withering Whip I Cold Front

- text: Cooldown reduced from 34s to 28s

- type: buff

- affected1: Cold Front I Mystic Vulnerability

- text: Fixed it stacking with - type: fix

- affected1: Mystic Vulnerability I Slowing Hex

- text: Slow reduced from 30% to 25%

- type: nerf

- affected1: Slowing Hex I Improved Spirit

- text: Spirit Power increased from +23 to +28

- type: buff

- affected1: Improved Spirit I Improved Burst

- text: Max Health damage reduced from 9% to 7%

- type: nerf

- affected1: Improved Burst I Knockdown

- text: Cooldown reduced from 48s to 40s

- type: buff

- affected1: Knockdown I Ethereal Shift

- text: Can no longer end it early

- type: nerf

- affected1: Ethereal Shift I Torment Pulse

- text: Pulse interval is now fixed and does not get reduced with cooldown reduction

- type: nerf

- affected1: Torment Pulse I Superior Cooldown

- text: Now grants +100 Spirit Shield

- type: buff

- affected1: Superior Cooldown I Escalating Exposure

- text: Spirit Resist On Damage reduced from -15% to -12%

- type: nerf

- affected1: Escalating Exposure

- text: Amp Per Stack reduced from 6% to 5%

- type: nerf

- affected1: Escalating Exposure

- text: Duration reduced from 15s to 12s

- type: nerf

- affected1: Escalating Exposure I Refresher

- text: Cooldown increased from 212s to 230s

- type: nerf

- affected1: Refresher I Mystic Reverb

- text: Slow reduced from 50% to 40%

- type: nerf

- affected1: Mystic Reverb M Vitality I Healing Rite

- text: Regen duration increased from 17s to 19s (same total heal)

- type: nerf

- affected1: Healing Rite I Extra Regen

- text: Regen increased from 2.8 to 3

- type: buff

- affected1: Extra Regen

- text: Ammo increased from 8% to 10%

- type: buff

- affected1: Extra Regen I Extra Stamina

- text: Stamina Recovery increased from 14% to 16%

- type: buff

- affected1: Extra Stamina

- text: Fire Rate reduced from 7% to 6%

- type: nerf

- affected1: Extra Stamina

- text: Now gives +25 Health

- type: buff

- affected1: Extra Stamina I Extra Health

- text: Weapon Damage increased from 5% to 6%

- type: buff

- affected1: Extra Health I Enduring Speed

- text: Movespeed bonus reduced from 1.4 to 1.1 (all heroes movement speed increased by 0.3)

- type: nerf

- affected1: Enduring Speed

- text: Slow resist reduced from 40% to 35%

- type: nerf

- affected1: Enduring Speed I Restorative Locket

- text: Spirit Resist increased from 8% to 10%

- type: buff

- affected1: Restorative Locket

- text: Now grants +1 Sprint

- type: buff

- affected1: Restorative Locket I Return Fire

- text: Cooldown increased from 25s to 30s

- type: nerf

- affected1: Return Fire

- text: Active bullet resist reduced from 25% to 20%

- type: nerf

- affected1: Return Fire I Healing Nova

- text: Spirit Power increased from +4 to +6

- type: buff

- affected1: Health Nova I Combat Barrier

- text: Weapon Damage reduced from 25% to 22%

- type: nerf

- affected1: Combat Barrier I Fortitude

- text: Health increased from +300 to +325

- type: buff

- affected1: Fortitude I Lifestrike

- text: Heal increased from 55% of melee damage to 65%

- type: buff

- affected1: Lifestrike I Superior Stamina

- text: Stamina Recovery increased from 20% to 25%

- type: buff

- affected1: Superior Stamina I Veil Walker

- text: Speed increased from 3 to 4

- type: buff

- affected1: Veil Walker I Majestic Leap

- text: Cooldown increased from 23s to 26s

- type: nerf

- affected1: Majestic Leap I Rescue Beam

- text: Cast range reduced from 36m to 32m

- type: nerf

- affected1: Rescue Beam I Leech

- text: Weapon Damage increase from +15% to +20%

- type: buff

- affected1: Leech

- text: Spirit Power increased from +12 to +18

- type: buff

- affected1: Leech I Siphon Bullets

- text: HP Steal Per Bullet increased from 45 to 50

- type: buff

- affected1: Siphon Bullets

## Heroes

- H Abrams

- text: Base health reduced from 600 to 570

- type: nerf

- affected1: Abrams

- text: Health per boon increased from 32 to 34 (1048 vs 1046 total)

- type: buff

- affected1: Abrams

- text: Fixed sensitivity bugs that allowed you to turn more than intended

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge

- text: now allows for some very minor movement to help nudge around small objects

- type: buff

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: growth increased from 2.5% to 4% per stack

- type: buff

- affected1: Bebop

- affected2: Sticky Bomb

- text: now loses 2 stacks on death

- type: nerf

- affected1: Bebop

- affected2: Sticky Bomb

- text: now has 15 max stacks

- type: buff

- affected1: Bebop

- affected2: Sticky Bomb

- text: range increased from 25m to 30m

- type: buff

- affected1: Bebop

- affected2: Hook

- text: now also hits enemy, killing them instantly

- type: buff

- affected1: Bebop

- affected2: Hook

- text: Fixed some cases where would grab players from around corners

- type: fix

- affected1: Bebop

- affected2: Hook

- text: movement slow reduced from 30% to 25%

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam

- text: duration no longer scales with Spirit Power

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam

- text: duration increased from 8s to 10s

- type: buff

- affected1: Bebop

- affected2: Hyper Beam

- text: now applies a 15% Fire Rate slow in the landing radius for 5s. Scales with Spirit Power (0.2)

- type: buff

- affected1: Bebop

- affected2: Exploding Uppercut H Dynamo

- text: cooldown increased from 12.5s to 15s

- type: nerf

- affected1: Dynamo

- affected2: Quantum Entanglement

- text: T3 now also also reduces cooldown by 4s

- type: buff

- affected1: Dynamo

- affected2: Quantum Entanglement

- text: Fixed T2 tooltip to clarify that it affects bullets only and not melee damage

- type: fix

- affected1: Dynamo

- affected2: Kinetic Pulse H Grey Talon

- text: Arrow cycle time increased from 0.45s to 0.55s (overall dps unchanged)

- type: change

- affected1: Grey Talon

- text: Fixed alternate cast causing you to hit the ground soon after cast

- type: fix

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: Fixed colliding with nearby objects during cast

- type: fix

- affected1: Grey Talon

- affected2: Guided Owl

- text: Fire Rate no longer scales with Spirit Power

- type: nerf

- affected1: Grey Talon

- text: Base bullet damage now scales with Spirit Power (0.1)

- type: buff

- affected1: Grey Talon

- text: 3s grace period for kill increased to 4s

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: Fixed grace period still requiring that he gets the kill, rather than the target just die

- type: fix

- affected1: Grey Talon

- affected2: Guided Owl

- text: Movespeed no longer scales with Spirit Power

- type: nerf

- affected1: Grey Talon

- text: Base stamina increased from 3 to 4

- type: buff

- affected1: Grey Talon H Haze

- text: max stacks increased from 30 to 40

- type: buff

- affected1: Haze

- affected2: Fixation

- text: T3 reduced from +0.2 to +0.15

- type: nerf

- affected1: Haze

- affected2: Fixation

- text: no longer grants +15% Fire Rate

- type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: base ability now grants 2 Targets Hit Per Shot

- type: buff

- affected1: Haze

- affected2: Bullet Dance

- text: base ability no longer grants +25% Evasion

- type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: T3 now grants +40% Evasion and +2 Bullet Dance Speed

- type: nerf

- affected1: Haze

- affected2: Bullet Dance H Infernus

- text: Damage Amp reduced from 25% to 20%

- type: nerf

- affected1: Infernus

- affected2: Catalyst

- text: T3 Damage Amp increased from 15% to 20%

- type: nerf

- affected1: Infernus

- affected2: Catalyst H Ivy

- text: Improved default camera position

- type: fix

- affected1: Ivy

- text: Take Flight control keys are now similar to's

- type: fix

- affected1: Ivy

- text: Fixed some issues with control on Take Flight when near a wall

- type: fix

- affected1: Ivy H Lady Geist

- text: Fixed a bug that could cause some units to take more damage than intended with when multiple targets are hit

- type: fix

- affected1: Lady Geist

- affected2: Essence Bomb

- text: can now be alternate-casted on allied heroes

- type: fix

- affected1: Lady Geist

- affected2: Life Drain

- text: Added double tap accidental protection for to help against instant cancellations

- type: fix

- affected1: Lady Geist

- affected2: Life Drain

- text: slow duration reduced from 6s to 4s

- type: nerf

- affected1: Lady Geist

- affected2: Malice

- text: amp duration reduced from 16s to 13s

- type: nerf

- affected1: Lady Geist

- affected2: Malice

- text: You can now see how many stacks you have on you as the opponent

- type: fix

- affected1: Lady Geist

- affected2: Malice H Lash

- text: Base bullet damage reduced from 10 to 9

- type: nerf

- affected1: Lash

- text: Heal vs heroes reduced from 80% to 70%

- type: nerf

- affected1: Lash

- affected2: Flog

- text: Heal vs creeps reduced from 30% to 25%

- type: nerf

- affected1: Lash

- affected2: Flog H McGinnis

- text: No longer has +25% Spirit Resist

- type: nerf

- affected1: McGinnis

- text: Now has +15% Bullet Resist

- type: buff

- affected1: McGinnis

- text: T1 no longer grants +1 charge

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: duration reduced from 30s to 24s

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: cooldown reduced from 30s to 24s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: health scaling reduced from 30% to 20%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: recharge time reduced from 5s to 3s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: cast range increased from 15m to 20m

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: damage reduction against troopers/neutrals increased from -40% to -50%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: damage reduction against objectives increased from -60% to -70%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: Fixed [Ricochet](Ricochet.md) not bouncing off of - type: fix

- affected1: McGinnis

- affected2: Mini Turret

- text: spawn time reduced from 1s to 0.25s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: attack delay reduced from 0.35s to 0.2s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: radius increased from 4.5m to 5m

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage H Mirage

- text: now uses a range for its travel distance instead of a travel duration (scales with range increase)

- type: change

- affected1: Mirage

- affected2: Tornado

- text: Enemies that have already been hit by now let the next scarab projectile pass through them

- type: buff

- affected1: Mirage

- affected2: Fire Scarabs

- text: base damage reduced from 16 to 12

- type: nerf

- affected1: Mirage

- affected2: Djinn's Mark

- text: scaling from spirit power increased from 0.4 to 0.55

- type: buff

- affected1: Mirage

- affected2: Djinn's Mark

- text: reveal duration increased from 2s to 3s

- type: buff

- affected1: Mirage

- affected2: Djinn's Mark

- text: now causes your camera to move to the destination during the channel

- type: change

- affected1: Mirage

- affected2: Traveler

- text: T1 is now "+2 m/s" (was -20s cd)

- type: change

- affected1: Mirage

- affected2: Traveler

- text: T2 is now "-30s cd" (was +2 m/s)

- type: change

- affected1: Mirage

- affected2: Traveler

- text: T3 fire rate increased from 20% to 30%

- type: buff

- affected1: Mirage

- affected2: Traveler H Mo & Krill

- text: T1 now grants +30% Bullet Resist While Channeling (no longer grants -28s CD)

- type: change

- affected1: Mo & Krill

- affected2: Combo

- text: cooldown reduced from 95s to 75s

- type: buff

- affected1: Mo & Krill

- affected2: Combo H Paradox

- text: Bullet growth per boon increased from 0.33 to 0.45

- type: buff

- affected1: Paradox

- text: bullet duration reduced from 1s to 0.7s

- type: nerf

- affected1: Paradox

- affected2: Time Wall

- text: Fixed not being spawned when looking down while casting

- type: fix

- affected1: Paradox

- affected2: Time Wall

- text: cooldown increased from 48s to 65s

- type: nerf

- affected1: Paradox

- affected2: Paradoxical Swap

- text: range reduced from 30m to 25m

- type: nerf

- affected1: Paradox

- affected2: Paradoxical Swap

- text: T1 now reduces cooldown by 15s

- type: change

- affected1: Paradox

- affected2: Paradoxical Swap

- text: T3 now increases range by 20m

- type: change

- affected1: Paradox

- affected2: Paradoxical Swap

- text: radius reduced from 7m to 6m

- type: nerf

- affected1: Paradox

- affected2: Pulse Grenade

- text: Damage Amp per Stack increased from 5% to 6%

- type: buff

- affected1: Paradox

- affected2: Pulse Grenade

- text: T3 no longer increases Damage Amp by 2%

- type: nerf

- affected1: Paradox

- affected2: Pulse Grenade

- text: T3 now also increases the radius by 1m per pulse

- type: buff

- affected1: Paradox

- affected2: Pulse Grenade H Pocket

- text: Shotgun falloff start reduced from 22m to 16m

- type: nerf

- affected1: Pocket

- text: damage now respects line of sight

- type: fix

- affected1: Pocket

- affected2: Enchanter's Satchel

- text: now shows an aoe indicator for Pocket while channeling

- type: change

- affected1: Pocket

- affected2: Enchanter's Satchel

- text: DPS Spirit Power scaling reduced from 0.4 to 0.34

- type: nerf

- affected1: Pocket

- affected2: Affliction

- text: radius reduced from 6.5m to 4.5m

- type: nerf

- affected1: Pocket

- affected2: Barrage

- text: T3 now also increases radius by 2m

- type: buff

- affected1: Pocket

- affected2: Barrage H Seven

- text: Base regen increased from 1.5 to 3

- type: buff

- affected1: Seven

- text: Movespeed scaling with Spirit Power reduced from 0.028 to 0.02

- type: nerf

- affected1: Seven

- text: T3 increased from +1m to +2m

- type: buff

- affected1: Seven

- affected2: Lightning Ball H Shiv

- text: Spirit damage scaling increased from 1.2 to 1.3

- type: buff

- affected1: Shiv

- affected2: Slice and Dice

- text: T1 improved from -3.75s to -4s

- type: buff

- affected1: Shiv

- affected2: Slice and Dice

- text: Rage decay rate reduced from 0.35 to 0.25

- type: buff

- affected1: Shiv

- affected2: Rage

- text: Rage buffer duration increased from 7s to 12s (how long it stays before starting to decay)

- type: buff

- affected1: Shiv

- affected2: Rage H Vindicta

- text: Reverted recent falloff damage changes

- type: buff

- affected1: Vindicta

- text: Fall off increased from 58m (default) to 64m

- type: buff

- affected1: Vindicta

- text: Bullet damage growth per boon reduced from 0.79 to 0.55

- type: nerf

- affected1: Vindicta

- text: duration no longer scales with Spirit Power

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: T2 now increases flight duration by 6s

- type: buff

- affected1: Vindicta

- affected2: Flight

- text: bonus move speed above base now scales at 50% effectiveness

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: No longer has -10% base bullet resist

- type: nerf

- affected1: Vindicta

- text: Health growth per boon reduced from 20 to 15

- type: nerf

- affected1: Vindicta

- text: Gun cycle time increased from 0.22 to 0.26 (dps rescaled to remain the same, after the above changes are calculated in)

- type: nerf

- affected1: Vindicta

- text: duration reduced from 2s to 1.75s

- type: nerf

- affected1: Vindicta

- affected2: Stake

- text: bonus souls is now unsecured

- type: nerf

- affected1: Vindicta

- affected2: Assassinate

- text: Shooting while flying now has similar speed impact as on the ground

- type: nerf

- affected1: Vindicta

- text: air acceleration decreased a little

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: % damage no longer affects Mid Boss

- type: nerf

- affected1: Vindicta

- affected2: Crow Familiar H Viscous

- text: no longer triggers on hit effect while in Ethereal Shift

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: Fixed Superior Stamina dash count not working with - type: fix

- affected1: Viscous

- affected2: Goo Ball

- text: stun duration reduced from 1s to 0.7s

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text: base damage reduced from 100 to 90

- type: nerf

- affected1: Viscous

- affected2: Splatter

- text: T2 reduced from +70 to +60

- type: nerf

- affected1: Viscous

- affected2: Splatter

- text: Spirit damage scale increased from 1.5 to 1.9

- type: buff

- affected1: Viscous

- affected2: Splatter

- text: Fixed Instant Cast not working for - type: fix

- affected1: Viscous

- affected2: Puddle Punch H Warden

- text: cooldown reduced from 14s to 12s

- type: buff

- affected1: Warden

- affected2: Alchemical Flask

- text: damage increased from 55 to 65

- type: buff

- affected1: Warden

- affected2: Alchemical Flask

- text: T1 is now +1 Stamina Reduction

- type: change

- affected1: Warden

- affected2: Alchemical Flask

- text: T2 is now +50 Damage

- type: change

- affected1: Warden

- affected2: Alchemical Flask

- text: channel duration reduced from 2.2s to 2s

- type: buff

- affected1: Warden

- affected2: Last Stand

- text: range increased from 12m to 13m

- type: buff

- affected1: Warden

- affected2: Last Stand H Wraith

- text: spirit scale reduced from 1.2 to 1.1

- type: nerf

- affected1: Wraith

- affected2: Card Trick

- text: generation via melee reduced by 50%

- type: nerf

- affected1: Wraith

- affected2: Card Trick H Yamato

- text: cooldown increased from 8.5s to 10.5s

- type: nerf

- affected1: Yamato

- affected2: Power Slash

- text: T2 now also reduces cooldown by 2s

- type: buff

- affected1: Yamato

- affected2: Power Slash

- text: no longer grants you bullet and spirit resist

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation

- text: duration reduced from 4.5s to 4s

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation
