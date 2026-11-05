---
title: "Street Brawl"
pageid: 21274
source: wiki-md
---

- [Seven](Seven.md)

- Only those who keep their wits about them will survive.

Street Brawl is a fast-paced, 4v4, combat-focused game mode in [Deadlock](Deadlock.md), offering a short game format designed for quick sessions. Street Brawl removes the standard [soul](Souls.md) economy entirely, placing players in a best-of-five series of skirmishes with the ability to obtain a fixed amount of items each round.

Before each round, players will be presented with three sets of three items to choose from. Players can choose to reroll one set of items each round. Players who queued for Street Brawl with the random hero option will be given an additional reroll for the first three rounds. Street Brawl has exclusive legendary [items](items.md) not available in standard matches. Additionally, both normal and legendary items can appear as "enhanced" versions, with improved numerical stats. If a player is presented with an item that normally upgrades from an item they have already chosen, they will be given another item of a lower tier as a bonus.

Having access to the same number of items reduces the likelihood of one particular player snowballing ahead of others, and players do not need to make decisions about what objectives to focus on. Each round, all abilities start ready to use, except for ultimate abilities, which start on a heavily reduced cooldown.

Street Brawl matches do not affect the player's matchmaking rating in standard mode.

Street Brawl was added in the [Old Gods, New Blood](Update_January 22, 2026.md) update.

## Overview

Team Size: 4v4 Format: Best-of-Five (First team to win

- get_streetbrawl_param

- m_iScoreToWin rounds wins the match). The team who takes down the [Guardian](Guardian.md) wins the round. Once a team wins 2 rounds, the enemy Guardian is removed and their final objective is to take down a [Walker](Walker.md).

Round Duration:

- get_streetbrawl_param

- m_vecRoundLengthMinutes

- 1 minutes. After this, the round goes into Overtime. If the round reaches

- get_streetbrawl_param

- m_vecRoundLengthMinutesUrgent

- 1 minutes, "Urgent" Overtime begins.

Ability Points: Every player receives

- get_streetbrawl_param

- m_vecAPPerRound

- 1 ability points in rounds 1 and 2,

- get_streetbrawl_param

- m_vecAPPerRound

- 3 points in rounds 3 & 4, and

- get_streetbrawl_param

- m_vecAPPerRound

- 5 points in round 5.

Boons: Players start with 10 boons in the first round. The number of boons received increases to 19, 25, 30 and finally 34 in the following rounds.

Base Respawn Times:

- get_streetbrawl_param

- m_vecRespawnTimes

- 1 seconds in rounds 1 & 2, and

- get_streetbrawl_param

- m_vecRespawnTimes

- 3 seconds in rounds 3-5.

Draft Time: Players have

- get_streetbrawl_param

- m_vecBuyTime

- 1 seconds to draft items each round.

## Legendary Items

There are Street Brawl Legendary items exclusive to this mode.

- Weapon Weapon Haunting Shot: Your next bullet deals additional [Spirit Damage](Spirit Damage.md) based on the enemy's current [Health](Health.md). This bullet is larger and pierces through enemies, applying a debuff which reduces the enemy's healing, movement speed, and damage outputs.

- Infinite Rounds: Your bullets have a chance to become unavoidable, piercing through enemies and ignoring their [Bullet Resistance](Bullet Resistance.md). You have infinite [Ammo](Ammo.md).

- Runed Gauntlets: Your next [Melee](Melee.md) pierces through parry. Landing a heavy melee reduces your existing [Cooldown](Cooldown.md)s.

- Armor Vitality Celestial Blessing: On use, applies a [cleansing](Dispel Magic.md) effect to your whole team, replenishing their [health](health.md) and [stamina](stamina.md) while increasing their [movement speed](Move Speed.md).

- Cloak of Opportunity: Occasionally block the next [debuff](debuff.md) that would apply movement lock, stunned, immobilized, chained, or slept to you, instead granting a temporary [barrier](Damage Barrier.md) and [movement speed](Move Speed.md), as well as a temporary [Unstoppable](Unstoppable.md) effect.

