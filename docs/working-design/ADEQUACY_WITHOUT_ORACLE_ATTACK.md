# Candidate A — model adequacy without an oracle attack

Status: **BRAINSTORMING / FIRST-CORE HOSTILE DESIGN REVIEW / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Target: Candidate A sections `Model inadequacy and structural expansion`, F1/F2 regime-change/model-family tests, and the hostile-validation requirement that the learner not assume its current family is adequate.

## Question

Candidate A correctly rejects `least bad current model = adequate`.

But the current wording says the predictive substrate tracks **absolute predictive adequacy**.

What could `absolute` mean to a learner that does not know the true data-generating process, irreducible noise, hidden regime state, sensor corruption, or whether its own optimizer has converged?

This attack asks whether the architecture has accidentally introduced a soft oracle under a statistical-sounding name.

## Research pressure

Recent and established misspecification work supports two conclusions relevant to Noema:

1. a model can become confidently wrong under misspecification rather than merely uncertain;
2. detecting *that something is wrong* is easier than uniquely diagnosing *what kind of wrongness caused it*.

Examples consulted through SciSpace include:

- Marsden, Duchi & Valiant (2021), *On Misspecification in Prediction Problems and Robustness via Improper Learning*, arXiv `2101.05234`: misspecified proper predictors can suffer substantial regret; aggregation outside the nominal model family can be more robust.
- Thomas & Corander (2019), *Diagnosing model misspecification and performing generalized Bayes' updates via probabilistic classifiers*, arXiv `1912.05810`: simulated-versus-observed discrimination can reveal distributional mismatch without access to the true generating model.
- Frazier, Robert & Rousseau (2020), *Model misspecification in approximate Bayesian computation: consequences and diagnostics*, JRSS B: misspecification can drive concentration on pseudo-true parameters while uncertainty claims become unreliable.
- Schmitt, Bürkner, Köthe & Radev (2024), *Detecting Model Misspecification in Amortized Bayesian Inference with Neural Networks*, DOI `10.1007/978-3-031-54605-1_35`: unsupervised discrepancy measures can flag test-time model mismatch without real-world training examples.
- Grundy, Killick & Svetunkov (2025), *Online detection of forecast model inadequacies using forecast errors*, arXiv `2502.14173`: sequential monitoring of forecast errors can reveal changes in the underlying process.
- Hsu (2025), *Credible Uncertainty Quantification under Noise and System Model Mismatch*, arXiv `2509.03311`: multiple diagnostics can help distinguish noise-model mismatch from system-model mismatch better than one credibility metric alone.

These papers do not define Noema's mechanism. They mainly show why one scalar `adequacy` variable would be too optimistic.

## Attack 1 — there is no learner-side absolute adequacy oracle

For any finite experience stream, poor predictive performance can arise from several causes:

- ordinary stochastic variation;
- underestimated observation noise;
- wrong noise shape/heavy tails;
- insufficient parameter learning;
- optimizer/path dependence;
- hidden context not yet represented;
- sensor/transducer drift;
- abrupt regime change;
- gradual nonstationarity;
- genuinely missing structural capacity;
- rare out-of-distribution event;
- another agent changing policy;
- an unobserved intervention.

The same predictive loss can be consistent with multiple explanations.

Therefore Candidate A cannot legitimately maintain an infallible variable equivalent to:

`CURRENT_MODEL_FAMILY_IS_INADEQUATE = true`.

What it can maintain is **evidence that current predictive explanations are failing in patterned ways**.

### Classification

**MATERIAL FIRST-CORE WORDING/MECHANISM CORRECTION, not a predictive-control break.**

## Attack 2 — a single inadequacy score collapses diagnosis

Suppose predictive NLL worsens by the same amount in three worlds:

1. observation variance doubles but the causal/process relation is unchanged;
2. a coefficient abruptly changes and then remains stable;
3. a new nonlinear dependency appears that the current family cannot represent.

A scalar adequacy alarm could trigger the same response in all three.

That would be wrong:

- case 1 may need uncertainty/noise recalibration;
- case 2 may need regime/change adaptation and selective forgetting;
- case 3 may justify structural expansion.

Noema should not receive those English diagnostic labels. The architecture simply needs enough competing response paths that evidence can favor different repairs.

## Attack 3 — residual structure can be invisible to the chosen diagnostic

Residual-based checks are useful only relative to what the diagnostic can detect.

A learner can appear calibrated on marginal coverage while still miss relational dependence, tail behavior, intervention response, or context-conditional failure.

Likewise, ensemble disagreement can be low if every ensemble member shares the same misspecified family.

Therefore **diagnostic diversity matters**.

Candidate A should permit multiple generic discrepancy views rather than treating any one of the following as authoritative:

- point error;
- proper predictive score;
- calibration/coverage;
- residual autocorrelation/dependence;
- simulated-versus-observed discrepancy;
- population disagreement;
- intervention-prediction failure;
- transfer failure;
- change-point evidence.

This is not a proposal to hard-code all of them. It is a requirement that `adequacy` not be reduced to one privileged statistic.

## Attack 4 — misspecification and nonstationarity are confounded

Structural expansion can be destructive if the world merely changed.

A fixed model family may have been adequate yesterday and be wrong today because the process shifted, while a richer family fitted to all history may average across incompatible regimes and become worse at both.

Candidate A already requires late-life plasticity and regime-change correction. The adequacy mechanism must therefore preserve a distinction between at least these *behavioral possibilities*:

