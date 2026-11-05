---
title: "Patch/Playtest/2024-05-23"
pageid: 584
source: liquipedia-deadlock-md
---

- name: Playtest - May 23 2024

- version: 2024-05-23

- release: May 23, 2024

- highlight1: Gameplay Updates

- highlight2: UI Updates

- highlight3: Bug Fixes

- highlight4: Item Updates

- highlight5: Hero Updates

- previous: Patch/Playtest/2024-05-192024-05-19

- next: Patch/Playtest/2024-05-242024-05-24

## General

Playtesting times are now starting 1 hour earlier. Weekdays are 5PM PDT and weekends are 3PM PDT.

Added in-game custom item builds support. Create your own builds or browse builds from the community in the heroes page.

Added post game player reporting option Ally player glow-through-world silhouette now communicates their current health Added ambient music track Added unique Haze footstep sound effects Fixed various issues with mic audio input and lag it introduced Small adjustments to how the crosshair UI area looks Mic input device is now selected from in-game settings rather than the steam client Improved various networking and hit registration related issues (this was released a couple days ago) Updated Trooper and Neutral shooting sound effects Various improvements to damage audio clarity for victims and attackers Sped up select Amber Hand VO that related to game state (shrines being under attack, protecting the urn runner etc) Adding game audio muted indicator in top left if the game is muted Camera can now be moved while the game is paused in replays

- text: Fixed the falling during pause

- type: fix

- affected1: Rejuvenator Fixed the Idol falling during pause Fixed the bottom most shop items having part of their icon be unclickable Fixed a few unit target abilities that could sometimes select a target behind a nearby wall (e.g. Bebop Sticky Bomb) Added some additional visual tells for the receiving end of Lash’s Death Slam Updated Bullet Shredder debuff effects

- text: is now invulnerable if there are no enemies it can actually attack

- type: buff

- affected1: Mid Boss Fixed your active items not hiding in the UI when you are dead and spectating a team mate Added support for binding mouse1 and mouse2 to any key (this was released a couple days ago) Fixed various movement stuck bugs with Ivy Added alt info to recent damage view to make it clearer that this can be brought up again after it disappears Improved Vindicta’s Stake effects to make it a little clearer when you are affected Fixed upgrading McGinnis’s Medicinal Specter to T3 while active causing it to heal everyone to full instantly Fixed a bug that could cause all of Paradox Pulse Grenade’s pulses to go off at once Fixed Kelvin’s Ice Beam sometimes not hitting Neutrals Fixed being able to see some things through the Veils in the map that you shouldn’t be able to see Removed stack of cardboard boxes inside connection hallway near bases to prevent cover from Neutrals Fixed getting stuck under stair at inner lanes near Guardian Fixed Abrams getting stuck on department store facade when using his ult Sapphire side materials tint color changed to white Sapphire side street materials changed to new asphalt blend Added new slide and reload animation for Wraith Out of combat run animation variants now only play during sprint state Fixed missing VO for Yamato ability use/upgrades Allies now compliment teammates when they see impressive use of channeled abilities (for instance, Gigawatt killing three people with Storm Cloud) Adjusted timing of select Abrams impact lines to time with either the rise of his leap or the descent accordingly Improved visibility of Seven’s bullet and travel path Improved visibility of Paradox’s bullet and travel path Improved visibility of Wraith’s bullet and travel path Improved visibility of Haze’s bullet and travel path Improved visibility of Lady Geist’s bullet and travel path Added custom tracer and muzzle flash for Seven’s gun Added custom tracer and muzzle flash for Paradox’s gun Added custom tracer and muzzle flash for Wraith’s gun

## Gameplay

Adjusted map around the middle lanes to have an area with Veils for laning Hero kill bounty ratio between Killer and Assister reduced from 2.75x to 2.55x (means slightly more to the Assister) Spirit scaling reduced by ~15% (the total effective Spirit damage is reduced by less than this, this is just the Spirit multiplier scaling portion and has largest impact on late game burst) Unclaimed souls now convert 10% slower

