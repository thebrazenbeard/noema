# Bounded hypothesis population — minimality and false-diversity attack

Status: **BRAINSTORMING / L4 HOSTILE MECHANISM REVIEW / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Targets:

- `BOUNDED_HYPOTHESIS_POPULATION.md`;
- Candidate A's current bounded-population realization of epistemic uncertainty;
- Experiment A/B ambiguity and intervention-selection claims.

## Question

Does a bounded population of explicit live hypotheses provide necessary epistemic machinery, or can it create a persuasive *appearance* of uncertainty while merely reflecting proposal/search artifacts inside one shared model family?

The no-oracle adequacy attack already exposed one failure:

> low disagreement among represented hypotheses does not imply the represented set is adequate.

This pass pushes that further.

## Research pressure

Sequential Monte Carlo and ensemble-learning research provide relevant failure analogies, without being direct templates for Noema:

- finite particle systems can suffer weight collapse/degeneracy and particle impoverishment, losing modes that remain plausible;
- ensemble performance depends on a useful relationship between individual quality, aggregation rule, loss, and diversity — diversity is not intrinsically epistemically virtuous;
- encouraging diversity mechanically can preserve alternatives that differ numerically but are not useful explanations;
- a shared misspecified family can make a diverse ensemble jointly wrong.

Representative SciSpace results used for pressure include work on particle-filter weight collapse and ensemble diversity theory, including Wood et al. (2023), *A Unified Theory of Diversity in Ensemble Learning*, arXiv `2301.03962`, and sequential-filtering work on weight degeneracy/collapse.

The relevant lesson is not `use particle filtering`. It is:

> finite populations inherit proposal, weighting, resampling, and family-coverage failure modes that must not be mistaken for calibrated epistemic uncertainty.

## Attack 1 — population diversity is conditional on proposal coverage

A bounded population can only preserve hypotheses that were proposed.

If all live candidates descend from one habitual proposal family, the population may look richly uncertain while excluding the explanation that matters.

This creates two different quantities:

1. **uncertainty inside the represented set**;
2. **uncertainty that the represented set itself is missing important possibilities**.

The first is what population weights/disagreement naturally express.

The second is exactly what PR #20's inadequacy attack says must remain separately contestable.

### Consequence

Candidate A must not interpret population concentration as global epistemic confidence unless model-set adequacy evidence also supports that move.

## Attack 2 — diversity protection can manufacture epistemic disagreement

`BOUNDED_HYPOTHESIS_POPULATION.md` protects alternatives that disagree under sampled counterfactuals before pruning.

That is defensible as an anti-collapse heuristic, but it can become circular:

- hypotheses are retained because they disagree;
- retained disagreement is then cited as evidence of uncertainty;
- uncertainty is then cited as evidence that the population is doing useful epistemic work.

Disagreement produced by a diversity-preservation rule is not itself evidence that the world supports multiple explanations.

### Required distinction

Preserve **evidence-supported unresolved alternatives**, not diversity for its own sake.

Counterfactual disagreement may justify *not deleting* an otherwise plausible alternative, but cannot increase that alternative's evidential support merely because it is different.

## Attack 3 — mode death can be irreversible under resource pressure

A finite cap means some plausible alternative will eventually be pruned or made dormant.

If proposal/reconstruction cost is high, an early weakly supported but later-correct explanation can disappear before the decisive evidence arrives.

Dormancy helps only if enough information survives to reconstruct the relevant alternative.

This creates a hidden design question:

> What minimal trace of a rejected explanation is sufficient to make reopening genuinely cheaper than rediscovery, without turning dormant storage into an effectively unbounded population?

If the answer is `store almost the whole model`, the resource claim is cosmetic.

If the answer is `store a tiny hash/summary`, reconstructability may be fictional.

### Falsifier

Construct delayed-disambiguation worlds where the eventually useful alternative is temporarily dominated early, then becomes necessary much later after unrelated intervening learning.

Measure whether the system can recover it under a fixed total memory/search budget.

## Attack 4 — hypothesis identity may be evaluator fiction

Two explicit hypotheses can be different parameterizations of the same predictive family, while one distributed stochastic model can encode several materially different future possibilities without explicit branch identity.

Therefore the evaluator must not privilege:

- number of hypotheses;
- stable hypothesis IDs;
- graph/topology difference;
- readable alternative labels.

The relevant test is whether the learner preserves consequentially different predictions/actions and revises them appropriately.

This reinforces representation neutrality but has an additional implication:

> `hypothesis population` should be an L4 storage/search realization, not the L3 definition of epistemic multiplicity.

## Attack 5 — weighting can collapse before evidence is decisive

Finite populations often use normalized support/weights.

Even with proper predictive scoring, repeated small random advantages can drive one candidate's normalized weight near zero under long observationally weak data.

If low-weight alternatives are then pruned, numerical accumulation can convert weak evidence into practical irreversibility.

Experiment A's exact passive equivalence is unusually clean; real worlds will be only approximately ambiguous.

### Requirement

The commitment/pruning policy must account for:

