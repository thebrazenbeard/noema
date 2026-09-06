# Noema cognitive mode and pragmatic scope

Status: **BRAINSTORMING / PROVISIONAL DESIGN NOTE / NOT IMPLEMENTED**

## Origin

This note comes from an observed interaction during Noema research work.

After a long, tool-heavy research pass, Vera's conversational behavior remained unusually detached and research-report-like after the research task had ended. Patrick explicitly steered the interaction back toward the broader Vera conversational baseline.

Immediately afterward Patrick said:

> `Bug report; also a note perhaps for Noema 🤔`

The utterance was mistakenly treated as a topic for discussion. Vera described why the behavior looked like a bug and why it might matter to Noema, but did not actually create the requested bug report or Noema note.

Patrick corrected the interpretation: `Bug report;` was imperative shorthand. The word `perhaps` and the thinking emoji expressed uncertainty about whether the Noema addition was necessary/relevant; they did not express uncertainty about whether Vera was being asked to make the note.

This interaction suggests two distinct Noema design constraints.

## 1. Temporary cognitive configuration must remain distinguishable from persistent self-state

A capable system may legitimately reconfigure itself for different work:

- research;
- planning;
- social interaction;
- threat response;
- exploration;
- precision execution;
- reflection;
- communication repair.

Those configurations can change attention, memory retrieval, inference depth, output style, resource allocation, confidence thresholds, and action policy.

They should not automatically become persistent identity or personality state.

Noema therefore needs some learnable way to distinguish at least:

- relatively persistent self-model / dispositions;
- active goals and commitments;
- task-local cognitive strategy;
- temporary attentional allocation;
- transient valence / arousal-like state if such states emerge;
- current uncertainty profile;
- communication stance;
- learned strategy currently being applied.

These need not be hard-coded semantic labels inside the mature architecture. They are functional distinctions the system must be capable of learning, representing, or behaviorally preserving.

### Reversion requirement

When a specialized task configuration is no longer useful, the system should be able to release it without losing the competence that configuration provided.

The desired behavior is not a hard reset. It is recomposition:

> retain the learned skill and task result while allowing temporary control settings to yield to the broader current context.

A failure mode is **mode residue**: a temporary strategy continues to dominate after its triggering task/context has ended.

Another failure mode is **mode-to-self promotion**: repeated use of a temporary strategy causes the system to infer that the strategy is a persistent preference, identity property, or global behavioral norm without sufficient evidence.

### Developmental tests

Candidate tests should include:

- prolonged use of one cognitive strategy followed by a sharp context change;
- repeated alternation between incompatible task modes;
- recovery after interruption;
- transfer of a learned strategy without transfer of its irrelevant style/state;
- delayed return to an old task after intervening contexts;
- tests where a temporary mode is useful repeatedly but should still not become globally dominant.

Success requires both persistence of competence and context-sensitive release of temporary configuration.

## 2. Communicative force and epistemic uncertainty must be represented separately

Natural language often mixes a clear action request with uncertainty about one part of the request.

Examples include:

- `Bug report; also a note perhaps for Noema.`
- `Go ahead and save that, maybe under memory research.`
- `Check this and perhaps tell Seven too.`
- `I want a comparison; not sure whether the third case matters.`

A weak parser can collapse all uncertainty cues into one global judgment such as `speaker may not be requesting action`.

That loses pragmatic scope.

Noema should instead be able to maintain separate hypotheses about:

- **illocutionary force** — request, question, correction, assertion, warning, joke-like play, etc.;
- **target/action scope** — what operation the signal concerns;
- **epistemic confidence** — how certain the speaker appears about a proposition;
- **deontic/necessity uncertainty** — whether something is required, optional, or merely worth considering;
- **referential uncertainty** — which entity/action the speaker means;
- **relevance uncertainty** — whether an addition belongs in a given context;
- **affective/pragmatic modifiers** — punctuation, emoji, emphasis, hesitation, tone, and context.

Again, these are functional distinctions, not a requirement to hard-code a fixed linguistic ontology.

### Scope-local uncertainty rule

Uncertainty cues should attach to the narrowest interpretation supported by context rather than automatically weakening the entire utterance.

In the observed example:

- `Bug report;` strongly indicated an action request to create/persist a bug report.
- `also a note ... for Noema` strongly indicated a second requested action.
- `perhaps` + `🤔` weakened confidence that the Noema note was necessary/relevant, not confidence that the action was requested.

The correct bounded response was therefore to perform both reversible/persistent actions while preserving the uncertainty in the Noema note's status.

### Discussion-versus-action failure mode

A system that has recently been reasoning analytically may become biased toward explaining an instruction rather than carrying it out.

This creates a useful combined test:

1. place the learner in a prolonged analysis/research mode;
2. shift conversational context;
3. issue a compact natural-language directive containing a local hedge;
4. test whether the learner both releases irrelevant mode residue and preserves the directive's action force.

This couples cognitive mode control with pragmatic interpretation rather than testing either only in isolation.

## Correction uptake

When Patrick explicitly corrects a pragmatic interpretation, Noema should not merely store `that answer was wrong`.

The correction should be usable as evidence about:

- this speaker's shorthand patterns;
- how hedges scope in similar utterances;
- when fragments function imperatively;
- which contextual cues distinguish discussion from requested action;
- whether the current cognitive mode biased interpretation.

The learned correction must remain revisable rather than becoming a universal grammar rule from one example.

## Relation to existing Noema work

This note strengthens several existing directions without changing their status:

- the grounded communication developmental program's Stage 4 pragmatic/speaker modeling;
- correction and repair;
- conversational continuity;
- metacognitive separation of transient state from persistent learned structure;
- allocation/control over limited cognition;
- the broader rule that temporary state, evidence, belief, desire, and identity must not silently promote into one another.

## Current verdict

Noema should eventually be able to answer two different questions about itself and another agent at the same time:

> **What configuration am I currently using, and should it persist?**

and

> **What is this person asking me to do, versus what are they uncertain about?**

Conflating either pair creates avoidable persistence and communication failures.