- text: [Vaults](Vaults.md) base bounty increased from 220 to 260

- type: buff

- affected1: Sinner's Sacrifice Strong Neutrals Spirit Resist increased from 25% to 35% Medium Neutrals Spirit Resist increased from 25% to 30% Starting at 15 minutes, one melee Trooper per wave will spawn with 1.75x health Medic Trooper health increased from 240 to 260 Sidelane Veils near Guardians are now one-way visibility (used to be blocked visibility in both directions) Neutrals can now lean side to side to fire when obstructed by map geometry and being attacked Zipline Boost ability speed increased from 100% to 130% Zipline Boost ability ramp time to reach max speed reduced from 2s to 1s\

- text: Zipline base speed boost after Base are killed increased from 100% to 120%

- type: buff

- affected1: Guardian

- text: Zipline base speed boost's ramp time after Base are killed reduced from 5s to 4s

- type: buff

- affected1: Guardian Being Disarmed no longer prevents you from reloading

## Items

- I Headshot Booster

- text: Cooldown reduced from 14s to 9s

- type: buff

- affected1: Headshot Booster I Spirit Strike

- text: No longer has +50 Health

- type: change

- affected1: Spirit Strike

- text: Now grants +75 Spirit Shield

- type: change

- affected1: Spirit Strike

- text: Now grants +0.7 HP regen

- type: change

- affected1: Spirit Strike I Mystic Burst

- text: No longer has +1 HP Regen

- type: change

- affected1: Mystic Burst

- text: Now grants +1 Sprint

- type: change

- affected1: Mystic Burst

- text: Cooldown reduced from 8s to 6s

- type: buff

- affected1: Mystic Burst I Withering Whip

- text: Moved from T3 to T2

- type: change

- affected1: Withering Whip

- text: Duration reduced 5s to 3.5s

- type: nerf

- affected1: Withering Whip

- text: Cooldown increased from 25s to 40s

- type: nerf

- affected1: Withering Whip

- text: Bullet Resist reduced from 25% to 20%

- type: nerf

- affected1: Withering Whip

- text: Cast range reduced from 20m to 15m

- type: nerf

- affected1: Withering Whip I Decay

- text: Cooldown increased from 22s to 27s

- type: nerf

- affected1: Decay I Slowing Hex

- text: Range increased from 30 to 35

- type: buff

- affected1: Slowing Hex I Reactive Barrier

- text: Cooldown reduced from 40s to 35s

- type: buff

- affected1: Reactive Barrier I Combat Barrier

- text: Bullet Shield increased from 275 to 300

- type: buff

- affected1: Combat Barrier

- text: Weapon Damage while Shielded from 20% to 24%

- type: buff

- affected1: Combat Barrier I Mystic Shot

- text: Now requires that shotguns middle pellet hit the target

- type: change

- affected1: Mystic Shot I Restorative Locket

- text: Now displays its current number of charges on its active icon

- type: change

- affected1: Restorative Locket I Silence Glyph

- text: Moved from T2 to T3

- type: change

- affected1: Silence Glyph

- text: Health increased from 50 to 75

- type: buff

- affected1: Silence Glyph

- text: Spirit Amp increased from 8% to 12%

- type: buff

- affected1: Silence Glyph I Ethereal Shift (Then called Shifting Shroud)

- text: Cooldown reduced from 70s to 55s

- type: buff

- affected1: Ethereal Shift

- text: Duration 2.5s to 2.75s

- type: buff

- affected1: Ethereal Shift I Majestic Leap

- text: Duration of no damage taken requirement reduced from 5s to 4s

- type: nerf

- affected1: Majestic Leap

- text: Now gives +75 Health

- type: buff

- affected1: Majestic Leap I Lifestrike

- text: Flat portion of the lifesteal increased from 90 to 110

- type: buff

- affected1: Lifestrike I Knockdown

- text: Spirit bonus reduced from 6 to 5

- type: nerf

- affected1: Knockdown

- text: Now grants +2 Sprint

- type: buff

- affected1: Knockdown

