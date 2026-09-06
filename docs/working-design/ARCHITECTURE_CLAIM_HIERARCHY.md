# Noema architecture claim hierarchy

Status: **BRAINSTORMING / CONSOLIDATION AUDIT / NOT AN APPROVED IMPLEMENTATION**

## Purpose

Apply the four-level discipline from `OBJECTIVE_REEXAMINATION_2026-09-06.md` to the current design so mechanism-level ideas stop silently inheriting architectural authority.

Levels:

- **L1 — target capability:** what Noema must demonstrably be able to do.
- **L2 — developmental/evidential constraint:** what may be supplied, what must be learned, and what evidence counts.
- **L3 — candidate computational requirement:** a type of state/computation that currently appears necessary across capabilities but remains falsifiable.
- **L4 — candidate mechanism / experiment:** a concrete realization or test that has not earned foundational status.

A claim may span levels, but the strongest architectural authority it receives is the highest level justified by evidence, not the level implied by its document title.

## L1 — target capabilities

These survive the objective review as direct project goals.

### Persistent developmental learning

Noema should change from experience while retaining useful prior learning across time.

Evidence requirements include delayed recall, continual adaptation, changed later behavior after novel experience, and resistance to catastrophic forgetting.

### Predictive world/self modeling

Noema should form revisable expectations about its environment and its own relevant state, including consequences of possible actions.

Prediction is not sufficient for intelligence, but the ability to anticipate and revise is a target capability.

### Uncertainty-sensitive behavior

Noema should preserve uncertainty when evidence is insufficient, revise confidence when evidence changes, and act appropriately when certainty is unavailable.

No specific internal probability representation is required by this target.

### Causal/intervention learning

Noema should learn when interventions change consequences in ways that distinguish competing explanations.

The target is behaviorally demonstrated causal competence, not possession of a human-authored `CAUSE` symbol.

### Reusable representation and abstraction

Noema should transfer learned structure across changed surface form, recombine learned relations, and eventually support analogy/metaphor-like generalization.

### Reusable skill learning

Repeated successful behavior should be able to become efficient context-sensitive competence rather than requiring full planning from scratch every time.

### Temporal abstraction

Noema should learn useful organization over multiple timescales: events, episodes, procedures, routines, projects, and longer contexts where evidence supports such structure.

### Delayed credit assignment

Noema should learn from consequences that appear after intervening time/events and selectively revise the earlier actions, beliefs, or strategies that materially contributed.

### Memory and historical continuity

Noema should retain attributable experience, distinguish past from present interpretation, selectively consolidate, forget, and reopen prior learning.

### Motivation and learned concerns

Noema should eventually develop persistent action-relevant preferences/concerns/commitments that are shaped by developmental history rather than only by a fixed designer reward table.

### Planning and robust action

Noema should compare possible futures, choose actions, maintain plans over time, and sometimes act robustly without resolving all uncertainty.

### Other-agent modeling and social learning

Noema should learn individual-specific histories, source reliability, differing information, likely behavior, and eventually richer mentalization/empathic adaptation.

### Grounded communication

Noema and Patrick/other agents should increasingly coordinate through learned signals whose use depends on shared world, history, context, correction, source attribution, and uncertainty rather than inherited semantic tables.

### Meta-learning and self-correction

Experience should be able to change not only beliefs but aspects of evidence gathering, allocation, hypothesis formation, confidence behavior, and learning strategy.

### Initiative / information seeking

Consequential uncertainty, anomaly, opportunity, learned concern, or capability gap should sometimes produce action/investigation without an external instruction naming the exact response.

## L2 — developmental/evidential constraints

These constrain capability claims but should not be mistaken for a cognitive module list.

### Explicit-prior attribution

Use the weakest useful priors consistent with tractable learning, but do not treat weaker structure as intrinsically superior.

Any supplied inductive bias or transducer capability must be explicit, independently testable where practical, and excluded from claims of what Noema learned itself.

### No hidden semantic answer injection

Do not supply evaluator-known object IDs, agent IDs, causal labels, self labels, truth labels, semantic roles, stable entity identity, privileged world coordinates, or other target answers while later crediting Noema for discovering them.

### Transducer attribution

A sensor/transducer may solve lower-level transformation problems. Whatever it solves is supplied capability, not a developmental achievement.

### Provenance/source integrity

Learner-visible streams need enough raw origin/timing separation that observation, issued action, replay/simulation, communication, and other materially distinct computational sources do not silently collapse.

Human semantic interpretations of those sources remain learnable.

### Epistemic/conative firewall

Desirability may influence attention, investigation, and action. It may not directly manufacture evidential confidence.

### Evidence before architecture claims

