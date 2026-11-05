---
title: "Powerups"
pageid: 1698
source: wiki-md
---

Powerups, also known as Bridge Buffs or Runes, are temporary buffs that spawn as a glowing stone on the bridges connecting two buildings near the [Urn](Urn.md) spawn and dropoff points, starting at 5 minutes and then every 5 minutes thereafter. They require a Heavy [Melee Attack](Melee Attack.md) to claim.

## Overview

Powerups are displayed on the [Minimap](Minimap.md) with unique icons indicating their type.

Powerups start weaker and grow stronger (from 5 minutes to 40 minutes). Exact values are the following: [Casting](Spirit Power.md): Starts at +

- casting_powerup_pickup Modifer ModifierValues

- 1

- valueMin [Spirit Power](Spirit Power.md) and +

- casting_powerup_pickup Modifer ModifierValues

- 2

- valueMin % [Cooldown Reduction](Cooldown Reduction.md) for

- casting_powerup_pickup Modifer Duration s Ends at +

- casting_powerup_pickup Modifer ModifierValues

- 1

- valueMax Spirit Power and +

- casting_powerup_pickup Modifer ModifierValues

- 2

- valueMax % Cooldown Reduction for

- casting_powerup_pickup Modifer Duration s [Gun](Weapon Damage.md): Starts at +

- gun_powerup_pickup Modifer ModifierValues

- 1

- valueMin % [Fire Rate](Fire Rate.md) and +

- gun_powerup_pickup Modifer ModifierValues

- 2

- valueMin % [Ammo](Ammo.md) for

- casting_powerup_pickup Modifer Duration s Ends at +

- gun_powerup_pickup Modifer ModifierValues

- 1

- valueMax % Fire Rate and +

- gun_powerup_pickup Modifer ModifierValues

- 2

- valueMax % Ammo for

- casting_powerup_pickup Modifer Duration s [Movement](Movement.md): Starts at +

- movement_powerup_pickup Modifer ModifierValues

- 1

- valueMin [Stamina](Stamina.md), +` * 0.0254 round 1`m/s [Sprint Speed](Sprint Speed.md), +

- movement_powerup_pickup Modifer ModifierValues

- 4

- valueMin % Stamina Regeneration Rate, and +

- movement_powerup_pickup Modifer ModifierValues

- 3

- valueMin % [Zipline](Ziplines.md) Speed for

- casting_powerup_pickup Modifer Duration s Ends at +

- movement_powerup_pickup Modifer ModifierValues

- 1

- valueMax Stamina, +` * 0.0254 round 1`m/s Sprint Speed, +

- movement_powerup_pickup Modifer ModifierValues

- 4

- valueMax % Stamina Regeneration Rate and +

- movement_powerup_pickup Modifer ModifierValues

- 3

- valueMax % Zipline Speed for

- casting_powerup_pickup Modifer Duration s [Survival](Vitality.md): Starts at +

- survival_powerup_pickup Modifer ModifierValues

- 1

- valueMin [Bonus Health](Health.md) and +

- survival_powerup_pickup Modifer ModifierValues

- 2

- valueMin (fixed) [Health Regen](Health Regen.md) for

- casting_powerup_pickup Modifer Duration s Ends at +

- survival_powerup_pickup Modifer ModifierValues

- 1

- valueMax Bonus Health and +

- survival_powerup_pickup Modifer ModifierValues

- 2

- valueMax (fixed) [Health Regen](Health Regen.md) for

- casting_powerup_pickup Modifer Duration s These temporary stat increases do not appear in the in-game stats, but they are listed as active effects on the left side of the player's HUD. The duration of powerup effects appears in the lower left of the HUD, above the soul count. When another player has the powerup, the icon is shown below their healthbar.

Powerups will be randomized at the 5 minute spawn, but at 10 minutes are guaranteed to spawn the other 2 buffs. (There might be an order to this, ie a bridge that spawns the gun buff at 5 minutes will always be a spirit buff at 10 minutes, unless the spirit buff was paired with the gun buff at 5 minutes.) A player will lose their Powerup on [death](death.md). It can also be removed by Cursed Relic.
