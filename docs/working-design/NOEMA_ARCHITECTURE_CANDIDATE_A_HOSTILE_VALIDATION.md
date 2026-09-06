# Noema Architecture Candidate A — Hostile Design Validation

Status: **BRAINSTORMING / HOSTILE DESIGN REVIEW / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Subject: `NOEMA_ARCHITECTURE_CANDIDATE_A.md`

## Review rule

This review asks a narrower question than empirical validation:

> Does Candidate A contain a credible, non-circular computational path for every current Noema requirement without violating the developmental/evidential constraints?

Ratings:

- **COVERED** — the architecture names a coherent responsibility and information path without obviously smuggling the target answer.
- **CONDITIONAL** — a plausible path exists, but a key realization or anti-cheating condition remains unresolved.
- **OPEN GAP** — the current architecture does not yet contain enough machinery to claim a functioning concept for this requirement.

A `COVERED` design rating is not evidence that the implemented system will learn the capability.

## L1 target-capability audit

| L1 target | Rating | Hostile finding |
| --- | --- | --- |
| Persistent developmental learning | COVERED | Fast recurrent learning + episodic retention + reopenable slow consolidation gives a coherent multi-timescale path. Late-life plasticity remains an empirical falsifier. |
| Predictive world/self modeling | CONDITIONAL | World-state prediction is central. A developmental route to an explicit or implicit self-model is not yet sufficiently specified; Candidate A only protects the distinction between temporary mode and durable learned state. |
| Uncertainty-sensitive behavior | COVERED | Bounded predictive population + fallible calibration + robust action/defer path directly addresses this target. Population realization is still replaceable. |
| Causal/intervention learning | COVERED | Action-conditioned prediction, command/outcome separation, intervention evidence, influence learning, and Experiment A provide a coherent path without an innate `CAUSE` label. |
| Reusable representation and abstraction | CONDITIONAL | Slow reusable structure and generic structural expansion are plausible, but the exact compositional/binding substrate is intentionally unresolved. |
| Reusable skill learning | CONDITIONAL | Candidate A specifies learned temporally extended policies and context-sensitive invocation, but skill discovery/termination/precondition learning remains mechanism-level open work. |
| Temporal abstraction | CONDITIONAL | The architecture explicitly requires learned boundaries/chunks rather than evaluator-supplied milestones. The discovery criterion is plausible but not yet computationally sharp enough. |
| Delayed credit assignment | CONDITIONAL | Influence traces and intervention/counterfactual preference avoid pure chronology, but the actual credit estimator over long horizons is unresolved. |
| Memory and historical continuity | COVERED | Episodic evidence, slow consolidation, provenance, selective retrieval/forgetting, and reopening form a coherent memory architecture. Distortion remains a required falsifier. |
| Motivation and learned concerns | OPEN GAP | Separation of concern from belief is strong, and multi-need/homeostatic families remain available, but the architecture does not yet explain how higher persistent concerns develop without reducing to a designer reward table. |
| Planning and robust action | CONDITIONAL | Action-conditioned prediction, simulation, skill invocation, and robust action under uncertainty exist, but there is no sufficiently concrete long-horizon planning/composition process yet. |
| Other-agent modeling and social learning | OPEN GAP | Source reliability and teacher fallibility are covered, but there is not yet a complete developmental computational path from recurrent observations to individual continuity, differing beliefs, and richer mentalization. |
| Grounded communication | CONDITIONAL | The signal/teacher/diagnostic boundaries are strong and the developmental program exists, but Candidate A does not yet show how its representation/composition machinery will support open-ended syntax/pragmatics at scale. |
| Meta-learning and self-correction | COVERED | Meta-control parameters, proposal/retrieval/allocation policies, calibration, and slow learning are explicitly learnable/revisable. |
| Initiative / information seeking | CONDITIONAL | The architecture can select inquiry/intervention/asking based on consequential reducible uncertainty and concern, but full endogenous initiative depends on the unresolved motivation layer. |

### L1 verdict

Candidate A is **not yet a complete full-Noema architecture**.

The two strongest full-architecture gaps are:

1. developmental motivation / higher concern formation;
2. other-agent/self-model development beyond source tracking and mode separation.

The strongest conditional cluster is shared:

> **compositional temporal structure** — reusable abstraction, skills, long-horizon planning, grounded communication, and delayed credit all depend on a sufficiently general learned composition/chunking substrate that has not yet been made concrete.

That is a more important remaining architecture problem than adding more named cognitive modules.

## L2 developmental/evidential audit