Acquisition, intervention, transfer, ablation, calibration, and resource-fair comparison are stronger evidence than decoder/readout interpretability alone.

### Bounded resources

Noema is a finite learner. Compute, memory, search, deliberation, and hypothesis retention must be tested under declared resource limits.

### Continual/streaming evaluation

Core developmental claims should be tested online where relevant rather than only through offline batch refitting.

### No experiment-to-architecture promotion

A benchmark may isolate one property without dictating the mature architecture used to solve it.

### Human teacher is evidence, not oracle

Patrick's communication and correction may be highly informative but should remain fallible, scoped evidence rather than a privileged belief-write channel.

### Diagnostics are not cognition

Operator-facing interpretation and visualization must remain separate from Noema's own learned communication and learner-visible state.

## L3 — candidate computational requirements

These currently look broadly necessary, but the exact decomposition may change.

### Persistent revisable state

Some state must survive immediate input and be changed by later evidence without requiring complete reconstruction from an external transcript.

### Predictive/generative capacity

Some machinery must relate current/past state and possible action to expected future experience. It need not be one monolithic world model.

### Uncertainty representation

The system needs behaviorally meaningful ways to avoid false point certainty and preserve materially different possibilities when they matter.

This does not yet establish explicit hypothesis populations or exact Bayesian distributions.

### Multi-timescale plasticity

Fast adaptation, durable learning, consolidation, reopening, and long-run stability likely require more than one effective learning timescale.

The physical implementation may or may not use separate stores/modules.

### Finite-resource allocation

Something must determine which signals, memories, simulations, uncertainties, and actions receive limited processing resources.

This does not establish one universal attention/selection algorithm.

### Action-conditioned evaluation

The system needs a way to distinguish passive expectation from consequences conditional on issued action and later compare possible actions.

### Compositional/reusable binding capacity

Some form of reusable relational composition appears necessary for transfer, nested agent models, analogy, planning, skills, and grounded language.

The implementation need not be a graph, symbolic relation table, or slot architecture.

### Local enough credit assignment

Learning must be able to change implicated knowledge/strategies without indiscriminately rewriting everything.

The exact provenance/influence mechanism remains open.

### Model-family inadequacy detection

The learner needs some operational route to detect that its current representational/explanatory family is collectively failing, rather than always crowning the least-bad current candidate.

This need not appear as an explicit `NONE_OF_THE_ABOVE` variable.

### Contextual bounded cognition

The system must stop spending resources when further cognition is unlikely to justify its cost and must be interruptible by materially new evidence/state changes.

A universal loop counter is not required.

### Learned efficient control/skills

There must be some route by which repeated successful action becomes cheaper/reusable while remaining context-sensitive and revisable.

### Temporal chunking/abstraction

The system likely needs learned structure that can represent and operate over temporal organization above single-step transitions.

### Long-delay dependency/credit support

Some retained state or trace must allow later outcomes to influence earlier implicated behavior/structure over meaningful delays.

### Valuation distinct from epistemic support

Some states/futures must become action-relevant in a way that is not identical to whether they are believed likely.

Whether primitive cognitive self-preservation belongs here remains explicitly unresolved.

## L4 — candidate mechanisms and experiments

The following are useful research artifacts but remain replaceable.

### DGFW

Dynamic Generative Factor Workspace is a hybrid candidate realization, not Noema's definition.

### Continuous substrate + latent-process hypotheses

A promising representation scheme, not established anatomy.

### Graph-like slow binding layer

Potentially useful for locality, ablation, and compositional reuse; must beat fair distributed alternatives and representation-mismatch controls.

### Learned reusable operators

A plausible path to relation abstraction. The general requirement is reusable composition; operator form remains provisional.

### EGSS / RGSS

Evidence-guided or residual-guided structure search is one candidate learning strategy. Search may ultimately be implicit/distributed or realized differently.

### Two-timescale soft-to-structural search

A tractability hypothesis, not a cognitive law.

### Bounded explicit hypothesis population

A candidate uncertainty mechanism. It is unnecessary if another bounded representation preserves relevant disagreement/calibration and wins on cost/performance.

### Hypothesis genealogy

Potentially valuable bookkeeping if explicit hypotheses earn a role. Genealogy is not an architecture requirement in that literal representation.

### Multidimensional confidence fields

Useful evaluator dimensions; native dedicated fields remain optional unless experiments demonstrate they are necessary.

### Anomaly debt / reopenable consolidation machinery

A promising strategy for preserving unresolved contradictory evidence while maintaining stability. The underlying L3 requirement is revisable durable learning, not a specific debt counter.

### N_min

Literal minimum hypothesis-loop count is demoted. Evidence maturity is the stronger design principle. A count may be an experimental control, debugging aid, or temporary engineering safeguard.

### N_max

