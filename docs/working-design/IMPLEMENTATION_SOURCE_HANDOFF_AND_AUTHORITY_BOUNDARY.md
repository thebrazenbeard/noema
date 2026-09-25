# Noema Implementation-Source Handoff and Authority Boundary

Classification: **IP_CONFIDENTIAL**

Status: **INERT HANDOFF CONTRACT / RESEARCH-SOURCE ARTIFACT / DOES NOT AUTHORIZE IMPLEMENTATION / DOES NOT AUTHORIZE TRAINING OR EXPERIMENT EXECUTION / NOT BT2 R1 REMEDIATION**

Date: 2026-09-13

Private repository: `thebrazenbeard/noema`

Research basis before this handoff artifact: PR #32 exact head `419f03b9b8c47e6ae519cc33ecca05ebb6e6c7ac`.

This document does not change the current authority ceiling. Its purpose is to make the next separately authorized source lane exact enough that implementation cannot silently redefine the research contract.

## 1. Why this handoff exists

PR #32 has reached research-contract closure for the structural-value falsification family, but the repository remains intentionally documentation-only. There is no `src/` tree, no `tests/` tree, no approved programming language/runtime, and no immutable implementation subject.

The next project step therefore cannot honestly be described as “run the experiment.” A source implementation must first exist, preserve the research boundaries, survive hostile source review, and bind its behavior to immutable provenance.

This handoff separates four questions that must not collapse into one another:

1. **Research contract:** what a fair experiment would have to mean.
2. **Implementation source:** whether software realizes that contract without adding hidden privileges or changing the claim.
3. **Execution/training:** whether an approved implementation is allowed to update learner state or run experimental trajectories.
4. **Protected effects:** merge, deployment, hosted/paid compute, publication, provider/credential/ruleset mutation, repository-visibility changes, or protected-system connection.

Passing one question never grants authority for the next.

## 2. Authority states

### R0 — research/design only

This is the current state.

Allowed work is limited to private research/design/source-governance artifacts and review of those artifacts. No implementation source, prototype execution, learner update, model training, experiment execution, or protected effect is implied.

### I0 — implementation-source authority

A future explicit authorization may open a bounded source lane to create the minimum implementation required by the frozen research contracts.

I0 does **not** imply permission to train a model, run an experimental learner trajectory, use hosted/paid compute, merge, deploy, publish, connect to protected systems, or change provider/repository controls.

The authorization should identify the source branch/PR, exact research parent, and whether deterministic local verification is included.

### I1 — deterministic source-verification authority

If explicitly included with I0, the source lane may run the minimum deterministic checks necessary to verify software mechanics: schema validation, serialization/hash tests, pure-function tests, hostile unit/property tests, and similarly bounded non-learning checks.

I1 is not permission to perform learning/training. A test that updates persistent learner parameters from a developmental stream, estimates empirical performance, or executes the preregistered experiment family belongs to the execution/training gate unless separately classified and authorized.

### E0 — learning/experiment-execution authority

This is a separate future gate. It covers any run whose purpose is to update learner state from developmental evidence, estimate candidate performance, execute SVF-0/SVF-1 trajectories, populate empirical resource/performance results, or support a capability claim.

E0 must bind an immutable implementation commit and a manifest that has passed the real implementation-aware validator. Research-only shape exemplars cannot satisfy this gate.

### P0 — protected-effect authority

Merge, deployment, publication, paid/hosted compute, visibility changes, provider/credential/ruleset mutation, production/protected-system connection, and comparable protected effects remain separately controlled even if I0/I1/E0 have been granted.

## 3. Future source-lane topology

Unless fresher authority says otherwise, the implementation-source lane should be isolated from `main` and should not mutate PR #32 in place.

The preferred topology is:

1. fresh-read `main` and the exact canonical PR #32 research head;
2. create a new bounded implementation branch from the exact research head that has passed the latest head-bound research adjudication;
3. open a private Draft PR stacked on the PR #32 branch, or on a later canonical base only if that base has been explicitly authorized;
4. record the exact parent SHA in the implementation PR body;
5. never treat the moving PR #32 branch name as sufficient provenance;
6. require rereview if either the research parent or implementation head moves.

No direct-to-`main` implementation work is permitted by this handoff.

## 4. Runtime and dependency decision is deliberately unresolved

