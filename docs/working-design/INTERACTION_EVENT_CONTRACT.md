# Noema interaction event contract

Status: **BRAINSTORMING / PROVISIONAL INTERFACE CONTRACT / NOT IMPLEMENTED**

## Purpose

The operator console is only useful if it is explicit about what actually crosses the boundary into Noema.

A convenient UI can accidentally leak semantic answers through metadata, object selectors, labels, helper APIs, or diagnostic state. The interaction contract therefore separates three event planes and constrains the information each plane may carry.

## Event planes

### 1. World/perceptual events

These are ordinary things Noema can perceive in its environment: visual/acoustic/tactile-like signals, state changes, agent movement, pointing gestures, object presentation, barriers, resource changes, and other scenario-visible consequences.

The event payload may contain low-level modality/timing information required by the sensory interface. It must not contain hidden simulator semantics such as stable object identity, class labels, causal role, agent intent, truth value, or evaluator answer keys.

### 2. Communication events

These are signals emitted by another agent and available to Noema as learnable observations.

Early examples include typed symbols, acoustic input, gesture, demonstrations, and corrections.

Allowed metadata is limited to low-level channel provenance needed to distinguish modalities and temporal origin. Meaning, speaker identity, reliability, pragmatic force, reference, command status, and truthfulness remain learned hypotheses.

### 3. Operator/control events

These are experimenter-side actions such as pause, checkpoint, load scenario, reset, toggle diagnostics, or start recording.

By default these events are **outside Noema's world** and do not become perceptual evidence.

If an experiment deliberately makes an operator action observable, the consequence must be routed through an ordinary world or communication channel. The control command itself must not appear as privileged semantic input.

## Minimal event envelope

A low-level event envelope may contain only the information necessary to preserve causally relevant timing and modality, for example:

- monotonic event/time index;
- source channel address;
- modality identifier;
- raw or minimally transformed payload;
- delivery timing/duration;
- action/efference marker only for Noema's own issued actuator commands where the developmental contract permits it;
- observation validity/availability where a physical sensor would expose that fact.

It must not contain semantic fields such as `object_id`, `speaker_name`, `trusted_source`, `correct_answer`, `intent`, `emotion`, `command`, `cause`, `goal`, or `meaning` unless Noema itself later learns and represents those concepts internally.

## Joint attention without hidden IDs

The console needs a practical way for Patrick to point at things.

A click in the UI must not inject the simulator's object identifier into Noema.

Instead, the console should translate Patrick's action into an observable pointing/attention event in the shared world: a ray, gesture, cursor-like marker, gaze direction, or another perceptible signal. Noema then has to infer what Patrick is referring to from ordinary context.

This preserves convenience for Patrick without turning pointing into an ontology oracle.

## Correction without answer-key injection

Patrick must be able to correct Noema early.

Correction is represented as another communication/world interaction, not as a privileged `wrong=true` flag tied to the internal hypothesis that the evaluator knows is wrong.

Noema may eventually learn that certain recurring signals from Patrick often function as corrections, but that is part of agent/source/pragmatic learning rather than a built-in semantic channel.

## Operator observability

The console should provide an operator-side event inspector that shows:

- what Patrick did in the UI;
- what low-level event was actually delivered to Noema;
- what hidden simulator/evaluator state was deliberately withheld;
- what diagnostic information was visible only to Patrick.

This is an anti-cheating and debugging feature. It lets us verify that a convenient interface action did not silently become a privileged input.

## Replay and audit

Developmental experiments should be able to log the low-level delivered event stream separately from operator-only controls and diagnostics.

A replay should reconstruct the same learner-visible event sequence without needing semantic UI metadata.

This creates a clean audit question: **could Noema's behavior be explained by anything that entered through the learner-visible event stream?**

If not, the experiment is invalid or the instrumentation boundary is leaking.

## Design consequence

The Noema Console is not merely a GUI. It is an information-flow boundary.

Every future input widget, pointing mechanism, voice/transcription path, world editor, or experiment control must declare which event plane it belongs to and exactly what learner-visible information it emits before it is treated as part of the developmental interface.
