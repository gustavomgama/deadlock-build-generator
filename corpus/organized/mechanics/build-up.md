---
title: "Build-Up"
pageid: 25365
source: wiki-md
---

- Afterburn and Toxic Bullets on Bebop](Buildup_example_2.jpg) Build-up is a mechanic that causes bullets or [melee attacks](Melee Attack.md) to accumulate a status effect over multiple hits.

Whenever a hero fires at an enemy, items and abilities with Build-up add a percentage to a meter on that target. Once the meter reaches 100%, the associated status effect is triggered. The progress of a build-up is shown as round icons above the target. Build-up per shot is reduced by [damage falloff](Falloff Range.md), dropping to as low as 10% of its base value at maximum range. For most effects, melee damage also applies build-up.

Build-up is a related but distinct mechanic from [Stacks](Stack.md). Unlike stacks, which are discrete increments that scale an ongoing effect, build-up functions as a percentage meter that triggers a single status effect upon reaching 100%.

## Items

Items with Build-up apply their percentage to the target through bullet hits. The build-up meter decays if the enemy does not receive any new stacks for 2 seconds, at a rate of 20% per second. Melee attacks count as 1 shot for build-up purposes. Each item's build-up per shot varies by hero, as it is affected by the hero's weapon fire rate and clip size; the exact percentages can be found on each item's page.

{| class="wikitable sortable" + List of items that use Build-up Name Effect on Trigger Slowing Bullets [Movement Slow](Movement Slow.md) Weighted Shots [Movement Slow](Movement Slow.md) Silencer [Silence](Silence.md) Inhibitor Damage Reduction and [Healing](Healing.md) Reduction Toxic Bullets

- Bleed ([Spirit Damage](Spirit Damage.md) over time) Spiritual Overflow

- [Fire Rate](Fire Rate.md), [Spirit Power](Spirit Power.md) and [Spirit Lifesteal](Lifesteal.md) |} Doesn't build-up with melee.

- Spiritual Overflow is a special case: its build-up affects the shooter rather than the target. However, the build-up meter still accumulates on the target being shot, meaning it is impossible to accelerate the process by shooting multiple different targets at once. It is also the only build-up source where the progress is not shown above the target.

## Heroes

Some heroes have abilities that use the Build-up mechanic, accumulating a percentage on the target until the associated effect triggers.

- Infernus ' Afterburn: triggers a Burn (Spirit damage over time) effect. Light Melee attacks count as 20% build-up; Heavy Melee attacks count as 35% build-up.

- Mina's Love Bites: triggers a Spirit damage proc. Melee attacks do not contribute to build-up.

- Mirage's Djinn's Mark: builds up stacks by shooting the target at certain intervals, triggering a Spirit damage proc either when the timer runs out, when max stacks are reached, or when activated by Mirage. Builds up with a single bullet per stack.

- Silver's Slam Fire (Tier 3): deals bonus Weapon damage if all 3 shots hit the same target.

- Vyper's Lethal Venom (Tier 3): triggers a Spirit damage proc. Can build up with melee and isn't blocked by Petrifying Bola.

Note: Graves ' Essence Theft appears visually as a Build-Up, but it's actually a stacking effect, as the effect is applied over time.

## Counters

Several items and abilities can mitigate or counter build-up effects: Plated Armor provides a chance to block bullet effects from incoming shots entirely, which includes any build-up effects.

Abilities and items that [disarm](Status Effect.md#Disarm) the enemy or reduce their [fire rate](fire rate.md), such as Mo & Krill's Sand Blast, Disarming Hex and Juggernaut.

- Dispel Magic removes any existing build-up applied to the player.

Items providing [Debuff Resist](Debuff Resist.md) reduce the lingering duration of build-up as well as the duration of already triggered effects.

- Debuff Reducer and its upgrades Spellbreaker and Unstoppable Blood Tribute Weighted Shots if the player has no build-up, Counterspell prevents the first shot of build-up. If the player already has a build-up counter, it prevents from triggering when the build-up crosses 100% threshold, but does not prevent the build-up itself.

Abilities and items that makes the player [immune to damage](Status Effect.md#Invincibility), such as Ivy's Stone Form or Ethereal Shift, will also prevent any build-up on the player.

Notes: Metal Skin, despite providing immunity to bullet damage, does not protect against build-up in any way; shots negated by Metal Skin still contribute their full build-up percentage.

- Return Fire does not build up effects against the attacker.
