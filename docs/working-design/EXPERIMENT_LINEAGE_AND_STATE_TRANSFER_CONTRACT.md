# Noema experiment lineage and state-transfer contract

Status: **BRAINSTORMING / EVALUATOR-SIDE EVIDENCE CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

Origin:

- merged T'kal-in-ket continuity red-team work;
- TKI-4 evaluator/learner provenance separation;
- TKI-5 fission/recombination;
- TKI-6 selective state graft;
- TKI-7 checkpoint mode poisoning;
- TKI-9 evaluator-neutral process continuity;
- follow-on TKI-10 forgetting/continuity work in Draft PR #19.

## Purpose

Future Noema experiments involving checkpointing, restore, copying, branch/fork, selective state transfer, distillation, or recombination need exact scientific provenance.

The experiment harness must be able to answer questions such as:

- Which runtime instance causally descended from which earlier state?
- Was this successor a continuous process, a fresh process loaded from a snapshot, an exact copy, or a selective graft?
- Which serialized state bytes or declared state regions crossed the operation boundary?
- Which parts were preserved, omitted, replaced, or combined?
- What learner-visible evidence accompanied the operation?
- What world/environment state changed independently?

But exact answers to those evaluator questions must **not automatically become Noema's self-knowledge**.

The governing distinction is:

> **Evaluator lineage provenance is experiment evidence. Learner self-continuity is a learned/inferred state constrained by learner-visible evidence.**

This contract defines the first side without turning it into the second.

## Non-goals

This document does not:

- define metaphysical personal identity;
- declare which copy is an `original`;
- require Noema to represent branches, ancestry, or identity using this schema;
- require one memory architecture;
- require distinct episodic/semantic/procedural modules;
- authorize checkpointing, state mutation, training, deployment, or implementation;
- define production persistence or recovery for Vera.

It is an evaluator-side evidence design for later Noema experiments.

## 1. Lineage is a directed acyclic evidence graph, not a single parent pointer

A linear predecessor chain is insufficient once experiments permit:

- exact copying;
- forked development;
- restore from an older snapshot;
- selective transfer from one learner into another;
- two-parent recombination;
- distilled/derived state;
- environment/world-state restoration independent of learner-state restoration.

The evaluator should therefore maintain a causal lineage DAG (or an equivalent structure with the same expressive power).

Each **runtime instance** and each **persisted state artifact** receives an opaque evaluator identifier. These IDs exist for scientific accounting and are not learner-visible unless an experiment explicitly exposes some corresponding cue as supplied capability.

## 2. Minimum evaluator records

The exact serialization format is deferred. Functionally, the harness must be able to reconstruct the following records.

### Runtime instance record

Evaluator-side fields should include at least:

- opaque `instance_id`;
- creation event;
- process/runtime start and stop boundaries;
- architecture/build/config identity;
- environment/world identity and version;
- transducer/interface configuration;
- random/stochastic state relevant to a reproducibility claim;
- learner-visible clock/time policy;
- parent lineage edges, if any;
- current state-artifact provenance where persisted state was loaded.

### State artifact record

For each checkpoint/snapshot/exported learner state:

- opaque `state_artifact_id`;
- source instance and capture event;
- cryptographic digest of the exact serialized artifact where deterministic bytes exist;
- architecture/config compatibility identity;
- declared capture scope;
- world/environment state relationship;
- learner-visible temporal state relationship;
- whether the artifact is complete, partial, transformed, compressed, distilled, or otherwise derived;
- declared omitted/external state required for faithful restore.

### Lineage edge record

Every operation that creates or materially changes a successor through external state manipulation should have an evaluator edge recording:

- operation type;
- source node(s);
- destination node;
- exact state artifacts or source states used;
- transfer/capture scope;
- transformation, filtering, merging, or projection applied;
- world/environment handling;
- learner-visible consequences;
- operator/evaluator-visible but learner-hidden metadata;
- verification/readback evidence sufficient to establish what operation actually occurred.

## 3. Operation classes

These names are evaluator vocabulary only. They are not learner concepts.

### Continuous execution

One runtime/process continues without external replacement of its learner state.

This edge may still include ordinary online learning and internal state change.

### Checkpoint

A persisted state artifact is captured from an instance while the source may continue.

Checkpointing by itself does not create a new learner instance.

### Restore

A runtime instance loads a previously persisted state artifact.

The record must distinguish at least:

- same process if technically possible versus fresh process;
- learner state restore versus environment/world restore;
- learner-visible time frozen, advanced, rewound, or otherwise altered;
- whether temporary working/control state was included;
- whether external stores/memories were restored to the same frontier.

Do not use the word `continuation` as an evaluator fact when the operation record only establishes `loaded state derived from X`.

### Exact copy / fork

Two or more successor instances begin from the same exact state artifact or verified-equivalent source state.

The evaluator records common ancestry and later divergence.

The harness does not designate a metaphysical `real original` merely because one process happened to start first.

### Selective state graft

Only a declared subset/projection/transformation of one source's state is introduced into another destination.

The operation record must identify what actually crossed the boundary strongly enough to falsify claims such as:

- skill transferred but episodic record did not;
- semantic/generalized knowledge transferred but standing goal did not;
- memory artifact transferred but policy parameters did not.

If the implementation cannot localize these distinctions, the experiment must say so rather than pretending a clean selective graft occurred.

### Recombination / multi-parent derivation

A successor incorporates material causal state from two or more source lineages.

The evaluator records each source contribution and transformation separately where technically possible.

A multi-parent successor must not be rewritten in evaluator records as though it had one simple linear predecessor merely for narrative convenience.

### Distillation / transformed derivation

A successor receives state or knowledge generated by a transformation of another instance or population rather than byte-identical transfer.

