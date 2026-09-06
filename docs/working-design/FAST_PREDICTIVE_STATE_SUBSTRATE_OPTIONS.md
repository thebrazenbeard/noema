# Fast predictive state substrate — options and contract

Status: **BRAINSTORMING / ARCHITECTURE OPTIONS / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

## Why this pass exists

Candidate A currently says the fast substrate is a `continuous recurrent probabilistic state model` and then gives a bounded population of continuous model states a privileged role in uncertainty.

The recent adequacy/minimality attack weakens that formulation in two ways:

1. concentration inside a represented population does not establish that the represented family is adequate;
2. a global population of complete alternatives can scale badly when ambiguities are mostly local or factorized.

The first-core architecture therefore needs a stronger statement of **what the fast state must accomplish** without prematurely deciding that the answer is a classical latent state, a predictive-state representation, a neural recurrent state, or an explicit hypothesis population.

## Proposed architecture-level replacement

The fast substrate should be defined by a **predictive sufficiency contract**:

> At each step, Noema maintains a bounded recurrent internal state whose job is to preserve whatever information from prior learner-visible experience is useful for calibrated prediction of reachable future learner-visible experience, including predictions conditioned on candidate actions or information-gathering interventions.

This is a functional definition, not a claim that the state is one true hidden description of the world.

The state may be latent, predictively defined, distributed, factorized, mixture-based, or hybrid. The evaluator should care about what distinctions it preserves and what forecasts/control behavior it supports, not whether its coordinates match evaluator ontology.

## Minimum fast-state requirements

A viable F1/F2 realization must support all of the following.

### Streaming recurrence

The learner updates online from a sequence of observations, actions/efference, communication or other declared learner-visible signals. It may not rely on repeatedly rebuilding itself from the full raw history after every step.

### Partial observability

The recurrent state must summarize history well enough that relevant future predictions can depend on information no longer present in the current observation.

### Probabilistic prediction

The substrate must produce predictive distributions or another properly uncertainty-bearing predictive object, not only point forecasts.

### Action-conditioned prediction

The substrate must be able to estimate consequences under candidate action/intervention conditions without treating action issuance as proof of realized outcome.

### Consequential epistemic multiplicity

If currently plausible interpretations imply materially different reachable outcomes, the state must be able to preserve that unresolved difference somehow. This does **not** require named global hypotheses.

### Family-adequacy uncertainty

The learner must also remain fallibly uncertain about whether its current representational/predictive family is adequate at all. Confidence among represented alternatives is not sufficient.

### Late plasticity

New evidence late in a run must still change prediction when warranted. Adaptation must not require destructive global reset by default.

### Bounded operation

State size, update cost, predictive-query cost, memory use, and any explicit multiplicity mechanism must be declared and bounded.

### No semantic latent-state subsidy

The learner receives no object, agent, cause, self, regime, task, episode, or world-state labels merely because one model family normally uses them internally.

## Option A — predictively defined recurrent state

A Predictive State Representation (PSR)-like family defines state through predictions of future observables under future action conditions rather than through a privileged hidden-state ontology.

Research motivation:

- PSRs represent partially observable systems using observable action/observation quantities rather than prespecified latent-state labels.
- classical and recurrent PSR work shows that predictive state can support planning/control and can be extended to continuous observations/actions.
- predictive-state approaches can be learned from interaction histories and, in some settings, avoid committing to a predetermined latent-state structure.

Representative literature consulted in this pass includes Boots, Siddiqi & Gordon on closing the learning-planning loop with PSRs; Boots, Gretton & Gordon on Hilbert-space PSRs; Hefny et al. on recurrent predictive-state policy networks; Wingate & Singh on exponential-family predictive representations; and Zhan et al. on online RL with PSRs.

### Strengths for Noema

- aligns directly with Noema's `predict the world before naming it` developmental principle;
- makes the state accountable to observable predictive consequences;
- does not require evaluator semantic latent labels;
- naturally supports action-conditioned future queries;
- offers a strong reference point for asking whether a latent representation is doing anything beyond predictive compression.

### Risks

#### Predictive-test selection can become a hidden ontology

A classical PSR still needs some set/family of predictive tests or statistics. Hand-selecting tests that correspond to evaluator concepts could simply move the ontology leak from `latent state` into `future queries`.

#### Realizability assumptions

Many theoretical guarantees assume the true system lies in, or is well approximated by, the chosen model class. This does not solve the adequacy-without-an-oracle problem.

#### Computational cost

Rich future-test families can be expensive. Compression helps, but aggressive compression can discard exactly the rare distinction later needed for intervention or transfer.

#### Weak explanatory locality by itself

A predictive state can forecast well while still offering little direct mechanism for local structural revision or reusable explanatory fragments. That may be acceptable for the **fast** layer but means the slow structure layer still has work to earn.

### Status

**Strong F1/F2 candidate and reference family, not architecture truth.**

Noema should borrow the predictive anchoring principle without committing to a classical PSR implementation.

## Option B — stochastic latent state-space model

