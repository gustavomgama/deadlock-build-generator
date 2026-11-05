---
title: "Dashing"
pageid: 21197
source: wiki-md
---

- Overview, Strafe Dashing, Dash Jumping, Dash Sliding, Short Dash Crouch Cancelling, Instant Air Dash

- name: Dashing

- file: dashing.mp4

- tech_type: Universal Tech

- difficulty: Basic Mechanics

- character_dependent: No

## Dash Directions

Using a keyboard, or a joystick to move, you can dash at any angle on the ground and in the air.

While in the air, you have access to one other direction to dash to; down towards the ground. When you dash towards the ground, it is called a Down dash. To down dash, double tap the duck key; once you press the duck key, you have a 28 ticks (0.44 second) window to press it again.

## Dash Jump

0.3 seconds after starting a grounded dash, a window to execute a [Dash Jump](Dash Jumping.md) will open for 0.2 seconds,abilites.vdata, m_flDashJumpStartTime and m_flDashJumpEndTime during which the stamina bar flashes a light blue. This window is solely activated by starting a grounded dash; if you leave the ground after initiating the dash, you are still able to dash jump. For more information, view the dedicated page on Dash Jumping.

## Dash Speed Buckets

While everyone in the roster has the same dash distance, they have different dash speeds. Characters fall into three buckets: Bucket 1 characters have the fastest dash speed, with peak speeds of 635 u/s on the ground and a total dash time of 0.62 seconds.heroes.vdata, hero_tengu, EGroundDashDuration Bucket 2 characters have 9% slower dash speed, with peak speeds of 579 u/s on the ground and a total dash time of 0.68 seconds.heroes.vdata, hero_gigawatt, EGroundDashDuration Bucket 3 characters have the slowest dash speed, being 14% slower than Bucket 1, with peak speeds of 562 u/s on the ground and a total dash time of 0.72 seconds.heroes.vdata, hero_shiv, EGroundDashDuration Dashing on the ground always sets your velocity to a fixed amount. Air Dashing is an impulse instead, meaning it can stack or conflict with prior momentum.

To dash, move and press the - dash key

- hover: By default, the left shift key. Your character will quickly move in that direction.

1. Hero Dash Buckets

- write_ground_dash_buckets

## Dash Slow

Some abilities and items reduce dash speed for the target or, rarely, for the caster. This Dash slow applies to dash speed without affecting time dashing. The end result is reduction in dash distance.

1. Abilities that decrease dash speed

- dashslow 1. Items that increase/decrease dash distance

- dash distance
