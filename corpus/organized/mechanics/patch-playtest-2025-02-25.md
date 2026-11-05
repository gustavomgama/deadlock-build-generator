---
title: "Patch/Playtest/2025-02-25"
pageid: 2162
source: liquipedia-deadlock-md
---

- name: Map Rework Update

- version: 2025-02-25

- highlight1: Map Rework (3 Lanes) & Explore Map Feature

- highlight2: Soul Orb Mechanic Changes

- highlight3: Sprint System Update

- highlight4: General Gameplay & Economy Adjustments

- highlight5: Hero Updates & Content Improvements

- highlight6: Item Updates & Content Improvements

- release: February 25, 2025

- previous: Patch/Playtest/2025-02-112025-02-11

- next: Patch/Playtest/2025-03-132025-03-13

- footnotes: Source: [Map Rework Update](https://store.steampowered.com/news/app/1422450/view/530965072572320687) Today's update introduces a reworked map layout, alongside a variety of improvements and bug fixes.

## Map Rework

The map has been redesigned around being 3 lanes rather than 4. This has a large range of accompanying map-wide changes regarding visuals, building layouts, pathways, neutral camps, air vents, breakables, powerup buffs, juke spots, mid boss, etc.

Added a new feature called "Explore Map" where you can run around an empty city to test movement and navigation. You can find this under the 'Play' menu.

## Gameplay Changes

1. Soul Orb Mechanics

- text: no longer need to be last hit by a player in order to generate s, as long as you are nearby. Troopers no longer have the "near death" flashing behavior.

- type: change

- affected1: Trooper

- affected2: Soul Orb

- text: lifetime in the air reduced significantly.

- type: change

- affected1: Soul Orb

- text: denies changed from 65/35% to 50/50%.

- type: change

- affected1: Soul Orb

- text: physical radius increased by 10%.

- type: buff

- affected1: Soul Orb

- text: Reduced horizontal movement of s from. (Note: Duplicate entry in source)

- type: change

- affected1: Soul Orb

- affected2: Trooper 1. Sprint Default sprint speed increased from 0.5 to 1.0.

Sprint disable duration reduced from 5s to 4s when dealing/taking damage with heroes.

Sprint disable duration reduced from 5s to 0.5s when dealing/taking damage with non-heroes.

1. Sinner's Sacrifice

- text: no longer grants a random Golden Statue buff.

- type: change

- affected1: Sinner's Sacrifice

- text: now has a looping timing window where if you kill it with a Heavy Melee (visual/audio cues provided), you receive 3 Golden Statue buffs. Last hitting with Light Melee grants 1 Golden Statue

- type: change

- affected1: Sinner's Sacrifice 1. Economy & Objectives

- text: Increased post-laning bounty to match the previous 4 lane global economy.

- type: buff

- affected1: Trooper Changed flex slot requirements: 1st flex slot changed from 3 M Guardian s down to 2 M Guardian s.

2nd flex slot changed from 2 M Walker s down to 1 M Walker.

The last 2 flex slots are unchanged.

Small Camp respawn time reduced from 4 minutes to 3 minutes.

Mid Camp respawn time reduced from 6 minutes to 5 minutes.

Neutral Creeps soul values reduced by 10% (overall camp count and frequency has been increased).

- text: Side s HP increased from 5,175 to 7,000.

- type: buff

- affected1: Walker

- text: Mid s HP increased from 8,000 to 9,000.

- type: buff

- affected1: Walker Mid Boss HP and HP growth increased by 30% Outer Zipline speed increased by 15%.

Breakable soul values reduced by 5%.

Gun Powerup min/max Fire Rate increased from 10/30% to 15/35%.

Gun Powerup not scaling Ammo to 60% as intended.

The new large amount of breakables in the Mid Boss middle area now initially spawn at the same time as Mid Boss.

1. Misc Gameplay All juke spots now have veils (the dead end closets with the mystery man in front).

Players no longer collide with Bosses to prevent some unintended interactions.

Crouch toggle now ends on a failed dash.

Adjusted what counts as a headshot when shooting through non-head hitboxes.

Reduce duration of buff effect for gaining Ability Points.

Players can no longer shoot or reload their weapon while climbing a Rope.

## Technical & Performance

Added support for DLSS as an FSR2 alternative for temporal anti aliasing and upscaling (requires NVIDIA 2x-class GPU or above).

For Vulkan users, upgraded FSR2 to AMD's new FSR3 temporal upscaler.

Enabled NVIDIA Reflex and AMD Anti-Lag 2.0 for reduced latency.

Client performance improvements.

Bicubic filtering for lightmaps at higher shadow quality settings.

Improve how we preload units to prevent shader compilation during gameplay.

Hero shader improvements.

Various netcode improvements: Increased tick rate from 60hz to 64hz.

Improved client reporting to prevent incorrect prediction offsets.

Improved accuracy of server lag compensation for hit detection.

Improved timing of server lag compensation for bullet origin points.

Improved accuracy of - M Soul Orb hitboxes for client prediction.

- text: Improved various close range abilities having casting errors (,,, etc).

- type: fix

- affected1: Bebop

- affected2: Lady Geist

- affected3: Mo & Krill

## User Interface

1. Damage Report Now visualizes the amount of damage reduced by resistances or shields.

Incoming Damage UI now visualizes general damage reduction and amplification.

Now shows the number of instances of damage done by each ability.

Damage Report no longer clears immediately upon respawn (keeps data from last life with label).

Breaking secondary stats out (e.g., H Shiv M Serrated Knives initial hit vs DoT).

Defaulting damage report to compact mode when initially taking damage.

A variety of UI bugfixes and polish changes.

1. Quick Buy Added the ability to right click on the header of a build category to add all items in that category to your Quickbuy queue.

Quickbuy's default behavior reverted to showing purchase prompts when the item is purchased (Settings option added to show prompt when queued).

Fixed a bug where you could queue an item that was a component of an item you already own.

Fixed several bugs that caused items to be skipped when purchasing items with the Auto Buy option enabled.

1. Builds/Shop Fixed a bug where purchasing an item would clear the item search box in the shop.

Fixed Steam profanity filter not being consistently applied to user-authored text in builds.

You can now create builds on the dashboard.

You can now create ability builds by clicking on the ability icons in the skill build area (also available on dashboard).

Fixed a bug where dragging and dropping items while editing a build would remove the annotation from the item.

Reworking default builds to assume items are bought in specified order.

Updated Hero default builds.

Added Suggested AP path for - H Haze, H Paradox, H Shiv, and - H Yamato.

1. General UI Changed all language around 'Hero Sandbox' to 'Hero Testing'.

Moved Private and Co-op bots under a single "Play Bot Match" button.

Added a News Post popup panel to the main menu.

Added a link to Patch Notes to the main menu.

Commends are now right-aligned.

Enemy commends now auto-dismiss after a short duration.

Fixed both "Leave Match" and "Leave Spectating" showing when hitting Esc while watching a match.

Fixed a bug where abilities showed their imbued item multiple times.

Added Status Effect Panels next to healthbar and bottom left (hoverable).

Added M Rejuvenator icon in the bottom left when held.

Added powerups to the bottom left HUD area, removing the middle left progress bar.

Added player speaking indicator on the minimap icon.

Changed default minimap values (smaller ziplines, player icon adjustments).

Added Health regen to active player stats on the left.

Updating images on the Zipline prompt UI to match new colors.

Fixing wash-color on new inline glyphs for active items.

Adding logic to make default build categories double height when they go over 9 items.

Matches that are safe to abandon now use the "Leave Match" label instead of "Abandon Match".

Settings for Custom Matches now default to whatever was last used.

Added a new Mid Boss M Rejuvenator Symbol with three visual states (not spawned, under 1 min, spawned).

## General Updates

Ziplines are now curved.

If a player abandons a match before 5 minutes, a message "This game will not be scored. It is now safe to leave." appears. After 5 minutes, the message is "This match can be abandoned without a penalty, but leaving will result in a loss.".

Updated the Heavy Melee vfx.

Gun audio system updates and early reflection acoustics experiments.

Updated regular damage and headshot damage sounds; NPC damage sounds are quieter.

Added positional tier 1 M Guardian death sounds.

Added sounds for tier 1 M Guardian melee swing, slam, hit, activate/deactivate.

Added positional M Walker death sounds.

Added sounds for - M Walker beam, stomp, and rocket barrage attacks.

Reduce duration of buff effect for gaining Ability Points.

Button hints now update when changing keybinds during a match.

Made bots better at purchasing and upgrading items.

Made bots better at not getting stuck in walls.

Added row indicator and auto-scroll for global leaderboards.

Taskbar icon only flashes once when about to respawn.

The - M Walker's area buff now shows up on the hud's active stats section.

Added support for pinging Ability 1-4 as "almost ready" with supporting VO.

Hooked up generic "Item is Ready", "Item is almost Ready", and "Item is on cooldown" VO.

Added missing unique death VO sounds for: H Fathom, H Trapper, H Wrecker, H Raven, H The Magnificent Sinclair, and - H Wraith.

Updated "many souls" VO lines to trigger at 6k souls instead of 6.2k.

Base attack music now starts immediately when an enemy enters the local player's base.

Damage audio does not play loudly if the player's health is not changing.

Elevated ability hit confirmation sounds in the mix.

Mix updates to deprioritize NPC, currency, and other sounds in base.

Protections added against low audio frequencies buildup.

Updated volume for - H Paradox and - H Viscous ' Select/Unselect lines.

"You can't hide from me" VO lines now only play for the speaker.

At match start, certain heroes will now chat with each other; otherwise, the patron speaks.

Minor VO bug fixes (missing lines, wrong names in pings, etc.).

Ping Update: Pre-match, pressing ping plays a random taunt (not all heroes yet).

Ping Update: New ping wheel options added for certain heroes (Come with me, Rejuv's Dropping, Cover Me, etc.).

Ping Update: Green lane is now alternatively referred to as "Park".

Added an effect for breaking bridge Powerups.

Sprint effects revisions to reduce noise.

Window materials updated (imposter interiors, improved reflections).

Added new signage, railing smartprop, oracle building model, city backdrop buildings.

Added under construction suspension bridge to yellow lane.

Improved blending of character and world shadows.

Improved lighting on city backdrop.

Added Bull/Bear statues to the jungle lane street.

Ability Point effects revisions to reduce lingering noise.

Powerup spawner effects revisions to reduce lingering noise.

Zipline speed effect revisions.

Stunned debuff effect revisions.

Updated last hit effects to reflect UI.

Changed minimum bot difficulty for some heroes.

Added chimes and bird sounds behind park gate.

Added looping sound to jump pads.

Added neutral camp spawn sound.

Added permanent powerup spawn sound.

Added a global spawn sound for bridge buffs.

## Hero Lab Changes

- H Fathom

- text:: Spit debuff is now a heavy slow (was immobilize), damage is dealt over duration (was initial impact).

- type: change

- affected1: Fathom Added unique footstep sfx.

- text:: Active's duration and damage halved if Fathom is not latched to a wall while casting.

- type: change

- affected1: Fathom

- text:: Shortened channel time for max duration/damage.

- type: buff

- affected1: Fathom

- text:: fixed failing to cast if sliding while casting.

- type: fix

- affected1: Fathom M Scalding Spray new VFX and animation.

Remastered sounds for - M Scalding Spray and - M Breach.

Fixed M Scalding Spray sound being too quiet for victim sometimes.

- H Raven Updated animation set (sprint, aims, parries, dashes, jumps, reloads).

Added sounds to - M Blindside debuff hit, loop, end.

Initial gun weapon audio.

Fixed bugs preventing VO from playing correctly.

- H Trapper

- text: Reworked and.

- type: change

- affected1: Trapper Adjusted hitboxes.

New sounds for all abilities.

Updated model (new traps, new coat).

## Controller Support

Added Switch Pro default configs [ Standard | Gyro | Gyro + FlickStick ].

Changed default suggested SteamInput config to Gyro Enabled.

Minor fix for glyph size inside settings keybinding popup.

Added option for regular vs. universal face button glyphs.

Smoother/quicker camera movement between crouching/standing.

Fixed performance issue when zipline hint appears.

Tweaks/remake of mouse button glyphs.

## Localization

Added Japanese localization support.

Added support for keybind glyphs in non-English languages.

Applied regional number formatting.

Fixed many instances of truncated text.

Allowed room for 3-line Hero Labs descriptions.

Prevented zip line boost prompt wrapping/cutoff.

Fixed Esc menu text wrapping/overlapping.

Fixed chat wheel label clipping.

Expanded keybinding setting row width for Reset label.

Added width limit for popup window titles.

Fixed Asian font clipping in search fields and Builds tab.

Added missing M Spirit Snare, M Flying Cloak, and - I Colossus modifier labels.

Fixed Custom Match lobby UI elements not rendering in some languages, preventing code sharing.