A fixed universal count is also not foundational. Contextual resource-bounded deliberation is the L3 requirement.

### Explicit epistemic control policy categories

`think / observe / intervene / ask / retrieve / simulate / act / defer` are useful evaluator descriptions of possible behavior. They should not automatically become eight hard-coded internal action classes.

### Experiment A

A narrow falsifier for calibrated ambiguity and intervention-driven revision under streaming bounded learning.

It does not establish Noema's mature representation.

### Experiment B

A follow-on falsifier for active epistemic intervention choice after A succeeds.

### Noema Console layout

The four-region UI is a practical candidate interface. The enduring L2 requirement is information-flow separation among learner-visible world/communication events, operator controls, and diagnostics.

## Document-level interpretation guide

Current working-design documents should be read according to their strongest justified role:

- `FOUNDATION.md` — primarily L1/L2 direction; implementation claims inside remain provisional.
- `INTELLIGENCE_CRITERIA.md` — L1 capability/evaluation inventory.
- `DEVELOPMENTAL_CONTRACT.md` — primarily L2.
- `DEVELOPMENTAL_CAPABILITY_GRAPH.md` — L1 dependency hypotheses with some L3 implications.
- `PREDICTIVE_SUBSTRATE_STRESS_TEST.md` — L3 hypothesis analysis.
- `FUNCTIONAL_CORE_STRESS_TEST.md` — L3 functional decomposition, not established primitives.
- `MINIMAL_COMPUTATIONAL_PRIMITIVES.md` — demoted from primitive claim to L3 reduction hypothesis.
- `PRIMITIVE_CONTRACTS.md` — provisional L3 contracts useful for falsification; names do not establish irreducibility.
- `IMPLEMENTATION_FAMILY_COMPARISON.md` — L4 comparison of realization families.
- `DGFW_STRESS_TEST.md` — L4 attack on one candidate realization.
- `INDUCTIVE_BIAS_BOUNDARY.md` — L2, with the correction that minimality is not purity.
- `FACTOR_FORMATION_CRITERIA.md` — L4 mechanism hypothesis; residual-only claims superseded where inconsistent.
- `RESIDUAL_GUIDED_STRUCTURE_SEARCH.md` — L4 historical mechanism path; superseded where EGSS broadens it.
- `EVIDENCE_GUIDED_STRUCTURE_SEARCH_REVISION.md` — L4 mechanism correction.
- `TWO_TIMESCALE_STRUCTURE_SEARCH.md` — L4 tractability hypothesis.
- `LATENT_PROCESS_REPRESENTATION.md` — L4 representation hypothesis.
- `GENERIC_BINDING_OPERATOR.md` — L4 realization of the L3 compositionality requirement.
- `EPISTEMIC_CONATIVE_ARBITRATION.md` — L2 firewall plus L3/L4 decision hypotheses.
- `REOPENABLE_CONSOLIDATION.md` — L3 problem statement with L4 candidate machinery.
- `BOUNDED_HYPOTHESIS_POPULATION.md` — L4 uncertainty realization.
- `HYPOTHESIS_MATURATION_GATE.md` — L4; literal-loop maturation is no longer the preferred general principle.
- `MODEL_INADEQUACY_AND_BELIEF_MATURATION.md` — L3 inadequacy requirement mixed with L4 maturation machinery; interpret accordingly.
- `EPISTEMIC_CONTROL_POLICY.md` — L3 bounded-cognition problem plus L4 descriptive policy classes.
- `EXPERIMENT_A_DESIGN.md` and related A documents — L4 falsification program.
- `COMMUNICATION_INTERFACE.md` — primarily L1/L2 communication requirement/interface boundary, implementation details L4.
- `COMMUNICATION_DEVELOPMENTAL_PROGRAM.md` — L1 developmental progression/evaluation program.
- `TEACHER_DEPENDENCE_AND_EPISTEMIC_AUTONOMY.md` — L2 safeguard.
- `OPERATOR_CONSOLE_SPEC.md` — L4 UI realization plus strong L2 information-boundary requirements.
- `INTERACTION_EVENT_CONTRACT.md` — primarily L2 information-flow contract.
- `DIAGNOSTIC_INTERPRETER_BOUNDARY.md` — primarily L2.

## Promotion rule

A candidate should move from L4 toward L3 only when multiple materially different realizations are tested and failure repeatedly tracks the absence of the underlying computation rather than the chosen implementation.

A claim should move from L3 toward L2/L1 only when it is better understood as a constraint or target rather than architecture.

The project should prefer demotion over promotion when evidence is ambiguous.

## Immediate consequence

Future design notes should identify their intended level near the top of the document.

This is not paperwork for its own sake. It is a guard against the project slowly converting vocabulary into anatomy.