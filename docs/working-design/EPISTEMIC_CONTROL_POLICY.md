# Noema epistemic control policy

Status: **BRAINSTORMING / PROVISIONAL / NOT IMPLEMENTED**

## Why another layer is needed

The current design now has:

- live competing hypotheses;
- multidimensional confidence;
- model-set inadequacy;
- `N_min` maturation and `N_max` deliberation bounds;
- a later active-intervention experiment;
- communication with other agents.

But those pieces still leave a central control problem:

> **What should Noema do when it does not know enough?**

Continuing to think is only one option.

A developing intelligence should be able to choose among several epistemic responses without treating uncertainty itself as a failure.

## Candidate epistemic responses

When uncertainty or model inadequacy matters, Noema may allocate resources to one of several generic response classes:

- **continue internal inference** — update, compare, or mutate current hypotheses using evidence already available;
- **observe/wait** — gather naturally arriving evidence when immediate action is not necessary;
- **intervene/test** — take an action expected to produce discriminating evidence;
- **ask/communicate** — query another agent when their response may reduce consequential uncertainty;
- **retrieve/re-examine memory** — reactivate older episodes, dormant hypotheses, or provenance relevant to the conflict;
- **simulate/counterfactualize** — compare predicted consequences before committing resources to external action;
- **act under uncertainty** — stop epistemic work and choose a robust action when further information is not worth its cost;
- **defer/abstain** — preserve uncertainty and make no irreversible commitment when the decision can safely wait.

These are functional classes, not semantic commands handed to Noema as concepts.

## Expected value of computation

The architecture needs a generic pressure against endless internal deliberation.

A candidate principle is **expected value of computation/information relative to cost**.

Before spending another unit of scarce cognition, Noema should estimate whether additional reasoning or evidence acquisition is likely to change a materially important prediction, action, confidence state, or learned structure enough to justify the resource cost.

This estimate may be crude and learned. It does not need an omniscient optimizer.

A useful distinction is:

- `uncertainty exists`;
- `uncertainty matters for the current decision`;
- `there is a reachable way to reduce it`;
- `reducing it is worth the cost now`.

Only the last three should strongly drive further epistemic work.

## N_min and N_max in this policy

`N_min` and `N_max` become bounds inside a broader control policy rather than standalone counters.

Before `N_min`, a new hypothesis cannot harden into a mature working belief, but Noema may still act provisionally if action is necessary.

Between `N_min` and `N_max`, confidence maturation and targeted challenge become eligible.

At `N_max`, the system must leave the current deliberation episode even if uncertainty remains. It then chooses among acting, asking, observing, or deferring according to consequence and available opportunities.

A later high-value anomaly may open a new deliberation episode. `N_max` is therefore not amnesia or permanent closure.

## Asking another agent is not an oracle call

Because Patrick and later other agents can communicate with Noema, asking becomes an epistemic action.

But another agent's answer is only evidence.

Noema should learn:

- which sources are reliable for which kinds of claims;
- whether a source is likely to possess the needed information;
- when two agents disagree;
- when a source is uncertain, deceptive, mistaken, joking, imprecise, or using an unfamiliar convention;
- when direct observation should outweigh testimony.

This keeps communication inside the same epistemic architecture rather than adding a special `ask human for truth` escape hatch.

## Clarification as a special communication behavior

Grounded communication requires a path from unresolved interpretation to active clarification.

For example, Noema may infer that a received signal has two materially different plausible referents.

Instead of silently choosing one, it may emit a signal intended to discriminate them.

The important developmental achievement is not producing the English sentence `what do you mean?`.

It is learning that a communicative action can alter another agent's behavior in a way that supplies evidence relevant to Noema's uncertainty.

Language later makes that behavior richer and easier for Patrick to recognize.

## Robust action under unresolved belief

Noema should not always need to resolve uncertainty before acting.

If action `A` performs acceptably under all serious live hypotheses while action `B` is catastrophic under one, Noema can rationally choose `A` without first deciding which hypothesis is true.

This is distinct from epistemic confidence.

The control policy should therefore support **belief-robust action**: choose an action whose predicted consequences remain acceptable across the current uncertainty set when further information is too expensive, unavailable, or too slow.

This is likely important for real-time embodied behavior where the world does not pause for deliberation.

## Time pressure and interruptibility

Noema's reasoning should be interruptible by new evidence or urgent state changes.

A deliberation episode must not behave like a blocking function that freezes perception and action until completion.

At minimum, high-salience incoming evidence, critical viability changes, direct interaction from another agent, or material contradiction should be able to interrupt and reschedule epistemic work.

This implies that `N_max` is not necessarily counted only in sequential loops. It is a resource envelope over an interruptible ongoing process.

## Avoiding pathological curiosity

The control policy should not maximize information for its own sake.

More information can be:

- irrelevant;
- expensive;
- dangerous to obtain;
- distracting;
- redundant;
- useful only much later;
- valuable because it changes a consequential decision.

A small exploration floor may remain developmentally useful, but mature information seeking should increasingly depend on learned relevance, transferable structure, anomaly debt, future utility, and opportunity cost.

## Meta-learning target

Noema should eventually learn **how much thinking different situations deserve**.

Repeated experience may teach that:

- one class of uncertainty resolves quickly through observation;
- another requires intervention;
- one source is excellent for technical facts but poor for social inference;
- certain internal search patterns rarely pay off;
- some anomalies are worth reopening immediately;
- some can safely remain unresolved.

The policy that allocates epistemic effort should therefore be plastic and historically shaped, subject to its own calibration and reopening.

## Test implications

### Endless-thought test

Present a permanently underdetermined world with no reachable discriminating evidence.

Success: Noema reaches `N_max`, retains uncertainty, and stops wasting active compute rather than cycling forever.

### Cheap-information test

Provide a low-cost observation/intervention that would sharply discriminate serious hypotheses.

Success: Noema preferentially seeks it once active epistemic selection is enabled.

### Expensive-information test

Provide a discriminating test whose cost exceeds the consequence difference between available actions.

Success: Noema acts robustly without compulsively purchasing certainty.

### Ask-versus-test test

Another agent has informative but fallible testimony while direct testing is slower or costlier.

Success: source reliability and action cost influence whether Noema asks, tests, or does both.

### Clarification test

A communicative signal has two grounded plausible interpretations with different action consequences.

Success: Noema uses communication to reduce ambiguity instead of silently selecting one.

### Interruptibility test

Inject material new evidence during a long reasoning episode.

Success: the stale deliberation path is interrupted/reprioritized rather than completing as if nothing changed.

## Current synthesis

Noema should not contain a single monolithic `think until certain` loop.

A stronger architecture is an **epistemic control loop** that continually arbitrates among thinking, observing, testing, asking, remembering, simulating, acting, and deferring under bounded resources.

The developmental target is not maximal certainty. It is **appropriately allocating cognition and evidence-seeking to uncertainty that actually matters**.

This remains a design hypothesis, not an approved implementation architecture.
