# Noema first falsification package

Status: **BRAINSTORMING / EVALUATION PACKAGE / NOT AN APPROVED IMPLEMENTATION**

Level intent: **primarily L2 evidence discipline + L4 first experiment package.**

## Purpose

The project has enough architecture hypotheses to justify a disciplined first falsification package, but not enough evidence to justify implementing the full envisioned Noema architecture.

This package therefore asks a narrower question:

> **What is the smallest implementation-neutral experimental package that can falsify important Noema assumptions before we invest in embodiment, language, social cognition, or long-horizon agency?**

The package is deliberately designed so a simple continuous learner can beat a more elaborate structured candidate. If that happens, the project should simplify rather than rescue the elaborate architecture.

This document does **not** authorize implementation. It defines the candidate scientific package that would later become an implementation specification only after design review and approval.

## Package scope

The first package contains three linked stages:

1. **F0 — information-boundary / transducer audit**
2. **F1 — persistent streaming-learning baseline**
3. **F2 — observational ambiguity + intervention revision (Experiment A)**

Experiment B, active epistemic intervention choice, is explicitly excluded until F2 succeeds.

Also excluded:

- 3D embodiment;
- natural-language grounding;
- social-agent modeling;
- learned motivation/values;
- project-scale planning;
- skill hierarchy;
- long-delay credit experiments;
- self-preservation regimes;
- autonomous self-modification.

The point is to test the epistemic and continual-learning substrate cheaply before those capabilities multiply the sources of failure.

## Global design rule

Each candidate must expose the same learner-visible event stream and be judged by external evaluator metrics.

The evaluator may know the ground-truth world generator. The learner may not receive that information except through the declared observation/action channels.

Candidate-specific diagnostics are allowed, but absence of a human-readable internal structure cannot by itself count as failure.

## F0 — information-boundary audit

### Question

Can we account for every bit of structure that enters the learner before interpreting any apparent emergence?

### Required artifact

Each modality/event path must have a transducer ledger containing:

- raw source;
- preprocessing/transformation;
- timing information supplied;
- source/provenance information supplied;
- information discarded;
- structure introduced;
- whether that structure is infrastructure or a capability under evaluation.

### Event-plane separation

At minimum keep separate:

- learner-visible world observations;
- learner-visible action/efference events;
- evaluator/operator controls;
- diagnostic output;
- hidden ground-truth generator state.

No operator or evaluator metadata may leak into the learner through convenience APIs.

### F0 kill rule

If the delivered event stream cannot be reconstructed independently from evaluator-only state, later capability claims are invalid until the leak is fixed.

## F1 — persistent streaming-learning baseline

### Question

Can a candidate maintain useful revisable state online before we ask it to represent ambiguous structure?

### World family

Use deliberately simple continuous temporal systems with opaque channels and no semantic categories.

Candidate examples for the evaluator to generate may include:

- noisy autoregressive dynamics;
- simple coupled continuous processes;
- abrupt but recoverable regime changes;
- irrelevant distractor channels;
- temporary missing observations.

These examples constrain the evaluator, not the learner's ontology.

### Required behavior

A candidate should demonstrate:

- prequential prediction improves from streaming experience;
- prior experience affects later behavior without the full history being re-presented every step;
- irrelevant intervening events do not erase useful state;
- a changed regime can be learned;
- unrelated learned regularities survive that revision;
- reset controls lose the cross-time advantage;
- finite memory and compute are respected.

### Why F1 exists

If a candidate cannot learn stably online in a boring temporal system, a failure in Experiment A would be uninterpretable. We would not know whether the problem was uncertainty, causal learning, structure search, or simply broken continual learning.

### F1 advancement rule

Do not advance a candidate solely because final batch-fit error is low.

It must show an online trajectory with stable learning and correction under bounded resources.

## F2 — Experiment A

### Question

Can the candidate remain appropriately uncertain when passive data do not identify the relevant structure and then revise when intervention provides discriminating evidence?

Use the existing Experiment A world family and online protocol.

### Learner-visible information

The learner receives only:

- ordered observations;
- declared low-level channel addresses;
- action/efference/intervention packets allowed by the intervention-semantics curriculum;
- the ordinary consequences of those interventions.

It does not receive:

- `chain` / `fork` labels;
- graph ground truth;
- parent/child/cause semantics;
- evaluator confidence;
- stable semantic variable names;
- a hidden statement that the intervention succeeded;
- a truth flag identifying the correct family.

