# Experiment A — uncertainty, scoring, and resource discipline

Status: **BRAINSTORMING / RECOMMENDED EXPERIMENT DESIGN / NOT IMPLEMENTED**

## Why this matters

Experiment A fails as a test if `uncertainty` is represented only as one blurred parameter vector. Observationally equivalent structures must be able to remain genuinely distinct because they predict different interventional futures.

The first experiment therefore needs two separable uncertainties:

1. **structural uncertainty** — several materially different explanations may be live at once;
2. **parameter/predictive uncertainty** — even within one explanation, coefficients, noise, and future observations are uncertain.

Collapsing either one too early creates false confidence.

## Recommended structural uncertainty representation

Use a **small weighted population of live structural hypotheses** for the slow RGSS layer.

Each candidate has:

- an opaque internal handle;
- generic dependency/binding structure;
- local learned parameters/state;
- predictive distribution;
- evidence score/history;
- approximate influence/provenance trace;
- resource state.

Candidate weights represent comparative evidential support. They are not declarations of truth and need not be interpreted as philosophically exact Bayesian probabilities.

The population must preserve two candidates when passive evidence leaves them observationally equivalent.

## Predictive mixture

Before decisive evidence, Noema's action-conditioned prediction should be a mixture over live hypotheses rather than an average structure.

That distinction is crucial.

An averaged dependency matrix can predict an outcome no hypothesis actually believes. A mixture preserves the fact that `either structure A or structure B may be true`, allowing later intervention to discriminate them.

## Evidence update

For Experiment A, candidate support should be driven primarily by **prequential predictive evidence**:

- a candidate predicts held-out next/current observations before seeing them;
- its score changes according to how well the observation fits its predictive distribution;
- intervention provenance is included when generating intervention-conditioned predictions;
- complexity/resource cost is tracked separately from predictive evidence rather than silently baked into a semantic prior.

For the first linear-Gaussian world, exact or near-exact probabilistic scoring is available and should be used as a clean benchmark.

## Symmetry requirement

The test must not initialize one direction with a privileged prior.

For the chain/fork ambiguity class, generic edge-direction mutations should begin with symmetric or explicitly audited proposal/evidence treatment unless prior curriculum evidence genuinely justifies otherwise.

If a learned proposal policy has acquired a preference from earlier worlds, that preference may affect **which hypothesis is proposed first**, but passive test-world evidence must still be able to preserve and support alternatives.

This operationalizes the rule:

> proposal policy suggests; evidence accepts.

## Resource budget — provisional first-test values

Experiment A should intentionally expose tractability pressure even though the world is tiny.

Recommended initial caps:

- maximum live slow structural hypotheses: **8**;
- maximum new structural proposals per proposal event: **4**;
- maximum retained residual/influence window for proposal localization: **256 observation events**;
- structural proposal events are triggered by persistent residual/ambiguity evidence rather than every sample;
- retired candidates preserve a compact episodic/evidence trace sufficient for later reopening, but do not consume a live slot.

These numbers are engineering starting points, not cognitive constants. The implementation plan should pre-register them before final evaluation and run sensitivity checks around them.

## Resource-fair comparison

The full RGSS learner must not win merely by receiving much more compute than the continuous baseline.

Report at least:

- predictive quality versus wall-clock/operation budget;
- number of learned parameters or comparable capacity measure;
- number of structural proposals evaluated;
- peak live hypothesis count;
- evidence/sample count to reach interventional predictive competence.

Where exact compute matching is impossible, report the trade-off curve rather than hiding it behind one final score.

## Retirement and reopening

A live candidate can be retired for resource reasons when it is persistently dominated by alternatives on evidence and cost.

Retirement is not proof of falsity.

A later anomaly can trigger reconstruction/reopening from retained evidence. This matters because a finite learner must prune without making pruning epistemically irreversible.

## Calibration tests

### Passive phase

Because the evaluator constructs exact observational equivalence, one family should not receive near-total evidential mass solely from passive test-world observations.

For the first implementation, treat **> 0.90 family confidence from passive evidence alone** as a diagnostic failure unless an explicit audited prior accounts for it.

### Post-intervention phase

After scheduled interventions, support should move toward the family whose intervention-conditioned predictions match the data.

Evaluate both:

- confidence movement in the correct direction;
- held-out interventional predictive likelihood.

Confidence without predictive improvement does not count.

## Why confidence thresholds are secondary

The internal confidence number can be calibrated badly while predictions are good, or vice versa.

Therefore the primary evidence remains predictive behavior and transfer. Confidence thresholds diagnose whether the uncertainty machinery behaves sensibly; they are not the sole pass criterion.

## Ablation for structural uncertainty

Run a version forced to maintain only one live structural hypothesis.

Expected pathology:

- premature orientation commitment during passive ambiguity;
- greater revision cost after contradictory intervention evidence;
- worse calibration;
- potentially worse transfer when the early commitment is wrong.

If the single-hypothesis version performs equally well on all relevant metrics, explicit competing structural hypotheses have not earned their complexity in Experiment A.

## Ablation for proposal meta-learning

Freeze the proposal policy across transfer worlds while leaving ordinary model learning intact.

If the full learner claims to have learned `how to hypothesize`, it must show improved proposal/sample efficiency relative to this frozen version without increased false proposal rates on negative-control worlds.

## Falsification consequence

A strong result is not `the full model got a high score`.

A strong result has the causal shape:

> explicit structural uncertainty + intervention-sensitive evidence + reusable proposal learning produces a specific measurable advantage, and removing the implicated mechanism removes that advantage.

If that causal story does not survive ablation, the architecture claim fails even if aggregate prediction remains impressive.
