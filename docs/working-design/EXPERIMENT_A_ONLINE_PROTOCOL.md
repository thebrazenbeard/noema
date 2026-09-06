# Noema Experiment A — online protocol

Status: **BRAINSTORMING / EVALUATION PROTOCOL / NOT IMPLEMENTED**

## Correction

Experiment A should not quietly become an offline causal-discovery benchmark where a batch solver receives the whole dataset and fits a model after the fact.

Noema is intended to be a persistent learner. The candidate and serious baselines should therefore experience Experiment A as a **stream**.

## Streaming rule

For the developmental candidate and continuous baseline:

- observations arrive in temporal order;
- intervention/efference packets arrive when issued;
- predictions are scored before the next outcome is revealed;
- internal state may update after each observation;
- memory and compute are explicitly bounded;
- the full raw history is not automatically re-presented for batch refitting.

A bounded episodic/replay buffer is allowed if it is part of the declared architecture and resource budget.

The evaluator/reference learner may use offline mathematics to verify the world and estimate an upper bound, but that does not count as developmental evidence.

## Why this matters

A batch solver can hide several problems that Noema must eventually solve:

- online confidence revision;
- credit assignment after surprise;
- local update rather than full retraining;
- memory selection under finite storage;
- retention of unresolved uncertainty across time;
- recovery after an intervention changes what evidence is available;
- persistent meta-learning across worlds.

## Checkpointed predictions

Score the learner at explicit checkpoints:

1. early passive exposure;
2. late passive exposure;
3. immediately before decisive intervention;
4. immediately after the first intervention outcome;
5. after a short sequence of intervention evidence;
6. on held-out intervention values;
7. after moving to a remapped world.

This produces an **epistemic trajectory**, not merely one final accuracy number.

## What should be visible in that trajectory

A strong learner should generally show:

- improving passive prediction;
- no unjustified structural certainty during passive equivalence;
- a sharp but evidence-proportional revision after decisive evidence;
- continued improvement on held-out interventions;
- limited disturbance to unrelated learned predictions;
- faster appropriate adaptation on later analogous worlds if meta-learning is active.

The benchmark does not prescribe the exact internal representation that produces the trajectory.

## Memory fairness

The candidate and continuous baseline should receive comparable raw-data memory budgets.

Explicit structural memory may count separately but must be charged against a declared resource budget. The candidate should not win merely because it is allowed to store every observation plus extra structure while the baseline is memory-starved.

## Compute fairness

Per-step and per-world compute should be measured.

A structure-search method that obtains better sample efficiency by spending unbounded search compute is not a clear win.

Report at least:

- evidence/sample count;
- approximate proposal count;
- active-hypothesis count where applicable;
- wall/CPU cost during controlled local evaluation;
- memory footprint or declared bounded proxy.

Exact hardware benchmarking belongs to implementation/testing, but the comparison contract is fixed here.

## Intervention surprise test

Immediately after the first decisive intervention, do not allow a full reset or retrain-from-scratch pass.

The learner must update from its prior state.

This directly tests whether new evidence can correct an established but underdetermined model without erasing unrelated learning.

A separate reset-and-refit result may be reported as a diagnostic baseline, but it is not equivalent to continual correction.

## Replay ablation

If the candidate uses replay/episodic memory, evaluate an ablation with replay disabled or sharply reduced.

This reveals whether local structural revision genuinely contributes or whether success depends primarily on repeatedly retraining over stored history.

## Final implication

Experiment A is therefore a **streaming epistemic-development test** embedded in a mathematically controlled world, not merely a static structure-identification problem.

That keeps the first falsifier small while still exercising the persistence and correction properties Noema is actually supposed to have.