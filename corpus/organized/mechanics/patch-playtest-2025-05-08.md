---
title: "Patch/Playtest/2025-05-08"
pageid: 2267
source: liquipedia-deadlock-md
---

- name: Shop Rework Update

- version: 2025-05-08

- highlight1: Full Shop Rework and New Items

- highlight2: Build Authoring and Quickbuy Redesign

- highlight3: Extensive Map Updates

- highlight4: Hero Rebalances and Gameplay Adjustments

- release: May 8, 2025

- previous: Patch/Playtest/2025-04-172025-04-17

- next: Patch/Playtest/2025-05-112025-05-11

- footnotes: Source: [Shop Rework Update](https://store.steampowered.com/news/app/1422450/view/524216645064852902)

## Shop Redesign

- text: Full shop rework, including many new items.

- type: change

- affected1: Shop

- text: Item slots are now all universal, rather than tree specific.

- type: change

- affected1: Shop

- text: Total slot count reduced from 16 to 12.

- type: change

- affected1: Shop

- text: Item costs are now discounted when you own the component.

- type: change

- affected1: Shop

- text: New artwork for all item icons.

- type: change

- affected1: Shop

- text: Reworked how tier bonuses work in the shop. They are no longer based on each item you buy, but instead based on your total spend in a tree. Bonuses are not linear (maxing out one tree fully isn't optimal bonus-wise).

- type: change

- affected1: Shop Various item names have been changed.

- text: Items now glow when there is an upgrade you can buy.

- type: change

- affected1: Shop

## Build Authoring

The Build Browser has been reworked and is now its own fullscreen UI.

Added a "Create Build" button when hovering over a player in post-game. This will create a local unpublished build based on the items the player purchased in that match (including imbue targets and the order in which items were sold).

Added a new feature: build tags. Build tags are a way to compactly describe the theme of a build. A tag has an icon and a description, and you can assign 3 tags to a build (they don't have to be unique). There are a small number of initial "standard" tags such as - M Weapon / M Spirit / M Vitality, but also things like level of complexity, whether the build is melee focused, etc. In addition to the standard build tags, the ability icons of the hero, and icons of items included in a build can also be used as tags.

Published builds that don't yet have tags will not show up in the public results in the build browser.

Added the ability to specify a suggested imbue target for items in a build. When using Quickbuy this will be automatically selected. When purchasing normally, the suggested ability will be highlighted in the imbue popup Added the ability to specify a sell priority value (0-100) for items in a build. When using Quickbuy, if you are out of slots, and you own an item with a sell priority, that item will automatically be sold to make room for your next purchase.

Build Categories can now be marked as Optional, which show up differently in the build UI and will not be added to Quickbuy when queuing a build.

You can now highlight both items and categories in the build editor, with a dedicated section on the left to edit the properties of the current selection (this replaces right-click context menus to update things like annotation notes and imbue targets).

You can remove items from a build by dragging them outside of the category UI.

## Quickbuy Redesign

Added a new larger Quickbuy queue UI adjacent to the shop that lets you remove and reorder items in the queue.

Added buttons to queue your entire build and to clear your Quickbuy queue.

The default Quickbuy hotkey has been changed from 'Shift+B' to 'G'.

Added an option to always queue your selected build at the start of a match.

Fixed several bugs that would cause Quickbuy purchases to fail.

## Base and Map Updates

New base design.

Amber side early development pass at industrial exterior.

Sapphire side early development pass at museum exterior.

Interior shape changed to round with a high domed ceiling (both sides using the same interior temporarily).

- text: Added Patron Throne that moves down into the ground to form the final area.

- type: new

- affected1: Patron Two ventilation tunnels from the player spawn to the final M Patron area combined into a single tunnel.

- text: s moved back closer to the player spawn area and pushed into alcoves.

- type: change

- affected1: Shrines Hallways along the Mid Lane entrance to the base changed to rooms with ropes leading up to the high ground.

Side passages from player spawn area to the - M Shrine s changed to curved stairs.

Increased areas in front of the Mid Lane base entrances.

Added Juke Closets in between base entrances on the interior side.

1. Mid Lane Laning Area

- text: Lowered buildings on the corners of the area that have access to.

- type: change

- affected1: Mid Boss

- text: Extended the rope from to the rooftop of these newly lowered buildings.

- type: change

- affected1: Mid Boss 1. Mid Lane Walker Arena Redesigned Boutique.

Expanded the rooftop all the way back to the wall.

Raised building separating the Boutique and the base.

- text: Continuous interior from jungle area to the.

- type: change

- affected1: Walker Stairs dip down into the building.

- text: Added high building archway behind the.

- type: change

- affected1: Walker

- text: Increased the window size in the covered hallway in between the and the jungle areas.

- type: change

- affected1: Walker 1. Outer Lane Walker Arena (Amber Park and Sapphire York) Removed the Skybridges just below the ziplines from the base side.

- text: Removed the Pedestrian bridge in between the and the.

- type: change

- affected1: Walker

- affected2: Guardian

- text: Reduced width of the street coming from the.

- type: change

- affected1: Guardian

- text: Added catwalk on the defender side to connect to the catwalk behind the.

- type: change

- affected1: Walker Added an awning in front of the Cultural Center.

Changed the Cultural Center interior path to go to the defender side catwalk.

Removed the high ground side entrance to the interior hallway on the outside of the lane.

- text: Centered the bounce pad coming out of the interior hallway in between the and the.

- type: change

- affected1: Walker

- affected2: Guardian 1. Bull/Bear Jungles Added a rope to access the roof from the jungle side.

Removed wall shrubs on the jungle side.

Removed the zap triggers on that rooftop.

Added breakables on the roof.

Lowered the tower building in the jungle area across from the connection area.

Lowered rooftop of the Clinic/Law Office (building next to the Bear/Bull statues).

Connected the rooftop of the Clinic/Law Office to the lowered roof leading to Mid Lane.

Lowered one side of the building beside the Fish Market/Nursery.

Added Juke Closet off the lowered rooftop.

Added breakables to all newly lowered rooftops.

Moved and rotated delivery trucks separating neutral camps.

1. Juke Closets Increased size of doorways of Juke Closets.

1. Breakable Crates Wooden crates replaced with new design and shader.

1. Art Pass Skybridges Pedestrian Bridges (old Power Up bridges) Department Store Chapel Bell Tower Apartment Complex Speakeasy Gallery Interiors Broadway Storefronts Nightclub Theater 1. Miscellaneous Map Updates Increased size of all doorways entering interior spaces.

Removed the veils below the old Power-Up bridges.

Removed the sign on the top of the Theater.

Added collision to the chimney pipes.

Raised interior ceiling of Radio Station/Apartment Complex on outer lanes next to the T1 M Shop s.

Removed the columns in the interiors of the Radio Station/Apartment.

Added lights to the Radio Station/Apartment interiors.

Removed veil at the front of Dept Store/New York Oracle.

## Soul Orb Mechanics

- text: Players gain back ammo when claiming an.

- type: buff

- affected1: Soul Orb

- text: Improved reliability of claims when experiencing momentary packet loss or latency.

- type: fix

- affected1: Soul Orb

- text: Reworked visual effects for s to more clearly communicate when they are claimable or expiring.

- type: change

- affected1: Soul Orb

- text: Reworked client feedback when shooting a prior to being awarded the.

- type: change

- affected1: Soul Orb

- affected2: Souls

- text: s no longer automatically claim when colliding with the world.

- type: change

- affected1: Soul Orb

## Game Feel and Optimization

Improved unit targeting logic.

Networking: Add method to smooth player jitter that may result from non-ideal networking conditions.

Fixed jittery motion for various in-world UI elements, such as targeting and ziplines.

Improve fairness in hit registration between high and low ping players during ability use and when shooting M Trooper s.

Fixed rare bug that would cause melee hits to have an incorrect range on the server.

Fixed various scenarios causing networking-related jitter when climbing ropes.

Reduced jitter from mispredictions while ziplining near another player.

Fixed issues with mispredicting (and bad stuttering) when going around corners on zipline.

## Movement

Air Acceleration has been increased to improve Wall Jump controls, but only while moving at lower speeds.

Wall Jump launch has different kick away speed from the wall based on whether you're pushing your movement direction toward, away, or neutral.

Fixed cases where it was impossible to Mantle Ledges to the left or right of your Wall Jump direction, just after a Wall Jump.

Fixed/improved control over air dashes just after a Wall Jump.

Wall Jump fatigue affects the vertical launch only, and recovers at 1.25s instead of 2s. This should encourage long lateral leaps, while keeping chimneying in check.

Fixed a bug where using Melee on the ground triggered Wall Jump fatigue.

Wall detection for wall jumps now takes into account all walls in a small radius around the player, not just the last wall touched.

Changes to Wall Jump behavior have reduced the effectiveness of "Corner Boosting" a bit.

While Wall Sliding, terminal velocity is in effect (for vertical speeds only). At -600u/s gravity is cancelled out.

Mantle Glide: Holding Crouch or Crouch Toggle while exiting a Mantle creates a small speed boost, allowing you to slide out of mantles.

## Camera

- text: Various Fixes for camera positions when characters push the camera into the ceiling in special cases ( & ' Ults).

- type: fix

- affected1: Vindicta

- affected2: Abrams Characters, M Guardian s, M Walker s and - M Shrine s will fade to a minimum transparency as they get too close to the camera.

Soft Camera Collision: As you move, the camera anticipates walls approaching from behind and to the right of your character resulting in less sudden jolts, and smooth near/far camera paths when turning in constricted spaces.

## General

Updated all default builds.

Net Worth display shows decimals until 10k (instead of only until 5k).

Updated all targeting in game with new visuals to be consistent for positive targeting AOEs.

- text: s are visible through walls during the laning phase. Replaces the HUD element showing icon and health.

- type: change

- affected1: Troopers Ally health bars visible through walls in addition to X-ray.

Nearby creep X-rays also visible through walls.

Added outlines to hero shader.

Minor update to the "Getting started" tutorial videos to reflect the three lanes and removal of - M Trooper last hits.

- text: Corrected name of Temple in the damage report where it was appearing as.

- type: fix

- affected1: Guardian

- affected2: Mid Boss Added a tooltip to explain the secondary build search language option in Settings.

Aligned labels of in-world pickup item labels with the corresponding modifiers so the HUD text that appears after picking up an item uses consistent terminology.

- text: s are now navigation blockers, discouraging s from walking through and into them.

- type: change

- affected1: Shrines

- affected2: Troopers

- text:,, and can now properly be cast while climbing ropes.

- type: fix

- affected1: Majestic Leap

- affected2: Warp Stone

- affected3: Phantom Strike

- text:'s teleport follow-up can now properly be cast while climbing ropes.

- type: fix

- affected1: The Magnificent Sinclair

- affected2: Spectral Assistant Bots will change their mind less frequently when considering retreating due to low health.

Bots now use ziplines when returning to base to heal.

Bots are now much better at ziplining out of base.

- text: Players will no longer be attacked by nearby Neutrals when attacking the in Sandbox.

- type: fix

- affected1: Sinner's Sacrifice Improvements to camera change on rope climb ejection.

## Sound, Music, and VO Changes

- text: Added sounds for transforming to weakened state.

- type: new

- affected1: Patron

- text: Added shock attack sound when in weakened state.

- type: new

- affected1: Patron

- text: Adjusted audio mix for greater threat perception when enemy and less threat when ally.

- type: change

- affected1: Walker

- text: Improved activate sound to trigger less often between attacks.

- type: change

- affected1: Guardian Updated zipline audio mix so allies and enemies using ziplines are more audible.

Improved footstep audio sync across all heroes.

Improved animation audio coverage across all heroes.

Updated audio mix between footsteps and movement across all heroes.

New footstep material sweetener sounds, increased overall volume.

Added more match start conversations.

Match start conversations are now cancelled by higher priority lines (like ping lines), regardless of which hero is talking.

Fixed match start conversations to handle game pauses correctly.

Voice lines that fire when an objective is denied will only be played for those close to the objective.

Removed shop music in hero test.

Updated weapon initial reflection acoustics model.

Damage audio feedback scales with "falloff" - it will be more quiet when damage is least effective.

Lowered and shortened headshot damage audio.

Removed some mix settings that were lowering player weapon when receiving damage.

Added support to play weapon fire from muzzle location.

Technical groundwork to change sound effects based on surface materials for things like footsteps and bullets with some meaningful performance savings.

Added unique surface impacts for bullets for various materials.

Technical groundwork to unify weapon sound and continue reducing fatigue, includes some additional support to include per-weapon low ammo sounds and acoustics.

- text: Remastered several characters' weapon fire sounds using the new feature set (,,, and ).

- type: change

- affected1: Wraith

- affected2: Dynamo

- affected3: Calico

- affected4: Abrams Improved bullet whizby audio detection.

Ensured technical parity between automatic and animation-driven footstep systems.

Match Start conversations now have a 50% chance of firing - this reduces repetition as well gives the patron a chance to speak individually to a hero.

Match Start conversation timings have been adjusted to make them flow faster and more naturally.

Match Start conversations will no longer partially fire, so if content has not been recorded you won't hear the start of a conversation than no follow-up.

Green lane is once again referred to as Greenwich by heroes.

Added a new Ping for "leaving the area" for most heroes.

- text: Adjusted VO frequency when leveling up so they're a little less chatty.

- type: change

- affected1: Patron Fixed several issues with heroes referring to other heroes with outdated names or not saying their name at all.

- text: Updated keeper VO - minor update that adds a few new interactions.

- type: change

- affected1: Shop

- text: Turned off/on a handful of stray VO lines to have things be more in line with current iteration of abilities (for instance no longer says "armor's not going to save you", when in fact, armor could save you).

- type: change

- affected1: Holliday Increased volume for hero effort VO sounds (jumping, dashing, mantling).

Teammates' pain VO will receive a volume boost when their health gets below a certain threshold.

Changed Hero Death VO to be directional.

## User Interface

Items now show M Spirit Scaling when alt is pressed.

General visual pass to minimap in concert with map changes to improve its read and usability.

Objective icons and lanes on minimap have been adjusted for visual and functional clarity.

New lower "basement" level texture was added to minimap when players traverse into deeper parts of the map.

All keyboard/controller button glyphs have been unified into a common UI element.

Keyboard, Mouse, and Button bind stylings have improved, especially in the case of "inline" bindings.

When an action is not bound to any key button, there is a symbol in its place.

When an ability or active item button is pressed during cooldown, the related element will shake and glow red briefly.

- text: Updated and improved search functionality in the.

- type: change

- affected1: Shop The cooldown alert message has been removed, but alert messages related to Charges, Silences, etc. remain.

- text: Objective healthbars now only show for the, s, and.

- type: change

- affected1: Patron

- affected2: Shrines

- affected3: Mid boss When stunned or disarmed the reticle now changes state and displays a duration meter.

Hiding gun disarmed FX and generic disarm particles since the reticle communicates the disarmed state.

Added overhead indicators for disarm abilities.

Don't show cooldowns on ability icons for the imbue popup.

Reordered ping wheel messages with lanes so the order matches the left to right order of the lanes.

Simplified and reworked the menu when you hit ESC while in-game.

Deadlock loading screens can now animate and show other controls.

Added charge-up icon and entry in labels in the same way we have cooldowns for items.

Added "unstoppable" as a status effect to show in tooltips.

The ultimate icons on the team's bar at the top of the HUD have been updated.

- text: Added UI indication when an item is upgradeable in the (when you already have a component for an item).

- type: new

- affected1: Shop Added a button to Post Game when you hover a player to view their items, that lets you create a build based on the ability and item choices the player made in that game.

Added charge-up icon and entry in labels in the same way we have cooldowns for items. (Repeated entry from original notes) Added purchase messages in the chat feed for T3 and T4 items that allies or enemies purchase.

Added a corner cap on items in inventory/scoreboard/etc to replace the old tier indicators and give better tree recognition.

Disabled low/mid health label under crosshair.

Made it so scaling values below 0.5 shows 2 decimals instead of 1.

Hovering items in the damage report now shows tooltip for that item.

- text: bonuses now appear faster.

- type: change

- affected1: Sinner's Sacrifice Added a UI state when Stamina is disabled with a debuff.

Top bar now uses the new vertical bar graphs.

Charge-up items ( I Mystic Burst, Tankbuster, QSR, Ethereal Bullets) now show 'cooldown' timing clock on icon while they are charging up.

When charge-up items are fully charged the HUD icon at center will show just like items that are refreshed on cooldown.

Renamed "Move Speed Resist" to "Slow Resist".

Items in your HUD are organized by cheapest to most expensive from left to right.

- text: Base s now share a single Icon / HP pool on Minimap.

- type: change

- affected1: Guardians

- text: now shows an icon for each of its phases.

- type: change

- affected1: Patron Active items are no longer sorted separately from the rest of the items; all items are now sorted alphabetically.

Range and Duration upgrades are now labeled as “Ability Range” and “Ability M Duration ” tooltip wise, to help with searching in the - M Shop.

## Heroes

- H Abrams

- text:: Added new animation logic support for Siphon Life and items.

- type: change

- affected1: Abrams

- affected2: Siphon Life

- text:: Base duration increased from 1.2s to 1.4s.

- type: buff

- affected1: Abrams

- affected2: Shoulder Charge

- text:: T1 is now "On Hero Collide: +25% Weapon Damage for 8s".

- type: change

- affected1: Abrams

- affected2: Shoulder Charge

- text:: T2 is now "-12s Cooldown".

- type: change

- affected1: Abrams

- affected2: Shoulder Charge

- text:: T3 is now "+0.2s Stun Duration and 40% Movement Slow for 4s".

- type: change

- affected1: Abrams

- affected2: Shoulder Charge

- text:: New cycle and pre cast 'goose step'.

- type: change

- affected1: Abrams

- affected2: Shoulder Charge

- text:: Added support for shoulder charging while in air.

- type: buff

- affected1: Abrams

- affected2: Shoulder Charge

- text:: New sounds added for hitting heroes, s, and walls.

- type: change

- affected1: Abrams

- affected2: Shoulder Charge

- affected3: Troopers

- text:: Radius increased from 9m to 10.5m.

- type: buff

- affected1: Abrams

- affected2: Seismic Impact

- text:: Effects revisions.

- type: change

- affected1: Abrams

- affected2: Seismic Impact

- text:: Fixed crash down sound triggering twice.

- type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text:: New slam animation.

- type: change

- affected1: Abrams

- affected2: Seismic Impact

- text:: New sounds added for in-air looping sound and descend sound.

- type: change

- affected1: Abrams

- affected2: Seismic Impact

- text: Added new 'out of combat' run and sprint.

- type: change

- affected1: Abrams

- text: New Crouch animations.

- type: change

- affected1: Abrams

- text: Improved hipfire animations.

- type: change

- affected1: Abrams

- text: Added custom jump catapult animation - an alternate jump animation when using fans and etc.

- type: change

- affected1: Abrams

- affected2: Majestic Leap

- text: Refined jump start to be cleaner.

- type: change

- affected1: Abrams

- text: Added custom Zipline Boosted loop.

- type: change

- affected1: Abrams

- text: Added Zipline swinging animation.

- type: change

- affected1: Abrams

- text: Fixed a regression where ' and ping VO were swapped.

- type: fix

- affected1: Abrams

- affected2: Siphon Life

- affected3: Shoulder Charge

- text: Removed competing camera modifier on.

- type: fix

- affected1: Abrams

- affected2: Seismic Impact

- text: Fixed camera position on client's ground target not using previews, causing it to be jittery.

- type: fix

- affected1: Abrams H Bebop

- text:: Fixed missing uppercut hero impact sound.

- type: fix

- affected1: Bebop

- affected2: Exploding Uppercut

- text:: Reworked code to reduce mispredicts.

- type: fix

- affected1: Bebop

- affected2: Hook

- text:: When hooks a, only will hear the hook success sound now.

- type: change

- affected1: Bebop

- affected2: Hook

- affected3: Trooper

- text:: Fixed the hook sometimes not breaking when the target is stuck.

- type: fix

- affected1: Bebop

- affected2: Hook

- text:: Fixed the target sometimes not being positioned in front of when rotated.

- type: fix

- affected1: Bebop

- affected2: Hook

- text:: Effect revisions for projections on vertical surfaces.

- type: change

- affected1: Bebop

- affected2: Hyper Beam

- text:: Fixed damaging enemies through thin walls.

- type: fix

- affected1: Bebop

- affected2: Hyper Beam H Calico

- text:: Fixed animation getting stuck when stunned during the ability cast.

- type: fix

- affected1: Calico

- affected2: Leaping Slash H Dynamo

- text: New updated model and animations.

- type: change

- affected1: Dynamo

- text:: T1 Fire Rate slow now matches the Move Slow.

- type: change

- affected1: Dynamo

- affected2: Kinetic Pulse

- text:: Added small lerp to VFX for the teleport and smoothed out camera transitions.

- type: change

- affected1: Dynamo

- affected2: Quantum Entanglement

- text:: Effect revisions to center focus on head.

- type: change

- affected1: Dynamo

- affected2: Rejuvenating Aurora

- text:: Updated effects revisions.

- type: change

- affected1: Dynamo

- affected2: Singularity

- text:: Increased tick rate, equals out to roughly the same DPS overall, just smoother.

- type: change

- affected1: Dynamo

- affected2: Singularity

- text: Hero pose ambient VFX added.

- type: new

- affected1: Dynamo

- text: Reload effects revisions.

- type: change

- affected1: Dynamo

- text: Fixed announcer match start line to be spoken by the friendly announcer (was randomly picking between friendly and enemy).

- type: fix

- affected1: Dynamo

- text: Various tooltip fixes.

- type: fix

- affected1: Dynamo H Grey Talon

- text: Base Bullet Damage power scaling reduced from 0.09 to 0.07.

- type: nerf

- affected1: Grey Talon

- affected2: Spirit

- text:: Added physical elements to the AoE visuals.

- type: change

- affected1: Grey Talon

- affected2: Spirit Snare

- text: T3 Power scaling reduced from 1.3 to 1.2.

- type: nerf

- affected1: Grey Talon

- affected2: Charged Shot

- affected3: Spirit H Haze

- text: VO remastering pass.

- type: change

- affected1: Haze

- text:: no longer wakes up from damage over time.

- type: buff

- affected1: Haze

- affected2: Sleep Dagger H Holliday

- text:: Fixed being able to spawn barrels on the other side of thin walls.

- type: fix

- affected1: Holliday

- affected2: Powder Keg

- text:: Fixed a bug where bounce pads might force you back to the ground after use.

- type: fix

- affected1: Holliday

- affected2: Bounce Pad

- text:: now plays VO when she lands a hit with her lasso as opposed to when she casts her lasso (so she won't say "shoot them" if she didn't actually grab anyone).

- type: change

- affected1: Holliday

- affected2: Spirit Lasso H Infernus

- text:: Projectile no longer slides against geometry.

- type: change

- affected1: Infernus

- affected2: Catalyst H Ivy

- text:: Fixed not replicating healing from (it worked with other sources of bullet lifesteal).

- type: fix

- affected1: Ivy

- affected2: Watcher's Covenant

- affected3: Bullet Lifesteal

- text:: Fixed cast sound being delayed and increased its volume.

- type: fix

- affected1: Ivy

- affected2: Stone Form

- text:: Fixed interaction with air vents and small geo.

- type: fix

- affected1: Ivy

- affected2: Stone Form

- text:: Adjusted visuals to have higher contrast.

- type: change

- affected1: Ivy

- affected2: Air Drop

- text:: Ally cast range increased from 8m to 12m.

- type: buff

- affected1: Ivy

- affected2: Air Drop

- text:: Slow duration reduced from 4s to 3s.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text:: Radius reduced from 14m to 12m.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text:: reduced from 200 to 150.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- affected3: Combat Barrier

- text:: Power scaling reduced from 2.5 to 1.5.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- affected3: Combat Barrier

- affected4: Spirit

- text:: T1 duration reduced from 12s to 8s.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- text:: T2 reduced from +300 to +200.

- type: nerf

- affected1: Ivy

- affected2: Air Drop

- affected3: Combat Barrier

- text:: T3 Silence reduced from 4.5s to 3s.

- type: nerf

- affected1: Ivy

- affected2: Air Drop H Kelvin

- text:: Reduced how sticky the is for allies.

- type: change

- affected1: Kelvin

- affected2: Ice Path

- text:: Fixed damaging enemies through thin walls.

- type: fix

- affected1: Kelvin

- affected2: Arctic Beam H Lady Geist

- text:: You're now only slowed when is damaging a target.

- type: buff

- affected1: Lady Geist

- affected2: Life Drain H Lash

- text: Base Resist reduced from 15% to 10%.

- type: nerf

- affected1: Lash

- affected2: Spirit

- text:: scaling reduced from 0.05 to 0.04.

- type: nerf

- affected1: Lash

- affected2: Ground Strike

- affected3: Spirit

- text:: Fixed a bug that caused to push the victim under the world.

- type: fix

- affected1: Lash

- affected2: Ground Strike

- text:: Updated ability icon.

- type: change

- affected1: Lash

- affected2: Flog

- text:: UI lock-on revisions to simplify readability.

- type: change

- affected1: Lash

- affected2: Death Slam

- text:: Fixed channel effect on to not disappear prematurely.

- type: fix

- affected1: Lash

- affected2: Death Slam

- text:: New sounds added for lock-on success sounds, in-air looping sound, victim impact sounds, and a 'miss' sound when does not successfully grab anybody or cancels the ability early.

- type: change

- affected1: Lash

- affected2: Death Slam H McGinnis

- text: New updated model and animations.

- type: change

- affected1: McGinnis

- text: Bullet Growth reduced from 0.311 to 0.29.

- type: nerf

- affected1: McGinnis

- text: Bullet Velocity increased from 590 to 650.

- type: buff

- affected1: McGinnis

- text: No longer has +15% Base Bullet Resist.

- type: nerf

- affected1: McGinnis

- text: Now has +1% Resist per Boon.

- type: buff

- affected1: McGinnis

- affected2: Spirit

- text:: Updated DPS tooltip to properly reflect the correct number.

- type: fix

- affected1: McGinnis

- affected2: Mini Turret

- text:: Updated ambient, tracer, and muzzle flash effects.

- type: change

- affected1: McGinnis

- affected2: Mini Turret

- text:: No longer have a 3 second minimum life time. They now spawn with 60% and bullet resist that decays over 6s.

- type: change

- affected1: McGinnis

- affected2: Mini Turrets

- affected3: Spirit

- text:: T3 duration reduced from +18s to +14s.

- type: nerf

- affected1: McGinnis

- affected2: Mini Turrets

- text:: Effects revisions and improvements.

- type: change

- affected1: McGinnis

- affected2: Medicinal Specter

- text:: Fixed audio buildup when multiple characters are being healed by at once.

- type: fix

- affected1: McGinnis

- affected2: Medicinal Specter

- text:: Now provides +15% Stamina Regen.

- type: buff

- affected1: McGinnis

- affected2: Medicinal Specter

- text:: T3 reduced from 4% to 3.5%.

- type: nerf

- affected1: McGinnis

- affected2: Medicinal Specter

- text:: Fixed missing sound as it travels before deploy.

- type: fix

- affected1: McGinnis

- affected2: Spectral Wall

- text:: The last 2 segments on the left/right sides of will now turn towards a nearby wall if there is one.

- type: change

- affected1: McGinnis

- affected2: Spectral Wall

- text:: Duration reduced from 5s to 4.5s.

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text:: Cooldown increased from 46s to 50s.

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text:: T2 reduced from -22s to -20s.

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text:: T3 reduced from 1s Stun to 0.75s.

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall

- text:: Projectile and ambient effects revisions.

- type: change

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Now allows full movement while channeling the ability.

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Fixed a bug where the Camera would not zoom out during the ability if user setting was set to QuickCast.

- type: fix

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Now slows your dash usage by 35%.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Damage per rocket reduced from 30 to 23.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Minimum distance increased from 7m to 9m.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: Cooldown increased from 140s to 150s.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: power scaling reduced from 0.35 to 0.25.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- affected3: Spirit

- text:: T3 damage per rocket reduced from +30 to +25.

- type: nerf

- affected1: McGinnis

- affected2: Heavy Barrage

- text:: T3 now also increases scaling by 0.1.

- type: buff

- affected1: McGinnis

- affected2: Heavy Barrage

- affected3: Spirit H Mirage

- text:: Improved camera animations during ability.

- type: change

- affected1: Mirage

- affected2: Tornado

- text: VO remastering pass as well as new VO content.

- type: change

- affected1: Mirage

- text: Animation for holding and throwing items has been added.

- type: new

- affected1: Mirage H Mo & Krill

- text:: Heal reduced from 1.3x to 1.2x.

- type: nerf

- affected1: Mo and Krill

- affected2: Scorn

- text:: T2 reduced from +100 Damage to +80.

- type: nerf

- affected1: Mo and Krill

- affected2: Burrow

- text:: Projectile no longer slides against geometry.

- type: change

- affected1: Mo and Krill

- affected2: Sand Blast

- text:: No longer deals damage.

- type: nerf

- affected1: Mo and Krill

- affected2: Sand Blast

- text:: Bonus health on kill/assist reduced from +70 to +50.

- type: nerf

- affected1: Mo and Krill

- affected2: Combo

- text: VO remastering pass.

- type: change

- affected1: Mo and Krill H Paradox

- text: VO remastering pass.

- type: change

- affected1: Paradox H Pocket

- text: Base bullet damage increased from 3.9 to 4.1.

- type: buff

- affected1: Pocket

- text:: No longer removed by (as this item no longer removes ultimate effects).

- type: change

- affected1: Pocket

- affected2: Affliction

- affected3: Debuff Remover

- text:: Duration reduced from 18s to 14s.

- type: nerf

- affected1: Pocket

- affected2: Affliction

- text:: DPS increased from 10 to 30.

- type: buff

- affected1: Pocket

- affected2: Affliction

- text:: Initial damage reduced from 18% to 10%.

- type: nerf

- affected1: Pocket

- affected2: Affliction

- text:: T2 now increases duration by +4s.

- type: change

- affected1: Pocket

- affected2: Affliction

- text:: T2 Healing Reduction reduced from -50% to -40%.

- type: nerf

- affected1: Pocket

- affected2: Affliction

- text:: T3 no longer has % Current HP damage.

- type: change

- affected1: Pocket

- affected2: Affliction

- text:: T3 increased from +10 DPS to +20 DPS.

- type: buff

- affected1: Pocket

- affected2: Affliction

- text:: T3 range increased from +5m to +6m.

- type: buff

- affected1: Pocket

- affected2: Affliction

- text: VO remastering pass as well as new VO content.

- type: change

- affected1: Pocket H Seven

- text:: Can no longer be self cast.

- type: nerf

- affected1: Seven

- affected2: Static Charge

- text: VO remastering pass.

- type: change

- affected1: Seven H Shiv

- text:: Threshold reduced from 22% to 20%.

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text:: T2 threshold reduced from +6% to +5%.

- type: nerf

- affected1: Shiv

- affected2: Killing Blow

- text: VO remastering pass as well as updated ping lines.

- type: change

- affected1: Shiv H The Magnificent Sinclair

- text:: Redirect telegraphs correctly on vertical geometry.

- type: fix

- affected1: The Magnificent Sinclair

- affected2: Vexing Bolt

- text:: Fixed a bug where Henry and Savannah wouldn't play VO when turning enemies into rabbits.

- type: fix

- affected1: The Magnificent Sinclair

- affected2: Rabbit Hex H Vindicta

- text: Minor rework on animation set.

- type: change

- affected1: Vindicta

- text:: Fixed zoom in sound triggering twice.

- type: fix

- affected1: Vindicta

- affected2: Assassinate H Viscous

- text: Gun: Improved firing effects.

- type: change

- affected1: Viscous

- text: Gun: Fixed alt-fire weapon thinking it could zoom. It would try if you held right-click and jumped.

- type: fix

- affected1: Viscous

- text:: Fix a bug where would sometimes not deal damage when the target was very close to a wall.

- type: fix

- affected1: Viscous

- affected2: Puddle Punch

- text:: Cooldown increased from 95s to 105s.

- type: nerf

- affected1: Viscous

- affected2: Goo Ball

- text:: Fixed it knocking back heroes with Unstoppable state.

- type: fix

- affected1: Viscous

- affected2: Goo Ball H Vyper

- text:: Debuff effect revisions to help identify targets better.

- type: change

- affected1: Vyper

- affected2: Petrifying Bola

- text:: Adjusted the volume of direct hits and explosion sounds.

- type: change

- affected1: Vyper

- affected2: Petrifying Bola H Warden

- text: VO remastering pass.

- type: change

- affected1: Warden H Wraith

- text: Gun: Falloff range reduced from 20m->58m to 18m->52m.

- type: nerf

- affected1: Wraith

- text:: Revisions to debuff effect.

- type: change

- affected1: Wraith

- affected2: Telekinesis

- text: VO remastering pass.

- type: change

- affected1: Wraith H Yamato

- text: VO remastering pass.

- type: change

- affected1: Yamato

## Item Sound and Visuals

- I Arcane Surge

- text: New sounds added.

- type: change

- affected1: Arcane Surge I Boundless Spirit

- text: New sounds added.

- type: change

- affected1: Boundless Spirit I Crippling Headshot

- text: Effects revision to show when the item procs.

- type: change

- affected1: Crippling Headshot I Curse

- text: New sounds added.

- type: change

- affected1: Curse I Decay

- text: New sounds added.

- type: change

- affected1: Decay I Ethereal Shift

- text: Fixed it not playing the correct cast sound.

- type: fix

- affected1: Ethereal Shift I Guardian Ward

- text: New sounds added.

- type: change

- affected1: Guardian Ward I Healing Nova

- text: New sounds added.

- type: change

- affected1: Healing Nova I Healing Rite

- text: New sounds added.

- type: change

- affected1: Healing Rite I Improved Burst

- text: Now uses charge-up mechanic (recharges its proc strength over its cooldown duration).

- type: change

- affected1: Improved Burst I Infuser

- text: New sounds added.

- type: change

- affected1: Infuser I Knockdown

- text: Updated overhead visual counter.

- type: change

- affected1: Knockdown

- text: Now stops all momentum on Stun so victims fall straight down.

- type: change

- affected1: Knockdown I Kinetic Dash

- text: New sounds added.

- type: change

- affected1: Kinetic Dash I Lucky Shot

- text: New sounds added.

- type: change

- affected1: Lucky Shot I Metal Skin

- text: Effects revision at start to make it more apparent.

- type: change

- affected1: Metal Skin

- text: Added metal footstep sweetener sound when is active.

- type: change

- affected1: Metal Skin I Mystic Reverb

- text: New sounds added.

- type: change

- affected1: Mystic Reverb I Mystic Burst

- text: Now uses charge-up mechanic.

- type: change

- affected1: Mystic Burst I Phantom Strike

- text: New sounds added.

- type: change

- affected1: Phantom Strike I Quicksilver Reload

- text: Fixed its fire rate buff not being networked, and therefore not showing up in left-hand panel.

- type: fix

- affected1: Quicksilver Reload

- text: Now uses charge-up mechanic.

- type: change

- affected1: Quicksilver Reload I Refresher

- text: New sounds added.

- type: change

- affected1: Refresher I Rescue Beam

- text: New sounds added.

- type: change

- affected1: Rescue Beam I Restorative Locket

- text: New sounds added.

- type: change

- affected1: Restorative Locket

- text: Now plays a sound every time a stack is gained.

- type: change

- affected1: Restorative Locket I Return Fire

- text: Returned Bullets factor in attacker movement and cannot be easily avoided by strafing.

- type: change

- affected1: Return Fire I Rusted Barrel

- text: New sounds added.

- type: change

- affected1: Rusted Barrel I Shadow Weave

- text: Added effect on activation.

- type: change

- affected1: Shadow Weave

- text: Fixed item not granting +20% weapon power.

- type: fix

- affected1: Shadow Weave I Slowing Hex

- text: New sounds added.

- type: change

- affected1: Slowing Hex I Spiritual Overflow

- text: New sounds added.

- type: change

- affected1: Spiritual Overflow I Unstoppable

- text: Effects revisions for better visibility and separation from other effects.

- type: change

- affected1: Unstoppable

## Localization

Fixed jittery health numbers in some non-English languages.

Adjusted the width of the individual M Soul count backer in the HUD by language to prevent player M Soul counts from spilling outside of the bounding box in languages where number formatting and/or length of the abbreviation for thousands results in longer text than English.

Applied language-specific width adjustments and padding to the team M Soul count panel to improve readability.

Localized the loading screen.

Added localized versions of the Great For New Players screenshot in the new player dialog window.

Added localized versions of the the Hero Labs screenshot shown at the hero selection screen.

Corrected HUD images containing text that were still showing up in English when playing in Korean.

Adjusted font sizing to fix instances of truncated text in the Hero Testing menu in Russian and Indonesian.

Enabled resizing of the new player dialog window to fit longer or shorter text appropriately in translation and prevent the "Got it!" button from being cut off in languages with longer text.

Enabled font scaling on the Imbue and Active tag labels and the Report button to prevent truncation in certain languages.

Fixed multiple instances of single character awkwardly wrapping to second line in Japanese.

Added localization support for bot hero pings.
