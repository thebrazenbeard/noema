# Dynamic Generative Factor Workspace (DGFW) stress test

Status: **BRAINSTORMING / ADVERSARIAL DESIGN REVIEW / NOT AN APPROVED ARCHITECTURE**

## Hypothesis under attack

A hybrid Noema core could combine a continuous sensorimotor substrate with dynamically created latent hypotheses/factors, learned relations/bindings, an uncertain belief workspace, action-conditioned simulation, finite-resource allocation, multi-timescale persistence, learned valuation, and local plasticity/metaplasticity.

The design is attractive only if it does **not** smuggle the ontology Noema is supposed to discover.

## Attack 1 — `factor` may just mean `object slot`

If factors are spatially segmented, fixed-count, mutually exclusive slots, Noema has been biased heavily toward objecthood.

### Requirement

A factor must be a **general provisional explanatory unit**, not an object slot. Factors may overlap, nest, compete, disappear, split, merge, and represent non-object regularities such as motion, temporal pattern, location, body contingency, agent-specific hidden state, relation, strategy, or value.

No factor is guaranteed to correspond to one real-world entity.

## Attack 2 — the world may not factor cleanly

Fluids, fields, crowds, distributed textures, and coupled processes may resist discrete decomposition.

### Requirement

The continuous substrate remains first-class. Factorization is optional learned compression, not a mandatory representation of all experience.

If a phenomenon is predicted better as distributed state than as discrete factors, Noema should be allowed to leave it distributed.

## Attack 3 — factor creation can become hidden hand-coding

A designer could quietly define rules such as "spawn a factor when a contiguous region moves together," which would merely implement object discovery by hand.

### Requirement

Factor birth/split/merge/retirement criteria should be **domain-general**. Candidate triggers may include persistent residual prediction structure, reusable conditional dependence, transfer benefit, intervention stability, or compression gain—not semantic predicates such as spatial objecthood, agency, or causality.

These triggers remain hypotheses and must themselves be stress-tested.

## Attack 4 — predictive non-identifiability remains

Different factor structures can explain the same observations equally well.

### Requirement

Noema should tolerate plural live factorizations when evidence does not distinguish them. Structure should earn confidence through intervention, transfer, recombination, and long-horizon predictive usefulness rather than being forced into one canonical decomposition.

## Attack 5 — relation learning may be the whole intelligence problem in disguise

Saying "learn relations" is not a mechanism. If relation types are hand-authored, compositionality has been imported rather than learned.

### Requirement

The substrate must support the **capacity for dynamic binding** without supplying semantic relation types. Candidate learned relation structures should emerge from reusable transformations/dependencies among factors.

A relation may begin as an unnamed reusable operator/pattern and acquire stable meaning only through experience.

This is currently one of the hardest unsolved parts of the hypothesis.

## Attack 6 — role binding can still be smuggled in

Even if relation names are learned, predefining semantic roles such as AGENT, PATIENT, CONTAINER, OWNER, or BELIEVER would leak ontology.

### Requirement

Any role-like structure must be generic/dynamic. The system may support ordered or addressable binding positions as computation, but their semantics must be learned and transferable.

The implementation must demonstrate role permutation/generalization rather than memorizing fixed position meanings.

## Attack 7 — factor graph growth can explode

Open-ended hypothesis creation can generate combinatorial explosion.

### Requirement

Allocation, evidence strength, reuse, redundancy, and decay must constrain active and durable structure. Low-value hypotheses may remain transient or be forgotten. Competing structures should not all receive equal compute.

This is a functional reason allocation is essential, not merely an optimization.

## Attack 8 — local revision conflicts with shared neural features

If many factors depend on one shared encoder, changing the encoder can alter everything and defeat structural locality.

### Requirement

Use **different plasticity timescales** conceptually:

- rapid changes to active factor/belief state;
- medium-term episodic/relational learning;
- slower changes to shared representational machinery after broader evidence/consolidation.

This is a principle, not yet a commitment to any particular training method.

## Attack 9 — source/mode tags could themselves become semantic cheating

If states are born labeled `OBSERVATION`, `MEMORY`, `IMAGINATION`, `BELIEF`, `DESIRE`, the learner receives human epistemology for free.

### Requirement

Only **raw origin/provenance channels** are innate: external sensor stream, internal simulation stream, recalled trace, action command/efference stream, interoceptive stream, etc. The human concepts and reliability expectations associated with those sources are learned.

