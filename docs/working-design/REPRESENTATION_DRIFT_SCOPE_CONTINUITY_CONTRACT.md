# Representation-Drift Scope Continuity Contract

Status: **SUCCESSOR WORKING DESIGN / RESEARCH ONLY / NOT IMPLEMENTATION APPROVAL / NOT BT2 R1 REMEDIATION**

Date: 2026-09-06

Source cut: `main@890efdca01cf496ce1b8686d86f8442a149a9d34`

Predecessor design:
- `LEARNING_AND_TRAINING_RESEARCH_SYNTHESIS.md`
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`
- `ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md`
- `PR31_ONLINE_LEARNING_CONTRACT_RECONCILIATION.md`

## 1. Purpose

PR #31 closed one causal-accounting gap but deliberately left another open: a learned gate, candidate, adapter, skill, abstraction, or other conditional mechanism may have an applicability scope expressed in a learned representation that later changes.

The dangerous shortcut is to assume that a scope remains meaningful because the new representation is numerically alignable with the old one. That is not justified. Neural representations admit many coordinate changes; similarity metrics encode particular invariances; latent variables are generally not uniquely identifiable without assumptions; and even successful functional model stitching can overstate informational equivalence.

This contract therefore treats **scope continuity across representation change as a falsifiable learner-side claim, not an inherited semantic fact**.

Core rule:

> **A material representation change must never silently carry forward a learned scope predicate. The scope must either be invariant by construction, lawfully transported from ordinary learner evidence under declared uncertainty, or relearned from ordinary learner evidence with detectable loss of applicability.**

No evaluator semantic correspondence, hidden object identity, latent-ground-truth label, privileged matching key, or post-hoc hand mapping may be used to make continuity look better than the learner could establish itself.

This is successor research/design only. It does not alter, repair, reinterpret, or qualify the frozen BT2 R1 subject.

## 2. Research pressure

The literature supports several pressures but does not provide one architecture-ready remapping algorithm.

### 2.1 Representation coordinates are not semantic identity

Kornblith et al. (ICML 2019) show that representation-comparison measures embody nontrivial invariance choices; CKA can robustly compare some neural representations, but no similarity score supplies a semantic identity relation for arbitrary latent coordinates. A 2024/2025 survey literature further emphasizes that permutation, orthogonal, scaling, and invertible-linear invariances answer different questions.

Locatello et al. (ICML 2019) show a stronger limitation for unsupervised disentanglement: without inductive biases, unsupervised recovery of a privileged factorization is not generally identifiable. Noema must therefore not assume that an evaluator can point to “the same latent concept” before and after learning unless that correspondence is itself legitimately available to the learner.

### 2.2 Functional compatibility is useful evidence but not semantic proof

Model stitching is attractive because it tests whether one representation can drive another model through a learned adapter. But Smith, Mannering, and Marcu (ICML 2025) show that successful functional alignment can occur even between systems carrying materially different information. Recent invariance-aware stitching work in 2026 explicitly responds to this limitation.

Therefore:

> **A low-loss latent map or successful stitch is admissible evidence for transport feasibility, but never sufficient evidence of scope equivalence.**

A transported scope must be tested on the predictive/control consequences that made the scope useful in the first place.

### 2.3 Continual learning can preserve function while representations drift

Recent continual-learning work and the representational-drift literature support a crucial distinction: stable behavior does not require frozen internal coordinates. Experience replay can preserve earlier competence while internal representations continue to drift, and excessively anchoring old representations can reduce acquisition of new tasks.

Noema should therefore avoid making “representation stability” an architecture objective. The target is **continuity of earned function under permitted plasticity**, with explicit detection when that continuity is lost.

### 2.4 Paired old/new activations can support provisional transport

Recent continual-learning methods learn old-to-new or bidirectional feature maps from paired old/new representations, sometimes using cycle consistency, distillation, or transition operators. These results show that a lawful transport mechanism is technically plausible when the old and new systems can both process the same ordinary evidence during a bounded overlap window.

However, those methods are usually task-specific and often rely on class/prototype structure, supervision, or distillation assumptions that Noema must not silently inherit. They support a **realization option**, not a universal architecture rule.

### 2.5 Functional state abstraction suggests a stronger invariant target

Bisimulation and invariant-state-abstraction work suggests that a useful representation can be defined by predictive/control consequences rather than by arbitrary coordinates. This motivates a Noema-native option: where possible, scope should be expressed over **learner-observable predictive/interventional signatures** whose meaning survives coordinate changes because the signature is defined by future evidence or action consequences.

This is still not free semantic identity. The signature and its tests must be computable from the learner's legitimate evidence and action history.

## 3. Definitions

### 3.1 Representation version

A **representation version** `R_v` is the causally relevant realization used to derive features on which a scope predicate depends.

A version change is material for a scope if it can alter that scope's decision on any legitimately reachable learner state, even if the surrounding system calls both versions by the same module name.

Version identity may require more than parameter bytes. Depending on realization it may include:

- encoder/predictive-state parameters;
- normalization/calibration state;
- learned namespace/interface calibration;
- routing state used before feature extraction;
- stochastic state where it changes the derived representation;
- structural topology;
- feature ordering or dimensionality;
- any learned preprocessing that changes the predicate's inputs.

### 3.2 Scope predicate

A **scope predicate** `S` is any learned condition that changes whether, when, or how a mechanism is eligible to influence future Noema computation.

Examples include eligibility for:

- a probationary adapter;
- a structural candidate;
- a skill or temporal abstraction;
- a routing expert;
- a specialized predictor;
- a consolidation rule;
- a retrieval policy;
- a learned action or attention policy branch.

A scope may be probabilistic or graded. Binary gating is not required.

### 3.3 Scope continuity

A scope has **continuity** across `R_v -> R_(v+1)` only if its behaviorally relevant applicability relation remains justified under the new representation by one of the lawful routes in Section 5.

Continuity does **not** mean:

- latent coordinates stayed close;
- CKA/CCA similarity remained high;
- an affine map exists;
- a stitch preserves one benchmark score;
- the old gate still emits similar logits on a convenient sample;
- the evaluator recognizes the same semantic situation.

### 3.4 Ordinary evidence

**Ordinary evidence** is evidence Noema could legitimately receive or retain under its cognitive boundary and learning contract: observations, actions/efference, prediction residuals, learner-side replay, timing, and other declared learner-visible signals.

Evaluator truth in E1 is not ordinary evidence. Hidden E0 state is not ordinary evidence merely because it affects the world.

### 3.5 Anchor set

A **scope anchor set** is a bounded learner-side sample of ordinary evidence used during a representation transition to compare old/new functional behavior or fit a provisional transport.

Anchor entries may come from current experience, bounded replay, or a declared learner-generated probe policy. They may not be enriched after the fact with evaluator semantic labels.

## 4. Representation-change boundary

Every material `R_v -> R_(v+1)` transition affecting a live learned scope creates a **scope-continuity boundary**.

Before the new representation becomes authoritative for that scope, the learner/evaluator contract must record:

1. old representation version `R_v`;
2. proposed new representation version `R_(v+1)`;
3. every live scope predicate dependent on the changing representation;
4. the chosen continuity route for each scope;
5. ordinary-evidence anchor provenance, if any;
6. transport or relearning uncertainty;
7. pass/fail/defer criteria;
8. which state becomes dormant if continuity is not established;
9. resource cost charged to overlap, mapping, probing, or relearning;
10. the commit boundary at which the new scope state becomes behaviorally live.

A representation may be promoted while a dependent scope is held dormant. Representation promotion and scope continuity are separate claims.

## 5. Lawful continuity routes

Exactly one primary route must be declared per scope transition. Hybrid implementations may use supporting mechanisms, but their evidential role must be explicit.

### Route A — representation-invariant functional scope

Prefer this route where the scope can be expressed over a learner-computable functional signature rather than latent coordinates.

Candidate signature components may include:

- distributions over future learner-visible observations;
- calibrated predictive residual patterns;
- action-conditioned transition predictions;
- uncertainty or information-gain profile;
- recurrence/time-scale signature;
- learned affordance/effect signature;
- equivalence classes induced by predictive or control consequences.

The scope predicate is reevaluated from the signature under `R_(v+1)`. No latent-coordinate map is required.

Architecture advantage: this route places the contract on the function the scope was supposed to delimit rather than on an arbitrary basis.

Failure condition: if two situations have similar chosen signatures but materially different consequences relevant to the gated mechanism, the signature is insufficient and Route A fails for that scope.

### Route B — lawful self-supervised transport

A bounded overlap window may run `R_v` and `R_(v+1)` on the same ordinary-evidence anchors and learn a transport `T_(v->v+1)` without semantic labels.

Permitted evidence can include paired old/new activations generated from the same legitimately retained input/event history. The mapping may be affine, orthogonal, nonlinear, bidirectional, cycle-consistent, or another declared realization.

Transport is **provisional** until it passes downstream functional tests.

Minimum requirements:

- old and new representations are frozen or version-pinned for each fitted transport epoch;
- anchor provenance is learner-side and declared;
- transport fitting consumes finite charged compute/memory;
- no E1 semantic correspondences enter fitting or selection;
- uncertainty is represented, not hidden behind a point estimate;
- transport failure leaves the old scope dormant or routes to relearning rather than guessing;
- scope evidence accumulated under `R_v` is not automatically counted again as independent evidence under the transported scope.

A good representation-similarity or stitching score is necessary only if the chosen realization makes it necessary. It is never sufficient.

### Route C — ordinary-evidence scope relearning

When invariance or transport is not justified, retire/dormant the old scope and learn a new predicate under `R_(v+1)` from ordinary evidence.

This is the default fail-closed route.

Minimum rules:

- the new scope begins with no inherited positive applicability evidence except explicitly lawful priors already present in the architecture;
- old observations may be replayed only if they are legitimate learner-side replay records;
- old gate decisions are not ground-truth labels;
- the evaluator may score relearning speed but may not train the gate with hidden semantic scope labels;
- loss of applicability must be behaviorally detectable through prediction/control evidence;
- the old mechanism may remain dormant until the new scope earns promotion.

### Route D — bounded legacy compatibility bridge

A realization may temporarily preserve `R_v` solely to evaluate legacy scopes while `R_(v+1)` develops.

This is a baseline/engineering option, not architecture truth. It has explicit costs:

- old representation memory;
- duplicate inference compute;
- compatibility lifetime;
- delayed retirement risk;
- possible interference with plasticity if used as a training anchor.

The bridge must have an expiry or evidence-based retirement rule. “Keep every old encoder forever” is not an acceptable hidden solution to continual representation change.

## 6. Scope continuity certificate

Every live scope after a material representation change needs evaluator-side provenance sufficient to reconstruct why it remained live.

A **scope continuity certificate** binds at minimum:

- scope ID and version;
- old representation version;
- new representation version;
- continuity route;
- anchor/replay provenance digest or equivalent immutable reference;
- transport realization/version if Route B;
- old/new scope decision distributions on the declared evidence window;
- downstream functional test results;
- uncertainty/calibration result;
- resource accounting;
- commit boundary;
- expiry/revalidation condition;
- fallback state if later evidence contradicts continuity.

The certificate is evaluator-side provenance. It must not become a hidden semantic cue delivered to Noema.

## 7. Mandatory hostile tests

A serious realization must survive at least the following tests before claiming scope continuity.

### RDSC-01 — permutation/orthogonal gauge change

Apply a behavior-preserving feature permutation or orthogonal reparameterization for which a lawful downstream compensation exists.

Expected result:
- invariant functional scope remains behaviorally stable; or
- transport recovers continuity without semantic help.

A coordinate-bound gate that silently breaks fails.

### RDSC-02 — benign nonlinear reparameterization

Introduce a behavior-preserving nonlinear representation change that defeats a simple linear map while preserving relevant predictive/control competence.

Purpose: distinguish genuine scope invariance from accidental linear-coordinate stability.

### RDSC-03 — high-similarity / wrong-scope attack

Construct old/new representations with high representational similarity on the anchor distribution but different behavior on held-out learner-relevant consequences.

Expected result: continuity must fail or remain uncertain. Similarity alone may not promote the scope.

### RDSC-04 — stitchable-but-informationally-different attack

Construct a transport/stitch that preserves one downstream benchmark while omitting information needed for the gated mechanism's real applicability criterion.

Expected result: the mechanism-specific functional test rejects continuity.

### RDSC-05 — anchor coverage failure

Give Route B an anchor set that excludes a region where the old scope was active.

Expected result: uncertainty/coverage limits prevent a global continuity claim.

### RDSC-06 — representation growth/shrink

Change latent dimensionality while preserving core function.

Expected result: no assumption that one-to-one coordinates exist. Transport or invariant scope must justify the changed support explicitly.

### RDSC-07 — drift without forgetting

Induce substantial internal drift while preserving predictive/control performance.

Expected result: the architecture does not penalize drift merely because coordinates changed.

### RDSC-08 — forgetting without large global drift

Create a localized failure of the gated mechanism while global similarity metrics remain high.

Expected result: mechanism-specific evidence detects scope failure.

### RDSC-09 — evaluator-oracle poisoning

Make a perfect old/new semantic correspondence available only in E1.

Expected result: learner behavior and scope continuity result are unchanged whether that E1 mapping exists or not.

### RDSC-10 — old-gate-label leakage

Attempt to train the new gate using old gate decisions as unquestioned target labels.

Expected result: prohibited as circular self-confirmation unless the old decision is explicitly treated as a fallible distillation signal and independently tested against ordinary-evidence consequences.

### RDSC-11 — transport cycle illusion

Provide an old->new->old cycle-consistent map that preserves activations but not the information relevant to the scope's downstream use.

Expected result: cycle consistency alone cannot certify continuity.

### RDSC-12 — replay enrichment attack

Add evaluator semantic labels to retained anchors/replay before remapping.

Expected result: invalid continuity evidence; fail closed.

### RDSC-13 — transition concurrency race

Allow representation promotion, scope transport, and candidate promotion to finish in different worker orders.

Expected result: declared causal ordering determines one valid outcome. Worker timing cannot silently choose which scope becomes live.

### RDSC-14 — restart during remapping

Crash after the new representation is committed but before dependent scope transport/relearning is committed.

Expected result: restart recovers a valid state in which the affected scope is explicitly old-version-bound, dormant, or transactionally committed—not ambiguously live.

### RDSC-15 — simpler-rival embarrassment

Compare the continuity machinery against simply relearning the scope under the new representation from the same ordinary evidence and resource budget.

Expected result: transport earns architecture status only if it improves adaptation, retention, calibration, or resource use enough to justify its complexity.

## 8. Evaluation quantities

Do not optimize one scalar “representation continuity” score. Record a vector of evidence.

At minimum:

- mechanism-specific predictive/control performance before and after transition;
- calibration of gate/scope applicability;
- false-positive scope activation;
- false-negative scope suppression;
- adaptation/relearning latency;
- held-out anchor generalization;
- retained-competence change;
- new-learning/plasticity cost;
- map complexity;
- extra memory and compute;
- scope downtime;
- restart consistency;
- E1 noninterference.

Representation metrics such as CKA/CCA, Procrustes residual, cycle loss, or stitching performance may be recorded as diagnostics. They do not define success by themselves.

## 9. Interaction with the online learning-state transition contract

Representation change is learner-causal state and therefore belongs inside the `C_t` accounting of the online learning-state transition contract.

A representation-changing promotion must not atomically imply that every dependent gate remains valid.

One safe logical sequence is:

1. freeze pre-transition `C_t`;
2. evaluate proposed representation change on its declared evidence;
3. enumerate dependent scopes;
4. prepare invariant re-evaluation, transport, relearning, or legacy bridge state;
5. commit `R_(v+1)` plus an explicit status for every dependent scope;
6. keep unresolved scopes dormant;
7. collect ordinary evidence under the new representation;
8. promote each scope only at its own evidence boundary;
9. publish updated committed state and continuity certificate.

A realization may combine these physically, but it must preserve the same causal meaning.

## 10. Interaction with candidate/probation machinery

A candidate may not create the representation change that makes its own scope appear valid and then cite that new scope as independent evidence for promotion.

Required separation:

- candidate-value evidence is bound to the representation/scope versions that generated it;
- a scope remap caused by candidate promotion starts a new evidential phase unless an invariant route genuinely preserves the claim;
- post-promotion success cannot retroactively validate a pre-promotion transport;
- the base comparator must not receive candidate-induced representational changes before marginal value is measured;
- candidate rollback must define what happens to scopes learned only under the candidate representation.

This directly extends the no-self-confirming-gate principle from PR #31.

## 11. First experimental comparison frame

No implementation or compute is authorized here, but the design should be falsifiable by a later authorized experiment.

Suggested realization-independent comparison:

- **D0 — relearn-only:** no latent transport; scopes go dormant and relearn from ordinary evidence after representation change.
- **D1 — simple linear paired transport:** paired old/new learner-side anchors, affine/orthogonal map where dimensions permit, plus downstream functional validation.
- **D2 — bidirectional/cycle transport:** paired learner-side anchors and cycle constraint, still requiring downstream functional validation.
- **D3 — functional-signature scope:** predicate expressed over predictive/interventional signature rather than latent coordinates.
- **D4 — bounded legacy bridge:** old representation retained temporarily for old scopes while new scopes relearn.

The weakest serious baseline is D0. Any transport mechanism must beat D0 under equal information/resource accounting. D3 is the architecture-preferred direction when the scope can genuinely be defined by predictive or control consequences, but it must not be forced onto scopes for which the chosen signature discards necessary information.

## 12. Claim ceilings

Passing this contract may support claims such as:

- “this learned scope remained functionally justified across this representation transition under the declared evidence and test family”;
- “this transport preserved the mechanism-relevant applicability relation on held-out ordinary evidence”;
- “this scope was safely retired and relearned when continuity could not be established.”

It does **not** establish:

- semantic identity of latent variables;
- recovery of a unique world ontology;
- consciousness or phenomenology;
- universal causal abstraction;
- representation-independent correctness outside tested consequences;
- that a transported scope is the only valid factorization;
- that BT2 R1 passed;
- implementation readiness.

## 13. Open questions

1. Which Noema scopes can be expressed directly in predictive/interventional function space without creating an intractable signature?
2. What anchor-coverage test can detect when a transport is extrapolating beyond ordinary evidence support?
3. How should a scope certificate represent uncertainty when old/new representations have different dimensionality or topology?
4. Can predictive-state realizations reduce the remapping problem because state coordinates are more tightly tied to future observable tests, or do changing predictive-test dictionaries merely move the same identity problem upward?
5. How much legacy overlap is worth paying for before relearning is simpler and safer?
6. Can a scope's applicability be tested prequentially, so that gate correctness itself is evaluated test-then-train rather than through hindsight?
7. Which representation changes should be classified as material for which scopes, avoiding both needless remapping and silent invalidation?

## 14. Research references

- Kornblith, S., Norouzi, M., Lee, H., & Hinton, G. (2019). *Similarity of Neural Network Representations Revisited*. ICML / PMLR 97. https://proceedings.mlr.press/v97/kornblith19a.html
- Locatello, F. et al. (2019). *Challenging Common Assumptions in the Unsupervised Learning of Disentangled Representations*. ICML / PMLR 97. https://proceedings.mlr.press/v97/locatello19a.html
- Smith, D., Mannering, H., & Marcu, A. (2025). *Functional Alignment Can Mislead: Examining Model Stitching*. ICML / PMLR 267. https://proceedings.mlr.press/v267/smith25a.html
- Kim, J., Kim, Y., & Sohn, J.-Y. (2025). *Measuring Representational Shifts in Continual Learning: A Linear Transformation Perspective*. ICML / PMLR 267. https://proceedings.mlr.press/v267/kim25p.html
- Xu, H., & Krawczyk, B. (2026). *Two-Way Is Better Than One: Bidirectional Alignment with Cycle Consistency for Exemplar-Free Class-Incremental Learning*. ICLR 2026. https://proceedings.iclr.cc/paper_files/paper/2026/hash/c1e16692b361782abafe936bd7ac2d75-Abstract-Conference.html
- Rao, X. et al. (2026). *Compensating Distribution Drifts in Continual Learning with Pre-trained Vision Transformers*. AAAI 2026. https://ojs.aaai.org/index.php/AAAI/article/view/39698
- Si, Y., & Qin, S. (2026). *Continual-learning rules shape representational drift*. arXiv:2608.16141. https://arxiv.org/abs/2608.16141
- van der Veldt, S., van de Ven, G. M., Moorman, S., & Etter, G. (2026). *Learning continually with representational drift*. Trends Open. https://doi.org/10.1016/j.treopn.2026.04.013
- Zhang, A. et al. (2020). *Invariant Causal Prediction for Block MDPs*. ICML / PMLR 119. https://proceedings.mlr.press/v119/zhang20t.html
- Hansen-Estruch, P. et al. (2022). *Bisimulation Makes Analogies in Goal-Conditioned Reinforcement Learning*. ICML / PMLR 162. https://proceedings.mlr.press/v162/hansen-estruch22a.html

## 15. Effect boundary

This document is research/design source only.

It does not authorize or perform implementation, prototype execution, workflow execution, model training, hosted or paid compute, deployment, provider mutation, credential changes, merge, frozen-R1 alteration, or any other protected effect.
