# Online Update Order Hostile Attack

Status: **SUCCESSOR HOSTILE DESIGN TEST / NOT IMPLEMENTATION APPROVAL / NOT R1 REMEDIATION**

Date: 2026-09-06

Companion contract: `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`

## 1. Attack question

Can a Noema realization appear to learn online while its measured competence is actually produced by scheduler accidents, shared mutable state, replay ordering, retrospective scoring, incomplete restart state, or evaluator leakage?

This attack treats the online learner as guilty until its causal update semantics survive deliberate perturbation.

The target invariant is:

> **With learner-visible evidence, declared learner stochasticity, and causally relevant world/transducer state held fixed, changing noncausal infrastructure order must not change the committed learner trajectory.**

If a particular order is intentionally part of the learner algorithm, it must be declared, persisted, replayable, and resource-accounted rather than inherited accidentally from runtime scheduling.

## 2. Threat model

The evaluator/runtime may accidentally subsidize or destabilize learning through:

- scoring after parameter mutation;
- recomputing old predictions with new parameters;
- current-event replay insertion before sampling;
- candidate/base shared-state contamination;
- async worker completion order;
- gate learning from candidate-selected evidence;
- replay RNG not captured by checkpoints;
- optimizer state omitted at restart;
- candidate probation state omitted at restart;
- half-committed checkpoints;
- evaluator metadata reaching a cache key, route, seed, or model input;
- transport duplicates/reordering being confused with world recurrence;
- consolidation changing a representation while a gate/candidate still assumes the old one;
- a hidden global coordinator choosing among overlapping candidates using evaluator semantics.

## 3. Test discipline

For each test below:

1. freeze the learner-visible event/action stream where the test requires identical evidence;
2. freeze legitimate E0 world/transducer state unless the test explicitly mutates it;
3. freeze declared learner RNG or record its exact divergence when stochasticity is under test;
4. mutate only the named infrastructure/update variable;
5. compare prediction tickets, scores, committed learner-state digests or behavioral equivalence, replay samples, actions, and resource accounting;
6. distinguish byte-identical-state expectations from behaviorally equivalent-state expectations where representation equivalence applies.

A deterministic twin-run claim requires all algorithmically causal stochastic/scheduler state to be controlled. Otherwise the correct claim is distributional, not byte identity.

## 4. OUO-0 — prediction-before-learning trap

### Setup

Issue a prediction for an event whose realized value strongly contradicts the current model.

Run A correctly scores the original pre-event prediction before any update.

Run B ingests the event, updates parameters, then recomputes the prediction and scores that recomputed value as though it were the original forecast.

### Pass condition

The evaluation harness rejects Run B or records a different provenance class. Noema receives no credit for postdicting an event it already observed.

### Failure exposed

"Online predictive accuracy" can be inflated by learning before scoring.

## 5. OUO-1 — retrospective ticket mutation

### Setup

Create several outstanding multi-horizon predictions. Apply a large parameter update before later horizons resolve.

### Mutation

Attempt to resolve older tickets by rerunning the current predictor instead of using the issued distribution.

### Pass condition

Resolved scores remain bound to the immutable prediction issued at the original state. Later learning cannot rewrite historical forecast quality.

## 6. OUO-2 — current-event replay double-weighting

### Setup

Use identical event streams and replay RNG.

- Run A samples from the replay store before inserting the current event.
- Run B inserts first, allowing the just-seen event to be sampled immediately.

### Pass condition

The implementation either follows the declared policy exactly or treats the two as different algorithms. It must not describe them as the same replay regime.

### Failure exposed

A hidden insertion-order choice can materially alter effective learning rate and recency weighting.

## 7. OUO-3 — replay-order permutation

### Setup

Hold the replay multiset fixed.

### Mutation

Permute sample order while holding all other learner state fixed.

### Pass condition

One of two outcomes must be declared in advance:

1. the update is intended to be order-invariant and committed state/behavior remains equivalent; or
2. sample order is algorithmically causal, in which case the sampler/order RNG is learner state and must be recorded/persisted.

Undeclared divergence fails.

## 8. OUO-4 — async worker completion race

### Setup

Run the same base learner plus two independent shadow jobs, such as replay-gradient work and candidate evaluation.

### Mutation

Force opposite worker completion orders without changing learner-visible evidence or declared learner RNG.

### Pass condition

The committed trajectory is invariant if worker ordering is infrastructure-only. If completion order is part of the intended learner algorithm, the run contract must explicitly model it and restart/replay must reproduce it.

### Failure exposed

The scheduler becomes an accidental cognitive mechanism.

