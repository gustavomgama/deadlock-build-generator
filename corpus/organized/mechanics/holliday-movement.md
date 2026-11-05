---
title: "Holliday/Movement"
pageid: 27911
source: wiki-md
---

List of known [movement tech](Character Tech.md) for Holliday.

- name: Bounce Pad

- file: hollidaybouncepad.mp4

- tech_type: Character Tech

- difficulty: Basic Mechanics

- character_dependent: Yes

- inputs: Bounce Pad → Move (WASD) onto Bounce Pad

- nofile: 1

## Bounce Pad

is - Holliday's second ability. In it, she places down a bounce pad that acts similarly to the [air vents](Jump_pad.md) found throughout the map, which allies and enemies can use.

- Holliday's and her teammates first use of a bounce pad will give 100% air control and allow for an explosion upon landing, dealing damage. If is maxed to T3, (only) Holliday will also apply 0.7s Stun to enemies in Stop Zone. Subsequent uses will not give this buff.

When spawned in, the bounce pad will appear 200 units in front of HollidayPlaceDistance, ability_bounce_pad in abilities.vdata after 0.2 seconds. The bounce pad lasts for - get_ability_prop AbilityDuration seconds, after which it will despawn.

- Holliday's will send at an initial vertical velocity of 900 u/sBounceVelocity (750) is multiplied by UpFactor (1.2), ability_bounce_pad in abilities.vdata, and initial horizontal velocity of 750 when you have any horizontal movementBounceVelocity (750), ability_bounce_pad in abilities.vdata.

On the first bounce, Holliday gains 100% air control until she lands on the ground, which allows her to maneuver and strafe easier in the air.

- Holliday still experiences the standard air drag of 0.2, although strafing will significantly eliminate effective air drag.

When placed standing directly in front of a wall, it will place the bounce pad vertically. Holding no movement inputs while doing this will let you stand on top of the vertical bounce pad; this enables you to look into the wall and input back and jump at the same time to get an instant wall jump into bounce pad, generating lots of momentum.
