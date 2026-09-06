# PR31 online-learning contract reconciliation

Status: **PROVISIONAL PR-INTERNAL RECONCILIATION / SUCCESSOR ONLY / NOT R1 REMEDIATION**

Date: 2026-09-06

## Why this note exists

PR #31 acquired two independently produced online-learning state-transition drafts during concurrent work:

- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT_DRAFT.md`
- `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`

They are strongly convergent rather than conflicting, but leaving their relationship unstated would create an avoidable authority/precedence ambiguity.

A direct-edit attempt on the non-`_DRAFT` contract was initially rejected by GitHub with a stale-content `409`. No force or blind overwrite was attempted. After refreshing the exact blob, the non-`_DRAFT` contract was updated to ingest the independent draft's useful state-class, prequential, world/transducer, and comparator distinctions while preserving the independent draft as provenance. This is itself a useful concurrency check: the source-control precondition prevented a stale write from erasing intervening work.

## Shared conclusion

Both drafts independently require the same central discipline:

> **predictions must be fixed before scored outcomes are used for learning, and every learner-affecting mutation must have a declared causal order and persistence boundary.**

Both also agree that:

- prequential/test-then-train scoring is the correct default evidence discipline;
- replay is a strong L4 baseline, not architecture truth;
- replay sampling/insertion/order must be explicit and resource-accounted;
- optimizer/plasticity state can be causally part of learner persistence;
- base/candidate comparisons need a common pre-outcome causal frontier;
- probationary/slow machinery must not contaminate the baseline it is being scored against;
- scheduling that changes committed learning is part of the algorithm, not neutral infrastructure;
- checkpoint/restart claims require all causally relevant learner state;
- simple recurrent learners with and without replay remain mandatory rivals;
- none of this retroactively changes the frozen BT2 R1 subject.

## Distinct useful contributions and disposition

`ONLINE_LEARNING_STATE_TRANSITION_CONTRACT_DRAFT.md` contributed especially clear:

- prequential/test-then-train framing and research lineage;
- explicit plasticity, replay, probationary, interface-calibration, and stochastic state classes;
- world/transducer progression as a named phase;
- compact C0-C4 comparison framing;
- explicit reminder that exact online recurrent-gradient methods are comparators rather than obligations.

The material state-class, prequential, world/transducer, and comparator distinctions are now represented in the non-`_DRAFT` contract. The draft remains useful as independent convergence/provenance rather than as a competing authoritative document.

`ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md` contributes especially clear:

- separation of learner-committed state, learner-visible evidence, evaluator/world causal state, and evaluator bookkeeping;
- a logically authoritative committed state `C_t` without requiring one physical blob;
- evaluator-side immutable prediction tickets;
- explicit fast/slow promotion boundaries and non-retroactive evidence windows;
- schedule noninterference versus intentionally learner-causal scheduling;
- duplicate/delayed/reordered/replayed event treatment;
- crash-consistent checkpoint semantics;
- explicit representation-drift pressure on learned scope;
- claim ceilings and open seams.

`ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md` supplies the adversarial test layer for both.

## Provisional precedence inside PR #31

Until PR #31 is adjudicated, use this hierarchy:

1. `LEARNING_AND_TRAINING_RESEARCH_SYNTHESIS.md` — research pressure and recommendation;
2. `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT_DRAFT.md` — independent research draft/provenance;
3. `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md` — **provisional consolidated contract candidate**;
4. `ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md` — hostile falsification suite for the contract candidate.

This is only PR-internal working precedence. It is not merged architecture authority.

## Material unresolved seam

The reconciliation does not solve BT2's representation-drift problem for learned scope. The consolidated contract can prevent hidden scheduler/causal contamination, but a gate/candidate whose applicability depends on a changing latent representation still needs one of:

- representation-invariant scope;
- an explicit lawful remapping mechanism that does not use evaluator semantic correspondence; or
- ordinary-evidence scope relearning with detectable loss of applicability.

That remains a separate successor architecture problem rather than being papered over by update-order discipline.

## Recommendation

Keep the independent draft through PR review as provenance. Treat the non-`_DRAFT` contract plus the hostile attack as the current consolidation target. Any later duplicate cleanup should be a fresh-head reviewed source decision rather than an automatic deletion.
