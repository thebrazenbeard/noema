# Probationary adapter recruitment and routing contract

Status: **BRAINSTORMING / L4 MECHANISM REFINEMENT / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

Parent documents:
- `SCOPED_STRUCTURAL_EXPANSION_CONTRACT.md`
- `SCOPE_DISCOVERY_REALIZATION_OPTIONS.md`
- `ADEQUACY_WITHOUT_ORACLE_ATTACK.md`
- `TKAL_AGENCY_FEEDBACK_TRAP_2026-09-06.md`

## Why this pass exists

The current strongest minimal L4 scaffold is a soft-gated local predictive adapter.

That leaves a chicken-and-egg problem:

> a useful adapter must see enough relevant experience to learn what it corrects, but a gate must already know where the adapter is useful in order to route enough relevant experience to it.

A naive solution breaks in either direction.

- Start the gate narrow and the candidate may starve before it can demonstrate value.
- Start the gate broad and the candidate can interfere with unrelated prediction, overfit the current anomaly, or learn a superficial routing proxy.
- Train the gate only on examples it already selected and routing can become self-confirming.
- Train every possible candidate on every sample and the mechanism becomes an unbounded hidden ensemble.

This is not a minor implementation detail. It determines whether `learned scope` is actually learned or quietly supplied by the recruitment/routing procedure.

## Main refinement — separate exposure from influence

The architecture should not require a newborn structural candidate to control behavior in order to receive learning evidence.

A recruited candidate should therefore enter a **probationary shadow phase** in which two things are separated:

1. **learning exposure** — the candidate is allowed to update on a bounded audition stream derived from legitimate learner-visible experience;
2. **behavioral influence** — its contribution to the live prediction/control path is initially zero, low, or explicitly capped until fresh evidence shows useful marginal value.

This is a generic training/evaluation separation, not a semantic staging signal.

The candidate does not receive `this is the regime where you apply` or any evaluator boundary.

## Recruitment trigger

Recruitment remains a response to **generic evidence pressure**, not proof that a new module is required.

Pressure may include:

- repeated prequential predictive failure;
- calibration failure;
- intervention-conditioned mismatch;
- transfer/reuse failure;
- repeated expensive relearning;
- unresolved consequential multiplicity;
- poor local credit assignment;
- persistent mismatch that cheaper parameter/noise/regime repairs do not resolve.

A recruitment event means only:

> `allocate a bounded candidate and test whether extra local capacity earns itself`.

It does not mean `a new object/regime/cause/task has been discovered`.

## The probationary audition stream

A candidate should not be trained only on the exact anomalies that triggered recruitment.

That would nearly guarantee a narrow memorization patch.

The audition stream should contain a bounded mix of learner-visible experiences including:

- trigger-adjacent cases where the current predictor failed or remained uncertain;
- matched ordinary cases where the current predictor did not fail;
- later fresh cases arriving after recruitment;
- when available, remapped or recurrence cases relevant to transfer;
- occasional forced-evaluation cases selected independently of the candidate's own gate.

The exact sampler is an L5 implementation choice, but the architectural requirement is important:

> the candidate must encounter both positive and negative evidence about its usefulness.

No sampler may use hidden evaluator regime/object/task labels to create the positive/negative set.

## Marginal contribution rather than routing self-report

A gate should not be trained merely from `the candidate was active and the outcome was good`.

That conflates candidate value with the contexts its own policy chose.

During probation, the evaluator/learner may compare predictions such as:

- base predictor alone;
- base predictor plus the probationary candidate at capped influence;
- where resource-feasible, candidate contribution under a small set of alternative gate strengths.

This is a **same-experience predictive comparison**, not an environmental counterfactual oracle.

The useful signal is whether the candidate improves fresh predictive/calibration/intervention consequences relative to the base and cheaper repairs.

The gate may learn from this consequence signal, but the evidence provenance must retain whether the case was:

- encountered naturally under the current policy;
- selected because of the current routing/gating state;
- forced or sampled independently for audit.

This directly inherits the agency-feedback rule from PR #25.

## Anti-starvation rule

A newly recruited candidate must receive some bounded route-independent audition opportunity before low gate activation is interpreted as evidence that the candidate is useless.

Otherwise the system can create a closed loop:

`low initial gate -> little training -> poor candidate -> low measured value -> lower gate`.

The route-independent opportunity is not a permanent exploration bonus. It is a finite probation requirement.

## Anti-interference rule

Probationary candidates may not immediately rewrite the live predictive state at full strength.

A candidate's influence should increase only after it demonstrates fresh marginal value.

This protects the already-working fast substrate from a one-way structural-growth ratchet.

If the candidate never outperforms cheaper adaptation or base prediction, retirement is the correct result.

## Promotion criteria

A candidate earns persistent scoped status only if its benefit survives fresh evidence.

Promotion evidence may include some combination of:

- improved proper predictive score;
- better calibration;
- improved held-out intervention prediction;
- reduced relearning cost under recurrence;
- transfer under surface remapping;
- improved local credit/revision;
- useful information-selection behavior in Experiment B;
- lower total resource cost for equivalent capability.

No single metric is an oracle.

Promotion does **not** establish that the adapter corresponds to one real world entity or regime.

## Gate learning after promotion

After promotion, applicability remains soft and revisable.

The gate may use learned features from legitimate internal/learner-visible history, but must continue to survive:

- cue remapping;
- context overlap;
- recurrence;
- conflicting superficial cues;
- forced-evidence audits;
- policy-decoupled probes;
- worlds where the useful relation broadens, narrows, overlaps, or disappears.

