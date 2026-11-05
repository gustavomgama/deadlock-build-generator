---
title: "Patch/Playtest/2024-11-21"
pageid: 1523
source: liquipedia-deadlock-md
---

- name: Playtest - November 21 2024

- version: 2024-11-21

- highlight1: Matchmaking Rework

- highlight2: Hero Updates

- highlight3: Item Updates

- highlight4: Gameplay Updates

- highlight5: Heal/Anti Heal Rebalance

- highlight6: New Items: Spirit Snatch, Arcane Surge and Spellslinger Headshots

- release: November 21, 2024

- previous: Patch/Playtest/2024-11-132024-11-13

- next: Patch/Playtest/2024-11-242024-11-24

## Matchmaking Rework

This update includes a new version of the matchmaker. The matchmaking pools are no longer split between normal and ranked, there is only one primary matchmaking mode and there are no limited hours.

Badges will update immediately whenever you gain or lose enough MMR to change badges. You no longer have to wait a week or play a certain game count. There will sometimes be monthly global maintenance updates where we readjust the global curve based on the population, cheaters banned, recalculation adjustments, etc (this will be done as needed and not necessarily every month).

Hero MMR is now used in the Matchmaker. Each player will have a "core" MMR and your MMR per hero will be offsets of your core MMR. When you queue, we will match you based on that hero's MMR. So if you are unfamiliar or play worse with a given hero, you will be put in an easier match than your usual. Judgement on your skill and familiarity with a hero will be based on the 20 most recent games with that hero. In your profile, we have UI that shows you what the matchmaker thinks your relative ranking for each hero is (give us feedback on this, we expect to iterate on this calculation).

Leaderboards are also included per region (North America, South America, Europe, Asia, Oceania). There is a top 1000 Core MMR leaderboard as well as a top 1000 Hero MMR leaderboard for each hero (for each region separately). To qualify for being considered in leaderboards in general, you must have 50 games played in the last 30 days. To qualify for a specific hero's leaderboard, you must have played at least 20 games on that hero in the past 30 days.

You can queue as any party size, however there are a few details. If the range of skill in your party is too wide, the amount of MMR you can gain will be reduced somewhat based on the degree. This is especially true if it’s a player we don't know anything about (like a very high mmr player queuing with a "new" player, we will minimize updates to the known player until we are more confident we can trust the skill of that party overall).

The previous limit on high MMR party sizes is increased from 2 to 3. This applies to Ascendant 1 and above. This is the old limit we had on disallowing too many high MMR players to be in the same party together, for matchmaking quality reasons.