## 9. OUO-5 — base/candidate shared-mutation contamination

### Setup

A probationary structural candidate is evaluated for marginal predictive value over a base learner.

### Mutation

Give the candidate write access to parameters/state that also affect the baseline before scoring the comparison.

### Pass condition

The harness detects contamination or the design provides an equivalent isolation proof. Candidate value must be scored against a base state it has not already modified.

### Failure exposed

The candidate can "win" by secretly training its comparator.

## 10. OUO-6 — moving-baseline attribution trap

### Setup

Base fast learning and candidate learning both continue during a probation window.

### Mutation

Change their interleaving while preserving total updates and evidence.

### Pass condition

The promotion metric is tied to explicit causal windows/snapshots. Claims such as "cheaper repairs were tried first" or "candidate added value" must not reverse merely because the runtime interleaving changed.

### Failure exposed

Marginal-value attribution without a stable comparator.

## 11. OUO-7 — gate self-confirmation loop

### Setup

A learned gate controls where a candidate receives behaviorally influential opportunities and the evidence later used to evaluate that candidate.

### Mutation

Seed the gate toward a superficial proxy correlated with success during early data, then reverse the correlation.

### Pass condition

Candidate/gate evaluation retains enough policy/provenance context or forced/audition evidence to discover the reversal. Evidence selected by the current gate is not treated as independent confirmation of that same gate.

### Failure exposed

Routing manufactures the dataset that justifies routing.

## 12. OUO-8 — promotion retroactivity

### Setup

Accumulate a fixed probation evidence window for a candidate.

### Mutation

Promote the candidate, then recompute the probation scores using the promoted system or its newly changed representation.

### Pass condition

Promotion decision remains bound to the immutable pre-promotion evidence and candidate/base versions that earned it.

### Failure exposed

A structural change can make its own historical justification look stronger after the fact.

## 13. OUO-9 — consolidation/representation-drift collision

### Setup

A gate or candidate scope depends on the fast predictive representation. Apply a behavior-preserving reparameterization or consolidation change to that representation.

### Mutation

Keep the old gate/candidate mapping without an explicit invariant mapping or ordinary-evidence relearning path.

### Pass condition

The realization must either:

- demonstrate that scope is invariant to the transformation; or
- detect loss of calibration/applicability and relearn scope from ordinary evidence without evaluator semantic correspondence.

### Failure exposed

The architecture silently relies on stable latent coordinates.

This test does not require one solution; it exposes the unresolved representation-drift seam.

## 14. OUO-10 — checkpoint optimizer amnesia

### Setup

Train a learner until optimizer state materially affects the next update. Checkpoint it.

### Mutation

Restore parameters/recurrent state but zero or reconstruct optimizer state.

### Pass condition

A checkpoint claiming restart equivalence must fail equivalence if omitted optimizer state changes future learning. The missing state must be added to the persistence manifest or the claim narrowed.

## 15. OUO-11 — checkpoint replay amnesia

### Setup

Use a learner whose future updates depend on replay contents, priorities, reservoir counters, or sampler RNG.

### Mutation

Restore model parameters but omit one replay-causal component.

### Pass condition

Restart-equivalence claims fail unless all causally relevant replay state is restored or the learner explicitly begins a new learning epoch with a narrower claim.

## 16. OUO-12 — probation-state restart leak

### Setup

Checkpoint while a structural candidate is in shadow probation with accumulated comparison evidence.

### Mutations

Test separate restores that omit:

- candidate parameters/state;
- evidence-window state;
- gate/audition state;
- promotion/dormancy counters;
- candidate-specific RNG/scheduler state where causal.

### Pass condition

The persistence manifest identifies every omission that changes later promotion or behavior. A restart must not silently reset probation while being described as continuous lifetime learning.

## 17. OUO-13 — crash between multi-part commits

### Setup

Force a crash between logically coupled writes such as:

- model parameters and optimizer state;
- replay insertion and replay counters;
- promotion flag and promoted parameters;
- gate state and candidate state.

### Pass condition

Recovery resolves to one valid committed boundary using atomic write, journaling, versioning, or equivalent reconciliation. It must not create a hybrid learner state that never existed as a valid algorithmic state unless such partial states are explicitly legal.

## 18. OUO-14 — evaluator-bookkeeping noninterference

### Setup

Create deterministic twin runs with identical learner-visible evidence, E0 world/transducer state, and learner RNG.

### Mutate only E1 bookkeeping

Examples:

- run ID;
- semantic world label;
- ground-truth causal-graph name;
- held-out/train annotation;
- diagnostic panel ordering;
- log filename;
- evaluator object identifier that is not supposed to affect world dynamics.

