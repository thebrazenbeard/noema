# Noema experiment state and persistence boundaries

Status: **BRAINSTORMING / EVALUATION CONTRACT / NOT IMPLEMENTED**

## Why this matters

Experiment A/B tests continual and meta-learning. Without explicit reset boundaries, a system can appear to transfer structure simply because world-specific identifiers, fitted parameters, hidden-family assignments, or evaluator artifacts leaked across trials.

The experiment must therefore distinguish **what is allowed to persist** from **what must reset**.

## State classes

### 1. Within-world epistemic state — persists during one world

May include:

- current continuous predictive state;
- live structural hypotheses;
- learned parameters for the current world;
- confidence/uncertainty;
- residual/anomaly history;
- current episodic evidence;
- current intervention-response estimates;
- local influence/provenance traces.

This state is expected to change as passive and intervention evidence arrive.

### 2. Cross-world generic learning state — may persist

May include only knowledge whose claimed purpose is generalization or learning-to-learn, such as:

- learned operational understanding of the intervention/efference channel from the A0 curriculum;
- generic proposal-policy parameters;
- generic learned binding/operator machinery if it has earned transfer value;
- calibrated generic expectations about uncertainty and evidence gathering;
- meta-learned allocation/revision policy;
- reusable structure whose transfer is itself part of the hypothesis under test.

Anything retained here must be explicitly named and independently ablatable.

### 3. World-specific state — must reset between independent worlds

Must not persist unless a particular transfer test explicitly says otherwise:

- current channel-to-channel dependency parameters;
- hidden family assignment;
- evaluator family labels;
- channel positions/identities as stable semantics;
- world-specific scale/offset/noise parameters;
- intervention target identity from the prior world;
- exact current-world structural hypothesis handles;
- cached answer keys or evaluator metadata.

## Transfer protocol

For A4/A6, transfer means:

> retain the generic learning state, reset world-specific state, then measure whether the learner becomes calibrated/intervention-sensitive more efficiently in a remapped world.

The remapped world changes channel permutation, numeric parameters, scale/offset, noise, distractors, and potentially which hidden family is true.

A transfer claim fails if advantage disappears when channel order is permuted or if inspection shows that world-specific fitted parameters were carried forward.

## Cold-start comparator

Every transfer/meta-learning evaluation should have a matched learner initialized with:

- the same fixed architecture;
- the same generic birth priors;
- no cross-world learned proposal/operator state from the preceding ambiguity tasks.

The transfer benefit is the difference between the continuing learner and this matched cold/meta-reset comparator under the same new-world evidence budget.

## Meta-learning ablation

A separate ablation should preserve ordinary within-world learning while resetting only cross-world proposal/inference-learning state.

This distinguishes:

- `I learned the previous world`; from
- `the previous world changed how I learn the next one`.

## Curriculum boundary

The A0 intervention curriculum is a distinct developmental prerequisite.

After curriculum completion, its learned generic intervention understanding may persist into A1-A6.

However:

- curriculum worlds may not use the exact A test parameters;
- they may not expose chain/fork family labels;
- they may not give stable semantic channel identities reused in A;
- the final A evaluation set must remain held out from curriculum tuning.

## Development / validation / final test split

To prevent benchmark overfitting, separate:

1. **development worlds** — available while designing/debugging the learner;
2. **validation worlds** — used for choosing fixed hyperparameters/resource budgets;
3. **final held-out worlds** — generated from pre-registered rules and not inspected for architecture tuning before the final evaluation.

The hidden-family balance and parameter ranges should be pre-registered before final testing.

If architecture changes after looking at final-test failures, that test set becomes development evidence and a new held-out set must be generated.

## Randomness boundary

Seeds used for final evaluation must not be available to the learner as input or encoded in channel order, filenames, run IDs, or other side channels.

Reproducibility for the evaluator is compatible with opacity to the learner.

## Diagnostic boundary

The operator/diagnostic interpreter may inspect internal state for the human experimenter, but its human-readable summaries cannot be fed back into Noema during Experiment A/B.

Otherwise terms like `orientation uncertain`, `dependency`, or `wrong hypothesis` could become a hidden teacher signal.

## Persistence audit

Each experimental run should emit an evaluator-side manifest of:

- state loaded at start;
- state reset;
- state allowed to persist;
- ablations applied;
- random seed/world-generation parameters kept evaluator-side;
- model/config version;
- resource budget.

This is instrumentation, not learner input.

## Success implication

A transfer result is credible only when the advantage survives after all world-specific state has been reset and disappears or weakens when the claimed generic meta-learned state is ablated.

This persistence boundary is also an early prototype for a broader Noema principle: continuity should preserve learned general structure and developmental history without confusing prior-world particulars with current-world truth.