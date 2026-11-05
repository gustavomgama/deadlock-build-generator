---
title: "Patch/Playtest/2024-07-04"
pageid: 572
source: liquipedia-deadlock-md
---

- name: Playtest - July 04 2024

- version: 2024-07-04

- release: July 04, 2024

- highlight1: Gameplay Updates

- highlight2: HUD Updates

- highlight3: Item Updates

- highlight4: Hero Updates

- previous: Patch/Playtest/2024-06-272024-06-27

- next: Patch/Playtest/2024-07-112024-07-11

## General

Added Asia servers and matchmaking region. Testing times for this region are Mon-Thur 5PM to 3AM and Fri-Sun 3PM to 3AM in China Standard Time (GMT+8).

Added South America servers and matchmaking region. Testing times for this region are Mon-Thur 5PM to 3AM and Fri-Sun 3PM to 3AM in Atlantic Standard Time (GMT-4).

Added a new Damage Report feature. You can now open a flyout panel within the shop to view a breakdown of your hero's incoming and outgoing damage throughout the course of a match. You can also hover an enemy hero to view a quick breakdown of their key stats and items. The data can be filtered by last respawn, 10 minutes, 5 minutes, 3 minutes, 1 minute, or 30 seconds.

Reworked the top bar HUD to reduce overall height While spectating or watching replays, the game now has a free cursor mode without needing to hold modifiers down (defaulted to on). Can toggle it off while spectating using the 'J' key.

Minimap now displays dead heroes for 5 seconds after their death Reworked the default suggested items for heroes to be much more simple (oriented more strongly for new player onboarding) Parties will now be a little more likely to be in the same lane, if there isn't a wide skill gap or other factors preventing it All instances of collecting souls (whether claiming your own or denying an opponent) will share the same sound. Being denied a soul orb by an enemy will have its own unique sound.

Fixed the HUD cooldown state thrashing while picking up the Soul Urn Fixed Spectral Wall sometimes not spawning depending on the map geometry nearby Added descriptive tooltips to Render and Audio options within settings. Render tooltips include an estimate of performance impact where applicable.

Fixed a bug where bullets could penetrate close range targets and hit 2 targets when not intended (was primarily obvious with neutral farming) Reduced the end of match delay from 10s to 4s

- text: Added a shatter sound effect for meleeing the mid boss

- type: change

- affected1: Rejuvenator Added ghost models inside the doorways of the juke closets to help clarify which are dead ends

- text: Fixed position of the "All Destroyed" Flex slot to be the 2nd slot rather than the 4th

- type: fix

- affected1: Walker Added a sound for when Infernus's Afterburn procs

- text: Added pickup sound

- type: change

- affected1: Rejuvenator Minimap now highlights Soul Urn dropoff location Updated Wraith Full Auto cast sound Added audio feedback for environmental damage Fixed sounds associated with last hit playing unreliably Updated sounds for Wraith Card Trick projectile, impact, and when you gain a card Added traffic and construction ambient sounds and updated general ambience mix

## Gameplay

Urn count changed from 2 to 1 (previous souls value restored) Urn pickup location moved to closer to the outer lanes (on the opposite side of the lane pillar, facing towards the bridge) Urn drop-off location now move to the same spot as the pickup (opposite end of the map, depending on which location the Urn spawns in) Urn pickup time reduced from 4s to 2s Urn now has a 2s drop-off time Urn no longer applies a 15% slow Urn now prevents you from using the zipline while carrying it The person delivering the urn now gets +25% soul bonus Reworked how Powerups work. There are now only 2 locations where they spawn instead of 6 (the two at the strong camps near the middle far edges of the map). The different powerup types are reduced from 6 to 4 and they have been reworked: Gun: +30% Clip and +20% Fire Rate for 100s Survival: +400 Max HP and +1% HP Regen for 100s Casting: +20% Cooldown Reduction and +25 Spirit for 100s Movement: +2 Stamina, +2 Sprint and +30% zipline boost for 100s Powerups now always cycle which ones spawn until they have each spawned, and then they are randomly allocated again

