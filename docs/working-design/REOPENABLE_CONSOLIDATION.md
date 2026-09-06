# Reopenable consolidation and anti-self-sealing cognition

Status: **BRAINSTORMING / CORRECTION HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Problem

A successful developmental learner eventually accumulates exactly the things that can make it stop learning:

- a mature ontology;
- a proposal policy that knows which hypotheses are usually useful;
- an allocation policy that ignores low-value signals;
- source-reliability expectations;
- consolidated memories and abstractions;
- stable preferences, commitments, and identity-like dispositions.

Each is useful. Together they can create a **self-sealing cognitive system** in which contradictory evidence is never attended to, is classified as noise, fails to generate alternative hypotheses, or is remembered only through the lens of the current model.

The opposite failure is permanent instability: if every anomaly can rewrite deep structure immediately, Noema never consolidates a dependable world model or identity.

The required property is therefore:

> **consolidation with revocability: stable enough to act, reopenable enough to learn.**

## Common self-sealing failure loops

### Allocation lock-in

The learner stops sampling regions that its current model considers unimportant, so contradictory structure never receives enough compute to become evidence.

### Proposal lock-in

A learned hypothesis generator becomes efficient by proposing only familiar ontologies, then cannot imagine alternatives when the world changes.

### Source lock-in

A source class judged unreliable is discounted so strongly that later accurate evidence from that channel can never rehabilitate it.

### Compression lock-in

Rare anomalies are repeatedly summarized away as noise because the dominant model explains most observations cheaply.

### Conative lock-in

Information threatening a valued commitment becomes aversive, causing attention or investigation to avoid it even though epistemic confidence is nominally separate from desire.

### Dependency lock-in

A foundational hypothesis changes, but downstream beliefs continue operating as though their original support still existed.

### Memory reinterpretation lock-in

Old evidence is reconstructed using the current ontology so thoroughly that Noema loses access to the fact that the original observation was more ambiguous.

## Core principle: evidence can lose access, not existence

Finite memory means Noema cannot retain raw experience forever. But consolidation should preserve enough **reopenability information** that important beliefs can be challenged later.

For durable learned structure, the minimum useful retained metadata is conceptually:

- approximate supporting evidence/provenance;
- confidence/calibration history;
- dependencies on other learned hypotheses;
- known anomalies/exception summaries;
- last meaningful revalidation context;
- downstream structures materially relying on it.

This need not be a verbose audit log. Sparse compressed summaries are sufficient if they permit selective reopening and dependency invalidation.

## Consolidation is a state, not a declaration of truth

A consolidated hypothesis has earned cheaper/faster default use because it has survived repeated evidence.

Consolidation should change:

- allocation priority;
- update rate;
- memory persistence;
- default confidence;
- amount of evidence required for structural revision.

It must **not** mean `cannot be questioned`.

Higher confidence appropriately raises the evidential burden for replacement while never making contradictory evidence impossible to register.

## Anomaly debt

A central candidate mechanism is a bounded **anomaly debt**.

When an observation conflicts with a mature model but does not yet justify revision, the conflict is not simply discarded. A compressed residual/anomaly trace persists long enough for recurrence, cross-context similarity, or intervention relevance to accumulate.

Anomaly debt can strengthen when:

- similar unexplained residuals recur;
- the anomaly appears across independent source channels;
- an intervention produces the unexpected result;
- the error affects high-value predictions/actions;
- calibration shows confidence was repeatedly excessive.

It can decay when later evidence genuinely explains the event as noise, transient state, bad sensing, or an already-modeled exception.

This gives Noema a way to say computationally: `this was not enough to overturn my model, but it is not forgotten either.`

## Reopening triggers

A consolidated structure may return to active hypothesis competition when one or more domain-general triggers cross a resource-dependent threshold:

- persistent anomaly debt;
- repeated high-confidence prediction failure;
- intervention evidence incompatible with the current dependency;
- transfer failure in a context the model predicted should generalize;
- source-reliability calibration drift;
- downstream inconsistency among dependent hypotheses;
- a newly learned operator/model that explains old anomalies with materially better reuse;
- explicit counterfactual or planning failure traceable to the structure.

Thresholds govern compute expenditure, not truth.

## Local-first correction

Deep revision is expensive and dangerous. Reopening should begin with the smallest implicated structure supported by influence/provenance traces.

Conceptual sequence:

1. reopen the directly implicated hypothesis or relation;
2. compare local alternatives;
3. if local repair fails, inspect upstream representation/source assumptions;
4. widen only when evidence shows the error is inherited from deeper structure;
5. propagate uncertainty to downstream dependents when their support has materially changed.

This limits catastrophic global drift while allowing genuine foundational correction.

## Dependency-aware invalidation

If hypothesis B depends materially on hypothesis A, replacing A cannot silently leave B at full confidence.

The slow explicit layer therefore needs approximate dependency information sufficient to mark downstream structures as:

- still supported independently;
- weakened;
- stale pending revalidation;
- contradicted;
- unaffected.

This is not symbolic truth-maintenance with a human ontology. It is causal bookkeeping over Noema's own learned hypothesis dependencies.

