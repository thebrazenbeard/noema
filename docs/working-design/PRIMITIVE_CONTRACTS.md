# Noema primitive computational contracts

Status: **BRAINSTORMING / CONTRACT DRAFT / NOT AN APPROVED IMPLEMENTATION**

## Purpose

The reduced Noema theory currently proposes five conceptual primitives:

1. provenanced signal flow;
2. generative structure;
3. valence / concern;
4. competition / selection;
5. plasticity across timescales.

This document makes them falsifiable enough to challenge. These are behavioral/computational contracts, not software interfaces or implementation choices.

---

## P1 — Provenanced signal flow

### Allowed inputs

- temporally ordered external sensory measurements;
- proprioceptive measurements;
- interoceptive/viability measurements;
- introspective/metacognitive-access signals where explicitly admitted by the developmental contract;
- issued motor/action commands;
- internally generated simulation/replay signals when such mechanisms are active.

### Allowed retained state

Only enough transient state to preserve:

- temporal order/duration;
- raw computational origin/channel;
- synchronization needed to compare issued action with subsequent experience.

Long-term meaning belongs in learned structure, not the signal interface.

### Allowed outputs/effects

- current signal packets/streams available to learning/modeling;
- motor/action commands to the environment;
- efference copy of issued actions;
- raw provenance markers sufficient to prevent observation, simulation, recall, and action-origin channels from silently collapsing.

### Forbidden semantic leakage

P1 must not supply:

- object segmentation or object IDs;
- agent/self labels;
- causal labels;
- absolute world coordinates;
- semantic source names such as `memory`, `belief`, `desire`, or `imagination` as human concepts;
- preinterpreted pain, threat, ownership, affordance, or goal categories.

Raw source identity is computational provenance only.

### Ablation expectations

- remove temporal order: temporal prediction, persistence, causal sequencing, and memory chronology should degrade sharply;
- remove efference access: self/body discovery, controllability learning, and intervention-sensitive causation should degrade;
- collapse all raw origin channels: source/mode discrimination should fail or become substantially harder.

### Developmental capabilities primarily enabled

- temporal regularity;
- sensorimotor contingency;
- later self/world distinction;
- source-aware memory and simulation;
- intervention learning.

---

## P2 — Generative structure

### Allowed inputs

- selected current signals from P1;
- active learned structures;
- current action/efference state;
- selected recalled traces;
- candidate bindings/operators;
- uncertainty and provenance associated with active hypotheses.

### Allowed retained state

- continuous/distributed predictive representation;
- optional explicit latent-process hypotheses;
- learned state-transition/constraint structure;
- competing hypotheses and confidence/uncertainty;
- dynamic bindings and reusable learned operators;
- approximate evidence/dependency links;
- temporal span and persistence estimates.

### Allowed outputs/effects

- predictions over future signals/states across multiple horizons;
- current-state inference under partial observation;
- action-conditioned/counterfactual rollouts;
- candidate explanatory structures for testing;
- expected consequences used by conative/action selection;
- influence traces sufficient for selective revision/ablation.

### Forbidden semantic leakage

P2 must not begin with:

- fixed `OBJECT`, `AGENT`, `SELF`, `CAUSE`, `GOAL`, `BELIEF`, `OWNER`, `CONTAINER`, etc. node/edge types;
- stable environment entity IDs;
- pretrained semantic embeddings containing the target ontology;
- a privileged parser that turns raw experience into human concepts;
- fixed object slots as the only representation;
- a graph assumed to be the ground-truth world structure.

Explicit structures are hypotheses, not facts.

### Ablation expectations

- remove persistent learned structure: no durable world model, transfer, planning, or identity continuity;
- remove competing hypotheses/uncertainty: premature certainty and failure under ambiguous observation;
- remove reusable binding/operator structure: abstraction, relational transfer, mentalization, analogy, and later language should degrade;
- remove counterfactual rollout: planning/intervention choice should degrade while passive prediction may remain.

### Developmental capabilities primarily enabled

