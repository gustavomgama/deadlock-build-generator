---
title: "Patch/Playtest/2024-09-26"
pageid: 962
source: liquipedia-deadlock-md
---

- name: Playtest - September 26 2024

- version: 2024-09-26

- release: September 26, 2024

- highlight1: New hero:

- highlight2: Gameplay Updates

- highlight3: Bug Fixes

- highlight4: New Server: South Africa

- highlight5: Map Updates

- highlight6: Item Updates

- highlight7: Hero Updates

- previous: Patch/Playtest/2024-09-192024-09-19

- next: Patch/Playtest/2024-09-272024-09-27

## General

Added a new hero, H Mirage Added an initial Anti-Cheat detection system. When a user is detected as cheating, during the game session the opponents will be given a choice between banning the user immediately and ending the match or turning the cheater into a frog for the rest of the game and then banning them afterwards. The system is set to conservative detection levels as we work on a v2 anti-cheat system that is more extensive. We will turn on the banning of users in a couple of days after the update is out. When a match is ended this way, the results will not count for other players.

Added global quickcast support. You can now configure your abilities and/or items to be on quickcast mode globally. You can also customize each ability individually to be quickcast or not. This also supports grenade style abilities.

Hero specific keybinds now say the ability name instead of ability 1-4 Added Zipline hotkey that can be independently bound from space/jump Fixed per-hero keys not inheriting user-defined default keys properly Added keybind indicator for hero-specific binds showing which keys have been bound for that hero Added Custom Match play mode Private lobbies now have an option to turn on cheats Private lobbies now let you select the specific servers to use Private lobbies now have an option to make the match publicly visible or private to only the players Private lobbies now support post-game and replays properly Private lobbies now allow picking specific lanes (solo and dual lane colors are displayed) Added a cheat report option in-game and post-game Can now mute and report enemy players using ESC while in-game Updated the game access invite UI to make it clear when users have been accepted (in most cases we look into where a user said their friend wasn't accepted, the user was actually accepted but they never claimed the game on the Steam notifications side) Added voice indicators for when players are speaking in party and team chat (green for party, white for team) Updated Player Card and action menu when clicking on a player in the friend list or ESC menu Fixed Rich Presence for Steam and in-game friend lists Party Code is now hidden when you enable Streamer Mode Added Region indicator to the matches on the watch tab Fixed search by MatchID not working for games that are live Added Spectator Fog of War toggle (hotkeys available in settings) Added

- za South Africa servers Added

- it Italian localization Instead of showing the total number of favorites for each build, we now tag popular builds using a mix of both recent and historical usage so that newer builds are easier to find Builds that haven't been updated in 30 days now have a distinct visual General rendering performance improvements Shadow quality improvements for higher shadow settings Fixed issues with player outline rendering in FSR2 Fixed regression with saturation volumes outline not showing up Displacement mapping no longer an official option and will likely be cut (it can be enabled with a ConVar after the game starts) Lighting improvements in map Picking up a powerup will now list all the stats they modify in the HUD instead of a generic name like 'Casting' or 'Gun' Spirit scaling is now always shown on the tooltips without needing to hold alt/tab Updated Viscous icon to look more different from Dynamo Added frosted shell effect on the rejuv crystal when Frozen Shelter is active Music and Sound effects will now pause during game pause

- text: Fixed trying to shoot people unsuccessfully behind cover

- type: fix

- affected1: Guardian Fixed Quicksilver Reload bonus damage not working correctly with things like Scorn and Flog Added timer sound to the last couple seconds of Flying Cloak Wall Jumps now use better animations to communicate directionality Fixed jumping between ziplines consuming stamina Fixed Magic Reverb not getting increased bonus damage from damage amps Improved preloading during queue time Updated Killing Blow effects Updated M Lightning Ball effects to reduce some visual noise Fixed some issues with Crimson Slash effect not appearing reliably H Viscous M Puddle Punch will now show a red preview for when the punch is out of range but within 2x of the cast range Fixed [Ricochet](Ricochet.md) not respecting LOS when picking the targets No longer play low ammo sounds when firing while sliding Fixed not being able to bind Reload to Mouse Wheel Up/Down Minimap line colors now match the color of the hero drawing them Fixed spectator keybinds not showing correctly Updated Flying Strike effects to reduce some visual noise Fixed Flex Slot unlock order not matching the usual order of unlocks Updated M Sleep Dagger projectile, impact and sleeping debuff visuals Fixed imbue and active abilities dialog not responding to keybinds if your ability/item binds included a modifier key or were bound to the mouse wheel Fixed H Dynamo not playing an animation during the cast delay on Singularity Updated bullet shield break effects Updated Unstoppable effects to be clearer at cast time Warp Stone: Casting while on the ground will no longer stop the player in place, will try to move forward along the ground instead Warp Stone: Fixed cases of Warp Stone getting caught on geometry Fixed various projectiles going through bosses (Wraith cards, Geist bombs, etc) Fixed Dash not always breaking breakables Breakables will now wait to spawn if a player is in the way H Abrams now has a new custom heavy melee animation Updated H Haze VO Fixed a bug where H Kelvin desperation VO for Arctic Beam and Ice Path were flipped Turned off a - H Shiv line where he referenced slowing down enemies when he wasn't actually doing so Removed reason 31 of why Lash is better than Bebop and replaced it with reason 26 of why Lash is better than Bebop (fixed a bug with Lash's hero select lines) Replaced a Grey Talon select line to make his intentions more clear H Infernus will no longer appear in every bot match Bots can now choose to play Lady Geist, Mirage, Shiv, and Warden Fixed min/max falloff range displaying incorrectly on Weapon Stats Tooltip