- Electric Slippers: While sliding, [evade](Bullet Evasion.md) bullets and gain increased [fire rate](Fire Rate.md) while dealing periodic [Spirit Damage](Spirit Damage.md) to nearby enemies.

- Eternal Gift: Every 2 seconds, provides a random permanent [stat buff](Stats.md) to your hero, while also occasionally dramatically reducing your next [respawn timer](Respawn.md).

- Nullification Burst: On use, removes any [positive buffs](Status Effects.md) on nearby enemies while blocking them from using any [stamina](stamina.md) or [healing](healing.md) for a short duration.

- Seraphim Wings: Massively reduces your gravity, granting you large amounts of [damage amplification](Damage Amplification.md) and [damage reduction](Damage Reduction.md) while airborne. Also passively grants improved air control and allows for an additional [air dash](Dash.md) or [air jump](Jumping.md) before landing.

- Shadow Strike: Any [stamina use](Stamina.md) causes you to become temporarily [invisible](Status Effects.md#Stealth). Dealing damage with a [melee attack](Melee Attack.md) while invisible applies periodic [spirit damage](Spirit Damage.md) while stealing [bullet and spirit resistances](Damage Resistance.md).

- Tech Spirit Frostbite Charm

- [Imbue](Imbue.md) an ability to grant it [cooldown reduction](Cooldown Reduction.md) and [spirit power](Spirit Power.md). When the imbued ability damages a target, it [freezes](Arctic Blast.md) them, dealing bonus [spirit damage](Spirit Damage.md).

- Mystic Conduit

- Passively provides a significant increase to [ability range](Ability Range.md) and [cooldown reduction](Cooldown Reduction.md) for self and nearby allies. Dealing high damage to an enemy Hero within a short period of time [heals you and nearby allies](Healing Nova.md).

- Mystical Piano

- On use, strikes the target area after a short delay with a large piano, [stunning](Stun.md) and reducing the [stamina](stamina.md) of any enemies hit. For a short duration after the stun, enemies are [dazed](Daze.md).

- Omnicharge Signet

- [Imbue](Imbue.md) an active non-ultimate ability to grant it [charges](charges.md). Already charge-based abilities gain even more charges.

- Prism Blast

- On use, [become untargetable and invincible](Ethereal Shift.md) for a short duration while [damaging lasers](Bebop.md#(4)-Hyper-Beam) rotate around you.

- Shrink Ray

- On use, significantly reduces self or target ally hero's model size for a duration while granting significantly increased [movement speed](Move Speed.md).

- Unstable Concoction

- On use, grants massively increased [movement speed](Move Speed.md), [health](health.md), [spirit power](Spirit Power.md), and [weapon damage](Weapon Damage.md) for a short duration before you explode, instantly [dying](Death.md) but also dealing large area damage based on your [max health](Health.md) and [stunning](Stun.md) enemies.

## Game Mode-Specific Differences

Street Brawl-specific balance changes are marked in the ability/item description in Street Brawl with a yellow circle icon.

1. Heroes All hero abilities have their range and radius reduced by 10%.

Some heroes have additional changes to their individual abilities. More info can be found on respective hero page: category=Heroes with Street Brawl changes mode=userformat ordermethod=title listseparators=,

- %TITLE%,, 1. Items Range and radius for all items is reduced by 10% Alchemical Fire: Damage reduced by 30% Cursed Relic: Duration reduced from 3.25s to 2.75s Golden Goose Egg: Disabled in this mode Mystic Expansion: Radius bonus reduced from +20% to +16% Greater Expansion: Radius bonus reduced from +30% to +25% 1. Structures Health Scaling: The defending [Guardian](Guardian.md) or [Walker](Walker.md)'s base health scales up each round: Round 1:

- get_streetbrawl_param

- m_vecObjectiveMaxHealth

- 1 Round 2:

- get_streetbrawl_param

- m_vecObjectiveMaxHealth

- 2 Round 3:

- get_streetbrawl_param

- m_vecObjectiveMaxHealth

- 3 Round 4:

- get_streetbrawl_param

- m_vecObjectiveMaxHealth

- 4 Round 5:

- get_streetbrawl_param

- m_vecObjectiveMaxHealth

- 5 Comeback Bonus: If a team is losing, their defending objective is granted bonus health. A losing team gets +

- get_streetbrawl_param ComebackBonusHealth health added to their objective. If they are at match point, they get +

- get_streetbrawl_param ComebackBonusHealthCritical health.

When the objective is a [Walker](Walker.md), it gains an additional +

- get_streetbrawl_param Tier2BonusHealth health.

[Structures](Structures.md) have faster and increased resist decay over time.

[Guardians](Guardians.md) have [Backdoor Protection](Walker.md#Backdoor_protection).

1. NPCs [Neutrals](Neutral.md) do not spawn in Street Brawl.

[Troopers](Trooper.md) spawn faster (every

- get_streetbrawl_param TrooperSpawnTimer

- 1 s in early rounds,

- get_streetbrawl_param TrooperSpawnTimer

- 3 s in later rounds) and spawn

- get_streetbrawl_param TrooperSpawnBeforeRoundStartTimer seconds before the round officially begins. They have starting [Spirit Resist](Spirit Resist.md) and increased Spirit Resist during overtime, and deal more damage to structures.

Incoming Trooper waves cannot be shot off the [Zipline](Ziplines.md).

1. Overtime Mechanics If a round exceeds the standard time limit, it enters Overtime.

Trooper Buffs: During Overtime, Troopers gain a health and damage multiplier that scales up each round: Rounds 1, 2, and 3: Health x

- get_streetbrawl_param OvertimeTrooperHealthScale

- 1, Damage x

- get_streetbrawl_param OvertimeTrooperDamageScale

- 1 Round 4: Health x

- get_streetbrawl_param OvertimeTrooperHealthScale

- 4, Damage x

- get_streetbrawl_param OvertimeTrooperDamageScale

- 4 Round 5: Health x

- get_streetbrawl_param OvertimeTrooperHealthScale

- 5, Damage x

- get_streetbrawl_param OvertimeTrooperDamageScale

- 5 Respawn Penalties: Player respawn times are increased: Standard Overtime adds

- get_streetbrawl_param OvertimeRespawnTimeIncrease

- 1

- get_streetbrawl_param OvertimeRespawnTimeIncrease

- 5 seconds to the base respawn time.

Urgent Overtime adds

- get_streetbrawl_param OvertimeRespawnTimeIncreaseUrgent

- 1

- get_streetbrawl_param OvertimeRespawnTimeIncreaseUrgent

- 5 seconds to the base respawn time.

1. Other differences Players cannot pause in Street Brawl.

[Healing](Healing.md) in base is twice as fast as standard play.

[Ziplines](Ziplines.md) have a modified cooldown on round start of

- get_streetbrawl_param ZipBoostCooldownOnStart seconds.

There is no item limit. If a player gets more than 12 items, their item UI will expand to accommodate the additional items.

## Item Draft

See "Item Draft" in individual [Hero](Hero.md) pages to see the chance of getting certain items for each hero.

While all heroes have a random chance to get any item, some items are weighted to be more likely to drop for specific heroes, and some counter items are more likely to drop when playing against specific heroes. Using a reroll will drop items of similar tier and rarity as the items in the current roll. Choosing the random hero option in character select allows the player to have an extra item reroll in the first 3 rounds. Item drops are mirrored between teams: if a player on one team is offered a rare, enhanced, or legendary item drop, a player on the enemy team will be offered an equivalent item drop.

1. Draft Tier Progression Each round, players are presented with 3 sets of items to choose from. The available tiers scale up as the match progresses to ensure players get access to stronger items later in the game: Round 1: Tiers 1, 2, and 3 Round 2: Tiers 2 and 3 Round 3: Tiers 2, 3, and 4 Round 4: Tiers 3 and 4 (with a chance for Tier 5 Legendary) Round 5: Tier 4 (with a chance for Tier 5 Legendary) 1. Counter Items These items are more likely to drop for a player in Street Brawl when playing against their corresponding hero.

- counters_table

## Strategy

Since [Troopers](Trooper.md) don't drop [Souls](Souls.md) in Street Brawl, players are less encouraged to hit them. However, pushing waves is still valuable to gain healing from Banner Troopers and pressure the enemy's objectives.