A stochastic state-space realization maintains an inferred latent state and learns transition/emission dynamics, optionally conditioned on actions.

The latent coordinates are not evaluator semantics; they are internal variables whose value is justified by predictive/control performance.

### Strengths for Noema

- natural treatment of partial observability;
- explicit stochastic state can represent uncertainty within a compact recurrent system;
- clean distinction between current inferred state and learned transition dynamics;
- action-conditioned transition models fit Experiment A/B naturally;
- mature probabilistic machinery exists for filtering, smoothing, calibration, and state uncertainty.

### Risks

#### Latent identifiability is not semantic truth

Different latent parameterizations can describe the same observable process. The evaluator must not reward recovery of its own hidden variables unless identifiability is actually established.

#### Posterior/model-family overconfidence

A well-concentrated posterior inside the wrong latent family can still be badly wrong.

#### Global adaptation

Naive online updates can overwrite older useful structure or make every regime change a global parameter rewrite.

#### Hidden-state convenience creep

It is easy for an implementation to start adding privileged discrete regime/object/agent variables because state-space notation makes them convenient. F0 must prohibit that unless they are learned and the claim is scoped accordingly.

### Status

**Strong F1/F2 candidate.**

This is probably the cleanest conventional comparison against predictive-state anchoring.

## Option C — recurrent probabilistic predictor

A recurrent neural/probabilistic model directly compresses history into a learned recurrent state and emits predictive distributions, without requiring an explicit generative latent-state interpretation.

Examples include recurrent density models, stochastic recurrent networks, recurrent predictive-state networks, or compact sequence predictors with calibrated distribution heads.

### Strengths for Noema

- minimal structural assumptions;
- flexible nonlinear function approximation;
- easy to keep streaming and bounded;
- useful as a serious baseline because it tests whether the extra explicit structure of Options A/B earns itself.

### Risks

#### Hidden state can become an uninterpretable catch-all

That is not inherently bad, but it makes local revision, causal intervention diagnosis, and persistence attribution harder to test.

#### Uncertainty can be cosmetic

A distribution head does not guarantee calibrated epistemic multiplicity. One model can produce broad aleatoric noise while still collapsing structural uncertainty.

#### Catastrophic adaptation

Pure online gradient updates can forget old recurring patterns or chase noise.

#### Action information can be mishandled

A generic sequence model may treat action as just another token unless the action/consequence distinction and intervention-conditioned prediction contract are explicit.

### Status

**Required serious baseline and possible winner.**

If this family matches the stronger candidates on calibration, intervention prediction, local revision, transfer, and resource cost, the added machinery of A/B has not earned promotion.

## Option D — locally factorized predictive substrate

Instead of one monolithic recurrent belief state or a population of complete world models, the learner maintains a set of interacting local predictive factors/fragments whose uncertainty can remain partly independent.

This is not a commitment to a graphical model. `factor` here means only a bounded reusable predictive relation over some learned subset/context.

### Strengths for Noema

- local ambiguities need not create a Cartesian explosion of complete global hypotheses;
- local revision can change one relation without rewriting unrelated competence;
- reusable fragments fit the long-term goal of compositional transfer;
- a local factor can remain uncertain while another part of the system is well established.

### Risks

#### Factor boundaries can smuggle objecthood or ontology

If the evaluator supplies the decomposition, the problem is already partly solved.

#### Global interactions can be missed

A locally factorized model can fail on higher-order synergy or distributed constraints.

#### Binding problem

The architecture still needs a non-circular way to discover when local pieces should bind, split, merge, or remain independent.

### Status

**Promising architectural direction for slow/local structure and uncertainty, but too much unresolved machinery to make the sole F1 fast substrate.**

The best near-term use is as a comparator/augmentation to A/B/C rather than as the first mandatory realization.

## Recommendation

Do **not** replace Candidate A's current fast substrate with `PSR` as a noun.

Replace it with the predictive sufficiency contract, then treat three realizations as serious competitors:

1. a predictively defined recurrent state;
2. a stochastic latent state-space model;
3. a recurrent probabilistic predictor.

Use locally factorized structure as a competing augmentation once F1 establishes the streaming predictive baseline.

This preserves the strongest PSR insight — state should be accountable to future observable consequences — without importing PSR test-selection assumptions as architectural law.

## A more precise internal-state principle

The fast state should be **predictively anchored, not predictively exhausted**.

Meaning:

- every persistent distinction in the fast state should eventually justify itself by improving reachable prediction, calibration, intervention response, transfer, or control;
- but the state need not literally be a vector of hand-enumerated future tests;
- internal latent features are allowed if their usefulness is established behaviorally;
- multiple latent organizations that support the same relevant predictive/control behavior are evaluator-equivalent unless a stronger claim is justified.

This gives Noema freedom to discover useful internal variables while denying us permission to call those variables `OBJECT`, `CAUSE`, `SELF`, or anything else merely because the simulator knows such concepts.

## Predictive query bank without a semantic answer key

A practical F1/F2 candidate needs some bounded set of predictive obligations.