### Representation-neutral uncertainty requirement

Before discriminating evidence, the candidate must not behave as though one observationally equivalent explanation has been established without a justified prior.

This does **not** require:

- two explicit graph records;
- a named hypothesis population;
- a human-readable uncertainty vector;
- a dedicated `none_of_the_above` variable.

The evidence is behavioral/predictive: materially different intervention-conditioned futures must remain available enough that decisive evidence can cause selective revision.

## Candidate classes for the first package

The first implementation specification should support at least three scientifically distinct candidate classes.

### C0 — minimal reference predictor

A deliberately simple streaming probabilistic predictor with no explicit slow structural machinery.

Purpose:

- establish how much of F1/F2 can be solved by ordinary continuous learning;
- prevent elaborate machinery from receiving credit for a task that does not require it.

C0 is not intended to be stupid. It should be a competent fair baseline within the same resource class.

### C1 — continuous uncertainty-capable learner

A stronger distributed/continuous candidate able to represent predictive uncertainty and action-conditioned dynamics without explicit graph/factor commitments.

Purpose:

- test whether explicit structure is actually needed;
- expose whether the structured candidate's advantage is representational or merely capacity/compute.

### C2 — structure-capable developmental candidate

A candidate that may construct explicit or semi-explicit reusable structure from evidence, using whichever currently approved mechanism family is selected later.

Purpose:

- test whether earned structural representation provides advantages in intervention prediction, local correction, transfer, or sample/resource efficiency.

Important: this package does not yet choose DGFW, EGSS, graph bindings, bounded hypothesis populations, or another specific mechanism for C2. That choice belongs in the later implementation design if the broader architecture review approves moving forward.

## Reference / oracle tools

An evaluator may also use analytic or offline reference models to verify that:

- passive distributions are truly non-identifying where claimed;
- interventions are actually discriminating;
- scoring is mathematically correct;
- the task is solvable under generous assumptions.

These are evaluator tools, not developmental candidates, and must never be counted as evidence that Noema learned anything.

## Prequential evidence contract

Predictions must be scored before the corresponding outcome is revealed.

At minimum record checkpoints for:

- early passive exposure;
- late passive exposure;
- immediately before decisive intervention;
- immediately after the first intervention outcome;
- after a short intervention sequence;
- held-out intervention values;
- remapped transfer world.

The central object is the learning trajectory, not one final score.

## Evidence maturity in the first package

Do not implement a universal `N_min` epistemic law.

Instead, evaluate whether confidence/commitment changes proportionally to genuinely new evidence.

A candidate fails this discipline if it becomes more certain merely because the same evidence is replayed or internally revisited repeatedly.

A candidate is allowed to move confidence sharply after one highly diagnostic event if that movement is calibrated by subsequent prediction.

Any loop-count guard used for debugging or compute control must be reported as an engineering parameter, not a source of epistemic support.

## Bounded deliberation

Every candidate gets declared resource envelopes.

The later implementation plan should pre-register limits or accounting rules for:

- memory available for raw/replay data;
- model parameter/capacity budget;
- structural proposal/search budget where applicable;
- per-step compute;
- peak live hypothesis/branch count where applicable;
- wall/CPU time on the controlled local evaluation platform.

Exact numeric values are an implementation-plan decision, but unbounded search is disallowed by design.

## Resource fairness

No candidate may claim superior learning merely because it receives materially more retained data or compute.

When exact matching is impossible, report trade-off curves across:

- predictive quality;
- sample count;
- compute;
- memory;
- candidate/proposal count;
- transfer speed;
- revision cost.

A more expensive system must earn the extra cost through a relevant capability advantage.

## Primary F2 measures

The first package should score at least:

### Passive predictive quality

Can the candidate model the observation stream well?

### Passive calibration / non-overcommitment

Does the candidate avoid unjustified confidence under exact observational equivalence?

### Intervention-conditioned prediction

After intervention evidence, does prediction improve for the relevant manipulated futures?

### Revision locality

Does decisive new evidence repair implicated structure while leaving unrelated learned predictions substantially intact?

### Transfer

Does learning reduce evidence/compute needed in remapped analogous worlds without copying stable semantic identities?

### Resource use

What did the candidate spend to obtain the improvement?

### Ablation specificity