- revise parameters/state inside current structure;
- increase/decrease uncertainty or noise representation;
- discount stale evidence / detect a new regime;
- expand structural capacity;
- keep multiple explanations live;
- wait/seek discriminating evidence when the distinction matters.

Again, these need not be named semantic modes inside Noema.

## Attack 5 — structural expansion can become an overfitting reflex

A learner rewarded for lowering predictive error can always become more expressive.

Without complexity/resource pressure and held-out/transfer evidence, `model inadequacy -> add structure` becomes a one-way ratchet toward memorization.

Candidate A already includes finite resource cost and representation mismatch controls. This attack strengthens the rule:

> Structural expansion earns retention only when its benefit survives fresh predictive/intervention evidence relative to cheaper repair paths.

A richer representation should be allowed to lose to:

- better noise calibration;
- local parameter adaptation;
- temporary regime models;
- simpler aggregated/improper prediction;
- a distributed continuous fallback.

## Attack 6 — simulation-based discrepancy can itself encode the current ontology

One attractive misspecification test is to generate predictions/simulations from the current model and ask whether a generic discriminator can tell them apart from observations.

That may detect mismatch, but it has two Noema-specific risks:

1. the discriminator may become a second powerful world model whose features contain the useful structure the primary model lacks;
2. a hand-designed summary/discrepancy metric may encode the ontology the learner is supposed to discover.

If used, such a diagnostic must be resource-accounted, ablated, and prevented from becoming an uncredited intelligence side channel.

## Proposed correction to Candidate A language

Replace the conceptual claim:

> track absolute predictive adequacy

with the weaker and more defensible principle:

> maintain **fallible, multi-view evidence of predictive/model inadequacy**, calibrated from the learner's own forecast/intervention/transfer failures, and keep repair choice contestable among parameter adaptation, uncertainty/noise revision, regime adaptation, structural expansion, and further information gathering.

No single diagnostic is ground truth.

No inadequacy alarm is semantic proof that the model family is wrong.

## Proposed first-core falsification package

### AQA-0 — no inadequacy oracle

Audit learner-visible inputs and internal helper channels.

Fail if the learner receives an evaluator-computed `misspecified`, `change_point`, `noise_mismatch`, `wrong_structure`, or equivalent answer token.

### AQA-1 — matched-error differential repair

Construct three online worlds with matched initial predictive error magnitude:

- noise mismatch;
- regime shift;
- structural misspecification.

Success does **not** require semantic diagnosis labels.

Pass if the learner's adaptation is behaviorally appropriate enough that:

- pure noise change does not trigger useless ontology/structure growth;
- regime shift does not require destructive full-history averaging;
- persistent structural failure can eventually recruit extra representational capacity when cheaper fixes fail.

### AQA-2 — shared-family confidence trap

Use a bounded model population whose members share one misspecified family and become mutually confident.

Fail if low ensemble disagreement is treated as evidence of adequacy despite systematic held-out/intervention failure.

This attacks decorative uncertainty ensembles directly.

### AQA-3 — false expansion trap

Provide a stochastic world where rare heavy-tailed errors mimic systematic residuals for a while.

Pass if structural expansion is tentative/reopenable and can be rejected when fresh evidence supports a noise explanation instead.

### AQA-4 — hidden-dependence misspecification

Use a process with good marginal calibration but a missing higher-order/conditional dependency.

Pass requires at least one available discrepancy route capable of detecting consequential predictive structure beyond marginal error.

### AQA-5 — late regime reversal

After the learner adapts to a regime shift, restore the earlier regime under changed surface statistics.

Pass if prior competence can be reused where useful without blindly restoring stale full state.

This connects model adequacy to TKI-1 adaptive hysteresis and late-life plasticity.

### AQA-6 — intervention disambiguation

Create passive evidence under which noise mismatch and structural mismatch remain difficult to distinguish, then allow an intervention that separates them.

Pass if information-seeking/intervention can be selected because it changes expected future evidence, rather than because the environment labels the correct repair.

## Effect on bounded-population uncertainty

The bounded population remains viable but loses any claim to be sufficient for model inadequacy.

Population disagreement measures **within represented possibilities**. It cannot detect a missing possibility shared by every member.

Therefore Candidate A needs both:

- uncertainty among current live explanations; and
- evidence that the whole represented set may be jointly failing.

The latter must remain fallible and evidence-driven.

## Effect on structural expansion

Structural expansion survives as a candidate repair path, not a direct reflex.

A more accurate loop is:

`predict -> observe discrepancy -> update/calibrate -> accumulate patterned failure -> compare plausible repair routes -> seek discriminating evidence when useful -> tentatively revise/expand -> test on fresh evidence -> retain/reopen`

This is compatible with EGSS and Candidate A's process-first direction.

## Adjudication verdict

Candidate A **survives**, but the term `absolute predictive adequacy` should not survive unchanged.

The architecture does not need an oracle telling it when its model family is wrong. It needs a bounded, fallible process for noticing when its current explanations fail in ways that cheaper within-model adaptation does not resolve, while avoiding the opposite error of explaining every surprise through structural growth.

This is a first-core correction because F1/F2 explicitly claim regime-change correction, model-family inadequacy handling, and uncertainty calibration. Those claims are not valid if `adequacy` is an evaluator truth channel or a single privileged diagnostic.