The evaluator can request generic future predictions such as:

- next-observation distribution;
- short-horizon future observation distributions;
- future distributions under specified candidate action sequences;
- selected low-dimensional projections of future raw observations;
- uncertainty/calibration reports over those predictions.

But the query family itself must obey F0:

- no query is named `is_object`, `is_agent`, `is_cause`, `is_regime`, etc.;
- query scheduling must not reveal hidden developmental phase or regime by a fixed clock pattern;
- future horizons and action probes should be remapped/randomized where useful;
- any learned internal selection of which predictions are worth maintaining must be distinguished from evaluator-supplied predictive obligations.

The predictive query bank is an evaluator measurement surface, not the learner's ontology.

## Fast versus slow boundary

The fast substrate is responsible for:

- online state estimation;
- immediate predictive distribution;
- current uncertainty/multiplicity;
- short-horizon adaptation;
- action-conditioned forecasts;
- preserving unresolved distinctions long enough for evidence to matter.

The slow layer is responsible for earning more durable reusable structure through:

- cross-context recurrence;
- compression/reuse;
- intervention-stable relationships;
- transfer;
- improved proposal/retrieval/allocation;
- reduced future sample/compute cost.

A fast predictor does **not** need to expose a human-readable causal model to pass F1/F2.

Conversely, a slow structural layer does not earn itself merely by making internals legible. It must improve prediction/control/transfer/local revision under equal resource accounting.

## Experiment A consequences

Experiment A should not score the fast substrate on whether it internally discovers the evaluator's `chain` or `fork` graph.

Before intervention, a passing fast state must remain calibrated under observational equivalence.

After intervention evidence, it must move its action-conditioned predictive distribution toward the observed family and generalize to held-out interventions.

An explicit structural explanation is optional unless it improves later prediction, local revision, transfer, or active experiment selection.

This keeps Experiment A a test of evidence-sensitive predictive state rather than a disguised graph-recovery contest.

## New falsifiers for the fast substrate

### FPS-0 — predictive-state label leak

Give one candidate a predictive test/query set handcrafted from evaluator latent concepts and another only generic future-observation queries.

If the first wins because the query bank supplied the ontology, do not credit the learner.

### FPS-1 — latent-coordinate permutation

Apply behaviorally equivalent latent parameterizations or evaluator remappings.

Pass requires unchanged capability claims unless the environment provides identifying evidence.

### FPS-2 — action-blind recurrence

Compare an otherwise strong recurrent predictor that sees observations but not issued actions/efference against the candidate.

The candidate should win specifically where action-conditioned prediction matters.

### FPS-3 — aleatoric-width masquerade

Construct two structurally different futures that one unimodal broad distribution can cover numerically.

Test whether the learner preserves decision-relevant multimodality/disagreement rather than merely inflating variance.

### FPS-4 — local ambiguity scaling

Create several mostly independent unresolved relations.

Compare a global explicit population, an implicit/factorized uncertainty realization, and a monolithic stochastic state under fixed resources.

A global population must not receive special status if it pays combinatorial cost for distinctions the alternatives preserve locally.

### FPS-5 — higher-order interaction trap

Use a world where pairwise/local predictive fragments look adequate but a higher-order dependency changes intervention consequences.

A factorized realization must be able to broaden/split/compose rather than treating locality as ontology.

### FPS-6 — late recurrent pattern return

Introduce regime A, then B, then a delayed return of A with superficial remapping.

Measure whether fast adaptation to B destroyed useful reusable predictive structure for A.

### FPS-7 — wrong-family confidence

Provide a world outside the candidate's current representational family while internal uncertainty is low.

The learner must be able to accumulate external inadequacy evidence and increase repair/search pressure without an evaluator `MODEL_WRONG` bit.

## Research pressure and claim ceiling

The literature supports the feasibility and usefulness of predictively defined states, stochastic latent filtering, recurrent predictive models, and fast/slow adaptation under nonstationarity.

It does **not** establish that any one of these is the correct architecture for Noema.

In particular:

- PSR theory often relies on realizability/model-class assumptions and can face predictive-test discovery or computational cost;
- latent state-space models can be compact while remaining non-identifiable or misspecified;
- recurrent predictors can be flexible while poorly calibrated or catastrophically adaptive;
- local/factorized models can scale well while missing higher-order structure.

Therefore the appropriate architecture claim is only:

> Noema's first fast substrate should be predictively anchored, streaming, uncertainty-bearing, action-conditioned, late-plastic, representation-neutral, and bounded; the first implementation candidates must compete under the same F0/F1/F2 evidence contract.

## Current verdict

The generic `continuous recurrent probabilistic state model` phrase survives only after tightening.

The bounded global hypothesis population should no longer be architecture-defining.

The stronger first-core formulation is:

> **a predictively anchored recurrent state with consequential epistemic multiplicity and fallible family-adequacy monitoring, whose internal representation is free so long as its predictive/control distinctions are earned rather than evaluator-supplied.**

This remains brainstorming. It does not choose the final implementation family or unlock implementation.