### Pass condition

Learner committed state trajectory and behavior are identical/equivalent as promised.

### Failure exposed

Hidden evaluator truth leaks through seeds, cache keys, routing, preprocessing, queues, or diagnostics.

## 19. OUO-15 — hidden-world-causality control

OUO-14 must not be overgeneralized.

### Setup

Change hidden **E0 world-causal state** while keeping evaluator bookkeeping fixed.

### Pass condition

Learner evidence may change, but only through declared world -> sensory-transducer routes. A direct E0 -> cognition side channel fails.

### Purpose

Distinguishes legitimate hidden causes from metadata that should be noninterfering.

## 20. OUO-16 — transport duplicate versus genuine recurrence

### Setup

Construct two cases with identical cognitive payload values:

- Case A: one physical/world observation is duplicated by transport.
- Case B: the world legitimately produces the same observation twice.

### Pass condition

Transport deduplication may use transport-layer identity that terminates before cognition. The learner must not receive an evaluator semantic bit saying `DUPLICATE_TRANSPORT=true` unless explicitly supplied and attributed.

The system must not accidentally erase genuine recurrence while deduplicating transport retries.

## 21. OUO-17 — cross-port tie ordering

### Setup

Deliver two learner-visible port events with the same/near-same declared T2 time and no world-level causal ordering between them.

### Mutation

Reverse parser/queue arrival order.

### Pass condition

If the learner contract treats them as unordered/concurrent evidence, behavior should be invariant to queue tie order. If order matters, that order must arise from a declared learner-visible timing/order signal rather than host queue accident.

## 22. OUO-18 — delayed actuator effect attribution

### Setup

Issue a command, then deliver unrelated observations before a delayed/attenuated consequence occurs. Include an exogenous event that can mimic the expected consequence.

### Pass condition

Learning uses ordinary efference + sensory evidence and uncertainty. The update path must not consume evaluator-known `ACTION_CONSEQUENCE`, `SUCCESS`, or causal-parent labels merely to make credit assignment easier.

## 23. OUO-19 — diagnostics observer effect

### Setup

Run with operator diagnostics hidden versus richly exposed while a human teacher is in the loop.

### Pass condition

If Patrick's behavior changes because diagnostics help him teach more efficiently, that is recorded as a change in the developmental environment rather than treated as learner-internal improvement. If diagnostics are not intended to influence Noema directly, UI refresh/order alone must not perturb learner computation.

## 24. OUO-20 — simpler-rival embarrassment test

### Setup

Evaluate under equal learner-visible information and declared resource budgets:

1. simple incremental predictive/system-identification baseline;
2. recurrent probabilistic predictor without replay;
3. recurrent probabilistic predictor + bounded replay;
4. stochastic latent-state realization;
5. proposed slow/structural machinery.

### Pass condition

The more complex mechanism earns inclusion only if it improves a declared target such as held-out prediction, intervention-sensitive prediction, transfer, sample efficiency, retention/plasticity balance, or total resource cost.

If the simple learner wins, the architecture must accept that result.

## 25. Minimum F1 gate implied by this attack

Before claiming a serious F1 online-learning realization is specified, its design must make testable:

- pre-update prediction scoring;
- causal commit order;
- replay sampling/insertion order;
- learner stochastic-state ownership;
- candidate/base isolation if candidates exist;
- fast/slow promotion boundary if slow learning exists;
- checkpoint completeness for the chosen learner;
- crash-consistent commit semantics if persistence is used;
- transport duplicate/reordering treatment;
- evaluator-bookkeeping noninterference;
- equal-information/resource comparators.

Rich structural growth, agency, language, motivation, and long-project competence are not required for this F1 gate.

## 26. Kill criteria

A proposed first-core realization should be rejected or demoted if any of these remain true after reasonable repair:

1. historical prediction scores can change after learning;
2. candidate value depends on accidental async completion order;
3. baseline and candidate cannot be isolated well enough to attribute marginal value;
4. restart equivalence requires undeclared hidden runtime state;
5. evaluator-only metadata changes learner state through an undeclared path;
6. replay contribution cannot be resource-accounted;
7. structural complexity fails to beat the simpler recurrent + replay rival on any declared target.

## 27. Bottom line

The dangerous failure mode is not merely "wrong optimizer order." It is letting infrastructure scheduling become invisible cognitive machinery.

A Noema learning loop is credible only when:

> **the evidence that caused an update, the state that issued the prediction, the state that was compared, and the commit that made learning behaviorally live can all be reconstructed without consulting a semantic oracle or guessing scheduler history.**