- text: Base and now have +40% Bullet Resistance. They lose 20% for each enemy hero nearby (down to a minimum of 0% bullet resistance). When they haven't taken damage for 60 seconds, they regenerate 4% max hp per second.

- type: buff

- affected1: Guardian

- affected2: Shrine

- text: Fixed not using their stomp properly

- type: fix

- affected1: Walker Troopers now deal 25% less damage to other troopers Troopers spawn rate before 10 minutes is now the same as after 10 minutes (30s->25s) Breakables are no longer pre-placed on the map, they now spawn in when they are able to roll for drops (3 minutes) Breakables now use pseudorandom rolls (makes streaks of success or failure less likely)

- text: [Golden Statue](Golden Statue.md) bonuses now have some dynamic weighting based on what has already dropped (makes it less likely that you have too many of one specific bonus over the course of the game)

- type: change

- affected1: Golden Statue

- text: [Golden Statue](Golden Statue.md) Cooldown Reduction bonus increased from 0.5% to 0.75%

- type: buff

- affected1: Golden Statue

- text: After 25 minutes, the Golden Statue bonuses that drop are slightly stronger: Max HP: +15 to +20 Weapon Damage: +2% to +3% Spirit Power: +2 to +3 Fire Rate: +1.5% to +2% CD Reduction: 0.75% to 1% Ammo: 3% to 5%

- type: buff

- affected1: Golden Statue Bullet falloff damage now starts at 25m instead of 27m Inner lane M Walker arena (Amber Orange and Sapphire Blue): Added hallway on street level from the warehouse interior to underneath the overpass Reworked stairs for defenders to reach the overpass to start near the - M Walker and exit with line of sight down the lane Added some juke closets around the map Added some balconies/awnings around the map Shortened the underground tunnels from the Subway entrance side Doorways into the Authority Building and Jazz Club are now offset Moved the new cover barrier in front of the inner lane Guardian closer to the Guardian

## Items

- I Headshot Booster

- text: Cooldown increased from 5s to 7s

- type: nerf

- affected1: Headshot Booster

- text: Fixed the item not visually going on cooldown when it procs

- type: fix

- affected1: Headshot Booster I Basic Magazine

- text: Ammo increased from 15% to 20%

- type: buff

- affected1: Basic Magazine I Restorative Shot

- text: Medic Bullets are renamed to Restorative Shot

- type: change

- affected1: Medic Bullets

- affected2: Restorative Shot

- text: Cooldown increased from 4s to 6s

- type: nerf

- affected1: Medic Bullets

- affected2: Restorative Shot I Monster Rounds

- text: Damage vs NPCs increased from +30% to +35%

- type: buff

- affected1: Monster Rounds I Active Reload

- text: Cooldown reduced from 25s to 23s

- type: buff

- affected1: Active Reload

- text: Active fire rate bonus increased from 15% to 18%

- type: buff

- affected1: Active Reload I Berserker

- text: Weapon Damage per stack reduced from +6% to +5%

- type: nerf

- affected1: Berserker I Titanic Magazine

- text: Reload penalty reduced from -15% to -10%

- type: buff

- affected1: Titanic Magazine I Intensifying Magazine

- text: Ammo reduced from 30% to 25%

- type: nerf

- affected1: Intensifying Magazine I Point Blank

- text: Now gives +1 Stamina

- type: buff

- affected1: Point Blank I Hunter's Aura

- text: Bullet Resist reduction reduced from -15% to -10%

- type: nerf

- affected1: Hunter's Aura

- text: Fire Rate slow reduced from -15% to -10%

- type: nerf

- affected1: Hunter's Aura

- text: Solo enemy hero case increased from 2x to 3x

- type: buff

- affected1: Hunter's Aura I Burst Fire

- text: Slide distance increased from +35% to +50%

- type: buff

- affected1: Burst Fire I Tesla Bullets

- text: Damage is now affected by falloff