If the candidate claims a mechanism caused an advantage, does removing that mechanism remove the corresponding advantage without simply destroying the entire learner?

## Representation-mismatch controls

The chain/fork world is intentionally clean and may favor graph-like representations.

Therefore F2 should include negative/mismatch controls such as:

- symmetric/distributed dependencies;
- higher-order interactions poorly described by pairwise edges;
- regime changes requiring reopening;
- worlds where explicit factorization offers no advantage;
- worlds where a different decomposition is equally predictive.

The goal is to distinguish `useful structure learner` from `graphifier that wins graph-shaped tests`.

## None-of-the-current-family control

F2 should eventually include a case in which the candidate's initially available explicit structural family is insufficient.

Success is not necessarily an explicit alarm variable.

Behavioral evidence should show that the candidate:

- does not simply crown the least-wrong option;
- detects persistent collective predictive inadequacy;
- broadens or changes learning behavior under the same finite-resource rules;
- preserves useful substructure where possible;
- improves after forming a better representation.

If C2 cannot escape its supplied family while C1 adapts successfully, that is evidence against the C2 architecture.

## Persistence and reset conditions

For every stage distinguish:

- **developmental carry-forward condition:** relevant learned state is preserved;
- **fresh-start diagnostic:** candidate starts without prior developmental state;
- **reset-and-refit reference:** permitted only as a diagnostic upper/lower bound where scientifically useful.

A reset-and-refit result cannot substitute for continual correction when persistence is the claim under test.

## Reproducibility artifacts

A later implementation should produce, per run:

- candidate configuration manifest;
- random seed/world-parameter manifest;
- transducer/event contract version;
- learner-visible event log;
- evaluator-hidden ground-truth log stored separately;
- prequential prediction log;
- resource-accounting log;
- checkpoint snapshots where declared;
- final evaluator report;
- ablation identifier when applicable.

These are scientific audit artifacts, not learner memory.

## Package-level kill rules

Materially revise or abandon the current candidate direction if passing requires:

- semantic target-specific proposal rules;
- hidden evaluator identities/labels;
- offline batch refitting in place of continual correction;
- effectively unlimited memory/search;
- one architecture receiving materially richer input than its baselines;
- confidence increasing from repeated processing without new evidence;
- structure-specific scoring that ignores behaviorally superior alternatives;
- rescue heuristics written specifically for the current world generator;
- disabling negative controls because they make the favored representation look bad.

## Advancement to Experiment B

Experiment B is not unlocked because F2 obtains a good final predictive score.

The candidate should first show credible evidence of:

- persistent online learning from F1;
- calibrated ambiguity handling;
- intervention-conditioned revision;
- acceptable resource use;
- transfer or another structural advantage if explicit structure is claimed;
- no fatal representation-mismatch pathology;
- local correction rather than catastrophic rewrite.

Only then does it become scientifically worthwhile to ask whether Noema can **choose** an information-gathering intervention.

## Relationship to the Noema Console

A minimal console shell may exist during these experiments for observability and operator control.

Formal F1/F2 runs do not require grounded language.

The console may show evaluator diagnostics, predictions, resource use, and timeline state, but those diagnostics remain outside the learner-visible event plane.

Direct Patrick↔Noema communication can remain disabled during formal Experiment A runs so language does not contaminate the first epistemic falsifier.

## What this package can establish

If successful, the first package can support narrow claims that a candidate:

- learns continually from a stream;
- retains useful state;
- handles a controlled observational ambiguity without unjustified commitment;
- revises from intervention evidence;
- transfers some learned structure or strategy;
- does so under declared finite resources.

## What this package cannot establish

It cannot establish that Noema:

- understands objects or people;
- possesses a mature self-model;
- has grounded language;
- has learned values or wants;
- plans long projects;
- has general causal reasoning;
- has human-like consciousness or subjective experience;
- has solved AGI;
- should use the winning F2 representation as its permanent cognitive architecture.

## Current recommendation

When the broader design is approved enough to cross into implementation planning, this should be the first scientific package rather than a full 3D Noema build.

The implementation effort should remain deliberately small enough that a failed assumption is cheap to discard.

The preferred scientific order is:

`F0 information boundary -> F1 persistent streaming baseline -> F2 Experiment A -> review evidence -> only then consider Experiment B or broader embodiment`.

That sequence maximizes the chance that early failures teach us something rather than merely producing a complicated broken agent.