| L2 constraint | Rating | Hostile finding |
| --- | --- | --- |
| Explicit-prior attribution | COVERED | Candidate explicitly permits useful priors while requiring declaration/attribution. |
| No hidden semantic answer injection | COVERED | Event boundary forbids privileged IDs/labels/coordinates and structural proposals remain semantically unnamed. |
| Transducer attribution | COVERED | Lower-level preprocessing is permitted but must be logged as supplied capability. |
| Provenance/source integrity | COVERED | Observation, efference, sensed consequence, communication, retrieval, and simulation are source-distinct. |
| Epistemic/conative firewall | COVERED | Valuation can allocate attention/action but cannot directly write evidential confidence. |
| Evidence before architecture claims | COVERED | Candidate explicitly remains replaceable and binds progression to F0/F1/F2, transfer, ablation, calibration, and fair baselines. |
| Bounded resources | COVERED | Model population, memory, proposal, deliberation, and cognition all require declared finite budgets. |
| Continual/streaming evaluation | COVERED | First slice is explicitly online/streaming; no full-history batch refit is assumed. |
| No experiment-to-architecture promotion | COVERED | Experiment A and structural machinery remain ablated candidate mechanisms. |
| Human teacher is evidence, not oracle | COVERED | Communication and source reliability are learned/fallible. |
| Diagnostics are not cognition | COVERED | Operator interpreter remains read-only and outside learner-visible state. |

### L2 verdict

No blocking L2 violation was found on paper.

The main implementation risk is **semantic leakage through convenience engineering** rather than a contradiction in the architecture itself. F0 remains mandatory before interpreting any later success.

## L3 computational-requirement audit

| L3 requirement | Rating | Hostile finding |
| --- | --- | --- |
| Persistent revisable state | COVERED | Recurrent belief state + durable slow state. |
| Predictive/generative capacity | COVERED | Central substrate directly generates passive/action-conditioned forecasts. |
| Uncertainty representation | COVERED | Bounded population of continuous model states is a concrete Candidate A realization. |
| Multi-timescale plasticity | COVERED | Fast learning, episodic retention, slow consolidation, reopening, late-life probes. |
| Finite-resource allocation | COVERED | Meta-control allocates cognition under explicit cost/budget. |
| Action-conditioned evaluation | COVERED | Issued action and realized consequence are separate, with forecast comparison. |
| Compositional/reusable binding capacity | OPEN GAP | Candidate A refers to reusable operators/bindings but does not yet specify a general computational substrate capable of relational reuse without hard-coded ontology. |
| Local enough credit assignment | CONDITIONAL | Influence traces/local revision are required but the exact mechanism is not yet strong enough to demonstrate locality over long delays. |
| Model-family inadequacy detection | COVERED | Absolute adequacy plus expansion trigger prevents least-bad-wins by construction. |
| Contextual bounded cognition | COVERED | Expected value of further cognition + hard safety budgets + interruption. |
| Learned efficient control/skills | CONDITIONAL | Storage/invocation path exists; skill discovery/composition remains tied to the open compositional-temporal gap. |
| Temporal chunking/abstraction | CONDITIONAL | Required to be learned, but the generic boundary/chunk discovery computation is not yet chosen. |
| Long-delay dependency/credit support | CONDITIONAL | Trace retention exists; causal influence estimation remains unresolved. |
| Valuation distinct from epistemic support | COVERED | Separate concern process/firewall is architectural, even though concern development is not solved. |

### L3 verdict

Candidate A binds most of the previously floating L3 requirements into an actual information-flow architecture.

One **genuine core architecture gap** remains:

> a general learned compositional-temporal representation capable of building reusable relations, chunks, skills, plans, and communication structures without being handed those boundaries or semantic roles.

This is now the highest-leverage architecture question.

## Hostile cross-cutting attacks

### Attack 1 — bounded population becomes decorative ensemble

Failure mode: all members learn the same effective model, so nominal multiplicity does not preserve meaningful structural uncertainty.

Required test:

- observationally equivalent environments where later interventions distinguish predictions;
- measure pre-intervention counterfactual diversity/calibration;
- compare against a single-model baseline;
- reject population machinery if it adds cost without preserving useful uncertainty.

Status: **survivable but empirical**.

### Attack 2 — structural expansion smuggles ontology

Failure mode: proposal operators encode the answer (`object`, `agent`, `cause`, fixed graph families) under generic names.

Required test:

- representation-mismatch worlds;
- out-of-family relations;
- alternate worlds where familiar regularities reverse;
- operator ablation and distributed baseline.

Status: **survivable if F0 + mismatch controls remain strict**.