- object/whole formation;
- persistent identity;
- spatial mapping;
- causal modeling;
- other-agent modeling;
- abstraction/analogy;
- planning/counterfactual reasoning;
- self-model formation.

---

## P3 — Valence / concern

### Allowed inputs

Innately:

- physical/cognitive viability deviation;
- primitive positive/negative directional pressure tied to viability;
- possibly minimal exploration/information pressure only to the extent needed to bootstrap learning.

Developmentally:

- learned predictions about consequences;
- learned concern structures consolidated through experience;
- current interoceptive and cognitive state;
- remembered outcomes and commitments.

### Allowed retained state

- multiple active concerns over potentially different horizons;
- learned persistence/inertia of preferences/commitments;
- context-sensitive consequence associations;
- provenance/history of learned concern formation sufficient for later revision.

### Allowed outputs/effects

- directional evaluation of predicted future states;
- pressure on allocation/action selection;
- salience contribution;
- data for learning trade-off/arbitration policies.

### Forbidden semantic leakage

P3 must not supply:

- high-level goals, moral values, personality, social preferences, obedience, curiosity-as-a-master-reward, or relationship semantics;
- a fixed global utility function encoding permanent exchange rates among concerns;
- direct changes to epistemic belief confidence because an outcome is desirable or undesirable.

### Ablation expectations

- remove primitive valence: the learner may predict but lacks endogenous directional reason to preserve viability or prefer one consequence;
- freeze learned concerns: higher-order preference development and individuality should fail;
- allow direct valence-to-belief confidence: wishful-belief pathology should appear in adversarial tests.

### Developmental capabilities primarily enabled

- endogenous preference formation;
- learned drives;
- sustained plans/commitments;
- value-sensitive action;
- social concern development;
- self-directed development.

---

## P4 — Competition / selection

### Allowed inputs

- candidate hypotheses and their evidence/confidence;
- candidate simulations/plans/actions;
- active concern/valence effects;
- uncertainty/information value;
- resource cost and current compute/memory budget;
- anomaly/residual pressure;
- learned allocation/arbitration policy.

### Allowed retained state

- learned context-sensitive allocation policy;
- learned conative arbitration policy;
- short-lived competition state;
- calibration history about which allocation/choice policies produce useful outcomes.

### Allowed outputs/effects

- allocate compute/attention among signals, memories, hypotheses, simulations, and unresolved anomalies;
- retain/prune competing candidate structures under resource limits;
- choose when additional evidence/intervention is worth its cost;
- select an executable action/policy under bounded time;
- decide which structures receive consolidation/revalidation resources.

### Forbidden semantic leakage

P4 must not contain:

- fixed semantic salience maps;
- hard-coded high-level task priorities;
- a central interpreter that "understands" all subsystem content;
- permanent designer-chosen utility weights defining mature behavior;
- a pathway by which preferred outcomes directly raise world-model confidence.

### Ablation expectations

- remove allocation: combinatorial/resource explosion or indiscriminate processing should occur;
- remove action arbitration: model may simulate but fail to act coherently;
- remove exploration/diversity floor: self-sealing attention/proposal lock-in should increase;
- freeze allocation policy: meta-learning of attention/investigation strategy should fail.

### Developmental capabilities primarily enabled

- attention/salience development;
- active information seeking;
- bounded planning;
- decision-making under competing concerns;
- selective memory/consolidation;
- anti-self-sealing exploration.

---

## P5 — Plasticity across timescales

### Allowed inputs

- prediction/intervention residuals;
- actual outcomes of actions;
- evidence/confidence changes;
- influence/provenance traces from implicated structures;
- accepted/rejected proposal history;
- allocation/arbitration outcomes;
- anomaly debt and revalidation results;
- memory/use/recency patterns.

### Allowed retained state

- fast parameter/adaptation state;
- medium-term episodic/structural changes;
- slow consolidated representation;
- proposal-generation policy;
- allocation/arbitration learning parameters;
- bounded metaplastic parameters controlling when/how future learning occurs.

### Allowed outputs/effects