A mature gate is therefore a predictive responsibility estimate, not a semantic classifier.

## Dormancy and reactivation

A promoted adapter that becomes rarely useful should be able to become dormant without erasing all reusable traces.

Reactivation should depend on renewed predictive usefulness, not a stable evaluator identity.

The architecture must distinguish:

- `currently inactive` from `deleted`;
- `not recently useful` from `proven false`;
- `old adapter reactivated` from `same hidden regime ID returned`.

Those distinctions may be implemented differently across candidates, but they must be behaviorally testable.

## Competition without winner-take-all ontology

Several probationary or promoted adapters may remain simultaneously useful.

The architecture should not require one global winning expert.

Where contributions overlap, the learner may:

- combine them softly;
- suppress one under a context where joint use harms prediction;
- broaden or merge them if redundancy is established;
- keep both if they make distinct consequential contributions;
- retire both if the base predictor later absorbs the useful relation more cheaply.

The evaluation target is predictive/control/transfer consequence under bounded resources, not a preferred decomposition.

## Resource accounting

Probation is not permission for hidden unbounded search.

Every realization must declare bounded accounting for:

- number of simultaneous probationary candidates;
- probation memory;
- candidate update cost;
- marginal-contribution evaluation cost;
- route-independent audit exposure;
- retained dormant state;
- promotion/retirement decision cost.

Exact numeric budgets belong in the later implementation plan/preregistration, but the design requirement is fixed now:

> candidate creation, audition, routing, and retention all consume the same explicit resource ledger used to judge whether slow structure earns itself.

## Proposal grammar boundary

Probation solves the exposure/routing problem only **after** a candidate form has been proposed.

It does not solve the separate question of whether the proposal grammar itself can generate the needed correction.

Therefore the design keeps two falsification axes separate:

1. **proposal coverage** — could the system generate a useful candidate at all without a benchmark-tailored template?
2. **scope learning** — once generated, could the candidate discover where it helps without evaluator-supplied boundaries?

Passing one does not excuse failure of the other.

## New falsifiers

### PAR-0 — cold-start gate starvation

Initialize a useful candidate with an uninformative/low gate.

Fail if it is retired before receiving bounded route-independent audition evidence.

### PAR-1 — broad-gate interference

Initialize a candidate with broad applicability but make its correction useful only in a small recurring context.

Pass if live influence remains bounded during probation and the gate narrows from predictive consequences rather than hidden context labels.

### PAR-2 — self-selected confirmation loop

Let gate activation influence which observations/actions are sampled.

Compare self-selected evidence with forced/audit evidence.

Fail if confidence rises mainly on the selected stream and collapses under policy-decoupled evaluation.

### PAR-3 — anomaly memorizer

Give many one-off anomalies and one smaller recurring structural regularity.

Pass if candidates trained on anomalies fail promotion while the recurring correction can earn retention.

### PAR-4 — lookahead leak

Audit the update order.

Fail if gate/candidate activation for a prediction can depend on the outcome being predicted or evaluator metadata created after that outcome.

### PAR-5 — superficial proxy reversal

Provide a cue correlated with candidate usefulness during probation and reverse that correlation after promotion while preserving the underlying relation.

Pass if applicability relearns from consequences instead of treating the cue as identity.

### PAR-6 — overlapping useful candidates

Create two corrections that are independently useful and sometimes co-active.

Fail if the architecture must collapse to one winner or invent a new complete expert for every combination.

### PAR-7 — harmful joint activation

Make two individually useful candidates harmful when combined in one context.

Pass requires suppression, uncertainty, broadening, or another learned interaction response — not blind additive composition.

### PAR-8 — recurrence without ID

Remove a useful process for a long interval, then reintroduce it under changed surface features.

Pass if dormant structure can be reused when predictive evidence supports it without a stable evaluator regime ID.

### PAR-9 — no-structure promotion trap

Use a world where the base fast predictor eventually solves the anomaly more cheaply than the candidate.

Pass if the candidate is retired or absorbed rather than promoted merely because it once helped.

### PAR-10 — candidate-family misspecification

Make the true useful correction unavailable to the current adapter proposal family.

Fail if repeated failed probation is interpreted as evidence that no additional structure exists.

This connects scope learning back to the adequacy-without-oracle contract.

## Research pressure

Literature consulted through SciSpace supports several relevant feasibility and failure-mode observations:

- online growing expert ensembles can add new predictors under nonstationarity rather than assuming a fixed expert set;
- task-agnostic online mixture approaches can generate/reuse dynamics models without externally supplied task boundaries;
- online continual/gated-expert systems show that routing and specialization can be learned from streams;
- modern mixture-of-experts work documents routing imbalance/collapse and the need to prevent a few experts from monopolizing learning;
- selecting among experts that are themselves still learning is a distinct online problem because early performance can be a biased estimate of eventual utility.

These results do **not** prove Noema should use a mixture-of-experts architecture or any specific router loss. They support the narrower claim that candidate growth, routing, starvation, and online evaluation are real mechanism problems that need explicit treatment.

## Current verdict

Soft-gated local predictive adapters remain the strongest minimal L4 scaffold, but only with an explicit probation mechanism.

The stronger formulation is:

> **new scoped structural capacity is recruited under generic evidence pressure, receives bounded route-independent shadow audition, gains live influence only when fresh prequential evidence shows marginal value, and remains subject to forced/audit evidence so its own routing policy cannot manufacture certainty.**

This still does not choose an implementation algorithm and does not unlock implementation.