- text: Updated buff effect

- type: change

- affected1: Rejuvenator Updated wall bounce effects for Viscous in ball form Added citadel_give_gold cheat command Improved read on the connecting rope for Flying Strike and reduced visual obstruction of the ending slash Music bug fixes for replay and spectating Allow announcer lines for kill streaks and various hero lines to play while the player is in an active combat encounter Timing critical music and sfx will pause and resume in response to game pause

## Gameplay

Side lanes are now a little further apart from the middle lanes Added a First Blood bonus bounty for the first kill each player gets. Grants 150 bonus souls.

Lane setup is now always 1-2-2-1 Zipline Boost now starts on cooldown again

- text: damage reduction from reduced from 35% to 28% (they die a little faster to now)

- type: fix

- affected1: Guardian

- affected2: Trooper Trooper share radius reduced (from allied hero to allied hero 50m->40m, from orb to allied hero 40m->35m) Reverted recent creep sharing duplication changes (back to how it was over a week ago, we want to see if it's still an issue with the other changes in this patch) Some latency-related calculation improvements that help orbs be a little less deny favored Orbs now appear a little smaller to the enemy that is trying to deny them Added a Soul Generator (like the one in hero sandbox) in the respawn area. Starts spawning orbs at 3 minutes. Each orb is worth 10 souls when shot. (primary purpose for this is cases when you are very close to an item purchase) Fire Rate slows now stack diminishingly Rejuv bonus creep HP increased from 50% to 70% Rejuv bonus is no longer consumed for dead players, they have it on their next life now

- text: no longer give half bounty when base are destroyed for that lane

- type: change

- affected1: Guardian

- affected2: Trooper Killer to Assist bounty ratio reduced from 2.0 to 1.7 (slightly more to assists) Midgame respawn time increased a bit (reaches 50s at 20 min instead of 40s at 20 min) Teleporter delay reduced from 5s to 4s

- text: now deal 10% more damage to players

- type: buff

- affected1: Guardian M Sinner's Sacrifice now grants a permanent golden statue bonus when it is killed Fixed M Sinner's Sacrifice sharing bounty to nearby allies Added indicator on the hud to help track your passive cooldown items when they are 1s from ready (headshot Booster, Medic Bullets, etc) Boon count increased from 11 to 14 (added to 16/18/20k) Non-Health boon bonuses rescaled over the 14 levels (same total as before) Aggressive crouch spamming within a very narrow window will now cause you to very briefly move progressively slower Added Rejuv drop on a loop in the sandbox mode Added infinite ammo option to sandbox ("No Reload") Fixed dashing downwards not destroying breakables Silence now deselects your ability if you had it open when silenced

## Items

- M Weapon I Monster Rounds

- text: Bullet Resist vs NPCs reduced from 35% to 30%

- type: nerf

- affected1: Monster Rounds I High-Velocity Mag

- text: Bullet Velocity reduced from +30% to +25%

- type: nerf

- affected1: High-Velocity Mag I Restorative Shot

- text: Cooldown reduced from 6.2s to 5.5s

- type: buff

- affected1: Restorative Shot I Hollow Point Ward

- text: Spirit Shield increased from +85 to +95

- type: buff

- affected1: Hollow Point Ward I Headshot Booster

- text: Fire Rate reduced from +5% to +4%

- type: nerf

- affected1: Headshot Booster I Kinetic Dash

- text: Fire Rate reduced from 25% to 20%

- type: nerf

- affected1: Kinetic Dash

- text: Fire Rate max duration reduced from 8s to 7s

- type: nerf

- affected1: Kinetic Dash I Berserker

- text: Damage required per stack reduced from 110 to 100

- type: buff

- affected1: Berserker I Mystic Shot

- text: Damage spirit scaling increased from 0.6 to 0.8

- type: buff

- affected1: Mystic Shot I Melee Charge

- text: Impact now increases your ammo for that mag instead of reloading (so if your ammo is 2/8, it becomes 10/8). Reloads you instantly if in the middle of a reload.

- type: change

- affected1: Melee Charge

- text: Cooldown increased from 8.5s to 10s

- type: nerf

- affected1: Melee Charge I Intensifying Magazine

- text: Max Weapon Damage reduced from 75% to 60%

- type: nerf

- affected1: Intensifying Magazine I Escalating Resilience

- text: Fire Rate reduced from 14% to 12%

- type: nerf

- affected1: Escalating Resilience I Headhunter

- text: Now requires

- type: change

- affected1: Headhunter

- text: No longer grants +50% Bullet Velocity

- type: change

- affected1: Headhunter

- text: Now grants +5% Fire Rate

- type: change

- affected1: Headhunter

- text: Fixed not being affected by cooldown reduction

- type: fix

- affected1: Headhunter I Pristine Emblem

- text: Now requires

- type: change

- affected1: Pristine Emblem

- text: Now grants +35% Bullet Velocity

- type: buff

- affected1: Pristine Emblem I Titanic Magazine

- text: Ammo increased from 100% to 120%

- type: buff

- affected1: Titanic Magazine I Sharpshooter

- text: Fixed falloff reduction not working properly

- type: fix

- affected1: Sharpshooter I Frenzy

- text: Low HP Spirit Resist changed to Bullet Resist

- type: change

- affected1: Frenzy I Spiritual Overflow

- text: Now grants +250 Bullet Shield

- type: buff

- affected1: Spiritual Overflow I Silencer

- text: Now grants +12 Spirit

- type: buff

- affected1: Silencer I Ricochet

- text: Fire Rate reduced from 12% to 10%

- type: buff

- affected1: Ricochet I Vampiric Burst

- text: Fixed casting it interrupting sliding

- type: fix

- affected1: Vampiric Burst I Siphon Bullets

- text: Moved to T4 Vitality

- type: change

- affected1: Siphon Bullets I Shadow Weave

- text: Now a T4 Weapon Item

- type: change

- affected1: Shadow Weave M Spirit I Ammo Scavenger

- text: Ammo reduced from 15% to 10%

- type: nerf

- affected1: Ammo Scavenger

- text: Health reduced from 60 to 40

- type: nerf

- affected1: Ammo Scavenger

- text: Duration reduced from 35s to 30s

- type: nerf

- affected1: Ammo Scavenger

- text: Max stacks reduced from 12 to 10

- type: nerf

- affected1: Ammo Scavenger I Spirit Strike

- text: No longer grants +0.8 Health Regen

- type: nerf

- affected1: Spirit Strike I Mystic Reach

- text: Ability Range increased from 16% to 18%

- type: buff

- affected1: Mystic Reach

- text: Now provides 6% Bullet Resist instead of 6% Spirit Resist

- type: change

- affected1: Mystic Reach I Withering Whip

- text: No longer grants +8% Fire Rate

- type: nerf

- affected1: Withering Whip

- text: Spirit Power increased from +4 to +6

- type: buff

- affected1: Withering Whip

- text: Now grants +1 Sprint

- type: buff

- affected1: Withering Whip

- text: Cast range increased from 24m to 30m

- type: buff

- affected1: Withering Whip

- text: Fire Rate slow increased from 40% to 45%

- type: buff

- affected1: Withering Whip I Quicksilver Reload

- text: No longer triggers if your ammo is at max value already

- type: fix

- affected1: Quicksilver Reload I Decay

- text: Cooldown increased from 32s to 45s

- type: nerf

- affected1: Decay

- text: Cast range scaling reduced from 0.2 to 0.16

- type: nerf

- affected1: Decay I Improved Reach

- text: Now provides 12% Bullet Resist instead of 12% Spirit Resist

- type: change

- affected1: Improved Reach

- text: Spirit Power increased from +21 to +23

- type: buff

- affected1: Improved Reach I Knockdown

- text: Now causes enemies to fall down faster

- type: buff

- affected1: Knockdown I Torment Pulse

- text: Health Bonus increased from 140 to 160

- type: buff

- affected1: Torment Pulse

- text: Spirit Power damage scaling increased from 0.25 to 0.33

- type: buff

- affected1: Torment Pulse I Rapid Recharge

- text: Faster Time Between Charges increased from +55% to +65%

- type: buff

- affected1: Rapid Recharge

- text: Cooldown Reduction For Charged Abilities increased from +25% to 30%

- type: buff

- affected1: Rapid Recharge I Magic Carpet

- text: Fixed it consuming stamina when jumping off

- type: fix

- affected1: Magic Carpet I Escalating Exposure

- text: Fixed the bonus damage being reduced twice by resistance

- type: fix

- affected1: Escalating Exposure I Refresher

- text: Bullet Resist increased from 8% to 16%

- type: buff

- affected1: Refresher

- text: Spirit Resist reduced from 16% to 8%

- type: nerf

- affected1: Refresher I Echo Shard

- text: Now has a 0.3s cast delay (like )

- type: change

- affected1: Echo Shard M Vitality I Melee Lifesteal

- text: Melee Damage reduced from 13% to 12%

- type: nerf

- affected1: Melee Lifesteal

- text: Heal vs non-heroes reduced from 40% to 30%

- type: nerf

- affected1: Melee Lifesteal I Extra Stamina

- text: Stamina Recovery increased from 10% to 14%

- type: buff

- affected1: Extra Stamina I Restorative Locket

- text: No longer requires max stacks to restore a stamina point

- type: buff

- affected1: Restorative Locket I Divine Barrier

- text: Bonus Health reduced from 75 to 50

- type: nerf

- affected1: Divine Barrier I Combat Barrier

- text: Fire Rate while shielded reduced from 8% to 6%

- type: nerf

- affected1: Combat Barrier

- text: Weapon Damage while shielded reduced from 28% to 25%

- type: nerf

- affected1: Combat Barrier

- text: Bullet Shield increased from +300 to +325

- type: buff

- affected1: Combat Barrier I Healing Nova

- text: Weapon Damage increased from 10% to 12%

- type: buff

- affected1: Health Nova I Return Fire

- text: While active grants +25% Bullet Resistance

- type: buff

- affected1: Return Fire

- text: Bullet Damage Returned reduced from 70% to 60%

- type: nerf

- affected1: Return Fire

- text: No longer grants +7% Fire Rate

- type: nerf

- affected1: Return Fire

- text: Spirit Power increased from +7 to +9

- type: buff

- affected1: Return Fire

- text: Fixed Ricochet'd bullets not returning the right amount of damage

- type: fix

- affected1: Return Fire I Bullet Armor

- text: Bullet Resist increased from 20% to 25%

- type: buff

- affected1: Bullet Armor I Veil Walker

- text: No longer grants +20% Fire Rate

- type: nerf

- affected1: Veil Walker I Improved Bullet Armor

- text: Bullet Resist increased from 45% to 50%

- type: buff

- affected1: Improved Bullet Armor I Fortitude

- text: Bonus Health increased from 275 to 300

- type: buff

- affected1: Fortitude I Lifestrike

- text: Cooldown reduced from 5.25s to 5s

- type: buff

- affected1: Lifestrike

- text: Fixed proccing heal more than once when hitting multiple targets

- type: fix

- affected1: Lifestrike I Shadow Weave

- text: Moved to T4 Weapon

- type: change

- affected1: Shadow Weave I Siphon Bullets

- text: Now a T4 Vitality Item

- type: change

- affected1: Siphon Bullets

- text: No longer grants +28% Weapon Damage

- type: change

- affected1: Siphon Bullets

- text: Now grants +18% Bullet Resistance

- type: change

- affected1: Siphon Bullets I Colossus

- text: Slow radius increased from 12m to 14m

- type: buff

- affected1: Colossus I Soul Rebirth

- text: Increases base respawn rate by +15s

- type: buff

- affected1: Soul Rebirth I Unstoppable

- text: Can no longer be cast during channels

- type: nerf

- affected1: Unstoppable

## Heroes

- H Abrams

- text: reduced from 16% to 15%

- type: nerf

- affected1: Abrams

- affected2: Infernal Resilience

- text: T3 reduced from 9% to 8%

- type: nerf

- affected1: Abrams

- affected2: Infernal Resilience

- text: spirit scaling increased from 0.2 to 0.3

- type: buff

- affected1: Abrams

- affected2: Siphon Life

- text: Fixed Cases where was unexpectedly'slamming' in to walls and stairs

- type: fix

- affected1: Abrams

- affected2: Shoulder Charge H Bebop

- text: range reduced from 30m to 25m

- type: nerf

- affected1: Bebop

- affected2: Hook

- text: duration spirit scaling reduced from 0.08 to 0.06

- type: nerf

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: radius reduced from 8m to 7m

- type: nerf

- affected1: Dynamo

- affected2: Singularity H Grey Talon

- text: Arrow cycle time reduced from 0.4s to 0.45s (overall dps unchanged)

- type: change

- affected1: Grey Talon

- text: can be alternate-casted to remain near the ground

- type: change

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: Fixed air dash during going half the distance

- type: fix

- affected1: Grey Talon

- affected2: Rain of Arrows

- text: bonus spirit on death now has a 3s buffer window

- type: change

- affected1: Grey Talon

- affected2: Guided Owl

- text: very slight turn rate improvements

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: radius increased from 12m to 13m

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: hitbox reduced by 10%

- type: nerf

- affected1: Haze

- affected2: Sleep Dagger

- text: Fixed refresher not working properly with - type: fix

- affected1: Haze

- affected2: Smoke Bomb

- text: Fixed some items that didn't proc before: Tesla Bullets, Lucky Shot, Mystic Shot

- type: fix

- affected1: Haze

- text: now more accurately shows who it is shooting

- type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: Fixed sometimes not obeying line of sight accurately

- type: fix

- affected1: Haze

- affected2: Bullet Dance

- text: bullets are now affected by - type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: evasion reduced from 50% to 25%

- type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: fire rate reduced from 25% to 15%

- type: nerf

- affected1: Haze

- affected2: Bullet Dance H Ivy

- text: now works against airborne targets

- type: buff

- affected1: Ivy

- affected2: Stone Form

- text: T3 now also grants +2m Radius

- type: buff

- affected1: Ivy

- affected2: Kudzu Bomb

- text: spirit power scaling increased from 0.6 to 0.7s

- type: buff

- affected1: Ivy

- affected2: Kudzu Bomb

- text: Fixed clicking noise when flying while disarmed

- type: fix

- affected1: Ivy

- text: Fixed being able to during the Take Flight animation to circumvent the vulnerable cast period

- type: fix

- affected1: Ivy

- affected2: Stone Form H Kelvin

- text: Headshot bonus damage reduced by 20%

- type: nerf

- affected1: Kelvin

- text: Bullet damage growth reduced from 1.2 to 0.9

- type: nerf

- affected1: Kelvin

- text: movement slow reduced from 70% to 50%

- type: nerf

- affected1: Kelvin

- affected2: Arctic Beam

- text: Moving through breakables while on now destroys them

- type: buff

- affected1: Kelvin

- affected2: Ice Path H Lady Geist

- text: cooldown reduced from 42s to 30s

- type: buff

- affected1: Lady Geist

- affected2: Life Drain

- text: cooldown reduced from 6.25s to 6s

- type: buff

- affected1: Lady Geist

- affected2: Malice

- text: T1 improved from -2.75s Cooldown to -3s

- type: buff

- affected1: Lady Geist

- affected2: Malice

- text: Fixed not healing extra based on amplifications (like Soul Shredder and stacks)

- type: fix

- affected1: Lady Geist

- affected2: Life Drain

- text: Sprint increased from 1 to 1.5

- type: buff

- affected1: Lady Geist H McGinnis

- text: Fixed looking up circumventing the min range on and - type: buff

- affected1: McGinnis

- affected2: Spectral Wall

- affected3: Heavy Barrage

- text: Can now cast parry to cancel your ult ()

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage

- text: Fixed various issues with indoors and near walls spawning the wrong number of segments

- type: fix

- affected1: McGinnis

- affected2: Spectral Wall H Mo & Krill Mo and Krill

- text: duration reduced from 2.75s to 2.5s

- type: nerf

- affected1: Mo & Krill

- affected2: Combo

- text: damage spirit scaling increased from 0.8 to 1.1

- type: buff

- affected1: Mo & Krill

- affected2: Combo

- text: kill trigger now has a 3s buffer window to get credit

- type: change

- affected1: Mo & Krill

- affected2: Combo

- text: T1 reduced from +1.5s to +1s

- type: nerf

- affected1: Mo & Krill

- affected2: Sand Blast

- text: range increased from 30m to 35m

- type: buff

- affected1: Mo & Krill

- affected2: Sand Blast

- text: base speed increased from 3 to 4

- type: buff

- affected1: Mo & Krill

- affected2: Burrow

- text: T3 speed reduced from +3 to +2

- type: nerf

- affected1: Mo & Krill

- affected2: Burrow H Paradox

- text: T3 now also grants +2% Damage Amp

- type: buff

- affected1: Paradox

- affected2: Pulse Grenade

- text: Fixed being unable to be damaged by multiple s

- type: fix

- affected1: Paradox

- affected2: Time Wall H Pocket

- text: no longer goes through walls, now respects line of sight

- type: nerf

- affected1: Pocket

- affected2: Affliction

- text: T3 reduced from +5% to +4%

- type: nerf

- affected1: Pocket

- affected2: Barrage H Seven

- text: stun duration reduced from 1.1 to 0.9

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: T3 reduced from 1.1 to 0.9

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: radius reduced from 6m to 5m

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: can now be alternate-casted on self (does not stun you)

- type: buff

- affected1: Seven

- affected2: Static Charge

- text: now respects line of sight

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: T3 now also gives +1m Radius

- type: buff

- affected1: Seven

- affected2: Lightning Ball H Shiv

- text: T2 reduced from +85 to +75

- type: nerf

- affected1: Shiv

- affected2: Slice and Dice

- text: Rage buildup per spirit damage reduced from 0.02 to 0.013

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text: Rage drain rate increased from 0.3 to 0.35

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text: Full Rage Bonus Damage reduced from 20% to 15%

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text: T2 increased from 5% to 10%

- type: buff

- affected1: Shiv

- affected2: Killing Blow H Vindicta

- text: Gun cycle time increased from 0.19s to 0.22s (same overall dps)

- type: nerf

- affected1: Vindicta

- text: distance enemies are allowed to move increased from 6m to 8m

- type: nerf

- affected1: Vindicta

- affected2: Stake

- text: Max Falloff reduced from 58m to 45m

- type: nerf

- affected1: Vindicta

- text: Fixed ending if you touch the ground

- type: fix

- affected1: Vindicta

- affected2: Flight

- text: Low HP indication now also shows up while unscoped

- type: fix

- affected1: Vindicta

- text: Base damage reduced from 160 to 140

- type: nerf

- affected1: Vindicta

- affected2: Assassinate

- text: Zoom level reduced a little bit

- type: change

- affected1: Vindicta

- affected2: Assassinate

- text: duration spirit scaling reduced from 0.2 to 0.15

- type: nerf

- affected1: Vindicta

- affected2: Flight H Viscous

- text: cleanse is now part of the T2

- type: nerf

- affected1: Viscous

- affected2: The Cube

- text: enemy warning time increased from 0.35s to 0.45s

- type: nerf

- affected1: Viscous

- affected2: Puddle Punch

- text: Bullet Damage reduced from 13 to 12

- type: nerf

- affected1: Viscous

- text: Can now use down dash during

- type: buff

- affected1: Viscous

- affected2: Goo Ball

- text: Fixed Phantom Strike not positioning you correctly when using it with your

- type: fix

- affected1: Viscous

- affected2: Goo Ball

- text: post cast delay reduced from 0.5s to 0.2s

- type: buff

- affected1: Viscous

- affected2: Splatter H Warden

- text: escape range and escape time increased by 15%

- type: nerf

- affected1: Warden

- affected2: Binding Word

- text: spirit scaling increased from 0.9 to 1.2

- type: buff

- affected1: Warden

- affected2: Last Stand H Yamato

- text: Bullet damage growth reduced from 0.5 to 0.45

- type: nerf

- affected1: Yamato

- text: fire rate slow reduced from 30% to 20%

- type: nerf

- affected1: Yamato

- affected2: Crimson Slash

- text: Fixed various issues with pathing

- type: fix

- affected1: Yamato

- affected2: Flying Strike

- text: duration reduced from 5s to 4.5s

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation

- text: T3 duration increased from +1.5s to +2s

- type: buff

- affected1: Yamato

- affected2: Shadow Transformation

- text: no longer provides unlimited ammo

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation

## Map Changes

Outer lanes at the middle of the map pushed further away from the inner lanes Added connection from canal near the urn platforms through the Radio Station and Apartment buildings Reworked interior corridors of Fish Market/Nursery to exit to the buildings sooner Added interior room partition from the Fish Market/Nursery to the Shops Moved rope to the Fish Market/Nursery rooftop to the back of the building Removed upper interior hallway from rope to the Fish Market/Nursery rooftops Moved truck from in front of archway with cosmic veil to the back of the Fish Market/Nursery Redesigned outer lane path (ziplines and trooper nodes) from Walker to Guardian on Amber Yellow and Sapphire Purple Added interior passage beside Subway Entrance to the outer lanes