- type: nerf

- affected1: Tesla Bullets

- text: Proc chance reduced from 30% to 25%

- type: nerf

- affected1: Tesla Bullets

- text: Jump radius reduced from 9m to 8m

- type: nerf

- affected1: Tesla Bullets I Escalating Resilience

- text: Now gives +14% Ammo

- type: buff

- affected1: Escalating Resilience I Lucky Shot

- text: Slow duration reduced from 2s to 1.5s

- type: nerf

- affected1: Lucky Shot

- text: No longer provides +20% Weapon Damage

- type: nerf

- affected1: Lucky Shot I Ricochet

- text: Ricochet damage increased from 45% to 50%

- type: buff

- affected1: Ricochet I Silencer

- text: Debuff duration reduced from 3s to 2s

- type: nerf

- affected1: Silencer I Crippling Headshot

- text: Bullet and Spirit Resist reductions reduced from -30% to -24%

- type: nerf

- affected1: Crippling Headshot I Siphon Bullets

- text: Steal duration increased from 15s to 20s

- type: buff

- affected1: Siphon Bullets I Sprint Boots

- text: Sprint Speed reduced from +3 to +2

- type: nerf

- affected1: Sprint Boots

- text: Now a component of Enduring Speed

- type: change

- affected1: Sprint Boots I Enduring Speed

- text: Now requires

- type: change

- affected1: Enduring Speed

- text: Now grants +2 Sprint

- type: buff

- affected1: Enduring Speed I Restorative Locket

- text: Can now be cast on allies (30m cast range)

- type: buff

- affected1: Restorative Locket

- text: Radius on gaining charges increased from 40m to 50m)

- type: buff

- affected1: Restorative Locket

- text: Cooldown increased from 18s to 24s

- type: nerf

- affected1: Restorative Locket I Reactive Barrier

- text: Now procs on displacement abilities (e.g. Hook, Paradoxical Swap, Upper Cut)

- type: buff

- affected1: Reactive Barrier I Healbane

- text: Debuff duration reduced from 7s to 6s

- type: nerf

- affected1: Healbane I Return Fire

- text: Health bonus increased from +75 to +100

- type: buff

- affected1: Return Fire

- text: Fixed spirit damage returned counting as bullet damage

- type: fix

- affected1: Return Fire I Bullet Lifesteal

- text: Increased from 22% to 24%

- type: buff

- affected1: Bullet Lifesteal I Rescue Beam

- text: Cooldown reduced from 40s to 35s

- type: buff

- affected1: Rescue Beam I Superior Stamina

- text: Removed spirit bonus when doing 2x air jumps/dash

- type: change

- affected1: Superior Stamina

- text: Now grants +8 Spirit

- type: change

- affected1: Superior Stamina

- text: Now grants +30% Air Dash and Air Jump distance

- type: change

- affected1: Superior Stamina I Fortitude

- text: Duration required to start regenerating reduced from 14s to 13s

- type: buff

- affected1: Fortitude I Majestic Leap

- text: Shields no longer prevent the item from being disabled

- type: buff

- affected1: Majestic Leap I Debuff Reducer

- text: The active now reduces the duration of existing debuffs by 80% of their current values. Grants +2m/s for 3s if a debuff was reduced.

- type: change

- affected1: Debuff Reducer

- text: Passive debuff resistance increased from 30% to 35%

- type: buff

- affected1: Debuff Reducer

- text: Now gives +125 Health

- type: buff

- affected1: Debuff Reducer

- text: Cooldown reduced from 45s to 25s

- type: buff

- affected1: Debuff Reducer I Unstoppable

- text: No longer has components (loses slow resist and movespeed bonus)

- type: nerf

- affected1: Unstoppable I Colossus

- text: Cooldown reduced from 65s to 45s

- type: buff

- affected1: Colossus

- text: Model size increase from 10% to 20%

- type: buff

- affected1: Colossus I Inhibitor

- text: No longer grants +10% Fire Rate

- type: nerf

