---
title: "Souls"
pageid: 368
source: wiki-md
---

- [Graves](Graves.md) The more they die, the stronger I become!

- Necro killstreak start 01.mp3 are a crucial element in [Deadlock](Deadlock.md), serving both as currency and experience points (XP) for heroes. Players collect souls by various means, including shooting Soul Orbs released when [Troopers](Trooper.md) die, taking [Guardian](Guardian.md)s/[Walker](Walker.md)s, killing enemy players, and finding Haunted Souls in boxes or crates. The amount of souls earned from a kill is a Bounty. Haunted souls are added to your total immediately but can drop upon death for other players to collect.

Every player starts the game with.

## Soul Values

Soul Value: Value of the target at the time. Starts at 0 min unless noted otherwise Soul Gain: How the value changes over the time of the match, measured in minutes

- heroes: 1

- trooper: 1

- denizen: 1

- mid-boss: 1

- sinners: 1

- crates: 1

- rift: 1

- urn: 1

- objectives: 1

- egg: 1

- trophy: 1

- well: 1

- summons: 1 1. First Blood bonus A player gets bonus souls when they get the first kill in a match.

1. Comeback Mechanics When a team is behind on souls, there are some "comeback mechanics" that come into play to allow the losing team to quickly catch up.

Killing an enemy hero will award up to `-1)*100`% more souls if that hero is stronger than the killer team's average networth, regardless of which team is leading in souls.

