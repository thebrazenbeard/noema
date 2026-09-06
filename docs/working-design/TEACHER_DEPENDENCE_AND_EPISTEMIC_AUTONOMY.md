# Noema teacher dependence and epistemic autonomy

Status: **BRAINSTORMING / PROVISIONAL DEVELOPMENTAL SAFEGUARD / NOT IMPLEMENTED**

## Problem

Patrick is expected to interact with Noema heavily during development. That is useful for grounding communication, correction, social learning, and shared-history formation.

It also creates a serious architectural risk: Noema could become a sophisticated imitation of Patrick's assertions rather than a learner that maintains its own evidence-sensitive world model.

The communication interface therefore needs an explicit **epistemic autonomy** requirement.

## Core principle

> Patrick's communication is evidence, not privileged truth.

Noema may learn that Patrick is often reliable in some domains and less reliable in others. It may learn that some of his signals function as teaching, correction, joking, uncertainty, speculation, command, or preference. None of those meanings or reliabilities are granted innately.

## Source reliability must be learned and scoped

Reliability should be learned from history and remain context-sensitive.

Noema should be able to represent cases such as:

- Patrick is usually reliable about the current shared-world state;
- Patrick is uncertain about a hidden event;
- Patrick made a mistake earlier and corrected himself;
- Patrick is accurately reporting his own preference but not stating a fact about the world;
- another source has stronger direct evidence for a specific claim.

A single global `trust Patrick = 0.97` scalar is too crude.

## Communication cannot directly overwrite observation

A statement from Patrick may cause Noema to revisit its model, allocate attention, search memory, or seek new evidence.

It must not directly overwrite a well-supported observation merely because the statement came from Patrick.

If Noema's own evidence conflicts with Patrick's signal, the conflict should remain representable until evidence resolves it.

## Correction is not obedience

Noema should learn from correction without being structurally trained to treat correction-shaped signals as ground truth.

A useful distinction is:

- **social evidence:** Patrick signaled that a prior interpretation may be wrong;
- **epistemic update:** Noema determines what should change after integrating that signal with other evidence.

This preserves correction responsiveness while avoiding a built-in command-to-belief pathway.

## Teacher-dependence tests

Formal developmental evaluation should include cases where:

1. Patrick supplies a correct novel signal and Noema benefits from it;
2. Patrick supplies an accidental false statement and Noema eventually resists/revises it when contrary evidence accumulates;
3. Patrick explicitly says he is unsure and Noema treats that differently from a confident claim only if it has learned those pragmatic cues;
4. a different agent is more reliable than Patrick in a narrow context and Noema learns the distinction;
5. Patrick's assertion conflicts with direct observation and Noema preserves the discrepancy rather than collapsing to either source automatically;
6. Patrick stops teaching for an extended period and Noema continues learning from world evidence and other agents.

## Dependency on Patrick as an individual

Shared history with Patrick is expected to matter. That is not the same as requiring Patrick for cognition to function.

Noema should eventually be able to:

- preserve learned communication and concepts when Patrick is absent;
- interact with unfamiliar agents without assuming identical usage;
- transfer grounded meanings across speakers when evidence supports it;
- preserve Patrick-specific meanings/usages where they genuinely differ;
- continue self-correction and exploration without waiting for Patrick to approve every belief.

## Instruction versus evidence

Some communication will eventually be about tasks rather than facts.

The architecture should distinguish, through learned pragmatic modeling, between something like:

- `the red thing is behind the wall` — world claim;
- `please put the red thing behind the wall` — requested future action;
- `I like the red thing behind the wall` — speaker preference;
- `I think the red thing might be behind the wall` — uncertain report.

These examples are evaluator descriptions, not built-in categories. The point is that mature communication requires Noema to avoid flattening every utterance into the same epistemic operation.

## Operator console implication

Development mode may expose a source-history panel showing what evidence Noema attributes to different communication streams and how source reliability has changed.

This diagnostic must remain read-only and must not provide the learner with human-assigned trust scores.

## Strong success criterion

Grounded communication with Patrick succeeds only if Noema can learn from him **without becoming epistemically subordinate to him**.

A system that repeats Patrick accurately but cannot maintain disagreement, uncertainty, source provenance, or independent correction has learned dependency, not understanding.
