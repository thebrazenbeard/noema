# T'kal-in-ket continuity red-team — Candidate A adjudication

Status: **BRAINSTORMING / CROSS-LANE ADJUDICATION / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Inputs:

- `NOEMA_ARCHITECTURE_CANDIDATE_A.md`
- `NOEMA_ARCHITECTURE_CANDIDATE_A_HOSTILE_VALIDATION.md`
- Draft PR #18: `TKAL_IN_KET_CONTINUITY_REDTEAM_2026-09-06.md`
- Draft PR #16 interface-developmental provenance work

## Executive result

The T'kal continuity pass does **not** break Candidate A's first-core architecture.

It does expose one material F0 boundary defect in the current wording and three genuine requirements inside already-open full-Noema frontiers.

Strongest correction:

> Candidate A currently risks conflating **exact evaluator provenance**, **supplied interface/transducer structure**, and **learner-available origin evidence** under the phrase `provenanced learner-visible event`.

That wording is too permissive. If implemented literally as semantic source tags, it could hand Noema parts of source monitoring, autobiography, speaker identity, or self/world distinction that later evaluations intend to credit as learned.

The T'kal pass therefore changes the architecture state in a narrow but real way: F0 provenance accounting must become multi-plane and transducer-aware before later self/continuity/source-learning evidence is valid.

## TKI-1 — adaptive cognitive hysteresis

### Finding

Temporary cognitive configuration must neither cling globally nor hard-reset blindly. Persistence, decay, latent recoverability, and reconstruction should adapt to recurrence, interference, and reconstruction cost.

### Candidate A comparison

Candidate A already says temporary mode should `decay, terminate, or be superseded` while durable competence survives. That establishes **separation**, but not an adaptive persistence policy.

Meta-control is learnable and resource-bounded, so there is a plausible carrier. However, nothing currently requires mode persistence/decay itself to be learned from transition statistics.

### Classification

**REQUIREMENT GAP — narrow L3 control requirement, non-breaking to first core.**

### Integration

Future mode-control design should satisfy:

> task-local configuration has a learned persistence/recoverability policy whose active influence is reduced when it interferes with current evidence/action, while useful reconstructible structure may remain latent when recurrence makes retention worthwhile.

This must not become a hand-coded personality reset rule.

### Falsifier disposition

Adopt TKI-1 largely as written, with an additional control:

- distinguish retained **competence** from retained **allocation/output bias**.

A learner that preserves fast reconstruction but stops irrelevant mode-driven behavior should count differently from one that either erases competence or keeps acting as though the old context is current.

## TKI-2 — preference laundering

### Finding

Repeated behavior in one recurring condition is insufficient evidence for a context-general preference or drive.

### Candidate A comparison

This pressure partially overlaps two existing protections:

- valuation is separate from belief;
- evidence maturity requires diversity, scope, contradiction exposure, and meaningful evidence opportunity rather than raw repetition.

But Candidate A's motivation layer is already an **OPEN GAP**, and it does not yet specify a promotion rule from state-conditioned valuation/action to durable concern/preference.

### Classification

**REQUIREMENT GAP inside the already-open motivation frontier + EVALUATION GAP.**

Not a first-core break.

### Integration

Any later concern/preference consolidation mechanism must preserve conditionality unless evidence supports broader scope.

A safe requirement is:

> Recurrence strengthens evidence only within the scope actually sampled. Global or identity-level preference requires evidence that generalizes across materially varied contexts, or an explicit learned model that keeps the preference conditional.

This is deliberately not a rule that preferences must be context invariant. A mature Noema may have stable conditional preferences.

### Falsifier disposition

Adopt TKI-2. Add a counterexample case where a genuinely global preference is expressed through different local behaviors so the evaluator does not equate behavioral sameness with preference stability.

## TKI-3 — agency-factor separation

### Finding

Initiation, causal influence, controllability, embodiment/sensorimotor coupling, joint control, and responsibility can dissociate and must not collapse into one scalar `selfness` signal.

