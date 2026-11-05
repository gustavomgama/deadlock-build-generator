---
title: "Movement"
pageid: 2032
source: wiki-md
---

- Portal:Movement In [Deadlock](Deadlock.md), there are a variety of methods for traversing the map.

## Overview

Movement is a concept that encompasses traversing the [map](map.md). In a broad sense, it is important for positioning, map rotations, ganking, and pushing, while from a mechanical point of view, it is the specific actions to escape, chase, initiate fights, or otherwise catch enemies out of position.

Several heroes and items have specific movement tech that cannot be executed otherwise.

Distances and speeds are displayed in-game by meters (m) and meters per second (m/s). As the game built on the Source 2 Engine, internal measurements are calculated by hammer units (hu), where 1 hammer unit can be approximated to 1 [inch](wikipedia_inch.md). Therefore, 1 hu is roughly equal to and represents.0254 m.

There is no fall damage in Deadlock.

## Basic Movement

1. Controls The character is controlled using movement keys (by default: W, A, S, and D). Pressing the jump key (by default: Space) makes the character jump, and holding it near a ledge allows the character to mantle (by default: Space). The crouch key (default: Ctrl) causes the character to crouch or slide if they have enough speed (8.9 m/s or 350 hu/s) or are on an inclined surface, such as stairs. Additionally, the dash key (default: Shift) enables the character to perform a [dash](Stamina.md) both on the ground and in the air. [Heroes](Heroes.md) have differing move speeds and [dash speeds](Stamina.md#Dash-Speed).

- Move Speed Movement Slow Sprinting will activate on its own, which occurs after a hero is out of combat for five seconds and persists until entering combat or zooming in. Zooming in while sprinting resets the player's speed back to base move speed. Most heroes can obtain sprint through items, but several start with it initially.

1. Air Jump Jumping while midair functions like a double jump, allowing the player to reach rooftops or get over tall walls. This consumes one stamina.

At the start of each game, you are only permitted one Air Jump per jump. This can be expanded to two with the - Armor Stamina Mastery.

Air Jumping 1. Wall Jump Pressing Space next to a wall will cause the character to perform a Wall Jump, which does not consume stamina. You can Wall Jump multiple times per jump, but each Wall Jump after the first one costs 0.5 [stamina](stamina.md) and incurs a fatigue that reduces the height of successive jumps. This fatigue recovers non-linearly over the course of 1.25 seconds and recovers completely upon landing. Using a heavy melee while airborne will also incur fatigue.

Wall Jumping 1. Air Dash Dashing midair can be done similarly to a grounded dash. A dash performed in the air is called an Air Dash, and consumes the same amount of stamina as a grounded dash. You can Air Dash only once per jump, but this limit can be expanded to two with the - Armor Stamina Mastery.

Air Dashing 1. Dash Jump A Dash jump is a fast long jump, which can be performed as an additive input during a dash during a set timing window and which costs 1 [stamina](stamina.md), for a total of 2 stamina. The timing of a dash jump is visualized by the stamina bars under your crosshair turning blue while dashing. While the crosshair is blue, the player can press jump to dash jump.

Dash Jumping 1. Down Dash Double tapping crouch midair performs a down dash, allowing the player to return to the ground quickly. This consumes 0.5 stamina. You can Down Dash only once per jump. This can be expanded to two with the - Armor Stamina Mastery.

Down dashing 1. Mantle Mantling is the act of climbing a nearby ledge. If a player holds the crouch key (default: Ctrl) while mantling, they will slide after climbing up, which is called a Mantle Glide.

If the player is hit by a [melee attack](Melee Attack.md) while mantling, they will get an 80% [Movement Slow](Movement Slow.md), which will taper down to 20% over 2s.

1. Stamina Stamina Stamina management is an important aspect of player movement.

## Map features

There are multiple elements on the map that let players move uniquely.

1. Jump Pads Jump pad Jump Pads are small vents that push heroes through the air after standing on them.

1. Ropes Ropes Ropes dangle from the roofs of buildings or inside buildings, allowing heroes to access rooftops or additional floors, and facilitate vertical traversal.

1. Teleporter Teleporter There are multiple pairs of teleporters throughout the map that can be entered to quickly traverse left and right across the map.

1. Ziplines Ziplines Ziplines are the most prominent method of traversal, as the heroes spawn riding the lines. They connect the opposing bases together and facilitate fights.

## Advanced Movement

As a physics based game, several principles in the real world are also modeled in-game. However, quirks with the game engine allow unique movement options that are not readily apparent.

1. Melee Jump Melee jumping is the technique of using a heavy melee timed with a Wall Jump to go up without double jumping, thus saving a Stamina bar.Melee Jumping and then Mantling 1. Corner Boost Corner boosting is a technique that exploits the game's wall jump mechanics to achieve greater vertical velocity than a standard wall jump. The effect is believed to occur due to the following implementation behavior: Velocity Reset on Wall Jump Initiation – When a wall jump is performed, the game first sets the character's velocity to a fixed absolute value.

Collision Normal Calculation – The game determines the direction of the jump by using the normal vector of the character's collision capsule at the nearest point of contact with the wall.

Upward-Angled Normals on Corners – Because the collision capsule is rounded, the normal vector near a corner can point diagonally upward or downward rather than purely sideways. When the normal is angled upward, the resulting velocity is applied at a steeper angle, leading to increased upward momentum.

1. Visual Comparison Normal Wall Jump – Final velocity is directed primarily sideways, following a standard wall jump.

Corner Boost – Final velocity is angled higher due to the upward-tilting normal, resulting in a stronger ascent.

{| style="margin: auto; border: none;" 1. Key ■ Light Blue: Collision capsule ■ Red: Absolute velocity ■ Green: Sideways velocity ■ Orange: Wall push ■ Purple: Final velocity |} Corner Boosting 1. Dropdown Corner Boost Same as Corner Boost, Dropdown Corner Boost can be done on any edge in the game. To perform it, drop down from an edge and wall jump to gain extra height without using stamina.Dropdown Corner Boosting 1. Friction 1. Dash Jump Cancel Dash Jump Canceling is a technique that allows for Jumping immediately after a Dash without performing a Dash Jump. After performing a Dash for a short duration it is possible to spend 1 [Stamina](Stamina.md) to perform a Dash Jump. Casting an ability during the Dash Jump window will immediately cancel it. This can then be followed up with a normal Jump. When done correctly a Dash Jump Cancel can be used to travel further than a Dash.

Only some abilities provide a benefit when used to Dash Jump Cancel. Abilities with long cast time or abilities that slow movement during cast provide almost no benefit.

{| class="wikitable" +Abilities that can be used to Dash Jump Cancel Hero Ability Notes Billy Blasted Chain Gang

- Hero: Calico Gloom Bombs

- Hero: Doorman Doorway Only works when placing the doors.

- Luggage Cart

- Hero: Drifter Stalker's Mark

- Hero: Dynamo Rejuvenating Aurora Requires Rejuvenating Aurora to be upgraded to T3.

- Hero: Grey Talon Spirit Snare

- Hero: Haze Sleep Dagger Smoke Bomb

- Hero: Holliday Powder Keg Bounce Pad Provides a significant increase in velocity.

- Hero: Infernus Napalm

- Hero: Ivy Entangling Thorns Kudzu Connection

- Hero: Kelvin Frost Grenade Frozen Shelter It is possible to cancel the Frozen Shelter before hitting the wall.

- Hero: Lady Geist Essence Bomb Malice Casting Malice requires the caster to wait before they can jump, which makes the Dash Jump Cancel significantly harder. Malice Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Hero: Lash Flog

- Hero: McGinnis Mini Turret Medicinal Specter Spectral Wall Heavy Barrage Due to the slow Heavy Barrage Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Hero: Mina Rake

- Hero: Mirage Fire Scarabs Each separate cast can be Dash Jump Canceled.

- Djinn's Mark

- Hero: Mo & Krill Scorn Sand Blast

- Hero: Paige Conjure Dragon Captivating Read

- Hero: Paradox Pulse Grenade Kinetic Carbine Paradoxical Swap

- Hero: Pocket Flying Cloak

- Hero: Seven Lightning Ball Static Charge Power Surge

- Hero: Shiv Serrated Knives Casting Serrated Knives requires the caster to wait before they can jump, which makes the Dash Jump Cancel significantly harder. Serrated Knives Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Bloodletting

- Hero: Sinclair Vexing Bolt Casting Vexing Bolt requires the caster to wait before they can jump, which makes the Dash Jump Cancel significantly harder. Vexing Bolt Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Spectral Assistant Rabbit Hex

- Hero: Vindicta Stake Crow Familiar Crow Familiar Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Assassinate Requires the ability to be fully cast and unscoped before jumping to be able to be followed up with a slide.

- Hero: Viscous Splatter Splatter Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Puddle Punch

- Hero: Vyper Screwjab Dagger Lethal Venom Petrifying Bola

- Hero: Warden Alchemical Flask Willpower Willpower Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Binding Word

- Hero: Wraith Card Trick Card Trick Dash Jump Cancel cannot be followed up with a slide without items that increase move speed.

- Full Auto Telekinesis |}

## Movement abilities

Certain abilities are classified in-game as Movement Abilties. These abilities are disabled by the - Tech Slowing Hex.

{| class="wikitable" style="text-align:center; width:auto;" Hero Ability Description Abrams Seismic Impact Leap high into the air and choose a ground location to crash into. When you hit the ground, all enemies in the radius are damaged and stunned.

- Calico Leaping Slash Dash forward before slashing all enemies in a circle, dealing Light Melee Damage.

Ava Turn to shadows and possess Ava. You gain Movement Speed and become Hidden on the Minimap, but cannot attack or cast abilities.

Return to Shadows Instantly turn to shadows, becoming Untargetable, gaining Movement Speed, and dealing Damage.

- Dynamo Quantum Entanglement Dynamo briefly disappears into the void and then reappears a short distance away. On reappearing, your weapon is reloaded and has a fire rate bonus for the next clip (Max 8s).

- Grey Talon Rain of Arrows Launches you high in the air, allowing you to glide slowly. While airborne, you gain Weapon Damage and multishot on your weapon.

Alt-Cast for reduced jump height.

Press Space to cancel the glide.

- Haze Smoke Bomb Fade out of sight, becoming invisible and gaining sprint speed. Attacking removes invisibility. Close enemies can see through your invisibility.

- Holliday Bounce Pad Drop a bounce pad in the world that launches any hero.

- Infernus Flame Dash Move forward at high speed and leave a flame trail that burns enemies. Infernus gains 50% slow resistance for the duration.

- Ivy Air Drop Take flight with an ally or a bomb. Drop your ally or bomb to cause a large explosion that causes movement slow. Ivy and ally gain a bullet shield when flying ends.

While lifted, your ally gains bullet resist but cannot attack and deals -50% damage. Air Drop has faster cast time when targeting an ally.

- Kelvin Ice Path Kelvin creates a floating trail of ice and snow that gives movement bonuses to him and his allies. Kelvin gains 60% slow resistance for the duration. Enemies can also walk on the floating trail.

Press Shift / Ctrl to travel up or down while in Ice Path.

- Lash Grapple Pull yourself through the air toward a target. Using Grapple also resets your limit of air jumps and dashes.

- Mirage Tornado Transform yourself into a tornado that travels forward, damaging enemies and lifting them up in the air. After emerging from the tornado you gain bullet evasion.

Traveler Channeled. Target an ally or visible enemy hero on the minimap, then teleport to where they were when your channel started. After teleporting, you gain movement speed as well as fire rate until your next reload.

- Mo & Krill Burrow Burrow underground, moving faster, and gaining spirit and bullet armor. Damage from enemy heroes will reduce the speed bonus. When you jump out, knock enemies into the air and perform a spin attack that damages and slows. Cooldown starts when Burrow ends.

- Paradox Paradoxical Swap Fire a projectile that swaps your position with the target enemy hero. While the effect occurs, you gain spirit lifesteal and the enemy takes damage over time.

- Pocket Flying Cloak Launch a sentient cloak that travels forward and damages enemies. You can press 2 to teleport to its location.

- Shiv Slice and Dice Perform a dash forward, damaging enemies along the path.

Ultimate Unlock: While rage is full an echo of Shiv retraces the dash path after a short delay, damaging enemies again.

- Sinclair Spectral Assistant While the Assistant is out, you can press [2] to swap positions with your Assistant.

- Vindicta Flight Leap into the air and fly. While in flight your weapon deals bonus spirit damage.

- Viscous Goo Ball Morph into a large goo ball that deals damage and stuns enemies on impact. The ball grants large amounts of Bullet and Spirit resist, bounces off walls and can double jump.

- Vyper Slither You have increased Slide Distance, can Slide up hills, and can turn faster while Sliding.

- Warden Willpower Gain a spirit shield and bonus movement speed.

- Wraith Project Mind Teleport to the targeted location.

- Yamato Flying Strike Throw a grappling hook to reel yourself towards an enemy, damaging and slowing the target when you arrive.

|}
