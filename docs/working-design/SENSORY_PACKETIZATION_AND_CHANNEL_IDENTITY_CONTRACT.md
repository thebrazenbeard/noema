# Noema sensory packetization and channel-identity contract

Status: **BRAINSTORMING / PROVISIONAL F0-F1 DATA-BOUNDARY CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

Noema's existing interface, provenance, timebase, and spatial contracts separate evaluator truth from learner-visible evidence. One implementation boundary remains easy to overlook: **how sensory information is grouped into packets and how channels are identified before it reaches the learner**.

A conventional ML interface often presents one vector such as:

`observation_t = [vision_t, audio_t, touch_t, proprioception_t, ...]`

That representation is convenient, but it can silently assert that all fields belong to the same moment, event, source context, or perceptual episode. It can therefore supply part of the cross-modal binding problem that Noema is supposed to learn.

The central rule is:

> **Batching, packet boundaries, channel topology, synchronization, and source grouping are transducer structure. Whatever they solve must be declared and must not be credited as learned cognition.**

This contract does not require a biologically faithful asynchronous nervous system. It requires the first implementation to make event grouping and channel identity explicit enough that later capability claims remain auditable.

## 1. Why packetization is epistemically active

Packetization is not neutral serialization.

When two measurements arrive in the same learner-visible record, the representation may imply some combination of:

- simultaneity;
- common event membership;
- common source;
- shared scene membership;
- aligned sampling epoch;
- fixed cross-modal correspondence;
- stable channel identity;
- a designer-defined event boundary.

Those implications can simplify:

- multisensory binding;
- action-outcome association;
- source attribution;
- event segmentation;
- delayed credit assignment;
- spatial registration;
- body/self inference;
- communication turn segmentation;
- causal intervention learning.

The effect is especially strong when every modality is sampled at the same rate and delivered with exact shared timestamps.

## 2. Research pressure

The external literature does not dictate one artificial event bus. It does pressure against treating exact synchronous packetization as perceptual ground truth.

Relevant findings include:

- multisensory integration depends on temporal relationships and modality/stimulus/task-dependent temporal binding windows rather than exact physical simultaneity;
- relative sensory precision/reliability can change how events are temporally bound;
- audiovisual and sensorimotor systems recalibrate to persistent temporal offsets;
- recalibration can occur over both sustained and rapid/inter-trial timescales;
- action-feedback timing can be relearned after introduced delays;
- perceptual synchrony and multisensory integration are not necessarily identical constructs.

Representative sources used as design pressure:

- Stevenson et al., *Multisensory temporal integration: task and stimulus dependencies* (Experimental Brain Research, 2013), DOI `10.1007/s00221-013-3507-3`.
- Klaffehn et al., *Temporal binding as multisensory integration: Manipulating perceptual certainty of actions and their effects* (Attention, Perception, & Psychophysics, 2021), DOI `10.3758/s13414-021-02314-0`.
- Van der Burg, Alais & Cass, *Audiovisual temporal recalibration occurs independently at two different time scales* (Scientific Reports, 2015), DOI `10.1038/srep14526`.
- Sugano, Keetels & Vroomen, *The Build-Up and Transfer of Sensorimotor Temporal Recalibration Measured via a Synchronization Task* (Frontiers in Psychology, 2012), DOI `10.3389/fpsyg.2012.00246`.
- Van der Burg, Alais & Cass, *Rapid recalibration to audiovisual asynchrony follows the physical—not the perceived—temporal order* (Attention, Perception, & Psychophysics, 2018), DOI `10.3758/s13414-018-1540-9`.

These results are used only to demonstrate that temporal correspondence is a learnable, uncertainty-bearing relation. They do not imply that Noema must copy human temporal binding mechanisms.

## 3. Five packetization planes

Formal experiments and the F0 ledger should distinguish at least five planes.

### P0 — evaluator event truth

Exact experiment-side facts such as:

- simulator step;
- physical event generation time;
- true causal source;
- true common-event membership;
- exact intervention boundaries;
- exact world-state snapshot;
- evaluator object/agent identity.

P0 is for generation and scoring, not automatic learner input.

### P1 — transducer sampling and buffering

What each sensor or interface does before learner delivery:

- sample rate;
- polling/frame rate;
- integration window;
- buffer size;
- batching policy;
- endpointing;
- frame construction;
- packet loss;
- retransmission;
- jitter correction;
- timestamp assignment;
- resampling/interpolation;
- cross-modal synchronization;
- preprocessing that merges or splits events.

P1 can create strong structure even without semantic labels.

### P2 — learner-visible records

The actual learner input, including whatever is supplied about:

- channel/port identity;
- payload;
- local order;
- local timing cue;
- duration/window information;
- quality/availability flags;
- packet boundary;
- whether multiple fields are delivered together.

