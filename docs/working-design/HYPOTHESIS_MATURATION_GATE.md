# Noema hypothesis maturation gate

Status: **BRAINSTORMING / CANDIDATE CONFIDENCE-GATING MECHANISM / NOT IMPLEMENTED**

## Correction

A bounded hypothesis population needs two different bounds:

1. a **maximum deliberation budget** so hypothesis search cannot run forever;
2. a **minimum maturation window** before certainty/commitment machinery is allowed to harden a newly proposed hypothesis.

These solve different problems.

The maximum prevents endless thinking. The minimum prevents premature certainty.

## Core idea

A newly proposed hypothesis begins in a **pre-commitment state**.

For the first `N_min` qualifying hypothesis-evaluation cycles, Noema may:

- update parameters;
- compare predictions;
- generate challengers;
- run bounded counterfactual checks;
- use the current best-supported model provisionally for prediction/action;
- retain ordinary uncertainty estimates for calibration and resource allocation.

But it may **not yet use certainty as a reason to consolidate the hypothesis, prune materially distinct challengers, or treat the hypothesis as settled**.

Only after the hypothesis survives at least `N_min` qualifying challenge/evidence cycles does it become eligible for confidence-based promotion to a working belief.

This is a maturation gate, not a rule that repeated looping itself creates confidence.

## A loop only counts when something epistemically happened

Repeatedly recomputing the same score over the same evidence must not make a hypothesis more certain.

A cycle should count toward maturation only when it includes at least one materially new epistemic event, such as:

- new observation evidence;
- a new intervention outcome;
- a held-out prediction test;
- comparison against a materially distinct challenger;
- a counterfactual test that exposes a new behavioral distinction;
- transfer to a new context;
- a meaningful failed prediction or anomaly;
- a new structural proposal that survives initial evaluation.

Exact qualifying-event rules belong in the implementation plan and should be pre-registered for Experiment A.

## What activates after `N_min`

After the minimum maturation window, the system may apply stronger commitment criteria.

Promotion should still require evidence, not age alone. Candidate criteria include:

- calibrated predictive quality above a floor;
- support margin over the strongest behaviorally distinct challenger;
- survival across materially different evidence conditions;
- no unresolved counterfactual disagreement that matters in the current scope;
- anomaly debt below a reopening threshold;
- acceptable complexity/resource cost.

A hypothesis that survives `N_min` loops but remains poorly supported stays provisional.

## Why this may be better than immediate certainty weighting

If confidence-based pruning is active from the first proposal cycle, random initialization, early noise, insertion order, or one lucky fit can kill alternatives before they receive a fair test.

The maturation window gives competing explanations a small guaranteed runway.

That is especially important in Experiment A, where passive evidence is intentionally non-identifying. A candidate should not be able to become "certain" merely because it happened to instantiate one orientation first.

## Interaction with the maximum loop budget

Let:

- `N_min` = minimum qualifying cycles before confidence-based promotion is permitted;
- `N_max` = maximum deliberation cycles/resources for the current epistemic episode.

Then:

- before `N_min`: explore/update, but no certainty-based consolidation;
- from `N_min` to `N_max`: promotion/consolidation may occur if evidence thresholds are met;
- at `N_max`: stop deliberating even if certainty is insufficient, preserve unresolved uncertainty, and act/predict with the best bounded belief state available.

This means the architecture can be both **patient enough not to decide too early** and **bounded enough not to think forever**.

## Decisive evidence before maturation

The gate should not force Noema to ignore overwhelming evidence that arrives early.

If a decisive intervention makes one hypothesis vastly better than its challengers before `N_min`, Noema may immediately use that model provisionally for prediction and action.

The restriction is on **hardening and deleting alternatives**, not on noticing strong evidence.

This preserves responsiveness without allowing one early event to become irreversible epistemic lock-in.

## Maturation is per claim/structure, not a global age

The relevant counter should attach to a hypothesis, dependency, or bounded claim scope.

An old system can still form a brand-new hypothesis that must earn maturation. Conversely, a mature learned structure does not need to restart from zero every time it is merely reused in the scope where it already has evidence.

A materially changed or reopened hypothesis may require partial or full rematuration depending on how much of the original support remains valid.

## Consolidation remains a later stage

Passing `N_min` should only make a hypothesis eligible to become a **working belief**.

Deeper consolidation should require stronger evidence over longer time and broader contexts.

A provisional lifecycle is therefore:

`proposed -> pre-commitment -> working belief -> consolidated`

with:

`contradictory evidence/anomaly -> reopened -> rematuration as needed`

No stage means metaphysical certainty.

## Experiment A tests

Experiment A should explicitly vary `N_min` and `N_max` under fixed compute budgets.

Failure modes to test:

- **too-small `N_min`:** premature lock-in before challengers are fairly evaluated;
- **too-large `N_min`:** needless hesitation despite decisive evidence;
- **too-small `N_max`:** the correct alternative often dies unresolved for lack of search time;
- **too-large `N_max`:** apparent success is purchased by effectively unbounded deliberation;
- **fake maturation:** repeated passes over identical evidence increase commitment;
- **early-evidence rigidity:** a strong early lead becomes impossible to reopen later.

The target is not one magical universal number. The experiment should identify whether a bounded maturation mechanism is useful and robust across a reasonable range.

## Current verdict

Patrick's loop-gating idea improves the bounded-population proposal.

The strongest current version is:

> **certainty-based commitment is gated by a minimum number of qualifying hypothesis challenge/evidence cycles, while the entire deliberation episode is separately capped by a maximum resource/loop budget.**

The counter grants eligibility for commitment; it does not manufacture confidence. Evidence still determines whether commitment is warranted.
