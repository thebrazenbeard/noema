# Noema model inadequacy and belief maturation

Status: **BRAINSTORMING / PROVISIONAL / NOT IMPLEMENTED**

## Core problem

A bounded hypothesis population can still fail if it assumes that one of its current hypotheses must be correct.

Noema therefore needs an explicit epistemic state for:

> **none of my current explanations are good enough.**

This state is distinct from ordinary uncertainty among plausible live hypotheses.

Ordinary uncertainty says: `one or more current alternatives may explain the evidence, but I cannot yet discriminate them.`

Model inadequacy says: `the current hypothesis set, taken as a whole, is failing.`

Without this distinction, Noema can crown the least-bad member of a bad population and become self-sealing.

## Model-set adequacy

Noema should maintain an adequacy judgment over the current live hypothesis set as a whole.

Evidence that may lower model-set adequacy includes:

- persistent prediction error shared by all live hypotheses;
- intervention outcomes that surprise all live hypotheses;
- repeated transfer failure;
- poor calibration across the whole population;
- systematic residual structure not localized to one current model;
- contradictory evidence that cannot be repaired by local parameter revision;
- repeated counterfactual or planning failure under all serious alternatives;
- a new candidate that explains previously unrelated anomalies with lower total complexity.

Model-set adequacy is not a semantic label such as `ontology wrong`. It is an operational signal that the current explanatory population is collectively insufficient.

## What happens when adequacy falls

Low model-set adequacy should not immediately trigger unlimited global search.

Instead it changes the search regime.

Provisional response sequence:

1. verify that the failure is not explained by corrupted input, transient noise, stale state, or a known nonstationary regime;
2. increase proposal diversity and relax local structural assumptions within a bounded resource budget;
3. reactivate relevant dormant lineages whose old predictions better fit the new evidence;
4. permit larger structural mutations than ordinary local repair;
5. preserve existing useful substructure that still predicts well rather than globally resetting everything;
6. if no improved candidate emerges before the reasoning budget expires, retain an explicit unresolved/inadequate state.

The correct output can therefore be `I do not currently have an adequate model` rather than false certainty.

## Confidence is multidimensional

One scalar confidence value is too lossy for a developing learner.

A hypothesis may fit passive observations well while having weak intervention support. Another may predict locally but transfer badly. A third may be highly calibrated only within a narrow context.

The current design therefore treats epistemic confidence as a small structured profile rather than one universal certainty number.

Candidate dimensions include:

- **predictive support** — how well the hypothesis predicts observed data;
- **interventional support** — how well it predicts outcomes when actions/interventions alter conditions;
- **calibration** — whether confidence tracks actual success/failure frequency;
- **scope** — where the evidence currently supports the hypothesis;
- **transfer support** — whether the learned relation survives changed surface form;
- **stability** — whether support persists across time/regimes;
- **challenger margin** — how strongly it exceeds the best materially distinct live alternative;
- **model-set adequacy contribution** — whether this hypothesis actually repairs population-wide failure or merely wins inside an inadequate set.

These dimensions need not all be independent physical variables in a future implementation. They are current design constraints on what a commitment score must not collapse prematurely.

## Maturation gate

Patrick proposed that certainty should not become eligible immediately. A hypothesis should first survive a minimum number of **meaningful epistemic cycles**.

This remains the stronger current design.

Let:

- `N_min` = minimum meaningful cycles before a hypothesis may mature into an ordinary working belief;
- `N_max` = maximum bounded deliberation budget for the current reasoning episode.

A meaningful cycle requires new epistemic content: new evidence, a materially different challenger, an intervention result, a held-out prediction, a transfer trial, a counterfactual test, an anomaly, or another event that could genuinely change the hypothesis state.

Replaying the same evidence does not advance maturation.

`N_min` only unlocks eligibility. It does not manufacture confidence.

After `N_min`, the hypothesis must still satisfy its relevant confidence dimensions and challenger/adequacy conditions.

## Deliberate challenge phase

Before a hypothesis moves from working belief toward consolidation, Noema should spend a bounded amount of effort looking for evidence that would make it fail.