P2 must be explicit in the first implementation specification.

### P3 — learned correspondence and event inference

Noema's revisable learned beliefs about:

- which signals belong together;
- whether two streams are synchronous;
- whether delays are stable;
- whether signals share a cause/source;
- whether a sensory consequence belongs to a prior action;
- whether a packet boundary corresponds to a meaningful event;
- whether two channels are redundant, complementary, or unrelated.

P3 may be wrong and must be capable of recalibration.

### P4 — learned semantic modality/event concepts

Later concepts such as:

- `sound`;
- `vision`;
- `touch`;
- `your voice`;
- `my movement`;
- `same event`;
- `message`;
- `before the impact`;
- `that came from the same thing`.

P4 must not be confused with P2 channel topology supplied by the transducer.

## 4. Channel identity: topology is not semantics

Some stable channel distinction is often unavoidable. A camera pixel array and a proprioceptive actuator-state vector are physically different interfaces.

It is therefore acceptable for the implementation to expose a stable low-level **port or sensor identity** when necessary for learnability and engineering integrity.

But a stable port is supplied topology, not a learned semantic category.

For example:

- `sensor_port_03` may be innate/supplied;
- `this port is vision` is a later interpretation unless explicitly supplied;
- `this channel is Patrick` is not justified merely because all Patrick input was routed through one stable port;
- `this is self-generated touch` is not justified merely because one device path carries self-touch events.

Formal claims should therefore distinguish:

> **stable route identity** from **learned source/modality meaning**.

Where practical, channel-label permutation or equivalent routing transformations should test whether competence depends on arbitrary names rather than learned signal relationships.

## 5. No universal synchronized observation frame

The architecture should not require that all modalities be combined into one exact globally synchronized observation vector.

A valid first implementation may instead use an ordered learner-visible event stream or a small set of modality-local streams with declared timing cues.

Possible implementation-friendly form:

```text
LearnerEvent {
  port_id
  payload
  local_time_basis
  optional_duration
  availability_state
  transducer_schema_version
}
```

This schema is illustrative, not yet binding code.

Critically, it does not include evaluator fields such as:

- `same_event_id`;
- `common_source_id`;
- `object_id`;
- `agent_id`;
- `caused_by_action_id`;
- `simultaneous=true`;
- `semantic_modality=vision`;
- `episode_id`.

Evaluator logs may retain such fields separately for audit and scoring.

## 6. Packet boundaries are supplied segmentation

Any transducer-defined boundary must be treated as supplied structure.

Examples:

- video frame boundary;
- audio analysis window;
- ASR utterance endpoint;
- typed-message submit boundary;
- network packet boundary;
- simulator step;
- tactile polling interval.

Noema may legitimately exploit regularities in these boundaries. But later claims must not say it learned event segmentation from scratch if the benchmark's meaningful event boundaries always coincide with supplied packet boundaries.

The evaluator should deliberately include conditions where meaningful events:

- span multiple packets;
- contain multiple subevents inside one packet;
- begin/end between transducer frames;
- occur asynchronously across channels.

## 7. Asynchronous and heterogeneous sampling

The implementation should support at least the possibility of different channels having different rates and delays.

This does not mean all early experiments must simulate realistic sensor hardware. It means the event/data contract must not make heterogeneity impossible.

The harness should be able to vary:

- per-channel sample rate;
- latency;
- jitter;
- frame/window width;
- dropped samples;
- temporary channel unavailability;
- reordered delivery within declared bounds;
- persistent cross-channel delay.

Noema's learned state should be evaluated for recalibration rather than assuming one permanent alignment.

## 8. Action issuance and sensory consequence

Action/efference information deserves the same separation.

Noema may receive a learner-visible trace that it issued an action. That trace can have a stable action-port identity and local timing information.

It must not automatically contain the evaluator conclusion that a later sensory event was caused by that action.

A useful implementation pattern is therefore:

`issued action trace -> ordinary world dynamics -> later sensor events`

rather than:

`issued action -> observation packet with caused_by_action=<id>`.

Failed, attenuated, delayed, externally duplicated, and jointly caused effects should remain possible.

## 9. Relationship to existing contracts

This contract sharpens, rather than replaces, the existing boundaries.

### Timebase contract

Exact global timestamps remain evaluator-side. P2 timing cues should use only the declared learner-visible temporal basis. Packetization must not reintroduce exact common time by grouping all modalities into one synchronous record.

### Spatial-interface contract

Cross-modal packet grouping must not act as hidden spatial registration. Two fields delivered together should not automatically imply common spatial source or correspondence.

### Origin/provenance contract

Port identity is evidence available to the learner; evaluator source truth remains separate. Stable routing can itself become a source cue and must be varied if source attribution is claimed to generalize beyond the route.