- affected1: Inhibitor

- text: Slow reduced from 35% to 25%

- type: nerf

- affected1: Inhibitor I Leech

- text: Spirit Power increased from +7 to +10

- type: buff

- affected1: Leech

- text: Weapon Damage increased from +8% to +12%

- type: buff

- affected1: Leech

- text: Bonus Health increased from +125 to +150

- type: buff

- affected1: Leech I Shadow Weave

- text: Ambush Fire Rate reduced from +60% to +40%

- type: nerf

- affected1: Shadow Weave

- text: Cooldown increased from 35s to 45s

- type: nerf

- affected1: Shadow Weave

- text: No longer instantly grants sprint

- type: nerf

- affected1: Shadow Weave I Infuser

- text: Spirit Power reduced from +18 to +16

- type: nerf

- affected1: Infuser I Extra Spirit

- text: Now gives +25 Health

- type: buff

- affected1: Extra Spirit I Quicksilver Reload

- text: Cooldown increased from 5s to 12s

- type: nerf

- affected1: Quicksilver Reload I Withering Whip

- text: Now grants +50 Health

- type: buff

- affected1: Withering Whip I Suppressor

- text: Duration reduced from 2.5s to 2s

- type: nerf

- affected1: Suppressor I Decay

- text: Bleed damage increased from 2.6% of current HP to 2.8%

- type: buff

- affected1: Decay

- text: Spirit bonus increased from +5 to +7

- type: buff

- affected1: Decay I Duration Extender

- text: Now grants +1.5 hp regen

- type: buff

- affected1: Duration Extender I Bullet Resist Shredder

- text: Debuff duration increased from 6s to 8s

- type: buff

- affected1: Bullet Resist Shredder

- text: Now gives +5% Bullet Armor

- type: buff

- affected1: Bullet Resist Shredder I Mystic Slow

- text: Duration reduced from 2.5s to 2s

- type: nerf

- affected1: Mystic Slow I Improved Burst

- text: No longer applies 50% slow

- type: change

- affected1: Improved Burst

- text: Now grants +100 Spirit Shield Health

- type: change

- affected1: Improved Burst

- text: Now grants +12% Weapon Damage

- type: change

- affected1: Improved Burst I Superior Duration

- text: Imbued duration increased from +30% to +32%

- type: buff

- affected1: Superior Duration

- text: Non-imbued duration increased from +22% to +24%

- type: buff

- affected1: Superior Duration I Improved Spirit

- text: Now grants +75 Health

- type: buff

- affected1: Improved Spirit I Knockdown

- text: Cooldown increased from 30s to 45s

- type: nerf

- affected1: Knockdown I Ethereal Shift

- text: Cooldown reduced from 30s to 25s

- type: buff

- affected1: Ethereal Shift I Mystic Reverb

- text: The target is now slowed by 50% during the 3s delay

- type: buff

- affected1: Mystic Reverb I Diviner's Kevlar

- text: Now provides +8% Cooldown Reduction

- type: buff

- affected1: Diviner's Kevlar

- text: Fixed the duration missing in the tooltip

- type: fix

- affected1: Diviner's Kevlar

- text: Buff duration increased from 10s to 12s

- type: buff

- affected1: Diviner's Kevlar

- text: Now grants +700 Spirit Shield and +700 Bullet Shield

- type: buff

- affected1: Diviner's Kevlar I Escalating Exposure

- text: Now has a base of -12% Spirit Resist reduction

- type: change

- affected1: Escalating Exposure I Boundless Spirit

- text: Health Regen increased from +10 to +15

- type: buff

- affected1: Boundless Spirit

- text: Bonus Health increased from +200 to +300

- type: buff

- affected1: Boundless Spirit

## Heroes

- H Abrams

- text: T3 is now Gain +100 Max HP and +15% Fire Rate per enemy hero hit for 25s

- type: change

- affected1: Abrams

- affected2: Seismic Impact H Bebop

- text: Base HP regen reduced from 2 to 1