This parallels chronoception and efference-copy decisions already in the developmental contract.

## Attack 10 — workspace centralization may become a homunculus

A `workspace` can accidentally become a magical executive that understands all representations and decides everything.

### Requirement

The workspace may hold/rout active contestable content, but it must not contain a privileged interpreter. Selection, binding, confidence, and routing must be implemented through learnable/general mechanisms rather than a hand-authored central reasoner.

Direct subsystem communication remains allowed alongside shared workspace access.

## Attack 11 — learned valuation can become reward relabeling

If every factor eventually gets one scalar reward estimate, Noema has not gained rich wants or commitments.

### Requirement

Valuation should be able to attach multiple learned consequences/concerns to modeled states across different horizons. Action selection may still need a final arbitration, but the internal value structure should not be collapsed prematurely into one permanent scalar meaning.

## Attack 12 — self-modification can destroy the learner

Metaplasticity is needed for learning-to-learn, but unconstrained self-modification can corrupt memory, values, or update rules irreversibly.

### Requirement

Early metaplasticity should change bounded learning parameters/policies under evidence and support reversibility/comparison where possible. Arbitrary self-rewrite is not required for early intelligence and should not be confused with self-actualization.

## Attack 13 — continuous and factor representations may diverge

A hybrid system can become two incompatible minds: one continuous predictor and one explicit factor workspace.

### Requirement

Factors should remain causally grounded in and predictive of continuous experience. A factor must be testable by what observations/interventions it predicts. The continuous layer must also be able to receive top-down predictions/attention from active factors without those factors becoming unquestionable labels.

Bidirectional predictive accountability is required; a hand-authored translator is not acceptable as the source of semantics.

## Attack 14 — higher-order abstractions may not fit the same factor machinery

A relation such as "support prevents collapse" differs qualitatively from a visual candidate whole. A rigid factor format may privilege low-level world structure and fail at abstraction.

### Requirement

Factors/relations must be able to reference other learned factors/relations and operate at multiple temporal/spatial/abstract scales. The substrate must permit hierarchical or recursive composition without predefining a fixed ontology depth.

## Attack 15 — internal disagreement needs causal traceability

If several hypotheses contribute to a prediction/action, later error must be attributable enough to learn selectively.

### Requirement

Predictions and actions should retain a causal trace of which active hypotheses/relations materially influenced them. This trace need not be human-readable, but it must support intervention/ablation and local credit assignment.

## Stronger surviving DGFW

After stress-testing, the DGFW survives only in this constrained form:

- a **continuous sensorimotor substrate** remains available and can model unfactorized phenomena;
- **dynamic latent factors** are optional, overlapping, revisable explanatory hypotheses rather than object slots;
- factor structure is created/merged/split/retired through domain-general evidence pressures rather than semantic heuristics;
- **learned relational operators and dynamic binding** enable compositional reuse without pre-authored semantic roles;
- multiple competing factorizations may coexist under uncertainty;
- a workspace routes contestable active hypotheses but contains no privileged interpreter;
- raw source/provenance channels remain separable without human semantic labels;
- action-conditioned simulation grounds factors in predicted consequence;
- rapid factor-state learning is separated conceptually from slower shared-representation consolidation;
- allocation controls hypothesis growth and finite compute;
- valuation remains multi-concern/multi-horizon rather than a single permanent reward meaning;
- factor/continuous layers remain bidirectionally accountable through prediction and intervention.

## Verdict

**DGFW remains the strongest current architecture hypothesis, but it is not yet an architecture we should implement.**

The central risk is now very clear:

> Can generic structure-discovery and binding machinery create useful latent factors/relations without the designer quietly encoding objecthood, causality, agency, or semantic roles into the creation rules?

That is the make-or-break question.

## Minimal falsification target before broad implementation

Before attempting a full 3D developmental system, the architecture should eventually face a tightly controlled experiment in which:

1. the input contains only minimally interpreted temporal/sensorimotor features;
2. no object IDs or segmentation are supplied;
3. several incompatible decompositions initially explain the same stream;
4. later interventions distinguish the decompositions;
5. the learner must create/revise latent structure accordingly;
6. the learned structure must transfer to a new surface configuration;
7. ablating the learned factor/relation must specifically remove the transferred capability.

If DGFW cannot satisfy this without bespoke domain rules, it should be rejected before the project accumulates more architecture around it.
