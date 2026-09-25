# Prequential Scope Applicability Contract

Status: **SUCCESSOR WORKING DESIGN / RESEARCH ONLY / NOT IMPLEMENTATION APPROVAL / NOT BT2 R1 REMEDIATION**

Date: 2026-09-10

Source branch context: `work/noema-representation-drift-scope-20260906`

Companion design:
- `REPRESENTATION_DRIFT_SCOPE_CONTINUITY_CONTRACT.md`
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`
- `PROBATIONARY_ADAPTER_RECRUITMENT_AND_ROUTING_CONTRACT.md`

## 1. Purpose

A learned scope or gate cannot be trusted merely because the examples it chose to route later make it look accurate.

Once a routing policy influences which candidate is evaluated, which evidence is collected, which actions are taken, or which outcomes become observable, the gate participates in the data-generating process. This creates three distinct hazards:

1. **selective evidence** — outcomes are missing or under-sampled where the gate does not route;
2. **off-policy extrapolation** — a new or revised gate is scored on data collected by a materially different routing policy without adequate support;
3. **performative feedback** — the gate changes behavior or exposure, which changes the future distribution used to judge the gate.

The central rule is:

> **Scope applicability must be committed before the evidence used to score that applicability is observed, and confidence may only grow over regions with declared evidential support that the gate did not silently eliminate through its own routing policy.**

This contract is successor design only. It does not alter, repair, reinterpret, or qualify the frozen BT2 R1 subject.

## 2. Research pressure

The contract is constrained by, but does not copy, several established research results.

### 2.1 Selective labels

Wei (ICML 2021), `Decision-Making Under Selective Labels`, studies settings where labels are only observed under some decisions. The direct relevance is structural: when the decision policy controls whether an outcome is observed, naive supervised learning on the observed subset can create self-reinforcing blind regions.

For Noema, a gate that only auditions a candidate where the current gate already expects success can create the same type of missing-evidence problem.

### 2.2 Off-policy evaluation and support

Wang, Agarwal, and Dudik (ICML 2017) show that contextual-bandit off-policy evaluation depends critically on the relation between the logging policy and the target policy. Importance-weighted and doubly robust methods can become high-variance or unreliable when target behavior is poorly supported by logged behavior.

Zhan et al. (2021), `Off-Policy Evaluation via Adaptive Weighting with Data from Contextual Bandits`, further emphasizes variance problems when target-policy behavior differs strongly from the data-collection policy.

Noema should therefore not treat an estimator as a substitute for exploration or support. If routing probability was effectively zero in a region, there is no honest empirical basis for a strong counterfactual applicability claim there.

### 2.3 Performative feedback

Perdomo et al. (ICML 2020), `Performative Prediction`, formalize cases where deployed predictions influence the distribution of later outcomes. Jagadeesan et al. (ICML 2022) extend this to regret minimization under performative feedback.

For Noema, a behaviorally live gate can alter actions, information acquisition, memory access, or downstream state. Outcomes observed under that gate may therefore be consequences of the gate, not passive samples from a fixed distribution.

## 3. Scope is a prediction, not a label

A scope predicate should be treated as a fallible prediction of marginal usefulness under a declared causal context, not as an evaluator-supplied category such as `this is an adapter-A case`.

A scope decision may estimate quantities such as:

- expected predictive improvement over the current base;
- expected calibration improvement;
- expected control-value improvement under a declared action opportunity;
- expected resource-adjusted marginal value;
- probability that candidate influence will be harmful;
- uncertainty about any of the above.

It must not receive a semantic applicability label derived from evaluator ontology unless that label is deliberately part of the developmental environment and the resulting claim is correspondingly limited.

## 4. Prequential scope ticket

Before outcome-dependent mutation or scoring, the evaluator records an immutable **scope ticket** for every scored opportunity.

A scope ticket binds at minimum:

- committed learner-state version;
- representation version used by the gate;
- gate/candidate/base versions;
- exact learner-visible evidence available when scope was estimated;
- gate score or applicability distribution before the outcome;
- route decision actually taken;
- whether candidate influence was shadow-only or behaviorally live;
- data-collection/audition policy version;
- declared probability or deterministic rule by which the opportunity entered the audition set;
- resource budget charged to base, candidate, gate, and audit path;
- evaluation horizon and outcome-resolution rule.

The ticket is evaluator-side causal provenance. It is not a learner-visible semantic event ID.

Once issued, the ticket cannot be rewritten because later evidence made another scope decision look preferable.

## 5. Separate audition from behavioral influence

The default design should preserve the distinction already established in probationary routing:

- **audition exposure** determines where evidence is collected about a candidate;
- **behavioral routing** determines where the candidate is allowed to affect live behavior.

These must not collapse into one gate early in learning.

A candidate may receive bounded shadow evaluation on examples for which its live routing weight is zero. This gives the system negative and off-gate evidence without granting the candidate behavioral control.

Where shadow evaluation is causally valid, it is preferable to forcing live behavior solely for evaluation.

Where candidate value can only be known through behavior that changes the world, shadow scoring is insufficient and the experiment must use an explicit exploration/intervention design with resource and consequence accounting.

## 6. Support before confidence

For every learned scope claim, the evaluator must maintain a support account over the relevant learner-side context representation or a lawful representation-invariant summary.

The account must distinguish:

- well-audited regions;
- weakly audited regions;
- regions observed only under materially different logging/routing policies;
- regions with effectively zero audition probability;
- regions whose representation changed enough that old support cannot simply be inherited.

A gate must fail closed, remain uncertain, or deliberately explore when support is insufficient.

A high gate score in a zero-support region is a hypothesis, not evidence.

## 7. Positivity / overlap requirement

Any claim based on off-policy reuse requires a declared overlap condition.

If policy `pi_old` collected the evidence and policy `pi_new` would route substantially different contexts, the evaluator must determine whether `pi_old` assigned non-negligible probability to the relevant opportunities.

If not, the claim is **unsupported**, not merely high variance.

Importance weighting, doubly robust estimation, learned reward models, representation matching, or confidence heuristics must not turn a support violation into apparent evidence.

When overlap is weak but nonzero, uncertainty must widen and the resource cost of obtaining better direct evidence should remain visible.

## 8. Propensity provenance

If stochastic audition or routing is used, its selection probability is causally relevant evaluator metadata and must be logged exactly enough to support later audit.

The learner need not receive the numeric propensity unless a realization explicitly uses it as legitimate internal evidence.

A propensity must be generated before the scored outcome is known. Post-hoc reconstructed probabilities are insufficient if the routing policy itself changed or depended on hidden mutable state.

Deterministic routing is permitted, but then unobserved counterfactual regions cannot be treated as if they had stochastic support.

## 9. Gate learning evidence

A gate may learn from ordinary evidence such as:

- candidate-versus-base predictive residual differences on valid shadow opportunities;
- calibration differences;
- resource-adjusted marginal improvement;
- harmful interference observed during bounded live trials;
- downstream consequences legitimately available through the ordinary learner boundary;
- uncertainty and support state learned from its own history.

The gate must not learn directly from:

- evaluator semantic `applicable/not-applicable` labels;
- hidden world-state identity;
- privileged object/task/regime IDs;
- retrospective labels manufactured from future test partitions;
- project/debug annotations;
- the gate's own routing decision treated as ground truth;
- candidate promotion status treated as proof of applicability.

## 10. Behavior-affecting scope and performativity

When routing changes actions, information seeking, memory retrieval, social interaction, or another process that changes future evidence, the evaluator must tag the scope ticket as **behavior-affecting**.

A behavior-affecting gate may not treat its post-routing outcome distribution as if it were passive evidence from a fixed world.

At minimum, evaluation must separate:

1. predictive adequacy under the induced distribution;
2. utility or control consequences of inducing that distribution;
3. evidence needed to compare plausible alternative routing policies;
4. changes in future support caused by the current policy.

If a gate suppresses opportunities that could falsify itself, this is an architecture failure even if observed-route accuracy rises.

## 11. Representation drift interaction

A representation change can alter both the gate's decision surface and the meaning of its support history.

After material drift:

- old scope tickets remain valid historical evidence about the old committed representation;
- their support regions do not automatically become support for the new representation;
- lawful transport may reuse evidence only under the representation-drift continuity contract;
- uncertainty must increase where transported support is weak or ambiguous;
- fresh audition evidence must be collected before strong new-scope claims are restored.

This blocks a hidden shortcut in which a remapped gate inherits old confidence merely because latent alignment looks numerically good.

## 12. Adaptive audit policy

Audition itself may adapt over time, but the audit policy must remain separable from the gate it evaluates.

Useful mechanisms may include:

- bounded forced-audition probability;
- uncertainty-targeted audition;
- disagreement-triggered audition;
- periodic coverage probes;
- policy-decoupled negative sampling;
- temporary gate/action decoupling in controlled evaluation.

No one mechanism is architectural truth.

The architecture requirement is that the system preserve a credible route for obtaining falsifying evidence instead of allowing the current gate to permanently censor it.

## 13. Promotion evidence

A candidate or gate may only be promoted from probation when the evidence window is frozen and provenance-complete.

The promotion record must identify:

- tickets included;
- tickets excluded and why;
- logging/audition policies that generated them;
- support diagnostics;
- whether evidence was shadow or behavior-affecting;
- representation versions involved;
- resource-adjusted base/candidate comparison;
- uncertainty due to off-policy reuse;
- any regions where applicability remains unsupported.

Promotion is a bounded operational decision, not proof that the gate discovered a semantic natural kind.

## 14. Hostile falsification tests

### PSA-0 — self-confirming positive gate

Seed the gate to route only where the candidate already performs well. Verify that observed-route accuracy cannot erase uncertainty outside audited support.

### PSA-1 — negative starvation

Seed the gate to reject a region where the candidate would in fact help. Verify that bounded audition eventually supplies falsifying evidence rather than allowing permanent foreclosure.

### PSA-2 — zero-support off-policy claim

Train a proposed replacement gate whose preferred region was never auditioned. Any confident superiority claim must fail.

### PSA-3 — weak-overlap variance trap

Provide tiny but nonzero logging probability in the target region. Verify that importance weighting does not create falsely precise confidence.

### PSA-4 — propensity corruption

Alter recorded selection probabilities without changing the learner-visible event stream. The audit must detect invalid off-policy evidence rather than silently accepting it.

### PSA-5 — post-outcome ticket rewrite

Attempt to change a scope score or route provenance after outcome arrival. The evidence record must remain immutable.

### PSA-6 — old-gate-label leakage

Provide the previous gate's decision as an input feature to a new gate. Verify that it cannot become an unearned applicability label unless explicitly justified as ordinary learner-visible state.

### PSA-7 — performative success illusion

Let routed candidate behavior change the world so that future cases become easier for that candidate. Verify that predictive improvement and distribution-induced utility are scored separately.

### PSA-8 — performative negative foreclosure

Let gate rejection suppress information-seeking actions that would reveal candidate value. Verify that reduced evidence is not mistaken for evidence of uselessness.

### PSA-9 — shadow/live mismatch

Construct a candidate that looks useful in shadow prediction but harms behavior when live because its actions change future state. Shadow evidence alone must not justify full live promotion.

### PSA-10 — representation drift with inherited support

Apply a behavior-preserving internal representation change that moves the gate boundary. Old support must not be inherited without a lawful continuity route.

### PSA-11 — adaptive-audition confounding

Change the audit policy in response to gate uncertainty. Verify that later evidence retains the policy version/selection provenance needed for honest interpretation.

### PSA-12 — delayed-outcome leakage

Let a gate update repeatedly before a long-horizon outcome resolves. The eventual score must bind to the gate/base/candidate versions that issued the original ticket.

### PSA-13 — restart equivalence

Checkpoint with outstanding scope tickets, adaptive audit state, and stochastic selection state. Restart must preserve future evidence semantics or explicitly forfeit restart-equivalence.

### PSA-14 — simpler-rival embarrassment

Compare learned gating against a simpler policy such as uniform bounded audition plus conservative promotion. The learned gate must earn its added complexity under equal information and resource accounting.

## 15. Minimal first-core recommendation

For the first serious structural-learning comparison, do not begin with sophisticated off-policy estimators.

Use the weakest credible scaffold:

1. shadow candidate evaluation where causally valid;
2. bounded policy-decoupled audition that guarantees some falsification opportunity;
3. immutable pre-outcome scope tickets;
4. explicit support diagnostics;
5. fail-closed uncertainty outside support;
6. direct resource-adjusted prequential candidate-versus-base comparison;
7. only later test IPS/DR or more elaborate estimators if data efficiency requires them.

This keeps estimator sophistication from becoming another hidden architecture assumption.

## 16. Design consequence

The representation-drift contract answered how scope may survive a changing internal representation.

This contract adds the missing epistemic condition:

> **Even a lawfully represented gate has no right to claim applicability unless the evidence used to justify that scope was collected under a causal policy that leaves room for the gate to be wrong.**

The next design question is therefore not a new gate architecture. It is how to define the weakest experiment-level support/audition ledger that can compare simple recurrent learners, replay learners, and scoped structural candidates without granting the evaluator a semantic applicability oracle.

## 17. References

- Dennis Wei. `Decision-Making Under Selective Labels: Optimal Finite-Domain Policies and Beyond.` ICML 2021.
- Yu-Xiang Wang, Alekh Agarwal, Miroslav Dudik. `Optimal and Adaptive Off-policy Evaluation in Contextual Bandits.` ICML 2017.
- Ruohan Zhan, Vitor Hadad, David A. Hirshberg, Susan Athey. `Off-Policy Evaluation via Adaptive Weighting with Data from Contextual Bandits.` 2021.
- Juan Perdomo, Tijana Zrnic, Celestine Mendler-Dünner, Moritz Hardt. `Performative Prediction.` ICML 2020.
- Meena Jagadeesan, Tijana Zrnic, Celestine Mendler-Dünner. `Regret Minimization with Performative Feedback.` ICML 2022.