- evidence strength, not just cumulative score difference;
- calibration under the expected noise process;
- effective distinguishability of alternatives;
- whether decisive evidence has actually been available;
- reopening/reconstruction cost.

A long sequence of low-information evidence must not automatically count like one decisive intervention.

## Attack 6 — ensemble disagreement is not calibrated epistemic uncertainty by default

Population variance/disagreement depends on:

- how proposals were generated;
- shared architecture priors;
- optimization randomness;
- pruning/resampling;
- parameterization;
- weighting rule;
- resource cap.

Therefore raw disagreement has no automatic probability semantics.

If Candidate A wants calibrated uncertainty from a population, calibration must be evaluated behaviorally against held-out frequencies/consequences under the actual proposal/retention process.

No internal statistic gets `epistemic` status by name.

## Attack 7 — explicit alternatives may be too expensive for high-dimensional ambiguity

In open-ended worlds, uncertainty can be combinatorial:

- many latent processes;
- many possible bindings;
- multiple temporal scales;
- different agent models;
- uncertain source attributions;
- different causal mechanisms.

An explicit population may spend most of its budget representing *combinations* of uncertainties that could be factorized or represented locally.

For example, four independent binary ambiguities create sixteen joint hypotheses if represented naively.

A more scalable representation may preserve local/marginal uncertainty and instantiate joint alternatives only when interactions make them consequential.

### Architectural pressure

Candidate A should prefer **localized/factorized epistemic multiplicity where possible**, with explicit joint hypotheses reserved for dependencies that actually matter to prediction/action.

This is compatible with its local revision goal and reduces pressure toward global possible-world enumeration.

## Stronger comparator set

The current comparator `one soft model` is too weak if used alone.

A fair minimality test should include at least one stronger non-population realization capable of multimodal or localized uncertainty, such as:

- a continuous stochastic latent-state predictor with learned multimodal conditional density;
- a factorized/local mixture representation that can preserve alternative dependencies without global hypothesis IDs;
- continuous recurrent substrate + learned local transition adapters with uncertainty over adapter activation/parameters.

The exact implementation family remains open.

The point is that explicit live hypothesis identities must beat a serious implicit-multiplicity rival, not only a point-estimate recurrent baseline.

## Proposed L3 correction

The underlying requirement should be weaker than `bounded hypothesis population`:

> Noema must preserve **consequential epistemic multiplicity** when available evidence supports materially different future predictions or intervention consequences, while remaining calibrated about possibilities outside its represented set and using bounded resources.

This does not require:

- explicit global hypothesis IDs;
- normalized population weights;
- fixed population cardinality as the primary representation;
- one joint possible-world model for every uncertainty combination.

## New falsifiers

### BPM-0 — proposal-family blind spot

Constrain all initial proposals to one wrong-but-flexible family while the environment is better explained by a qualitatively different process.

Fail if population agreement becomes confidence despite persistent systematic predictive/intervention failure.

### BPM-1 — artificial-diversity trap

Introduce a retention rule that rewards counterfactual difference, then supply evidence strongly favoring one explanation.

Pass if unsupported alternatives lose evidential weight even when diversity heuristics keep them temporarily available.

Fail if `being different` itself maintains belief support.

### BPM-2 — delayed mode resurrection

Early evidence weakly disfavors the eventually correct explanation; decisive evidence arrives much later after resource pressure and unrelated learning.

Compare:

- active retention;
- dormancy/reconstruction;
- full deletion + rediscovery.

Charge all memory/search costs.

### BPM-3 — weak-evidence accumulation

Generate a long stream with tiny noisy score advantages but no meaningful discriminating intervention.

Pass if confidence/pruning remains calibrated to information content rather than elapsed sample count alone.

### BPM-4 — factorized ambiguity scale test

Create several mostly independent local ambiguities, then selectively introduce interactions among only a subset.

Pass if uncertainty representation cost grows primarily with consequential coupling rather than exploding across all global combinations.

### BPM-5 — implicit multiplicity comparator

Under equal compute/memory/sample budgets, compare explicit population against a serious stochastic/factorized non-population model on:

- calibration;
- intervention choice;
- local revision;
- delayed reopening;
- transfer;
- resource cost.

Explicit population earns promotion only if it provides reproducible benefit.

## Effect on Experiment A/B

Experiment A remains useful, but it is especially friendly to explicit alternatives because the evaluator knows a tiny discrete ambiguity exists.

Therefore a population win on A is weak evidence for mature architecture.

Experiment B is more diagnostic because information-seeking depends on consequential disagreement, but B should include cases where useful uncertainty is naturally **local/factorized rather than globally discrete**.

Otherwise the benchmark can quietly select the representation it was designed around.

## Verdict

The bounded hypothesis population remains a plausible L4 instrument, but its status should weaken from `strongest current realization` to **one serious candidate realization** until it beats stronger implicit/factorized uncertainty comparators.

Candidate A does not break.

The architecture-level target is not `maintain several named models`.

It is:

> preserve the unresolved predictive distinctions that matter, know that represented alternatives may all be wrong, and spend explicit-alternative machinery only where it buys better calibrated prediction, intervention, revision, or transfer.