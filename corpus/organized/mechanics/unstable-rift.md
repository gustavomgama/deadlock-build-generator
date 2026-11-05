---
title: "Unstable Rift"
pageid: 38417
source: wiki-md
---

- Unstable Rift/Update history Unstable Rift/Music

- l1: Overview

- l2: Update History

- l3: Music Unstable Rift is an Objective in [Deadlock](Deadlock.md).

## Overview

When an Unstable Rift spawns, it first appears as an in-world only visual effect on top of a random side lane's bridge. 60 seconds after this effect appears, an announcement is made to all players and the Rift becomes visible on the map. 20 seconds after the announcement, the Rift opens and creates a capture point with a ` * 0.0254 round 0`m radius around the bridge, indicated by a green circle effect.

The Rift takes

- citadel_koth_cashin TotalTimeToCapture s to be captured (not counting comeback modifiers). Both teams earn progress as long as they have at least one player in the capture point, but the Rift can only be claimed once there's only one team in the point. The progress rate is the same regardless of how many players per team are in the point. Any players in the rift point are revealed on the [Minimap](Minimap.md).

A player does not contest the Rift while sent to - Hotel Guest

- l1: the Baroness by - The Doorman, or while reviving with the [Rejuvenator](Rejuvenator.md).

1. Timing Based on when the initial visual effect appears, Unstable Rifts spawn starting at 11 minutes, and respawn every 7 minutes thereafter. However, this timing is variable by up to one minute, meaning the first Rift can spawn at any time between 10 and 12 minutes, and subsequent Rifts can spawn between 6 and 8 minutes after the previous Rift.

1. Comeback mechanics The team that is trailing in souls receives bonuses that scale linearly based on how behind they are, up to a `*100`% difference in total net worth. The bonuses are dynamic and update in real time, so teams can lose or earn bonuses while contesting the rift. These bonuses are (at maximum difference): Capture time reduced to - citadel_koth_cashin TotalTimeToCaptureFavored s (` / ) * 100 round 0`% shorter) for the trailing team, and increased to - citadel_koth_cashin TotalTimeToCaptureUnfavored s (` / - 1) * 100 round 0`% longer) for the leading team.

Bonus [Bullet](Damage Resistance.md), [Spirit](Damage Resistance.md), and [Debuff Resist](Debuff Resist.md), provided within a 35m radius. The max resist starts from - citadel_koth_cashin ComebackAuraModifier

- modifierProvidedByAura ResistMaxAtStart % at minute 0, scaling by +

- citadel_koth_cashin ComebackAuraModifier

- modifierProvidedByAura ResistMaxPerMinute % per minute, up to - citadel_koth_cashin ComebackAuraModifier

- modifierProvidedByAura ResistMaxCap % at minute 30.

They also receive bonus rewards if they capture the rift (see below).

## Rewards

The rift's base soul bounty is - + Souls and increases by Souls per minute of game time. However, unlike other objectives, the rift's bounty starts scaling from 13 minutes, instead of from minute 0.

- rift: 1

- rift_base: 1482

- rift_min_time: 13 When a team wins the rift: Rift Troopers will spawn in that lane for the winning team. They are larger, colored black, and don't drop souls when killed. They spawn at a minimum of 5 troopers, every 0.5 seconds.

On the first rift, they have +100% health and damage compared to normal troopers, as well as - citadel_koth_cashin TrooperModifier MeleeResistPercents

- 1 % [Melee Resist](Melee Resist.md), and - citadel_koth_cashin TrooperModifier SpiritResistPercents

- 1 % [Spirit Resist](Spirit Resist.md). The bonus health and damage increases by +`-`% (additively) for each consecutive rift, up to - citadel_koth_cashin TrooperModifier HealthPercents

- 4 %, and the bonus spirit resist increases by +`-`%, up to - citadel_koth_cashin TrooperModifier SpiritResistPercents

- 4 % (the melee resist does not increase).

All souls are distributed instantly and equally to all team members.

If the rift has been contested for over

- citadel_koth_cashin TimeToWarnAboutGivingUp s, a warning shows up. After

- citadel_koth_cashin TimeToGiveUp s of being contested, the Rift ends in a draw. No Rift Troopers are spawned, and all souls are released as - citadel_koth_cashin GiveUpOrbs [Soul Orbs](Soul Orbs.md) to be claimed by either team. The orbs float for several seconds, and if unclaimed, they disappear and the souls are lost.

1. Comeback reward If the trailing team wins the rift, they get a soul bonus that scales based on game time and the team's soul deficit. They also get up to +9 Rift Troopers (14 total).