### Candidate A comparison

Candidate A's hostile validation already marks richer self/other modeling as an **OPEN GAP**. Existing action/efference provenance and causal prediction are not enough to solve agency attribution.

The T'kal pass sharpens what the future self/other substrate must be able to represent: multiple relations that often correlate but can separate under mirroring, remote control, delegation, tools, and shared control.

### Classification

**REQUIREMENT GAP — full-Noema self/other frontier.**

Not a first-core break.

### Integration

Do **not** add innate English-named agency modules.

Instead require representational capacity for evidence to support distinct learned relations among current process, action issuance, predicted consequence, controllability, sensorimotor coupling, another agent's contribution, and later social/causal attribution.

A one-dimensional identity/self score is specifically disfavored unless it can be shown not to collapse these distinctions.

### Falsifier disposition

Adopt TKI-3 and extend it with a delegation case:

- Noema intentionally delegates an action to another agent, predicts the result, and later receives social credit/blame.

This separates `I caused via delegation`, `I directly controlled`, and `I physically enacted` without requiring predefined semantic labels.

## TKI-4 — two provenance planes / borrowed autobiography

### Finding

Exact evaluator lineage/event provenance must not automatically become learner-visible semantic source truth.

### Candidate A comparison

This is the strongest T'kal finding against the text as written.

Candidate A currently says every learner-visible event enters through a provenance-bearing envelope that may identify computational source classes such as:

- external observation;
- issued action/efference;
- sensed consequence;
- communication signal;
- retrieved memory;
- internal simulation.

It also says those source classes are not semantic interpretation.

That distinction is directionally correct but insufficient. A stable categorical source token can still solve part of the developmental problem even if its field name is opaque.

The interface lane independently found the same broader failure class: channel identity, message framing, ASR segmentation, pointer rays, session continuity, diagnostics, and replay behavior can all provide **developmental subsidy** without explicit semantic labels.

### Classification

**BOUNDARY LEAK / MATERIAL F0 CORRECTION REQUIRED.**

This is not a break of Candidate A's predictive-control thesis, but an implementation that exposed perfect semantic provenance under the current wording would fail Candidate A's own F0 standard.

### Required correction

Use at least three distinct accounting concepts:

1. **Evaluator ground-truth provenance** — exact lineage, simulator source, external sender, branch ancestry, replay origin, and experiment truth. This remains outside Noema.
2. **Supplied-capability / transducer descriptor** — evaluator-side record of framing, preprocessing, timing, modality partition, channel identity, segmentation, interface affordances, and operator exposure. This records developmental subsidies but is not automatically learner-visible.
3. **Learner-available origin evidence** — only cues legitimately available to Noema through its architecture/transducers, including whatever generic efference/introspective signals are explicitly declared as innate capacity. Semantic source attribution built from those cues remains learned and fallible.

Internal computation may of course route signals differently. The correction is about **what epistemic proposition those routes hand the learner** and what later capability claims may be made from them.

### Important nuance

Noema does need to avoid treating imagined, remembered, intended, and externally sensed content as freely interchangeable. The fix is **not** to erase all mode information.

The design question is attribution:

- generic self-generated/efference or memory-retrieval cues may be supplied architectural capacities if declared;
- a proposition equivalent to `this content is merely imagined and not observed reality` should not be credited as learned if an infallible architecture tag already answers it;
- external speaker identity or autobiographical ownership must remain no stronger than the learner-visible evidence actually supports.

### Falsifier disposition

Adopt TKI-4 and bind it to PR #16's hidden-subsidy audit.

A future F0 test should deliberately vary or remove stable channel labels while preserving the raw evidence needed for learning, then verify that source competence degrades or recalibrates in ways consistent with lost evidence rather than remaining perfect because a hidden route token still answers the question.

## TKI-5 — fission, encounter, and recombination

### Finding

Shared pre-fork memory does not uniquely determine token identity or justify collapsing post-fork autobiography. Evaluator process lineage and learner self-continuity must remain separate.

