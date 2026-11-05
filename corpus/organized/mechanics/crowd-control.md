---
title: "Crowd Control"
pageid: 904
source: wiki-md
---

See also [Status Effects](Status Effects.md) for a comprehensive list of all sources of Crowd Control and other Status Effects.

- [Venator](Venator.md)

- All they'll be able to do is stand there and burn.

Crowd Control (CC) refers to [effects](Status Effects.md) that alter an opponent's capability to function, including their movement, ability use, weapon firing, and many others. Some CC effects have reduced duration when applied shortly after other CC effects; see [Diminishing Returns](untitled.md#Diminishing-Returns).

They can be applied both by [Hero](Heroes.md) abilities and [Items](Items.md) from the [Shop](Shop.md).

## Types of Crowd Control

1. Movement Slow Reduces the target's movement speed by a percentage.

For example, a 30% slow reduces a 10 meters / second movement speed to 7 m/s.

Movement Slow cannot reduce a target's speed below 2 meters / second.

1. Stun Prevents the target from shooting, using abilities, using items, and moving. Stun also causes the target to be [Interrupted](Crowd Control.md#Interrupt).

Examples include Infernus ' Concussive Combustion, Ivy's Stone Form, and Dynamo's Singularity.

1. Sleep Similar to [Stun](Crowd Control.md#Stun), it prevents the target from shooting and using abilities. However, unlike Stun, it does not prevent movement; instead, it slows the target to 2m/s.

Sleep does not [Interrupt](Crowd Control.md#Interrupt) channels. Receiving any damage wakes the target instantly.

Sources of Sleep include abilities such as Haze's Sleep Dagger and Rem's Naptime.

1. Immobilize Reduces all speed to 0 and stops all voluntary movement, though the target can still be displaced by others. Additionally, it prevents the use of movement related abilities. It removes all upwards acceleration, making airborne targets fall to the ground.

Examples include Warden's Binding Word, Paige's Captivating Read, and Arctic Blast.

1. Silence Prevents the target from activating abilities, though they can still use [Item](Items.md) actives.

A common cause of confusion is that Silence does not [Interrupt](Crowd_Control.md#Interrupt), meaning abilities that have started will always continue through Silence, such as Seven's Storm Cloud.

Examples include Silence Wave, Silencer, Focus Lens, and more.

1. Item Silence Prevents the target from using [Item](Items.md) actives, though they can still use abilities.

Examples include Cursed Relic (disables all items) and Slowing Hex (disables movement items).

1. Disarm Prevents the target from firing their main weapon but melee attacks can still be used. Note that abilities that use weapon-damage can still be used while Disarmed, such as Haze's Bullet Dance.

Examples include Mo & Krill's Sand Blast and Disarming Hex.

1. Interrupt Interrupts instantly cancels all ability casts and channels. It alone does not prevent further use of abilities. When targets are [Stunned](Crowd Control.md#Stun) they are also Interrupted.

Examples of Interrupt (other than Stun) include the Cursed Relic and Knockdown [Items](Items.md) and Grey Talon's Spirit Snare.

1. Displace Exerts some force on the target that modifies their acceleration or velocity, moving or knocking them around.

Examples include Lash's Ground Strike, Bebop's Exploding Uppercut and Grapple Arm, Vindicta's Stake, the Rescue Beam and Knockdown [Items](Items.md), and more.

1. Time Stop The target acts as if time is frozen or slowed, slowing their movement, animations, casts, channels.

The effects of time stopped abilities can still function. For example, if Dynamo is time stopped during his Singularity channel, it still pulls and stuns enemies. Note that this technically lengthens the duration of the Singularity.

Examples include Apollo's Itani Lo Sahn, Paradox's Kinetic Carbine, and The Doorman's Hotel Guest.

1. Hex The target is transformed into a rabbit.

The target gains a smaller model and hitbox and moves faster, but will take increased damage. Hexed targets cannot use their weapon, melee, abilities, or items. Abilities and heavy melee attacks will not be interrupted when hexed.

The only source of Hex is Sinclair's Rabbit Hex.

## Crowd Control Reductions and Immunities

Mechanics and effects that reduce the duration or intensity of crowd control, either partially or completely.

1. Diminishing Returns Only some CCs are subject to this reduction: [Stun](untitled.md#Stun), [Sleep](untitled.md#Sleep), [Immobilize](untitled.md#Immobilize), Chain (tether), and [Silence](untitled.md#Silence), the same set of debuffs that triggers Reactive Barrier. Applying one of these to an enemy affected by another of them within the last 9 seconds reduces its duration. The reduction starts at 15% and scales to 35% with the number of recent CCs. The maintained list of sources is at [Reactive Barrier's Triggers list](Reactive Barrier.md#Barrier-Triggers).

Abilities that apply multiple CCs as part of one action count as one CC (e.g.

- Abrams's Shoulder Charge grab + stun, Lash's Death Slam grab + stun).

1. Slow Resistance Reduce the effectiveness of slows.

\mathit{Modified Speed} = \mathit{Base Speed} * (1 - \mathit{Slow} * (1 - \mathit{Slow Resistance})) For example, Infernus ' Flame Dash normally moves at 12 meters per second, but with a 30% slow and its innate 50% slow resistance it is slowed down by 15% to 10.2m/s.

1. Invincibility Become unable to be hit or targeted. All projectiles and area effects phase through while you also can not be targeted by [Items](Items.md) such as Cursed Relic or [Abilities](Abilities.md) such as Mo & Krill's Combo.

Examples include Ethereal Shift and Calico's Return to Shadows and the transformation phase of Yamato's Shadow Transformation.

While Yamato cannot move during the transformation phase, both Ethereal Shift and Return to Shadows allow limited [movement](movement.md).

1. Purge Instantly remove all debuffs.

Some debuffs delay the crucial negative effect, such as Mirage's Djinn's Mark. Therefore, if the mark is applied, then the target purges their debuffs, the mark never detonates.

Examples include Viscous ' The Cube (Tier 3), Yamato's Shadow Transformation, and Dispel Magic.

1. Unstoppable Become immune to all forms of crowd control.

For example the Unstoppable [Item](Items.md), Abrams ' Seismic Impact (Tier 3), and Yamato's Shadow Transformation.
