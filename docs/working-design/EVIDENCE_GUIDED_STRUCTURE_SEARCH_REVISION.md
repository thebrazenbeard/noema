# Noema structure-search correction — residuals are not enough

Status: **BRAINSTORMING / SUPERSEDING CORRECTION WHERE IN CONFLICT / NOT IMPLEMENTED**

## The problem discovered by Experiment A

The current Residual-Guided Structure Search (RGSS) idea is incomplete.

Experiment A deliberately creates two structural explanations that are **exactly observationally equivalent** before intervention. A sufficiently good passive predictor can therefore have essentially no systematic prediction residual that tells it to create the missing alternative.

That exposes a failure in the phrase `residual-guided`:

> **important structural uncertainty can exist even when prediction error is low.**

If Noema only searches for new structure when its current predictions fail, a successful but underdetermined model can become self-satisfied and never represent alternatives that matter under intervention.

## Correction

Broaden the mechanism provisionally from **Residual-Guided Structure Search (RGSS)** to **Evidence-Guided Structure Search (EGSS)**.

RGSS remains one proposal route inside EGSS; it is no longer the whole search theory.

EGSS may receive structure-search pressure from several domain-general sources:

1. **Persistent residuals** — the current model repeatedly predicts badly.
2. **Structural degeneracy / underdetermination** — materially different low-cost structures fit current evidence comparably well.
3. **Counterfactual disagreement** — live or sampled alternatives predict meaningfully different consequences under possible interventions or changed conditions.
4. **Transfer failure** — a representation predicts familiar data but fails to reuse across remapped contexts.
5. **Credit-assignment failure** — errors cannot be localized well enough to revise selectively.
6. **Compression/reuse opportunity** — recurring dependencies can be represented more economically by a reusable latent process/operator.
7. **Exploratory structural mutation** — a bounded diversity floor searches outside current high-salience/residual regions so the ontology cannot become perfectly self-sealing.

None of these sources says what the candidate structure means.

## Important distinction — uncertainty does not require explicit branching

A second overconstraint was exposed.

Experiment A should **not require** Noema to literally construct two explicit graph hypotheses before the intervention simply because the evaluator knows there are two Markov-equivalent families.

That would make our preferred representation part of the success criterion.

Before decisive evidence, success instead requires:

- calibrated non-commitment;
- predictions that do not pretend one unsupported orientation is certain;
- retained capacity to revise when intervention evidence arrives;
- no irreversible consolidation of one explanation merely because passive prediction is good.

This uncertainty may be represented as:

- multiple explicit hypotheses;
- a multimodal continuous belief;
- unresolved distributed structure;
- another representation that passes the behavioral tests.

Explicit branching must **earn its resource cost**.

## What changes in Experiment A

### Before intervention

The evaluator measures whether Noema is unjustifiably confident, not whether it contains human-readable `chain` and `fork` records.

Across randomized hidden-family trials, pre-evidence predictions under hypothetical interventions should remain calibrated to the unresolved ambiguity.

### After externally scheduled intervention

The decisive evidence may create:

- prediction residual;
- sharp posterior/confidence change;
- structural revision;
- explicit factorization/branch retirement;
- or another local learned change.

The learner succeeds if its future predictions and transfer behavior become appropriately family-sensitive without global destructive rewrite.

### Why Experiment B is stronger

Experiment B requires Noema to decide that an intervention is worth performing because different plausible models imply different outcomes.

That creates a stronger requirement for representing **decision-relevant epistemic disagreement** before intervention.

Thus:

- **A tests calibrated ambiguity + evidence-driven revision.**
- **B tests active recognition and exploitation of epistemic disagreement.**

This is a cleaner separation than forcing A to simulate B internally.

## Consequence for the candidate architecture

The bounded latent-process population remains a strong candidate, but it is no longer privileged by the benchmark.

The full candidate should be able to leave a relationship distributed when explicit branching provides no measurable benefit. Structural hypotheses become worthwhile when they improve one or more of:

- intervention-conditioned prediction;
- transfer;
- local revision;
- counterfactual discrimination;
- compression/reuse;
- calibrated uncertainty under bounded resources.

## Consequence for proposal learning

`proposal is not acceptance` still holds, but proposal itself has more than one trigger.

A learned proposal policy should therefore learn questions such as:

- where does my current model systematically fail?
- where do several explanations remain comparably supported?
- where would a structural distinction change predicted consequences?
- where did a similar representational choice improve transfer before?

It must not reduce those questions to task-family labels.

## New falsifier

EGSS is weakened if ambiguity-aware proposal requires exhaustive enumeration of every possible structure.

Experiment A should therefore distinguish:

- evaluator/reference enumeration, which is allowed for the oracle baseline;
- candidate search, which must remain bounded and cannot simply enumerate the complete three-channel DAG space and later claim that method scales.

The tiny world may make enumeration cheap, but the candidate is deliberately prohibited from relying on that convenience as its core search strategy.

## Naming status

`EGSS` is provisional shorthand for the corrected mechanism.

Existing RGSS documents remain useful for the residual-triggered path. Where they imply that persistent residual error is the only legitimate source of structural proposals, this document supersedes them.

The final design specification should consolidate the terminology rather than carrying both as competing architectures.