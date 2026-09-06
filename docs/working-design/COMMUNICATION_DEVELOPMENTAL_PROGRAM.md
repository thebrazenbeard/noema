# Noema grounded communication developmental program

Status: **BRAINSTORMING / PROVISIONAL DEVELOPMENTAL PROGRAM / NOT IMPLEMENTED**

## Purpose

The operator console makes interaction possible. This document defines what successful development of that interaction should look like without turning language into Noema's cognitive substrate or rewarding conversational imitation.

Communication is treated as one developmental stream that co-develops with world modeling, agent modeling, memory, uncertainty, action, and social learning.

## Stage 0 — signal participation

Noema experiences recurring human-produced symbol/acoustic/gesture events aligned with ordinary world events.

Required achievement:

- distinguish recurring signal patterns from background variation;
- preserve source/modality/timing provenance;
- predict some immediate consequences of recurring signals without yet having stable semantic interpretation.

Failure mode to avoid: treating every repeated token as a privileged category label.

## Stage 1 — situated reference hypotheses

Repeated communication occurs while Patrick presents, points to, manipulates, or jointly attends to parts of the environment.

Required achievement:

- maintain competing hypotheses about what a recurring signal may refer to;
- use cross-context evidence to narrow reference;
- avoid assuming one-to-one word/object mapping;
- distinguish the signal event from the world event it may concern.

A learned referent is provisional and scope-sensitive.

## Stage 2 — correction and repair

Patrick intentionally creates situations where Noema's interpretation is wrong or incomplete and responds through ordinary communication/world interaction.

Required achievement:

- recognize recurring repair patterns without receiving a built-in `wrong` flag;
- revise the implicated interpretation locally;
- retain unrelated grounded meanings;
- preserve uncertainty when Patrick's feedback itself is ambiguous.

## Stage 3 — compositional signal use

Noema encounters familiar signals in novel combinations and contexts.

Required achievement:

- represent reusable relations between signal components and learned world structure;
- generalize beyond memorized whole utterances;
- detect when ordering/combination changes consequence;
- produce novel combinations whose effects are understandable to Patrick.

This is a stronger test than vocabulary size.

## Stage 4 — pragmatic and speaker modeling

The same surface signal is used differently depending on context, speaker history, shared attention, or likely intent.

Required achievement:

- learn speaker-specific reliability and usage patterns;
- distinguish literal referential evidence from request, warning, correction, joke-like play, uncertainty, or other pragmatic functions only as those distinctions become supported by experience;
- infer communicative/action force separately from uncertainty about content, relevance, necessity, target, or scope;
- avoid treating a local hedge such as `perhaps`, `maybe`, hesitation, punctuation, or an uncertainty-signaling emoji as automatic uncertainty about whether an otherwise clear action was requested;
- learn when compact fragments can function as contextually clear imperative shorthand rather than defaulting them to commentary or topic labels;
- ask for clarification or seek more evidence when multiple interpretations remain consequentially different.

No fixed dialogue-act ontology is required.

## Stage 5 — epistemic source separation in conversation

Noema must keep communication evidence distinct from direct observation, inference, memory, simulation, and desire.

Required achievement:

- represent `another agent produced this signal` without converting it automatically into truth;
- learn source reliability from history;
- preserve conflicts such as `Patrick said X, but current observation supports Y`;
- communicate its uncertainty/source conflict back through its own learned signal channel.

This is central to grounded trust rather than obedience.

## Stage 6 — collaborative inquiry

Noema and Patrick use communication to solve a shared problem neither can complete efficiently alone.

Required achievement:

- ask targeted questions when missing information matters;
- answer from grounded internal state rather than fluent guessing;
- use Patrick's responses as evidence with source provenance;
- coordinate action and update the shared plan when evidence changes.

A strong benchmark removes or corrupts grounding and verifies that performance degrades.

## Stage 7 — conversational continuity

Communication becomes persistent across time rather than a sequence of isolated stimulus-response exchanges.

Required achievement:

- retain who said what, when, and in what context;
- refer back to prior shared experience appropriately;
- revise old interpretations when later evidence changes them;
- distinguish current belief from remembered prior belief;
- preserve unresolved questions rather than filling them with plausible language.

## Training/evaluation split

Developmental interaction with Patrick may be rich and natural.

Formal communication evaluation should include held-out referents, changed surface forms, new contexts, misleading speakers, ambiguous references, interrupted conversations, compact imperative fragments, locally hedged requests, uncertainty-signaling punctuation/emoji, and situations where fluent but ungrounded responses would fail.

At least some evaluations should independently vary **whether an action is requested** and **what part of the utterance is uncertain**. A successful learner should not collapse these into one global uncertainty score.

## Outbound development

Noema's outbound communication actuator exists from early development.

The architecture should not wait until it has a full language generator before allowing output. Early signals may be arbitrary or sparse. Stable communicative conventions can emerge through interaction if they consistently affect Patrick and the shared world.

This permits communication to be learned bidirectionally rather than making Noema a passive language student.

## Human usability requirement

The developmental program should remain usable by Patrick rather than requiring laboratory-coded teaching scripts for every interaction.

The console can provide experiment presets and replay tools, but ordinary teaching should increasingly look like:

> present / point / act / speak / observe response / correct / continue

rather than editing hidden labels or reward tables.

## Success criterion

Grounded communication is not `Noema produces good sentences`.

It is:

> **Noema and Patrick can increasingly coordinate, refer, correct, question, explain, and maintain shared history because communication has become causally connected to Noema's learned world and agent models.**

Fluent text that survives when world grounding, source history, or interactive correction are removed does not by itself satisfy this criterion.