No programming language, numerical library, ML framework, serialization stack, or package layout is approved by the research line.

The implementation lane must make that decision explicitly rather than inheriting an unstated default.

Before substantive learner implementation, it should persist an implementation decision record that identifies at least:

- language/runtime and exact version policy;
- dependency set and lock/reproducibility mechanism;
- deterministic/random-seed controls;
- canonical serialization and hashing route for immutable artifacts;
- probabilistic/numerical requirements;
- testing/property-testing support;
- resource-metering route for memory, retained state, replay, candidate state, and relevant compute proxies;
- checkpoint behavior, noting that first-core fixed-envelope V2 primary trajectories currently forbid checkpointing unless a separately frozen checkpoint-resource envelope exists;
- how evaluator-only diagnostics are isolated from developmental learner state;
- why the choice is the smallest practical realization rather than an architecture expansion.

A framework is a tool, not evidence. Pretrained semantic components, hidden foundation-model services, evaluator labels, task/family identities, or other undeclared information channels are outside the developmental evidence boundary.

## 5. Minimum implementation-source deliverables

An I0 lane should implement no broader cognitive architecture than needed to create a real falsifiable subject.

### 5.1 Canonical event/interface types

Implement the minimum typed representation of learner-visible events, intervention-provenance packets, pre-outcome prediction/scope tickets, evaluator-only bookkeeping, and immutable identifiers required by the existing interface contracts.

Learner-visible and evaluator-only paths must be separable in source, not merely by convention.

### 5.2 V2 preregistration validator

Implement the V2 schema plus semantic validator obligations, including the resource, decidability, and comparator-matrix addenda.

The validator must distinguish at least:

- schema/shape failure;
- unavailable authoritative evidence;
- information-boundary failure;
- cross-field/comparator failure;
- resource-accounting failure;
- support/audition failure;
- freeze/provenance failure;
- a genuine implementation-bound valid result.

It must not emit `PASS_FROZEN_VALID` for a research-only placeholder subject.

### 5.3 Condition and provenance registry

Implement immutable resolution for candidate IDs, source commits/artifacts, information/opportunity/resource/replay/scope-policy conditions, comparator references, transfer contracts, schedule commitments, metric specifications, and relevant preimages.

Branch names are convenience pointers. Immutable commits and content-addressed artifacts define the subject.

### 5.4 C1 recurrent probabilistic substrate

Implement the smallest recurrent probabilistic online predictor sufficient for the SVF-0 persistence gate and as the base substrate for C2.

The source lane must not add semantic task/family labels, pretrained semantic embeddings, or evaluator-side hidden variables to developmental inputs.

### 5.5 C2 bounded-replay rival

Implement C2 as the declared C1 base substrate plus only the preregistered bounded replay capability needed for the C1/C2 comparison.

Replay capacity, insertion/selection behavior, update limits, retained evidence, and resource charges must be inspectable. Replay records cannot become richer after the fact through evaluator annotations.

### 5.6 C4 bounded structural candidate

Implement C4 on the same declared base-substrate contract used by the fair C2 rival, plus only bounded structural-candidate machinery admitted by the research contracts.

The first source subject must remain deliberately small. Generic computational structure is permitted; built-in semantic answers such as hidden family identity, `chain`, `fork`, causal-role labels, or a privileged `do()` oracle are not.

Structural state, candidate population, proposal/search work, scope inference, audition, support records, and retained traces are part of the resource/evidence accounting rather than free sidecars.

### 5.7 Comparator and ticket instrumentation

Implement independent C2-versus-C4 comparison support and, where lawful, C4 internal base-only/shadow diagnostics as different evidence objects.

Every primary scored prediction or scope decision must be committed before its corresponding scored outcome is visible.

Internal C4 shadow evidence never substitutes for an independent C2 comparison.

### 5.8 Resource/support ledger

Implement machine-readable accounting for the resource and support distinctions required by the research ledger.

Zero/unknown support, missingness, counterfactual-unobserved opportunity, invalidation, direct support, transported support, and off-policy-supported evidence must remain distinguishable. No estimator may manufacture evidence in a zero-support region.

### 5.9 Evaluator/world boundary

Implement only enough evaluator/world source to bind immutable world-generator, parameter-distribution, seed, intervention-schedule, scoring, negative-control, and aggregation artifacts.

