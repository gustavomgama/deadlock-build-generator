---
title: "Wall Jumping/Edge Boost"
pageid: 23958
source: wiki-md
---

- Wall Jumping Overview, Corner Boost, Edge Boost, Fast Climb

- name: Edge Boosting

- file: edgeboost.mp4

- tech_type: Universal Tech

- difficulty: Advanced Easy

- character_dependent: No

- inputs: [Wall Jump](Wall Jumping.md) on a vertical edge while moving.

Edge Boosting are a variation of [Wall Jumps](Wall Jumping.md), allowing players to gain extra horizontal distance in their current velocity direction by Wall Jumping off the edge of a wall. While Edge Boosts share a similar name to [Corner Boosts](Corner Boosting.md), they function differently.

When near a wall, the game will detect the closest point to your collision capsule and use the normal of it to determine which way you are going to Wall Jump. When Edge Boosting, you are attempting to shift the normal towards your intended momentum (typically forwards or backwards) by Wall Jumping as late as you can.

Edge Boosting is in essence a normal Wall Jump, unlike Corner Boosts; you do not trade off vertical impulse for horizontal impulse. Instead, you "stack" your Wall Jump velocity with already pre-existing velocity.

Edge Boosting is particularly great for preserving momentum, since you lose less forwards velocity compared to a regular Wall Jump. Edge Boosting is extremely hard to execute in a real game, since you cannot hang off an edge with your collision capsule the way you can with Corner Boosts and the window to Wall Jump with the best normal is typically one or two ticks. While difficult, Edge Boosting can be mastered for efficient rollouts and escape routes that are hard to follow.

To execute, Wall Jump off an edge as late as you can for the maximum velocity. Take advantage of Wall Sliding to time the input.

- name: Edge Boosting (Wall Detection Style 2)

- file: edgeboostwcmd.mp4

- tech_type: Universal Tech

- inputs: Use the command citadel_wall_detection_style 2

- notes: Take note of the direction of the arrow; because your collision capsule is rounded, there are normals where it points away from your current momentum and others where it is nearly parallel to your direction.