Given the updated no hour limits, if we think a match is a bad quality (like 5am games where there weren't a lot of players to pick from), we will weigh the match less heavily towards a rank update relative to what we would do with an average quality match.

If you prefer playing with only solos, there is a convar (mm_prefer_solo_only) you can use.

When queuing as a party, you will have an option to override the default balance oriented lane assignment system and make the system prioritize putting your party members in the same lanes together.

Added Swap Lanes feature. During the rooftop and zipline phase at the start of the game, you can now request to swap lanes with your teammates by clicking the button below their portrait on the scoreboard. If the other player accepts your request, you will immediately be swapped. You may decline an incoming request by right clicking it.

There is an option to notify you anytime your rank levels up. There is also an option to show the average badge of each team for the post game.

## Items

- M Weapon I Rapid Rounds

- text: Fire Rate increased from 10% to 11%

- type: buff

- affected1: Rapid Rounds I Monster Rounds

- text: Bonus Health reduced from 50 to 30

- type: nerf

- affected1: Monster Rounds I Berserker

- text: Weapon Damage per stack increased from 5% to 6%

- type: buff

- affected1: Berserker I Soul Shredder Bullets

- text: Spirit Amp reduced from 10% to 8%

- type: nerf

- affected1: Soul Shredder Bullets

- text: Spirit Lifesteal reduced from 20% to 18%

- type: nerf

- affected1: Soul Shredder Bullets I Headhunter

- text: Head Shot Bonus Damage reduced from +140 to +130

- type: nerf

- affected1: Headhunter

- text: Heal per Headshot reduced from 8% to 7%

- type: nerf

- affected1: Headhunter I Heroic Aura

- text: Cooldown reduced from 25s to 20s

- type: buff

- affected1: Heroic Aura

- text: Bullet Lifesteal reduced from 20% to 18%

- type: nerf

- affected1: Heroic Aura I Alchemical Fire

- text: DPS burn lingers on targets for 1s

- type: change

- affected1: Alchemical Fire I Hunter's Aura

- text: Fire Rate slow reduced from 10% to 9%

- type: nerf

- affected1: Hunter's Aura I Glass Cannon

- text: Now requires and grants the slow passive

- type: change

- affected1: Glass Cannon

- affected2: Slowing Bullets I Silencer

- text: Reworked item. Passively builds up on enemies, silencing for 2s and then reducing spirit damage output by 40% for 4s. Enemies affected cannot be affected again for 12s. Grants +20% Weapon Damage, +15% Spirit Resist and 20% Debuff Reduction. (Buildup is a bit slower than

- type: change

- affected1: Silencer I Lucky Shot

- text: Damage multiplier increased from 90% to 110%

- type: buff

- affected1: Lucky Shot

- text: Now grants +150 Bullet Shield

- type: change

- affected1: Lucky Shot I Toxic Bullets

- text: Healing Reduction reduced from 65% to 50%

- type: nerf

- affected1: Toxic Bullets I Active Reload

- text: Bullet Lifesteal reduced from 20% to 18%

- type: nerf

- affected1: Active Reload I Vampiric Burst

- text: Bullet Lifesteal reduced from 100% to 80%

- type: nerf

- affected1: Vampiric Burst Spellslinger Headshots

- text: New T3 Weapon Item: Requires. Landing a headshot on enemy heroes increases your total Spirit Power by 3% for 12s. Cooldown 1.5s. Max stacks 12. Grants +12% Weapon Damage, +8% Spirit Amp/18% Spirit Lifesteal (component passive), and +150 Health.

- type: change

- affected1: Spellslinger Headshots

- affected2: Soul Shredder Bullets M Vitality I Melee Lifesteal

- text: Lifesteal reduced from 20% to 18%

- type: nerf

- affected1: Melee Lifesteal

- text: Now grants +3% Bullet Resist

- type: change

- affected1: Melee Lifesteal I Reactive Barrier

- text: Bullet Shield health reduced from 400 to 350

- type: nerf

- affected1: Reactive Barrier I Return Fire

- text: Now requires

- type: change

- affected1: Return Fire

- affected2: Extra Regen I Debuff Reducer

- text: Debuff Resist reduced from 30% to 28%

- type: nerf

- affected1: Debuff Reducer

- text: Weapon Damage increased from 6% to 8%

- type: buff

- affected1: Debuff Reducer I Divine Barrier

- text: Now has +8% Ability Range again instead of +6 Spirit Power

- type: change

- affected1: Divine Barrier

- text: No longer grants +1 Sprint

- type: change

- affected1: Divine Barrier I Healing Nova

- text: No longer has +6% Ability Range

- type: change

- affected1: Healing Nova I Healbane

- text: Duration increased from 6s to 7s

- type: buff

- affected1: Healbane

- text: Healing Reduction reduced from 45% to 40%

- type: nerf

- affected1: Healbane I Debuff Remover

- text: Active buff duration on purge increased from 3s to 4s

- type: buff

- affected1: Debuff Remover

- text: Purging a debuff now also heals you for 10% Max HP

- type: change

- affected1: Debuff Remover I Rescue Beam

- text: Heal reduced from 26% to 24%

- type: nerf

- affected1: Rescue Beam

- text: Now grants +6% Ability Range

- type: change

- affected1: Rescue Beam

- text: Cooldown increased from 26s to 36s

- type: nerf

- affected1: Rescue Beam

- text: Pull speed reduced by 15%

- type: nerf

- affected1: Rescue Beam I Metal Skin

- text: Active now reduces your Move Speed by 1.5

- type: change

- affected1: Metal Skin I Superior Stamina

- text: Now grants +75 Health

- type: change

- affected1: Superior Stamina

- text: Now increases Wall Jump count by 1 as well

- type: change

- affected1: Superior Stamina I Majestic Leap

- text: Now grants +6% Spirit Resist

- type: change

- affected1: Majestic Leap I Phantom Strike

- text: Cast range now ignores the Z height (similar to Lash's Death Slam)

- type: change

- affected1: Majestic Leap I Bullet Lifesteal

- text: Lifesteal reduced from 28% to 26%

- type: nerf

- affected1: Bullet Lifesteal I Restorative Locket

- text: Regen per stack reduced from 35 to 32

- type: nerf

- affected1: Restorative Locket I Spirit Lifesteal

- text: Lifesteal reduced from 23% to 22%

- type: nerf

- affected1: Spirit Lifesteal I Lifestrike

- text: Lifesteal reduced from 65% to 55%

- type: nerf

- affected1: Spirit Lifesteal I Leech

- text: Bullet Lifesteal reduced from 35% to 32%

- type: nerf

- affected1: Leech

- text: Spirit Lifesteal reduced from 35% to 32%

- type: nerf

- affected1: Leech M Spirit I Ammo Scavenger

- text: While at max stacks you gain +2 Sprint

- type: change

- affected1: Ammo Scavenger I Infuser

- text: Cooldown reduced from 37s to 32s

- type: buff

- affected1: Infuser I Decay

- text: Healing Reduction reduced from 70% to 55%

- type: nerf

- affected1: Decay

- text: Damage increased from 1% to 1.4%

- type: buff

- affected1: Decay

- text: Healing Reduction reduced from 70% to 55%

- type: nerf

- affected1: Decay

- text: Cast delay changed from 0.25s to 0.1s, to match other similar actives

- type: change

- affected1: Decay

- text: No longer interrupts sliding, to match other similar actives

- type: change

- affected1: Decay I Withering Whip

- text: Cooldown reduced from 18s to 15s

- type: buff

- affected1: Withering Whip

- text: No longer interrupts sliding, to match other similar actives

- type: change

- affected1: Withering Whip I Improved Spirit

- text: Health increased from 100 to 125

- type: buff

- affected1: Improved Spirit I Silence Glyph

- text: No longer a tracking projectile using a unit target, releases an aim-based projectile that silences on impact

- type: change

- affected1: Silence Glyph

- text: Cooldown reduced from 32s to 24s

- type: buff

- affected1: Silence Glyph

- text: Cast delay changed from 0.0s to 0.1s, to match other similar actives

- type: change

- affected1: Silence Glyph I Ethereal Shift

- text: Post Shift now also grants +20 Spirit Power

- type: change

- affected1: Ethereal Shift I Rapid Recharge

- text: Time between charges reduced from 65% to 60%

- type: nerf

- affected1: Rapid Recharge I Knockdown

- text: Cast range now ignores the Z height (similar to Lash's Death Slam)

- type: change

- affected1: Knock Down

- text: Cast delay changed from 0.25s to 0.1s, to match other similar actives

- type: change

- affected1: Knock Down

- text: No longer interrupts sliding, to match other similar actives

- type: change

- affected1: Knock Down I Mystic Slow

- text: Now grants +1 Sprint

- type: change

- affected1: Mystic Slow

- text: Health increased from 140 to 160

- type: buff

- affected1: Mystic Slow I Torment Pulse

- text: Now grants +15% Melee Resistance

- type: change

- affected1: Torment Pulse I Diviner's Kevlar

- text: No longer grants +20% Spirit Lifesteal

- type: change

- affected1: Diviner's Kevlar

- text: Now grants +7% Ability Duration

- type: change

- affected1: Diviner's Kevlar I Echo Shard

- text: Cast delay reduced from 0.3s to 0.25s

- type: buff

- affected1: Echo Shard I Mystic Reverb

- text: Damage increased from 40% to 45%

- type: buff

- affected1: Mystic Reverb I Refresher

- text: Cooldown increased from 230s to 260s

- type: nerf

- affected1: Refresher I Curse

- text: Cast delay changed from 0.0s to 0.1s, to match other similar actives

- type: change

- affected1: Curse I Slowing Hex

- text: No longer interrupts sliding, to match other similar actives

- type: change

- affected1: Slowing Hex Spirit Snatch

- text: New T3 Spirit Item: Requires. Causes your melee attacks to steal 12% Spirit Resist and 26 Spirit Power for 16s. Cooldown 6s. Buff you receive stacks if you hit different heroes. Grants +15% Melee Damage, +8% Spirit Resist, +125 Health and +1 Sprint.

- type: change

- affected1: Spirit Snatch

- affected2: Spirit Strike Arcane Surge

- text: New T3 Spirit Item: Requires. After successful Dash Jump, the next ability you use will also have +20% Range, +20% Duration and +20 Spirit Power. Grants +100 Health, +1 Stamina and +15% Slow Resist.

- type: change

- affected1: Arcane Surge

- affected2: Kinetic Dash

## Hero Labs

- H Fathom

- text: Weapon: Bullet damage per boon reduced from 0.57 to 0.35

- type: nerf

- affected1: Fathom

- text: Updated particles

- type: change

- affected1: Fathom H The Magnificent Sinclair

- text: Now always casts alongside your Assistand, at reduced damage

- type: change

- affected1: The Magnificent Sinclair

- text: Update upgrades to match new behaviors

- type: change

- affected1: The Magnificent Sinclair

- text: Reduce Spirit Scalling from 1.4 to 1.2

- type: nerf

- affected1: The Magnificent Sinclair

- text: The Magnificent Sinclair now knows the difference between rabbits and frogs, and transforms targets properly into rabbits

- type: change

- affected1: The Magnificent Sinclair

- text: Can no longer be cast on yourself

- type: change

- affected1: The Magnificent Sinclair

- text: Now applies a max speed limit, rather than increasing speed

- type: change

- affected1: The Magnificent Sinclair

- text: T3 upgrade now applies hex at full duration to all targets in the radius

- type: change

- affected1: The Magnificent Sinclair

- text: Now reloads your weapon on cast

- type: change

- affected1: The Magnificent Sinclair

- text: Now fires in a burst of two

- type: change

- affected1: The Magnificent Sinclair

- text: Spirit Damage reduced from 1x60 at 0.5 scaling to 2x30 at 0.3 scaling

- type: nerf

- affected1: The Magnificent Sinclair

- text: Tracer now matches weapon tracer

- type: change

- affected1: The Magnificent Sinclair

- text: Improve target finding

- type: change

- affected1: The Magnificent Sinclair

- text: Fix a bug where sometimes, you couldn't redirect your bolts after the Assistand casts it

- type: fix

- affected1: The Magnificent Sinclair

- text: Smooth camera transition when teleporting

- type: change

- affected1: The Magnificent Sinclair

- text: Reduce cast range from 20m to 15m

- type: nerf

- affected1: The Magnificent Sinclair

- text: Update upgrades to match new behaviors

- type: change

- affected1: The Magnificent Sinclair H Trapper

- text: Reduce initial radius from 5m to 3m

- type: nerf

- affected1: Trapper

- text: Reduce duration from 9s to 8s

- type: nerf

- affected1: Trapper

- text: Increase base cooldown from 20s to 25s

- type: nerf

- affected1: Trapper

- text: Change T1 upgrade to be -20% Spirit Damage to targets in the posion

- type: change

- affected1: Trapper

- text: Change T2 upgrade to be +4 Durations

- type: change

- affected1: Trapper

- text: Can now target creeps & troopers

- type: change

- affected1: Trapper

- text: Fixed an issue where the trap would deal damage from the other side of a wall

- type: fix

- affected1: Trapper

- text: Fixed an issue where the trap would sometimes fail to spawn

- type: fix

- affected1: Trapper H Vyper

- text: Petrify renamed to - type: change

- affected1: Vyper

- text: Visual revisions to projectile

- type: change

- affected1: Vyper

- text: No longer interrupts sliding

- type: change

- affected1: Vyper

- text: Revisions to projectile and impact to improve visibility

- type: change

- affected1: Vyper

- text: Now applies a screen effect

- type: change

- affected1: Vyper

- text: Gun: Reduce damage from 12 to 11

- type: nerf

- affected1: Vyper

- text: Gun: Tracer revisions to improve visibility due to the high fire rate

- type: change

- affected1: Vyper H Wrecker

- text: Can now jump at a reduced height while holding the ball

- type: change

- affected1: Wrecker

- text: Decrease trigger radius from 92 to 65

- type: nerf

- affected1: Wrecker

- text: New visual updates

- type: change

- affected1: Wrecker

- text: Increased base DPS from 40 to 60

- type: buff

- affected1: Wrecker

- text: Increased cast range from 12m to 15m

- type: buff

- affected1: Wrecker

- text: Now has a max range of 20m

- type: change

- affected1: Wrecker

- text: Now requires LOS to stay Latched

- type: change

- affected1: Wrecker

- text: No longer breaks enemy movement

- type: change

- affected1: Wrecker

- text: Removed fire rate buff

- type: change

- affected1: Wrecker

- text: Added 50% base heal percentage

- type: change

- affected1: Wrecker

- text: Reduced T1 upgrade from +75% to +25% heal percentage

- type: nerf

- affected1: Wrecker

- text: Increased range from 5m to 10m

- type: buff

- affected1: Wrecker

- text: Update targeting cone slightly

- type: change

- affected1: Wrecker

- text: Remove screen darkening effect on cast

- type: change

- affected1: Wrecker

- text: Astral Walk renamed to - type: change

- affected1: Wrecker

- text: New visual updates

- type: change

- affected1: Wrecker
