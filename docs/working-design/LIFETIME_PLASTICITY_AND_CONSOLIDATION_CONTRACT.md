# Noema lifetime plasticity and consolidation contract

Status: **BRAINSTORMING / CAPABILITY + EVIDENCE CONTRACT / NOT AN APPROVED IMPLEMENTATION**

Level intent: **L1 lifetime-learning capability + L2 evidence discipline + L3 computational pressure.**

## Purpose

The external hostile research pass strengthens a failure mode that the current Noema design only partially captured:

> A learner can retain old knowledge and still become progressively unable to learn genuinely new structure.

Therefore lifetime intelligence requires two independent properties:

1. **stability** — useful prior learning remains available;
2. **plasticity** — materially novel learning remains possible late in development.

Neither is sufficient by itself.

This document also tightens the treatment of consolidation. Durable storage is not automatically beneficial. Consolidation must earn its cost by improving future prediction, reconstruction, transfer, control, or resource efficiency without producing harmful overgeneralization.

No specific neural, replay, synaptic, modular, or complementary-learning-system mechanism is selected here.

## 1. Lifetime plasticity is an L1 capability

Noema should remain able to acquire genuinely new structure after a long developmental history.

A candidate fails lifetime learning if it becomes any of the following:

- **frozen:** old knowledge is preserved but new structure cannot be learned;
- **amnesic:** new learning remains easy but systematically destroys old competence;
- **overconsolidated:** mature structures resist revision even when evidence changes;
- **permanently labile:** everything remains editable, so no durable reusable competence forms;
- **capacity-saturated:** representational space becomes effectively unavailable for novel factors, skills, or relationships;
- **meta-fossilized:** the learner can still fit local parameters but can no longer change how it learns or represents unfamiliar structure.

The evidence target is therefore not one final retention score. It is a **learning-capacity trajectory across developmental time**.

## 2. Late-life novelty probe

A serious continual-learning evaluation should include novelty probes at multiple ages of the same developmental run.

At minimum:

- **early probe:** after little accumulated learning;
- **middle probe:** after substantial but not maximal experience;
- **late probe:** after long exposure, consolidation, skill formation, and regime changes.

Each probe introduces a structural regularity that is genuinely novel relative to the learner's prior developmental experience.

A valid novelty probe must not be solvable merely by:

- recalling a previous answer under remapped labels;
- adjusting one already-used scalar coefficient;
- reactivating an old task-specific head;
- receiving a semantic cue that identifies the solution family;
- resetting the learner to a fresh state.

The exact novelty type can vary by experiment. Examples include a new temporal dependency class, new higher-order interaction, new compositional relation, or new regime requiring representational reorganization.

## 3. Plasticity measurement

The evaluator should compare early/middle/late novelty acquisition on at least:

- samples required to reach a declared predictive or control criterion;
- prequential improvement rate;
- final held-out performance;
- amount of unrelated prior competence damaged during acquisition;
- compute/memory spent;
- whether the learner needed global reset or unrestricted replay;
- whether new structure transferred to a related but surface-remapped case.

The target is not identical learning speed at all ages. Mature systems may rationally be more conservative.

The failure is **unexplained collapse of capacity to acquire new useful structure**.

## 4. Stability-plasticity must be measured jointly

A mechanism cannot claim success by optimizing only one side.

For each late novelty probe record both:

- **new-learning gain**, and
- **old-learning retention / local integrity**.

This produces a frontier rather than a single number.

A candidate that learns new structure rapidly by globally rewriting unrelated knowledge should not beat a slower candidate merely because its novelty score is higher.

Likewise, a candidate that preserves old scores perfectly by refusing to revise should not be called stable intelligence.

## 5. Consolidation must earn itself

The current design already distinguishes fast and slow learning pressures. The stronger rule is now:

> **Consolidation is justified by future utility, not by age, salience, repetition, or durability alone.**

A candidate consolidation event should be beneficial because it improves one or more of:

- prediction under future variation;
- transfer/generalization;
- compressed reusable representation;
- reconstruction from partial evidence;
- skill reuse;
- planning/control efficiency;
- resistance to irrelevant interference;
- resource efficiency.

And it should not create unacceptable costs such as:

- false generalization;
- rigidity after regime change;
- suppression of rare but important alternatives;
- loss of late-life plasticity;
- inability to distinguish episodic exceptions from general rules.

This is an evaluator principle. Noema does not need a native variable literally called `consolidation utility`.

## 6. Consolidation comparison conditions

When a future implementation includes replay/consolidation, compare at least:

### K0 — no explicit consolidation

