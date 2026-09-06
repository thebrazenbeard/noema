# Noema grounded communication and operator interface

Status: **BRAINSTORMING / PROVISIONAL / NOT AN APPROVED IMPLEMENTATION ARCHITECTURE**

## Core correction

Noema should not be designed as an intelligence that becomes useful only after it eventually learns language.

The stronger requirement is:

> **Noema's intelligence must not depend on language as its cognitive substrate, but communication should be a first-class developmental track from the beginning.**

Language is therefore neither the mind nor a late accessory. It is an environmental signal and action channel that must become grounded in the same persistent world model, agent models, memory, uncertainty, action, valuation, and learning processes that support the rest of cognition.

## Patrick ↔ Noema communication channel

Patrick should be able to communicate with Noema during development.

Early communication may be limited or immature, but Patrick's speech, text, gestures, demonstrations, corrections, and other signals can enter Noema as observations produced by another agent. Noema should learn what those signals refer to through experience rather than receiving their meanings as privileged ground truth.

Grounding evidence may include:

- co-occurrence with perceived entities, events, actions, and consequences;
- joint attention and repeated reference;
- temporal and spatial context;
- another agent's behavior before and after a signal;
- correction and contradiction;
- memory of prior uses by the same and different agents;
- action-conditioned tests of competing interpretations.

Noema should eventually be able to emit communicative signals back through its own action interface. Text and voice are acceptable communication modalities, but using them must not silently provide a pre-authored semantic ontology.

## Separation from diagnostic interpretation

Development also needs an operator-facing diagnostic channel so Patrick can inspect Noema before Noema has mature language.

That channel is conceptually separate from Noema's learned communication.

A diagnostic interpreter may render inspectable internal state into human-readable summaries such as:

- current competing hypotheses and confidence;
- active predictions;
- relevant recalled episodes;
- salient or highly allocated observations;
- candidate actions and expected outcomes;
- prediction errors and revision targets;
- evidence provenance and epistemic mode.

The diagnostic interpreter is **read-only with respect to Noema's cognition**. Its human-readable labels are for the experimenter and must not be fed back into the learner as privileged semantic facts.

If diagnostic output is ever deliberately reintroduced to Noema, it must enter through an ordinary observable communication channel and be treated as another agent-produced signal, not as internal ground truth.

## Anti-cheating boundary

Communication support must not leak answers that Noema is supposed to learn.

The interface must not supply hidden semantic labels such as `OBJECT`, `SELF`, `AGENT`, `CAUSE`, `TRUE`, `HELPFUL`, `PAIN`, stable object identity, another agent's hidden beliefs, or evaluator conclusions merely because those labels are convenient for a conversational UI.

A word or sentence may be observed as a signal. Its referent, pragmatic force, reliability, speaker-specific meaning, and relationship to the world should remain learnable hypotheses.

## Grounded communication as an intelligence criterion

Conversational fluency alone does not count.

A meaningful communication capability should require Noema to demonstrate that language or other signals are causally grounded in learned world and agent models. Candidate tests include:

- learning a novel word or signal through situated interaction rather than a definition table;
- resolving ambiguous reference using shared context and asking for clarification when evidence is insufficient;
- revising an interpretation after correction without erasing unrelated knowledge;
- distinguishing what another agent said from what Noema itself observed or believes;
- transferring a learned term or relation into a novel situation;
- coordinating action through communication in ways that fail when grounding evidence is removed;
- detecting when the same signal is used differently by different agents or in different contexts.

## Operator interface implication

A future Noema Console exposes two explicitly different channels:

1. **Learned communication:** Patrick ↔ Noema through ordinary perceptual and action channels.
2. **Diagnostic instrumentation:** Noema → interpreter → Patrick, with no privileged reverse path.

The console is now specified concretely in `OPERATOR_CONSOLE_SPEC.md`: a shared world pane, direct text/voice communication pane, read-only state/diagnostic pane, and separate operator controls. The first usable version may exist before 3D embodiment is complete; Experiment A remains language-free during formal runs while the surrounding console can still be used for observation and experiment control.

## Current provisional modality stance

Typed text is the first practical direct communication channel because it can be exposed as minimally interpreted symbol sequences without requiring Noema to first solve speech perception.

Voice should also be supported as a first-class route, but its sensory boundary must remain explicit: raw/low-level acoustic input tests speech learning, while external speech-to-text is an optional sensory transducer that imports segmentation/spelling and therefore cannot count as evidence that Noema learned those perceptual capabilities itself.

Noema should have an outbound communication actuator from early development even when its output is initially immature or meaningless.

## Open questions

- exact raw symbol encoding for early text;
- exact acoustic front end for developmentally pure voice;
- whether diagnostic interpretation is deterministic over inspectable structures, model-assisted, or both;
- how interpreter uncertainty is represented so Patrick can distinguish Noema's actual state from the interpreter's gloss;
- what tests best separate grounded communication from memorized linguistic response patterns.