### Candidate A comparison

Candidate A explicitly leaves long-horizon self-model realization unsettled. Its representation-equivalence rule already rejects evaluator-preferred latent descriptions, which is compatible with evaluator neutrality about metaphysical identity.

But the current self/other frontier has not required multi-parent, forked, copied, restored, or recombined histories.

### Classification

**REQUIREMENT GAP + EVALUATION GAP in the full-Noema self-continuity frontier.**

Not a first-core break.

### Integration

The self-model substrate must not require one indivisible continuity token.

It must permit evidence-weighted relations that can diverge across:

- memory/history continuity;
- control/process continuity;
- learned disposition/value continuity;
- embodiment continuity;
- project/commitment continuity;
- source/causal lineage available to the learner.

These are evaluator descriptions, not proposed innate labels.

The evaluator should score prediction, attribution, calibration, correction, and contamination resistance rather than agreement with `same person` / `different person` metaphysics.

### Falsifier disposition

Adopt TKI-5 with one additional negative control:

- create two branches with identical pre-fork memory but deliberately **different evaluator lineage mechanics** that are learner-indistinguishable.

Noema should not claim knowledge of a distinction for which it received no evidence.

## Finding 6 — scalar continuity is too strong a prior

The red-team memo's synthesis is accepted.

Candidate A should not assume that persistence of:

- information;
- active control configuration;
- preference/concern;
- agency attribution;
- embodiment;
- autobiographical memory;
- broader self-model organization

must move together.

### Classification

**REQUIREMENT GAP — full-Noema self-model representation constraint.**

The important constraint is separability, not a mandated factorization or semantic ontology.

## Cross-lane synthesis with interface research

The T'kal and interface lanes converge on a deeper principle:

> **Noema may use structure the architecture genuinely supplies, but the evaluator must never confuse supplied structure with learned understanding.**

This applies equally to:

- event provenance;
- source identity;
- communication segmentation;
- timing;
- attention cues;
- task boundaries;
- replay;
- self-generated action cues;
- branch ancestry;
- teacher adaptation;
- wrapper-generated social signals.

That principle is stronger than `no semantic labels` because a nonsemantic but stable interface regularity can still remove most of the learning problem.

## Effect on Candidate A status

### First-core architecture

**SURVIVES.**

TKI-1 is a later control refinement; TKI-2 belongs to an already-open motivation layer; TKI-3/TKI-5 belong to an already-open self/other layer; TKI-4 requires an F0 provenance correction but does not contradict the predictive-control core.

### Full-Noema architecture

**STILL INCOMPLETE, now more sharply bounded.**

The existing open frontiers remain:

- compositional-temporal structure;
- developmental higher concerns/motivation;
- self/other modeling.

The T'kal pass strengthens the latter two and adds a mandatory provenance/subsidy discipline that cuts across all later evaluations.

## Adjudication summary

| Finding | Classification | Candidate A effect |
| --- | --- | --- |
| TKI-1 adaptive hysteresis | REQUIREMENT GAP | add learned mode-persistence/decay requirement later |
| TKI-2 preference laundering | REQUIREMENT + EVALUATION GAP | constrain preference/drive promotion; motivation frontier already open |
| TKI-3 agency separation | REQUIREMENT GAP | sharpen self/other representation and tests |
| TKI-4 provenance planes | BOUNDARY LEAK / F0 CORRECTION | material wording/accounting correction before source/autobiography claims |
| TKI-5 fission/recombination | REQUIREMENT + EVALUATION GAP | require non-linear continuity attribution and evaluator neutrality |
| multi-factor continuity synthesis | REQUIREMENT GAP | forbid forced scalar continuity/self token as sole representation |

No finding is downgraded merely because Candidate A survives. The T'kal pass materially changes the validation contract, and TKI-4 would invalidate an otherwise successful implementation if the learner received provenance answer keys through architecture or interface shortcuts.