Fast/online learning only, subject to the same global resource budget.

Purpose: determine whether the claimed slow process is actually needed.

### K1 — blanket consolidation/replay

A broad policy that transfers/replays most retained experience or mature state without a selective generalization criterion.

Purpose: expose overgeneralization and unnecessary resource use.

### K2 — selective consolidation candidate

The candidate mechanism under test.

Purpose: determine whether selective durable learning improves future competence under equal or declared resources.

A biologically inspired mechanism receives no special credit. Only behavioral/evidential advantage matters.

## 7. False-generalization controls

A consolidation system can look good on average while becoming dangerously overconfident.

Therefore include cases where:

- a frequent regularity has rare legitimate exceptions;
- two superficially similar contexts require different rules;
- a formerly general rule later becomes context-specific;
- a low-frequency structure becomes important after a regime shift;
- strong short-run regularity is deliberately misleading over a longer horizon.

The evaluator should score both successful transfer and **false-transfer cost**.

## 8. Reopening mature structure

Consolidated structure must remain reopenable when later evidence materially contradicts it.

Success means:

- contradictory evidence can accumulate without being discarded solely because prior structure is mature;
- revision can target implicated structure rather than erase unrelated learning;
- a corrected structure may later reconsolidate;
- old structure may remain valid in the contexts where evidence still supports it.

This is compatible with the existing reopenable-consolidation work, but the requirement is broader than any particular anomaly-debt mechanism.

## 9. Forgetting can be adaptive

The project should not use `maximum retention` as the lifetime objective.

Forgetting or compression may be useful when it:

- frees capacity;
- removes obsolete details;
- reduces interference;
- preserves generalized structure while discarding redundant episodes;
- improves plasticity;
- lowers resource cost.

But forgetting must also be accountable. A candidate should not delete inconvenient contradictory evidence merely because doing so improves current fit.

## 10. Resource-pressure test

Lifetime learning should be tested under finite storage and compute.

A useful pressure test gradually increases accumulated experience while holding the candidate within a declared resource envelope.

The system should then demonstrate some combination of:

- selective retention;
- compression;
- forgetting;
- reuse;
- reorganization;
- local restructuring.

Unbounded raw-history replay is not an acceptable substitute for lifetime cognition.

## 11. Relationship to the first falsification package

The first falsification package currently defines F1 as persistent streaming learning before Experiment A.

This contract strengthens F1 in two ways:

1. F1 should include at least one **late-within-run novelty acquisition check**, even if the run is still small relative to a mature Noema lifetime.
2. Any consolidation/replay mechanism introduced in F1 must be compared against simpler alternatives and scored for both generalization benefit and false-generalization cost.

The first package does not need to solve full lifelong cognition. It must simply stop candidates with obvious early stability-plasticity pathologies from advancing to more expensive experiments.

## 12. Relationship to future integrated lifetime tests

The strongest evidence arrives much later, when Noema has accumulated:

- multiple skills;
- changing world models;
- communication history;
- agent models;
- commitments;
- temporal abstractions;
- prior meta-learning.

At that point a late-life probe should require genuinely new learning that was not prefigured by the developmental curriculum.

A system that passes early continual-learning benchmarks but loses representational plasticity after years-equivalent development still fails the Noema target.

## 13. Candidate L3 pressures

This contract makes several computational pressures more plausible, without selecting mechanisms:

- some way to protect useful structure from indiscriminate overwrite;
- some way to keep enough representational/plastic capacity available for novelty;
- selective consolidation/forgetting under finite resources;
- uncertainty-sensitive reopening of mature structure;
- local enough credit assignment to avoid global destructive revision;
- meta-plasticity or an equivalent capacity for learning dynamics themselves to remain adaptable.

These are still L3 hypotheses. A sufficiently simple mechanism may satisfy several at once.

## Kill conditions

A candidate direction should be materially revised if lifetime competence depends on:

- periodic full resets;
- unlimited memory growth;
- replay of the complete historical stream as the normal learning mechanism;
- freezing an ever-growing fraction of the learner until novelty acquisition collapses;
- deleting contradictory evidence to protect consolidated beliefs;
- preserving old performance only by preventing representation-level learning;
- task-boundary labels that tell the learner when to create new capacity;
- architecture-specific metrics that hide loss of late-life learning ability.

## Current verdict

Noema's lifetime-learning requirement is stronger than `do not catastrophically forget`.

It is:

> **Remain capable of forming genuinely new, transferable, revisable structure throughout development while preserving useful prior competence under finite resources.**

And consolidation should be treated as successful only when it improves future cognition more than it harms flexibility, calibration, or generalization.
