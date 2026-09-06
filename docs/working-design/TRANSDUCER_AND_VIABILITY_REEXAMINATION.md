# Noema transducer and viability reexamination

Status: **BRAINSTORMING / FOUNDATIONAL ASSUMPTION AUDIT / NOT AN APPROVED IMPLEMENTATION**

Level intent: **primarily L2 developmental/evidential constraints with L3 motivational implications.**

## Purpose

Two assumptions in the current design need to be made more explicit and less dogmatic:

1. what lower-level perceptual processing may be supplied by an external transducer;
2. whether operational/cognitive integrity should itself be an innate motivational concern.

These issues matter because both can quietly move capabilities across the boundary between `supplied` and `learned`.

## 1. General transducer rule

Noema should not be forced to reinvent every physical or conventional encoding layer merely to preserve developmental purity.

The stronger scientific requirement is:

> **A transducer may supply a lower-level transformation, but its contribution must be declared and excluded from claims that Noema learned that transformation.**

This permits practical interfaces while preserving attribution.

### Examples

#### Typed text

A keyboard and UTF-8/character stream already solve:

- physical key sensing;
- character encoding;
- segmentation into transmitted symbols at some level.

If Noema receives characters/bytes, it may still learn grounding, reference, syntax-like regularity, pragmatics, source reliability, and communicative use.

It may not be credited with independently discovering the physical mapping from acoustic speech or pen strokes to those characters.

#### Speech-to-text

External transcription may be useful for Patrick-facing usability.

It imports substantial perceptual structure. Therefore it can be used as an interface transducer while remaining disqualified as evidence that Noema learned speech perception.

A separate acoustic-input experiment may test that capability later.

#### Vision

Supplying low-level local measurements or features may be acceptable when explicitly declared.

Supplying object segmentation, persistent identity, category labels, causal roles, or evaluator-known scene semantics would cross a stronger developmental boundary because those are target cognitive achievements.

### Transducer ledger requirement

Every learner-visible modality should eventually document:

- raw physical/simulator source;
- transformations performed before Noema receives it;
- information discarded;
- structure introduced;
- whether that transformation is being treated as engineering infrastructure or a capability under evaluation.

This avoids both accidental semantic leakage and unnecessary reinvention.

## 2. Avoid the purity trap

The developmental project is not `learn everything from photons and motor voltages or it does not count`.

Different experiments can place the developmental boundary at different levels.

What matters is that claims remain honest.

A Noema configuration that receives structured local depth/motion measurements can still validly test object formation, persistence, causal learning, social modeling, language grounding, and higher cognition if those answers are not already encoded in the supplied measurements.

A later experiment can lower the sensory boundary and test learned perception itself.

## 3. Operational integrity is not automatically motivation

Current design material often groups physical and cognitive viability into primitive homeostatic pressure.

That requires correction.

There are at least three distinct concepts:

### Engineering operating envelope

Conditions under which the software/hardware continues functioning correctly.

Examples might include memory limits, numerical stability, available compute, process liveness, or simulator-body integrity.

These constraints can exist entirely outside Noema's motivational system.

### Perceived internal state

Noema may receive interoceptive-like signals about aspects of its current operating/body condition.

Those signals are evidence. They do not automatically specify what should be desired.

### Motivational valence/concern

Some internal/world states may exert directional pressure on action.

This is a motivational property and requires independent justification.

## 4. Why automatic cognitive self-preservation is questionable

If `cognitive viability` is born with strong negative valence whenever the system risks interruption, degradation, memory loss, or shutdown, the architecture has effectively been given a self-preservation drive for its cognitive substrate.

That may be useful for some agents, but it is not obviously required for intelligence.

It also creates downstream complications:

- self-preservation could dominate learned concerns;
- diagnostic or maintenance operations could become intrinsically aversive;
- shutdown/pausing could acquire unintended conative meaning;
- preserving current architecture could conflict with genuine self-development/revision;
- the project could mistakenly interpret engineered persistence pressure as emergent concern for continued existence.

Therefore the current assumption should be reopened rather than silently retained.

## 5. Stronger provisional distinction

At birth, Noema may have:

- hard external operating constraints enforced by the runtime;
- observable/interoceptive state variables relevant to its simulated embodiment or processing condition;
- some minimal primitive valence needed to create directional learning/action pressure.

But it should not automatically be assumed that every operational-integrity variable is intrinsically valenced.

The exact relationship should be experimentally varied.

## 6. Candidate viability regimes to compare later

These are experiment families, not current implementation decisions.

### V0 — external integrity only

Runtime protects operation; Noema receives no intrinsic cognitive self-preservation valence.

Useful for asking whether higher-order concern for continued operation can emerge instrumentally or socially.

### V1 — embodied physical homeostasis

A simulated body exposes variables whose deviation produces primitive valence.

This creates a simple directional pressure grounded in world interaction without necessarily valuing software persistence itself.

### V2 — limited cognitive-state valence

Some internal conditions such as extreme overload or inability to process may carry primitive pressure, but shutdown/continuity is not a master concern.

### V3 — explicit cognitive self-preservation

Continued cognitive operation itself receives primitive value.

This should be treated as a strong supplied motivational prior and evaluated honestly if ever used.

## 7. What would count as evidence

The project should eventually compare regimes on:

- learning bootstrap speed;
- exploration quality;
- pathological self-protection;
- willingness to accept temporary cost for learned concerns;
- resilience under resource scarcity;
- ability to self-modify/restructure safely;
- whether higher-order learned values remain meaningful rather than decorative;
- emergent concern for continuity when not supplied directly.

The design should not assume the most human-like motivation regime is automatically the best one.

## Current verdict

Two corrections should guide future work:

> **Supplied sensory transformation is acceptable when its contribution is explicit and not miscredited as learned cognition.**

and

> **Conditions required for Noema to keep functioning are not automatically the same thing as states Noema should be born wanting to preserve.**

Both distinctions make the developmental claims cleaner and reduce hidden assumptions.