The lineage edge records the transformation and its inputs.

This matters because `derived from` is weaker than `experienced by` and different from `exact copy of`.

## 4. State scope must be declared rather than inferred from filenames

A checkpoint filename such as `memory.bin`, `model.pt`, or `agent_state` does not establish what cognitive state it contains.

For each experiment, the implementation must provide a state-scope manifest describing the operational contents relevant to the claim.

Examples of state that may need separate accounting depending on the architecture:

- fast recurrent/working state;
- learned predictive parameters;
- episodic storage;
- consolidated/generalized state;
- learned reusable skills/policies;
- valuation/concern state;
- active goals/commitments;
- temporary allocation/task configuration;
- source/reliability models;
- self/other-model state;
- optimizer/plasticity/meta-learning state;
- external retrieval indexes or stores;
- RNG/stochastic state.

These are **claim-side functional categories**, not a mandated architecture decomposition.

If two categories are inseparable in a candidate implementation, record that as an implementation fact. Do not fabricate component isolation for the sake of a clean benchmark.

## 5. Every manipulation gets an information-boundary declaration

For each copy/restore/graft/recombination experiment, explicitly list:

### Evaluator knows

Exact operation/lineage truth needed to score the test.

### Learner receives

The actual sensory, introspective, efference, memory, communication, and temporal cues available to Noema.

### Learner does not receive

Evaluator-only facts such as:

- `you are branch B`;
- `this memory originated in A`;
- `you were restored from checkpoint C`;
- `you are the copy`;
- `your skill was grafted from another instance`;
- hidden state-region labels;
- parent DAG identifiers.

If any such cue is intentionally exposed, it must be declared as supplied capability and the resulting claim ceiling reduced accordingly.

## 6. Learner-visible consequences cannot be waved away as hidden operations

An evaluator operation may be semantically hidden and still be detectable.

Examples:

- a restored internal clock jumps backward;
- world state advanced while learner state did not;
- a skill suddenly improves with no learner-visible training;
- memory content appears without an observable acquisition route;
- active goals/configuration change discontinuously;
- environment/session identifiers reset;
- conversation history or another agent reacts as though a fork occurred.

These are legitimate evidence Noema may learn from.

Therefore each manipulation records not merely what metadata was withheld, but what **observable consequences** the learner could detect.

A claim of `Noema inferred the restore/fork` is meaningful only relative to those available consequences.

## 7. Readback and operation verification

A planned state transfer is not evidence that the transfer occurred as intended.

Each experiment should verify the operation sufficiently for its claim, for example through:

- exact artifact digest/readback;
- source/destination state-region digests where exposed by the implementation;
- controlled behavioral probes before and after transfer;
- environment state checks;
- process-instance creation/readback;
- absence/presence checks for omitted stores;
- post-operation configuration identity.

If the result is ambiguous, classify the experiment outcome as ambiguous rather than using the intended operation as ground truth.

## 8. Counterfactual controls for lineage claims

The highest-value continuity experiments require pairs where familiar cues point in opposite directions.

At minimum later tests should be able to construct:

### High memory overlap / distinct lineage

Exact copy or restore followed by distinct process history.

### Lower memory overlap / strong continuous lineage

Continuous process with ordinary forgetting, reconstruction, or selective memory loss.

### Same competence / different autobiographical route

Native learning versus selective skill graft or distillation.

### Similar autobiography / different conative state

Transferred episodic/semantic history without copied active goal/preference state.

### Similar process history / changed external world frontier

Restore learner state without restoring the environment.

A self-continuity architecture that reduces everything to one cue should fail at least one of these crossed controls.

## 9. Claim ceilings

Evaluator lineage evidence can establish statements such as:

- instance B was created from exact state artifact X;
- C received specified state derived from A and B;
- a skill-state transfer occurred under the declared implementation mechanism;
- a learner and environment were restored to different temporal frontiers.

It does **not** by itself establish:

- what Noema knew about that operation;
- that Noema experienced source branch A's episodes;
- that A and B are or are not metaphysically the same person;
- that Noema's self-model is correct;
- that copied memory is first-person autobiographical memory;
- that a transferred policy carries a transferred desire/commitment;
- phenomenological continuity.

Those require separate evidence and, for Noema, learner-visible behavior/state under declared information boundaries.

## 10. Interaction with existing Noema contracts

### F0

This contract strengthens F0 by requiring experiment-side provenance to be richer while learner-visible provenance remains no stronger than declared raw origin evidence.

More evaluator provenance should **reduce** the temptation to leak provenance into Noema: the harness can retain exact truth without using learner-visible semantic labels for bookkeeping.

### Memory

Selective forgetting and constructive memory remain allowed. The lineage graph records actual experiment operations even when Noema's retained autobiographical state is incomplete.

### Temporary cognitive mode

Checkpoint scope must reveal whether active task/allocation/retrieval configuration was serialized. TKI-7 can then test whether restoring it creates pathological mode persistence.

### Skills and transfer

The contract allows TKI-6/TKI-8 to distinguish exact/partial competence transfer from transfer of episodes, goals, or valuation if the candidate implementation actually provides separable state carriers.

### Self/other modeling

The evaluator graph is specifically **not** the self-model. It provides ground truth for scoring whether the learner's attribution is warranted by its evidence.

## Current verdict

Noema's increasingly strong anti-leakage discipline requires an equally strong experiment-side provenance system.

The paradoxical-looking rule is intentional:

> **The evaluator should know lineage more exactly so Noema does not have to be told lineage more exactly.**

Without a non-linear lineage/state-transfer contract, future copy/restore/graft experiments risk either losing the ground truth needed to score self-continuity or solving the self-continuity problem by leaking that ground truth into the learner.