- revise learned parameters;
- create/retire/split/merge latent structures;
- create/remove/rebind learned operators/dependencies;
- alter confidence and temporal scope;
- consolidate/reopen/forget;
- revise proposal policy;
- revise allocation and conative arbitration policy;
- alter bounded learning rates/thresholds/strategies through metaplasticity.

### Forbidden semantic leakage

P5 must not contain category-specific edit rules such as:

- `co-movement -> create object`;
- `autonomous motion -> create agent`;
- `controllable -> self`;
- `precedence -> cause`;
- `negative valence -> pain concept`;
- task-specific solution templates.

It also must not permit unconstrained arbitrary self-rewrite merely because metaplasticity exists.

### Ablation expectations

- remove fast plasticity: ordinary online learning collapses;
- remove structural plasticity: model can tune parameters but cannot discover new reusable organization;
- remove slow consolidation: catastrophic forgetting/ephemeral learning should dominate;
- remove reopening: mature false beliefs become difficult or impossible to correct;
- remove metaplasticity: the learner can learn facts but not improve its evidence-gathering/hypothesis-generation/arbitration strategies.

### Developmental capabilities primarily enabled

- learning from experience;
- object/self/agent/causal structure discovery;
- continual learning;
- learning-to-learn;
- selective forgetting;
- self-correction;
- self-development.

---

# Cross-primitive constraints

## C1 — Epistemic/conative separation

P3 may influence what P4 chooses to investigate or act upon. P3 may not directly increase/decrease P2 confidence in a world hypothesis.

Evidence from the resulting investigation may legitimately change P2 through P5.

## C2 — No semantic privilege through initialization

A primitive passes its contract only if initialization/pretraining does not already contain the target concepts being claimed as developmental achievements.

## C3 — Internal hypothesis identity is not world identity

P2 may use persistent internal handles for local revision and memory. P1 may not supply stable world IDs, and P2 must treat referential continuity as learned/uncertain.

## C4 — Consolidated is not immutable

P5 may reduce learning rate and increase default confidence/persistence for well-supported structure, but contradictory evidence must remain able to accumulate and reopen it.

## C5 — Distributed representation remains legal

P2/P5 must not force all useful phenomena into explicit factors/operators. Explicit structure must earn itself against a distributed baseline.

## C6 — Bounded resources are part of the experiment

P4 must operate under explicit finite compute/memory budgets. Unlimited search would hide the tractability problem rather than solve it.

# Capability coverage check

The five primitives together currently appear necessary for the main developmental graph:

- temporal prediction: P1 + P2 + P5;
- sensorimotor contingency: P1 + P2 + P5;
- object/whole formation: P2 + P5, constrained by P1 anti-leakage;
- persistent identity: P1 + P2 + P5;
- body/self discovery: P1 + P2 + P5;
- causal intervention: P1 + P2 + P4 + P5;
- agent modeling: P2 + P5;
- memory continuity: P2 + P4 + P5;
- preference/drive formation: P3 + P4 + P5;
- curiosity/information seeking: P2 + P3 + P4 + P5;
- error diagnosis: P2 + P4 + P5;
- transfer/abstraction: P2 + P5;
- planning: P2 + P3 + P4;
- learning-to-learn: P2 + P4 + P5;
- self-directed development: all five.

No obvious developmental target currently requires a sixth conceptual primitive.

# Current falsification target

Before treating the five-primitive reduction as a design foundation, challenge it with synthetic cases designed to expose a missing primitive.

The most useful tests should ask whether the system can fail in ways that cannot be repaired by changing only:

- signal provenance;
- learned generative structure;
- valence/concerns;
- selection/allocation;
- plasticity.

If a recurring capability requires a genuinely new kind of computation rather than a specialization/composition of these five, the primitive set is incomplete.

The strongest candidates to challenge first are:

- episodic reconstruction over long delays;
- nested other-mind reasoning;
- compositional analogy;
- durable commitment under changing short-term valence;
- recovery from a deeply wrong consolidated ontology.