- type: nerf

- affected1: Bebop

- text: cast range increased from 60m to 70m

- type: buff

- affected1: Bebop

- affected2: Hyper Beam H Grey Talon

- text: now grants +4 permanent Spirit Power for each hero killed with it

- type: buff

- affected1: Grey Talon

- affected2: Guided Owl

- text: Fixed not piercing if it collides with a Mini Turret

- type: fix

- affected1: Grey Talon

- affected2: Charged Shot H Haze

- text: no longer instantly grants sprint

- type: nerf

- affected1: Haze

- affected2: Smoke Bomb

- text: duration increased from 6s to 8s

- type: buff

- affected1: Haze

- affected2: Smoke Bomb

- text: T1 is now -15s CD

- type: change

- affected1: Haze

- affected2: Smoke Bomb

- text: T2 is now +6 Invis Sprint

- type: change

- affected1: Haze

- affected2: Smoke Bomb

- text: T3 is now Gain +30% Bullet Lifesteal for 8s

- type: change

- affected1: Haze

- affected2: Smoke Bomb

- text: T1 changed from +1s Sleep Duration to Drains 1 Stamina

- type: change

- affected1: Haze

- affected2: Sleep Dagger H Infernus

- text: dps linger duration increased from 0.4s to 1s

- type: buff

- affected1: Infernus

- affected2: Flame Dash H Ivy

- text: Fixed some bugs with that caused it to sometimes disconnect/reconnect unintentionally

- type: fix

- affected1: Ivy

- affected2: Watcher's Covenant

- text: distance threshold to pick a new target increased from 2.5m to 6m

- type: buff

- affected1: Ivy

- affected2: Watcher's Covenant

- text: can now be cast again on an ally while the buff is active to make it prioritize that hero when possible

- type: buff

- affected1: Ivy

- affected2: Watcher's Covenant H Kelvin

- text: Fixed not going where you had targeted if you moved quickly during the cast

- type: fix

- affected1: Kelvin

- affected2: Frost Grenade

- text: T3 bonus now lingers for 6s extra

- type: buff

- affected1: Kelvin

- affected2: Ice Path H Lash

- text: time to lock on increased from 0.8s to 0.9s

- type: nerf

- affected1: Lash

- affected2: Death Slam H McGinnis

- text: damage reduction against troopers/neutrals increased from -30% to -40%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: damage reduction against objectives increased from -50% to -60%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: falloff damage increased from -30% to -35%

- type: nerf

- affected1: McGinnis

- affected2: Mini Turret

- text: cooldown reduced from 30s to 28s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: recharge time reduced from 6s to 5s

- type: buff

- affected1: McGinnis

- affected2: Mini Turret

- text: T1 and T2 swapped

- type: buff

- affected1: McGinnis

- affected2: Spectral Wall

- text: T1 stamina drain reduced from 2 to 1

- type: nerf

- affected1: McGinnis

- affected2: Spectral Wall H Mo & Krill

- text: Fixed not gaining bonus HP when enemies died during it unless you got the killing blow

- type: fix

- affected1: Mo & Krill

- affected2: Combo

- text: Health growth per boon reduced from 47 to 44

- type: nerf

- affected1: Mo & Krill

- text: While burrowed you have the same cast rules as the unborrow phase (i.e. can cast items and Scorn)

- type: change

- affected1: Mo & Krill

- affected2: Burrow H Seven

- text: cast range now scales with Spirit (0.1)

- type: buff

- affected1: Seven

- affected2: Static Charge H Vindicta

- text: cooldown reduced from 50s to 45s

- type: buff

- affected1: Vindicta

- affected2: Flight

- text: up and down speed improved a bit

- type: buff

- affected1: Vindicta

- affected2: Flight H Warden

- text: now drains 1 stamina from the target on cast

- type: buff

- affected1: Warden

- affected2: Binding Word H Wraith

- text: T3 cooldown reduced from -35s to -30s

- type: buff

- affected1: Wraith

- affected2: Project Mind