The Soul Urn will give additional souls to the team that is behind based on game duration and total soul deficit. (see [Soul Urn](Soul Urn.md#Reward-scenarios) for details) The losing team gains up to `-1)*100`% more souls from Troopers, Haunts, Sinner's Sacrifices and Objectives, based on how behind they are (peaks at `-1)*100`% max net worth difference). The first 3k in net worth difference is ignored. (This means that the first 3k souls should be subtracted when calculating comeback values, e.g. 100k to 105k is calculated as a 2k difference) After 10 minutes in a match, killing a player whose net worth is above 15% higher than the killer team's average net worth increases that player's [respawn time](Death.md). The increase varies based on the net worth difference and match duration, from +6s for 15% net worth at 10 minutes to +22s for 30% net worth at 25 minutes.

1. Catch up Mechanics Catch up mechanics allow for players with low net worth to catch up to the other players on their team.

The two players per team with the lowest net worth have a passive gain of souls per second based on the total souls per second gathered by the team (`*100`% and `*100`% for the lowest and second-lowest player, respectively). This occurs after laning phase (8 min).

For example, if a team gathered 200 souls in the last second, the lowest player earns 5 extra souls.

`*100`% of the comeback souls earned by a player above the enemy team's average networth are split equally among the two lowest players on the team.

For example: Team A has 25k average souls per player, while Team B has 30k average per player, so team A has comeback bonus. However, one of the players in Team A has 40k souls. If that player were to receive 100 comeback souls, they instead receive `)*100` souls, and the two lowest players on team A receive `/2)*100` souls each.

## Gathering Souls

Teams with fewer souls will gain more souls from all sources (see Comeback Mechanics).

1. Soul Distribution [Hero](Heroes.md) kill souls are distributed between nearby players with the following rate: To count as an assister for a player kill, you have to have damaged them in the last 10 seconds.

{| class="wikitable" +Hero Kill Soul Distribution Players % share to each player Total % 1

- get_hero_gold_share_frac

- 1 `|0|-1 * 1`% 2

- get_hero_gold_share_frac

- 2 `|0|-1 * 2`% 3

- get_hero_gold_share_frac

- 3 `|0|-1 * 3`% 4

- get_hero_gold_share_frac

- 4 `|0|-1 * 4`% 5

- get_hero_gold_share_frac

- 5 `|0|-1 * 5`% 6

- get_hero_gold_share_frac

- 6 `|0|-1 * 6`% |} Additionally, for kills with two or more players, the player who got the kill receives bonus souls.

[Trooper](Trooper.md) souls are distributed between nearby players with the following rate: {| class="wikitable" +Trooper Kill Soul Distribution Players % share to each player Total % 1

- get_trooper_gold_share_frac

- 1 `|0|-1 * 1`% 2

- get_trooper_gold_share_frac

- 2 `|0|-1 * 2`% 3

- get_trooper_gold_share_frac

- 3 `|0|-1 * 3`% 4

- get_trooper_gold_share_frac

- 4 `|0|-1 * 4`% 5

- get_trooper_gold_share_frac

- 5 `|0|-1 * 5`% 6

- get_trooper_gold_share_frac

- 6 `|0|-1 * 6`% |} Soul distribution is the same regardless if the Trooper drops a Soul Orb or if it is killed by a melee attack.

1. Haunts (Jungle Creeps) Jungle camps contain [Haunts](Haunts.md) that give souls to players on kill. They do not release soul orbs.

Souls from Haunts are split between all allied players who dealt damage to said Haunts. Unlike Hero and Trooper souls, Haunt souls are always shared equally.

Souls from Haunts are haunted souls.

1. Sinner's Sacrifices Some jungle camps contain one or more [Sinner's Sacrifice](Sinner's Sacrifice.md) machines, which grants souls to the player by hitting them with [melee attacks](Melee Attack.md). Those souls are haunted.

1. Breakables Breaking the wooden crates scattered throughout the map will have a chance to spawn some souls.

Chance for any given crate to drop souls when broken is approximately 60% Amount of souls dropped is a function of in-game time: [Souls Dropped] = 23 + 2.0*[Game Time in Minutes] For example: At 30:00 game time, a broken crate will drop 83 souls.

Breaking the heavy crates with a heavy melee always spawns souls.

Amount of souls dropped is approximately double that of wooden crates.

1. Other Trophy Collector and - Golden Goose Egg give the player passive souls per minute.

Killing cockroaches in underground tunnels grants the player 1 soul each.

## Soul Orbs

[Troopers](Trooper.md) release souls in Soul Orbs. They drop two orbs on death, one that floats and one that falls on the ground. However, if they are killed by a [Melee Attack](Melee Attack.md) they only release the ground orb, and the player instantly receives the remaining souls. This also includes [abilities](abilities.md) that deal [Melee Damage](Melee Damage.md), and - Mina's Rake.

Each orb has `*100`% of the kill bounty. The ground orb cannot be denied (they appear as white to enemies) and remains for 18 seconds before disappearing (scaling to 40 seconds after 10 minutes).

The floating orbs spawn dark-colored, and can be shot and confirmed (or denied) once they light up. Ally orbs are green and enemy orbs are orange. Hitting an enemy orb will deny their souls and grant them to the player who hit it and nearby allies. The ally team has a "grace period" of roughly 80ms to confirm their orbs. If the orb "pops" without being claimed after roughly 1 second, it's automatically rewarded to nearby allies, and if there are no allies nearby the souls are lost.

The floating orbs may be shot or hit with a [Melee Attack](Melee Attack.md) to claim the souls. Orbs can be claimed by a single bullet or pellet, regardless of damage. The bullet that hit the orb is refunded to the player's magazine. Certain abilities like Serrated Knives or - Malice can also confirm or deny orbs.

Soul confirmation accounts for latency, which in some situations can cause the player to lose the orb even if they visually seem to have hit it first.

1. Local Soul Sharing When souls are to be shared, the game checks two distances to add allied heroes to the "pool" of heroes to split the received souls: 45m from the soul orb itself when it is broken 30m from the hero that killed the Trooper If an allied hero is within either of these distances, souls are shared between the killer and those allied heroes.

1. Soul Well After 2:30 of game time pass, the well in each team's base starts releasing orbs worth 10 souls each, every two seconds. These orbs can be either green or orange-colored but behave the same regardless. The souls are split equally across all nearby living allies when the orb expires, or go entirely to the player who confirms them before expiration.

## Haunted Souls

- [The Hidden King](The Hidden King.md)'s herald

- Great job, you didn't just take their money, you took a little bit of their self respect!

Souls earned from neutral sources such as killing [Haunts](Haunts.md), destroying Sinner's Sacrifice machines, and destroying [Crates](Crates.md) are haunted and are lost on death. If a player dies with at least Convar

- citadel_player_neutral_gold_drop_min + Convar

- citadel_player_neutral_gold_drop_min_increase_per_minute /minute haunted souls they will be dropped in a Soul Bag, which can be claimed by any player by hitting it with a [Heavy Melee](Melee Attack.md). Soul Bags will despawn after 3 minutes. These bags are marked with a circle icon on the [Minimap](Minimap.md) and have a green glow effect. If a player dies with fewer than Convar

- citadel_player_neutral_gold_drop_min + Convar

- citadel_player_neutral_gold_drop_min_increase_per_minute /minute haunted souls, no Soul Bag will drop-they are permanently lost.

Haunted souls are converted into secured souls over time, meaning they will no longer be dropped on death. This conversion rate is dynamic: Percentage Drain: Each second, `*100`% of the player's current haunted souls are converted. This means larger amounts of haunted souls secure faster initially.

Base Drain: In addition to the percentage, a flat amount is secured every second. This starts at - Convar

- citadel_secure_gold_fixed souls/second and increases as the match progresses (scaling with the global bounty growth of `*100`% per minute).

Example at 10 Minutes: A player carrying 1,000 haunted souls will secure them at a rate of roughly 7.9 souls/second (5 from percentage + ~2.9 base).

Example at 20 Minutes: That same player carrying 1,000 haunted souls will secure them faster, at a rate of roughly 9.2 souls/second (5 from percentage + ~4.2 base), due to the base rate scaling over time.

Haunted souls may be spent in the shop, but are spent after secured souls. They are indicated by the silver-green ball on the Hero's hip known internally as a Soul Bag, as well as in the number on the HUD with a red icon.

Haunted souls count towards leveling up. However, if the player dies and loses those souls, they will remain at the last unlocked level but lose progress to the next level equivalent to their dropped souls.

On the character UI, the large souls number is the total number of secured and haunted souls added together.

## Leveling Up

Gathering souls will gradually "level up" your hero, granting a variety of benefits. See [boons](Boon.md) for detailed information.