The design question is not merely:

> `what supports this hypothesis?`

but also:

> `what reachable observation or intervention would produce a materially different outcome if this hypothesis were wrong?`

This **challenge phase** is not unlimited skepticism. It is a bounded falsification attempt applied when a belief is about to become cheap/default/persistent.

Candidate challenge operations include:

- identify the strongest live challenger and the condition where predictions diverge most;
- search for a reachable intervention with high discriminative value;
- test a held-out context where the model's transfer claim matters;
- inspect anomaly debt specifically associated with the candidate;
- test whether confidence rests on one fragile source or repeated independent evidence;
- compare against a simpler or structurally different candidate where available.

Failure to find a useful challenge does not prove truth. It merely allows maturation if the evidence profile is already strong enough.

## Hypothesis genealogy

Noema should retain bounded lineage information when hypotheses evolve.

A hypothesis may:

- descend from a previous hypothesis by local revision;
- split into competing alternatives;
- merge with another explanation;
- become dormant;
- be reopened after contradiction;
- be retired while leaving reconstructable evidence traces.

Genealogy should record enough to answer operational questions such as:

- what evidence caused the split/revision;
- what earlier evidence still supports the descendant;
- which failures caused retirement;
- which old alternative may be worth reactivating under new anomaly debt;
- whether a learned proposal strategy repeatedly recreates the same failed structure.

Genealogy is not autobiographical narrative. It is an epistemic dependency/history structure that supports local correction and meta-learning.

## Belief confidence versus action commitment

Noema should not require high epistemic certainty before acting.

Belief and action solve different problems.

A system can rationally hold:

- `60% belief that state A is true`, while
- `90% action commitment to action X`, because X performs acceptably across both A and its serious alternatives.

Conversely, Noema may be 99% certain about a fact that is irrelevant to any current action.

Therefore:

- epistemic confidence estimates support for a hypothesis;
- action commitment depends on predicted consequences across live beliefs, active concerns, uncertainty, risk, and decision relevance;
- action selection must not feed desirability back into epistemic confidence.

This preserves the existing epistemic-conative firewall.

## Failure modes this design is meant to prevent

### Least-bad coronation

All current hypotheses are poor, but one scores slightly better and is treated as truth.

**Protection:** population-wide adequacy state.

### Confidence by repetition

A hypothesis becomes mature because the same evidence was processed repeatedly.

**Protection:** meaningful-cycle maturation count.

### Consolidation by applause

A hypothesis accumulates support but is never exposed to a serious challenger.

**Protection:** bounded challenge phase before consolidation.

### Ontology self-sealing

The learned proposal policy only proposes descendants of its current worldview.

**Protection:** low-adequacy search regime, dormant-lineage reactivation, and bounded exploratory structural mutation.

### Genealogical amnesia

Noema repeats an old failed explanation because it forgot why it was abandoned.

**Protection:** bounded hypothesis lineage and failure provenance.

### Certainty-as-command

A high-confidence belief automatically determines behavior.

**Protection:** separate belief confidence from action commitment.

## Experiment A/B consequences

Experiment A should include a **none-of-the-above control** where the learner's initially available candidate family is deliberately incapable of representing the true generator.

Success requires the system to:

- avoid unjustified certainty among the inadequate alternatives;
- detect population-wide failure;
- broaden or mutate its structure search;
- form a candidate that materially repairs the failure under the same bounded resource rules.

Experiment B should later test whether model inadequacy itself can trigger targeted information-seeking when a discriminating action is available.

A system that only chooses between supplied alternatives has not demonstrated open-ended epistemic correction.

## Current verdict

The bounded hypothesis population should be treated as a **working explanatory set**, not as an exhaustive possibility space.

The stronger current epistemic loop is:

`observe -> update live alternatives -> evaluate model-set adequacy -> propose/repair if needed -> mature only after meaningful evidence cycles -> challenge before consolidation -> act under remaining uncertainty -> preserve genealogy -> reopen when later evidence demands it`.

This remains a design hypothesis, not an approved implementation architecture.