The implementation-source lane does not acquire permission to execute the developmental experiment merely by implementing its generator.

Externally scheduled SVF-1 intervention must remain non-adaptive to hidden family identity, candidate predictions, scored outcomes, and evaluator diagnostics.

## 6. Required hostile source tests

Before an implementation head can be called source-ready, hostile tests must demonstrate that the source rejects or exposes at least these cases:

1. SVF-0 structural claim substitution or forced C2/C4 comparison.
2. Hidden-family-, outcome-, prediction-, or diagnostic-adaptive SVF-1 scheduling.
3. C2/C4 base-substrate mismatch disguised as structural value.
4. Learned-scope versus bounded-audition comparison with other candidate machinery changed.
5. C3 omitted while a report attempts a stronger-than-C2 claim ceiling.
6. Diagnostic/oracle state or outputs entering a developmental learner path.
7. Replay enrichment with evaluator-only or future information.
8. Uncharged durable structural/candidate/audition state.
9. Zero/unknown support laundered into positive applicability evidence.
10. Missing or irretrievable commitment preimages.
11. Broken comparator/metric/candidate references.
12. Vague non-decidable acceptance, stopping, aggregation, support, kill, or resource rules.
13. Restart-equivalence claims without the required persisted causal state.
14. First-core fixed-envelope checkpointing without a separately frozen checkpoint-resource envelope.
15. Representation-version changes that silently inherit old scope/support confidence.
16. Placeholder or fabricated implementation provenance receiving `PASS_FROZEN_VALID`.
17. Branch-head movement silently changing a frozen subject.
18. Resource-frontier points cherry-picked or redesigned after scored outcomes.

These tests prove source-boundary behavior only. They do not prove Noema learns anything.

## 7. Source-readiness evidence package

A future implementation-source head is not ready for experimental authorization until its lane can produce a review packet containing:

- exact implementation commit SHA;
- exact research-parent SHA;
- complete changed-file inventory;
- dependency/runtime lock evidence;
- canonical source/artifact hashes where required;
- validator version and exact test subject;
- hostile unit/property-test results permitted by that lane's authority;
- explicit list of any checks not run because execution authority was withheld;
- clean-clone/reset reproducibility evidence when permitted;
- confirmation that no learner training/experiment execution occurred;
- confirmation that no hidden evaluator information path was introduced;
- resource-meter coverage map;
- independent hostile source review bound to the exact implementation head.

A PASS at this stage should be labeled **SOURCE_IMPLEMENTATION_REVIEW = PASS** or equivalent. It must not be called behavioral qualification, experiment success, or capability evidence.

## 8. Transition to a real experiment subject

Only after a real implementation commit exists may a real preregistration manifest bind that commit.

The sequence is:

1. implementation source reaches an exact reviewed head;
2. immutable world/scoring/resource artifacts exist;
3. a V2 manifest binds those immutable artifacts and the exact implementation commit;
4. the implementation-aware validator checks the real subject;
5. if valid, the manifest may receive `PASS_FROZEN_VALID` as a provenance/contract status;
6. **only then** can a separate E0 decision authorize execution/training of that frozen subject.

`PASS_FROZEN_VALID` still does not mean the experiment ran or the architecture succeeded.

## 9. Stop and escalation conditions

An implementation lane must stop and request new authority or research adjudication if it discovers that:

- the smallest implementation requires changing a research invariant rather than merely realizing it;
- a runtime/library silently adds pretrained or evaluator-derived information;
- C2/C4 fairness requires a material architecture change not represented by the frozen conditions;
- the resource meter cannot observe a causally material resource class;
- deterministic source verification would require learner training or experiment-like execution not covered by its authority;
- the research parent moves;
- the implementation head moves after a review PASS;
- a requested action would merge, deploy, publish, spend hosted/paid compute, connect to a protected system, or mutate provider/credential/ruleset/visibility state.

## 10. Explicit non-authorization

This handoff contract does not itself grant I0, I1, E0, or P0 authority.

It does not authorize implementation, test execution, learner-state updates, model training, experiment execution, paid/hosted compute, merge, deployment, publication, provider/credential/ruleset changes, repository-visibility changes, or protected-system connection.

It defines the minimum bounded source lane to open **if and when** Patrick explicitly authorizes that transition.