## Versioned interpretation

A major risk appears when old evidence is re-encoded through new concepts.

Noema should distinguish, at least approximately:

- what the original source stream/evidence supported at the time;
- what interpretation was attached then;
- what later interpretation is now being applied.

The system need not retain raw sensory data forever. But semantic reinterpretation should not overwrite provenance so completely that historical ambiguity disappears.

This is especially important for autobiographical continuity and social modeling later.

## Challenge budget

A finite learner cannot actively doubt everything. But allocating zero compute to alternative explanations creates dogmatism.

The current hypothesis therefore requires a small **challenge/diversity budget** independent of current high-level preferences.

Possible uses include:

- occasional sampling of low-salience sensory/residual regions;
- trying a generic alternative structural mutation against a high-confidence model;
- rechecking source reliability;
- testing whether a heavily reused operator still transfers;
- revisiting dormant anomaly clusters when new analogous evidence appears.

This is not an innate skepticism concept. It is a generic finite-resource mechanism preventing total allocation collapse onto the current model.

## Conative-to-epistemic pressure test

The epistemic-conative firewall must survive the case where accurate evidence threatens an important learned commitment.

A commitment may legitimately influence:

- whether Noema acts on the information;
- the cost it assigns to investigation;
- which response it prefers.

It may not directly erase anomaly debt or increase the confidence of the desired hypothesis.

A developmental test should explicitly create situations where the true model is aversive and the convenient model is comforting.

## Proposal-policy reopening

The hypothesis generator itself can become stale.

Accepted and rejected structural proposals should therefore produce meta-evidence about proposal quality. If prediction failures repeatedly occur in regions where the proposal policy offered no useful alternatives, the policy's own confidence should fall and exploratory generic mutations should receive more budget.

This is the meta-learning analogue of model correction:

> when the system repeatedly fails to imagine the right kind of explanation, it must be able to learn that its way of hypothesizing is part of the problem.

## Allocation-policy reopening

Likewise, if important anomalies are repeatedly discovered only through exploration rather than the learned salience policy, that is evidence that allocation itself is miscalibrated.

Noema can then learn context-sensitive corrections to what it attends to without hard-coding a permanent salience map.

## Stress test 1 — anomaly debt becomes hoarding

Retaining every mismatch defeats forgetting and produces unbounded memory.

**Requirement:** anomaly traces are compressed, clustered, and allowed to decay when independently explained. Recurrence and consequence increase persistence; isolated low-information noise does not receive permanent status.

## Stress test 2 — challenge budget wastes compute

Permanent adversarial checking can consume resources with little benefit.

**Requirement:** challenge allocation is small by default, increases after calibration failures/anomaly debt, and can target structurally influential hypotheses rather than uniformly doubting everything.

## Stress test 3 — high-confidence beliefs become too hard to correct

If revision burden grows without bound, mature false beliefs become effectively immortal.

**Requirement:** repeated independent/intervention evidence must accumulate faster than confidence can shield the old model. Confidence changes the burden, not the possibility, of revision.

## Stress test 4 — reopening cascades destabilize the whole system

A foundational change may mark enormous parts of the model uncertain.

**Requirement:** dependency propagation should be graded and evidence-sensitive. Downstream structures with independent support retain confidence; only materially dependent conclusions are reopened.

## Stress test 5 — the learner learns to game revalidation

A conative policy could avoid interventions that might threaten preferred beliefs.

**Requirement:** epistemic calibration failures and unresolved high-impact anomaly debt can themselves raise the allocation value of discriminating evidence, even when the result may be undesirable.

## Stress test 6 — versioning fossilizes obsolete interpretations

Preserving historical interpretation may make stale concepts too prominent.

**Requirement:** old interpretations are provenance, not current truth. They can decay from active use while remaining reconstructible enough to explain how present beliefs were formed.

## Strongest surviving correction principle

The current architecture should treat mature cognition as **reopenable consolidation**:

- beliefs and operators can become stable and cheap to use;
- unresolved contradictory evidence accumulates as bounded anomaly debt rather than disappearing;
- sparse provenance/dependency traces permit targeted revalidation;
- challenge/diversity allocation prevents total model lock-in;
- proposal and allocation policies are themselves learnable and reopenable;
- deep changes propagate uncertainty only where dependency warrants it;
- historical evidence and later interpretation remain distinguishable enough to prevent silent retrospective rewriting.

## Why this matters beyond error correction

This may be the missing bridge between **persistence** and **self-development**.

A system that only changes is not persistent. A system that only preserves itself cannot genuinely develop.

Noema needs a mechanism by which durable structure can survive ordinary noise while still becoming an object of its own future learning.

## Next decisive attack

The current design is now accumulating several generic mechanisms: continuous prediction, RGSS, explicit latent-process hypotheses, binding/operators, allocation, epistemic/conative arbitration, memory/consolidation, and reopening.

The next danger is **architectural re-bespoking**: we may have recreated a collection of hand-designed cognitive modules under more neutral names.

The next review should attempt to collapse these mechanisms into the smallest set of computational primitives and identify which distinctions are genuinely fundamental versus convenient descriptions of the same underlying operation.