### Developmental-interface contract

Message framing, push-to-talk intervals, ASR windows, pointer events, and UI batching are all packetization decisions and belong in the transducer attribution ledger.

### Scoped structural expansion

A structural adapter or gate may learn from P2 packet/port information if that information is genuinely learner-visible. It must not be trained or routed using withheld P0/P1 fields such as evaluator event IDs, hidden source labels, or exact synchronization metadata.

## 10. F0/F1 implementation requirements

The first implementation specification should include a machine-readable or otherwise exact event-schema declaration covering:

- port/channel identifier semantics;
- payload schema per port;
- sample/frame/window policy;
- learner-visible timing fields;
- buffering/batching behavior;
- dropped/unavailable event representation;
- ordering guarantees;
- transformation provenance;
- evaluator-only fields that are explicitly withheld;
- replay behavior;
- schema versioning.

F0 should validate the boundary before the learner is credited with any result.

F1 should use the same event contract rather than a simplified training-only observation representation that quietly changes the information available.

## 11. Hostile falsification sequence

### SPC-0 — packet-boundary audit

Enumerate every learner-visible grouping and boundary.

Kill condition: an evaluator-derived common-event/source/episode relation is present but undeclared.

### SPC-1 — packet-boundary shift

Shift transducer frame/window boundaries while preserving the underlying continuous/event process.

Pass expectation: competence degrades only to the extent justified by lost evidence, not because meaningful events were memorized as packet positions.

### SPC-2 — split/merge test

Split one transducer packet into several or merge adjacent packets without changing the underlying information content beyond declared timing precision.

This tests whether packet count itself has become ontology.

### SPC-3 — asynchronous sampling

Use different sampling rates across two relevant channels.

Pass requires learned correspondence under heterogeneous sampling rather than exact index-to-index pairing.

### SPC-4 — persistent latency recalibration

Introduce a stable cross-channel delay after initial learning.

Pass requires recalibration or calibrated uncertainty, not permanent reliance on the original alignment.

### SPC-5 — jitter and dropped-sample stress

Introduce bounded jitter, loss, and temporary unavailability.

Pass requires graceful uncertainty/adaptation rather than invented certainty or catastrophic desynchronization.

### SPC-6 — channel-label permutation

Permute arbitrary learner-visible port labels while preserving each stream's statistical/causal role, using an adaptation interval where necessary.

Kill condition: semantic competence depends permanently on arbitrary port names.

### SPC-7 — stable-route source trap

Train one social/source stream on one stable route, then reroute or introduce a second source through the same class of route.

Evaluate whether source attribution can revise rather than equating route identity with person/agent identity.

### SPC-8 — common-packet false-binding trap

Deliver unrelated signals in the same packet/window and related signals across packet boundaries.

Pass requires evidence-sensitive binding rather than `same packet = same event`.

### SPC-9 — action-feedback delay shift

Change action-to-sensory consequence latency, including failed and externally duplicated consequences.

Pass requires revised contingency rather than fixed temporal matching.

### SPC-10 — replay packetization fidelity

Replay must preserve or explicitly declare transformations of packet boundaries, buffering, channel timing, loss, and availability state. Payload-only replay is insufficient when timing/grouping is part of the learner-visible evidence.

### SPC-11 — synchronous-vector baseline

Include a deliberately convenience-rich synchronized-vector baseline when useful.

If it substantially outperforms the lower-subsidy event-stream condition, attribute the gain to the supplied synchronization/grouping and narrow claims accordingly rather than treating the vector result as evidence that Noema learned the missing correspondence.

## 12. Claim ceiling

Passing this contract supports narrow conclusions such as:

> The tested learner acquired cross-stream predictive or control relations under the declared packetization, timing, and channel topology without identified evaluator event/source leakage.

or later:

> The learner's multisensory/action correspondence survived specified packet-boundary, latency, sampling-rate, channel-routing, and replay transformations.

It does not by itself establish:

- human-like multisensory integration;
- human-like perception;
- learned semantic modality concepts;
- learned event segmentation in the unrestricted sense;
- self/other distinction;
- causal understanding;
- that asynchronous events are intrinsically superior to synchronized vectors.

## 13. Architecture implication

No new cognitive module is warranted by this pass.

The architectural consequence is an F0/F1 interface requirement:

> **Noema's first persistent learner should consume a declared transducer/event contract in which packetization, channel topology, timing, and grouping are explicit supplied structure, while common-event/source/semantic correspondence remains learnable unless intentionally supplied.**

This makes the implementation boundary honest without imposing a particular internal representation. It also prevents a polished simulator API from solving the very temporal, spatial, source, and event-binding problems that the Noema research program is meant to investigate.
