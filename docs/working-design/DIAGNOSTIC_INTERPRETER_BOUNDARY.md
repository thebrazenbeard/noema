# Noema diagnostic interpreter trust boundary

Status: **BRAINSTORMING / PROVISIONAL DIAGNOSTIC CONTRACT / NOT IMPLEMENTED**

## Problem

Patrick needs readable diagnostics before Noema has mature language. But an interpreter that turns internal state into English can create two dangerous illusions:

1. it can accidentally become a privileged teacher if its summaries are fed back into Noema;
2. Patrick can mistake the interpreter's explanation for Noema's own thought or statement.

The diagnostic layer therefore needs a strict trust boundary.

## Three diagnostic classes

### Class A — direct instrumentation

Raw inspectable quantities or structures exposed by Noema itself, such as:

- hypothesis identifiers and support values;
- maturity state;
- current challenger margin;
- prediction distributions;
- memory/provenance references;
- allocation weights;
- deliberation counters/budgets;
- structure lineage events.

These are measurements of internal state, not English interpretations.

### Class B — deterministic derived diagnostics

Human-readable values computed by transparent fixed transformations from Class A, such as:

- `3 live hypotheses`;
- `N_min not reached`;
- `largest challenger margin = 0.18`;
- `model-set inadequacy flag active`;
- plots and timelines.

The derivation should be inspectable and reproducible.

### Class C — interpretive gloss

A separate external interpreter may generate prose such as:

> Evidence currently favors H7, but Noema remains unresolved because H12 predicts a materially different intervention outcome.

This is a **gloss for Patrick**. It may be useful, but it is not Noema's own language unless Noema itself emitted those words through its learned communication channel.

## Visual separation requirement

The console must visually distinguish:

- Noema's own emitted communication;
- direct/derived instrumentation;
- interpreter-generated gloss.

A diagnostic sentence must never appear in the same transcript styling as a Noema message.

## Interpreter uncertainty

The interpreter can itself be wrong.

If a gloss requires mapping opaque learned structure into human concepts, the console should expose the interpreter's confidence or ambiguity and provide a path back to the underlying instrumentation.

The diagnostic layer must not silently convert a speculative interpretation into a fact about Noema.

## No reverse privileged path

Class A/B/C diagnostics do not feed directly back into Noema.

If Patrick deliberately quotes a diagnostic interpretation to Noema, it re-enters only through the ordinary Patrick→Noema communication channel and is treated as another agent-produced signal with normal source uncertainty.

That preserves a crucial distinction between:

- what Noema internally represents;
- what an external tool thinks that representation resembles;
- what Patrick later tells Noema about it.

## Counterfactual inspection

The console should allow Patrick to inspect what different live hypotheses predict under a selected candidate intervention **without applying that intervention to Noema's world**.

This is operator-side analysis of existing internal predictions. It must not change Noema's belief state unless an actual learner-visible event occurs.

This gives Patrick a way to understand why Noema is uncertain without becoming part of the evidence stream by accident.

## Diagnostic observer effect

Patrick's behavior may change after seeing diagnostics. That can legitimately alter Noema through later ordinary interaction.

Formal evaluation therefore needs a blind mode where selected diagnostics are hidden or delayed so Patrick cannot unconsciously teach toward the internal answer.

Development mode can remain fully instrumented.

## Diagnostic honesty rule

The console should prefer `unknown`, `not represented`, or `interpreter uncertain` over inventing a human-readable explanation for an opaque state.

The goal is inspectability, not forcing every internal representation into anthropomorphic prose.

## Architectural implication

Noema's internal representations must expose enough stable provenance, uncertainty, genealogy, and prediction hooks to support diagnostics without requiring a second opaque model to infer everything from behavior.

If a proposed cognitive substrate cannot be inspected except through black-box linguistic interpretation, that is a design cost and should count against it in architecture selection.