- text: Stun duration starts after hitting the ground

- type: change

- affected1: Knockdown I Superior Cooldown

- text: HP regen reduced from 6 to 4

- type: nerf

- affected1: Superior Cooldown I Escalating Resilience

- text: Max Bullet Resist increased from 30% to 36%

- type: buff

- affected1: Escalating Resilience I Improved Burst

- text: Damage reduced from 11% Max HP to 10%

- type: nerf

- affected1: Improved Burst I Frenzy

- text: When below 40% HP you now gain 25% Spirit Resist

- type: change

- affected1: Frenzy I Curse

- text: Ammo increased from 15% to 20%

- type: buff

- affected1: Curse I Refresher

- text: Now grants +10% Spirit Resist

- type: buff

- affected1: Refresher I Glass Cannon

- text: Fire Rate reduced from 15% to 10%

- type: nerf

- affected1: Glass Cannon I Silencer

- text: Now provides 15% Ammo

- type: buff

- affected1: Silencer I Leech

- text: Spirit bonus reduced from 12 to 8

- type: nerf

- affected1: Leech I Phantom Strike

- text: Damage reduced from 200 to 150

- type: nerf

- affected1: Phantom Strike

## Heroes

- H Abrams

- text: T1 and T2 swapped

- type: change

- affected1: Abrams

- affected2: Siphon Life

- text: now allows for a bit more steering control

- type: buff

- affected1: Abrams

- affected2: Shoulder Charge H Bebop

- text: T3 changed from Silence to Disarm

- type: change

- affected1: Bebop

- affected2: Sticky Bomb

- text: Improved hitbox detection to not grab targets that are behind cover

- type: fix

- affected1: Bebop

- affected2: Hook

- text: width increased from 2.5m to 2.7m

- type: buff

- affected1: Bebop

- affected2: Hyper Beam H Dynamo

- text: Base gun damage reduced from 18 to 15

- type: buff

- affected1: Dynamo

- text: Gun damage growth reduced from +1.1 to +0.8

- type: nerf

- affected1: Dynamo H Grey Talon

- text: Spirit scaling reduced from 2.2 to 1.2

- type: nerf

- affected1: Grey Talon

- affected2: Guided Owl

- text: T3 changed from +200 damage to "Kills enemy heroes below 20%". Low health enemies are highlighted while guiding the owl.

- type: change

- affected1: Grey Talon

- affected2: Guided Owl H Haze

- text: no longer breaks invisibility when cast (previously was part of the T3)

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: Spirit scaling increased from 2.3 to 2.6

- type: buff

- affected1: Haze

- affected2: Sleep Dagger

- text: no longer gets +140 damage with the T3

- type: nerf

- affected1: Haze

- affected2: Sleep Dagger

- text: T3 is now "-30% Damage Penalty On Victim for 4s after wakeup"

- type: change

- affected1: Haze

- affected2: Sleep Dagger

- text: cast time increased from 0.7s to 0.8s

- type: nerf

- affected1: Haze

- affected2: Bullet Dance

- text: evasion from 70% to 50%

- type: nerf

- affected1: Haze

- affected2: Bullet Dance H Ivy

- text: duration increased from 3.5s to 4s

- type: buff

- affected1: Ivy

- affected2: Kudzu Bomb

- text: T2 duration increased from +1.5s to +2s

- type: buff

- affected1: Ivy

- affected2: Kudzu Bomb

- text: Replicated Healing increased from 50% to 65%

- type: buff

- affected1: Ivy

- affected2: Watcher's Covenant

- text: Fire Rate reduced from 20% to 15%

- type: nerf

- affected1: Ivy

- affected2: Watcher's Covenant

- text: T1 changed to +15% Rate

- type: change

- affected1: Ivy

- affected2: Watcher's Covenant H Kelvin

- text: cooldown reduced from 26s to 23s

- type: buff

- affected1: Kelvin

- affected2: Frost Grenade

- text: While ing you no longer slow down when you shoot your gun

- type: buff

- affected1: Kelvin

- affected2: Ice Path