### Attack 3 — absolute inadequacy is secretly evaluator knowledge

Failure mode: learner gets an implicit `your model is wrong` channel.

Required architecture rule:

- learner only receives ordinary predictive/intervention evidence;
- absolute adequacy diagnostics may be evaluator-side;
- learner-side expansion pressure must arise from its own prediction/calibration/transfer failure signals.

Status: **Candidate A wording must be interpreted this way.**

### Attack 4 — episodic memory becomes a hidden transcript oracle

Failure mode: unlimited exact replay defeats the intended persistent-learning problem.

Required test:

- bounded store;
- retrieval cost;
- selective encoding;
- no automatic full-history batch refit;
- replay ablation;
- contamination tests.

Status: **covered by the resource/memory contract**.

### Attack 5 — meta-controller becomes the real intelligence

Failure mode: a hand-coded controller contains the task logic while the learned model merely supplies scores.

Required rule:

- initial controller operations may be generic, but task-specific allocation, source reliability, confidence thresholds, inquiry policy, and strategy must be learnable/ablatable;
- evaluator should compare fixed versus learned meta-control.

Status: **conditional implementation risk**.

### Attack 6 — concern system becomes designer policy in disguise

Failure mode: the fixed reward/need specification already determines the mature agent's preferences.

Status: **real open architecture problem**.

The project should not solve this by merely renaming reward dimensions `drives`.

### Attack 7 — learned temporal abstraction is secretly curriculum segmentation

Failure mode: the teacher/environment marks episode/subgoal boundaries that become the learner's abstractions.

Required test:

- continuous streams without privileged boundaries;
- boundary perturbation;
- reversed/violated early curriculum regularities;
- transfer where useful chunks cross original episode boundaries.

Status: **real conditional risk tied to the compositional-temporal gap**.

### Attack 8 — self-monitoring becomes another privileged decoder

Failure mode: internal confidence/competence estimates are treated as inherently correct because they are internal.

Required test:

- separately score first-order task performance and second-order calibration;
- induce contexts where self-estimates are systematically wrong;
- require calibration learning rather than readout rationalization.

Status: **covered conceptually; empirical validation required**.

## F0/F1/F2 readiness

### F0

**DESIGN-READY.**

Candidate A has a clear learner-visible event boundary, provenance contract, transducer attribution, operator-plane separation, and diagnostic firewall.

### F1

**NEAR DESIGN-READY / IMPLEMENTATION DETAILS REQUIRED.**

The architecture now identifies what must exist:

- continuous recurrent probabilistic predictor;
- bounded uncertainty realization;
- persistent state;
- online update;
- minimal episodic/trace memory;
- resource accounting;
- late-within-run plasticity and regime-change tests.

Still required before an implementation plan:

- choose the smallest fair continuous recurrent model family;
- specify the bounded uncertainty/population update rule;
- specify memory/compute budgets and baseline parity;
- preregister predictive/calibration metrics.

These are implementation-design decisions, not missing architectural capabilities.

### F2

**NEAR DESIGN-READY / ONE ARCHITECTURE QUESTION REMAINS OPTIONAL.**

Experiment A can test Candidate A's uncertainty and intervention revision without first solving the full compositional-temporal gap.

The structural-expansion layer should remain an ablated variant. A simple continuous Candidate A should be allowed to win F2 without explicit graph-like structure.

## Overall verdict

### First-core architecture

Candidate A **passes hostile paper validation as a coherent first-core architecture candidate**, subject to normal implementation-design choices and empirical F0/F1/F2 falsification.

The first-core concept is sufficiently bound that further broad architecture brainstorming would now have diminishing returns compared with tightening the implementation-neutral F1/F2 contracts.

### Full Noema architecture

Candidate A **does not yet pass full-concept validation**.

Three architecture frontiers remain materially unresolved:

1. **general compositional-temporal structure learning** — likely the common substrate problem behind abstraction, skills, planning, communication, and delayed credit;
2. **development of persistent higher concerns/motivation** without merely installing a designer policy;
3. **developmental self/other modeling** beyond source tracking, mode separation, and simple reliability models.

Of these, the first is the highest-leverage next design target because it touches the largest number of L1/L3 gaps while remaining testable before mature social/motivational development.

## Recommendation

Do not add more standalone cognitive modules.

The next architectural design pass should attack exactly one question:

> **What is the weakest general-purpose learned compositional-temporal substrate that can represent reusable relational/process structure across prediction, memory, skills, planning, and communication without importing object/agent/role/subgoal ontology?**

Candidate A should remain stable everywhere else unless that pass exposes a contradiction.