- text: Channel move speed increased from 4 to 6

- type: buff

- affected1: Kelvin

- affected2: Arctic Beam

- text: T1 changed from "+2 Channel Move Speed" to -8s Cooldown

- type: change

- affected1: Kelvin

- affected2: Arctic Beam H Lady Geist

- text: cast time reduced from 0.65s to 0.5s

- type: buff

- affected1: Lady Geist

- affected2: Soul Exchange

- text: Fixed clipping aggressively against map geometry edges

- type: fix

- affected1: Lady Geist

- affected2: Malice H Lash

- text: Base Stamina increased from 2 to 3

- type: buff

- affected1: Lash

- text: base Damage Per Meter reduced from 8 to 6

- type: nerf

- affected1: Lash

- affected2: Ground Strike

- text: Fixed some cases with not hitting units positioned just below the impact zone

- type: fix

- affected1: Lash

- affected2: Ground Strike

- text: angle increased from 20 degrees to 30 degrees

- type: buff

- affected1: Lash

- affected2: Flog

- text: cooldown reduced from 35s to 30s

- type: buff

- affected1: Lash

- affected2: Flog H McGinnis

- text: Fixed certain rooftops allowing turrets to be built on them

- type: fix

- affected1: McGinnis

- affected2: Mini Turret H Mo & Krill

- text: healing against non-heroes reduced from 1x to 0.7x

- type: nerf

- affected1: Mo & Krill

- affected2: Scorn

- text: no longer prevents enemies from reloading while disarmed

- type: nerf

- affected1: Mo & Krill

- affected2: Sand Blast H Paradox

- text: Max Damage Amp reduced from 125% to 100%

- type: nerf

- affected1: Paradox

- affected2: Kinetic Carbine

- text: range reduced from 45m to 40m

- type: nerf

- affected1: Paradox

- affected2: Paradoxical Swap H Pocket

- text: T3 added, now heals Pocket for 100% of its damage (33% vs non-heroes)

- type: change

- affected1: Pocket

- affected2: Barrage

- text: Fixed some issues with projectiles getting caught on map geometry

- type: fix

- affected1: Pocket

- affected2: Barrage

- text: pathing improved, it will no longer bounce erratically off map geometry

- type: fix

- affected1: Pocket

- affected2: Flying Cloak H Vindicta

- text: T3 reduced from +4m/s to +3m/s

- type: nerf

- affected1: Vindicta

- affected2: Flight

- text: T3 improved from -30% Healing Suppression to -40%

- type: buff

- affected1: Vindicta

- affected2: Crow Familiar H Warden

- text: travel speed increased from 800 to 1000

- type: buff

- affected1: Warden

- affected2: Alchemical Flask H Wraith

- text: no longer has a cast delay

- type: buff

- affected1: Wraith

- affected2: Royal Flush

- text: time to spawn cards increased from 0.4s to 0.6s

- type: nerf

- affected1: Wraith

- affected2: Royal Flush

- text: no longer allows the victim to shoot back

- type: buff

- affected1: Wraith

- affected2: Telekinesis H Yamato

- text: renamed to and reworked into a new ability

- type: change

- affected1: Yamato

- affected2: Shadow Transformation

- text: no longer has radius impact behavior

- type: change

- affected1: Yamato

- affected2: Shadow Transformation

- text: now gives you 4.5s of invulnerability after the initial 2s invulnerable channel period. You transform and refresh your abilities, improving ability speeds by 60% and gaining unlimited ammo. "Ability Speeds" affects Power Slash cast time, Flying Strike flying time, and Crimson Slash cast time.

- type: change

- affected1: Yamato

- affected2: Shadow Transformation

- text: cooldown increased from 90s to 100s

- type: nerf

- affected1: Yamato

- affected2: Shadow Transformation

- text: T2 is now +4 m/s during Shadow Form

- type: change

- affected1: Yamato

- affected2: Shadow Transformation

- text: T3 is now +1s duration

- type: change

- affected1: Yamato

- affected2: Shadow Transformation
