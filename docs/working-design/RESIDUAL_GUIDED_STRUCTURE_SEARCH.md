# Residual-guided structure search

Status: **BRAINSTORMING / CANDIDATE MECHANISM / NOT AN APPROVED IMPLEMENTATION**

## Purpose

The current DGFW hypothesis needs a way to create useful latent factors and relations without hard-coding objects, agents, causes, selves, or semantic roles.

The core problem is combinatorial: the learner cannot enumerate every possible hidden structure. Candidate generation therefore needs to be guided by where the current model systematically fails, while candidate evaluation remains domain-general.

## Candidate mechanism

Provisionally call this **Residual-Guided Structure Search (RGSS)**.

RGSS is not a semantic detector. It is a generic model-revision loop.

### 1. Maintain a current uncertain model

Noema maintains one or more active hypotheses about latent world structure and predicts future sensorimotor experience across several horizons.

Predictions retain provenance about which active latent structures materially contributed.

### 2. Preserve structured residuals

When prediction and observation diverge, do not immediately rewrite the model.

Retain a bounded trace of the residual together with:

- temporal context;
- relevant sensory/source channels;
- action/efference context;
- contributing hypotheses;
- confidence/uncertainty;
- later outcome if available.

The residual is not labeled as `object error`, `causal error`, `agent error`, etc.

### 3. Search for recurring unexplained dependency

The learner looks for residual patterns that recur or remain compressible across episodes, viewpoints, actions, or contexts.

Candidate proposal is triggered by **persistent unexplained dependency**, not by human semantic rules.

Examples of domain-general signals include:

- residual covariance/dependence across channels or time;
- repeated conditional dependence on an action or latent state;
- repeated failure of one hypothesis under a specific context;
- recurring transformation that can be reused across otherwise different episodes;
- systematic multimodality suggesting that one current representation conflates distinct regimes.

None of these says what the new structure means.

### 4. Generate local structural mutations

Instead of searching arbitrary models from scratch, propose bounded changes around the implicated region of the current model.

Generic mutation operators may include:

- introduce a provisional latent factor;
- split one factor into competing alternatives;
- merge redundant factors;
- add/remove a dependency;
- introduce a reusable transformation/operator;
- rebind an operator to different latent arguments;
- increase/decrease temporal span;
- retain a distributed representation instead of factorizing;
- fork a competing model rather than replacing the current one.

The operators describe representation mechanics, not ontology.

### 5. Evaluate candidates as a Pareto problem

A single weighted scalar objective can hide designer assumptions. Instead, keep candidates on a bounded **Pareto frontier** across several criteria:

- predictive adequacy across horizons;
- intervention-conditioned accuracy;
- cross-context transfer/reuse;
- uncertainty calibration;
- complexity/resource cost;
- local explanatory/credit-assignment benefit;
- counterfactual usefulness when applicable.

A candidate is dominated when another candidate is no worse on all relevant criteria and better on at least one.

This delays arbitrary commitment to a designer-chosen fixed weighting.

### 6. Use action to discriminate hypotheses

When several live structures predict different consequences of available actions, Noema can estimate which action would be informative while also considering viability/valence and other current concerns.

The action is not chosen merely to maximize surprise. It should discriminate among meaningful live hypotheses at tolerable cost.

### 7. Consolidate only after repeated survival

A latent structure that repeatedly improves prediction, intervention response, transfer, or compression can move from provisional working structure toward durable learned representation.

Consolidation is gradual. A strong candidate can still be revised, split, or retired later.

## Why RGSS could produce target concepts without encoding them

### Candidate objecthood

Several sensory features may repeatedly generate residuals when modeled independently. A latent factor tying their dynamics together improves long-horizon prediction, survives occlusion/intervention, and transfers to new appearances.

The factor is never told it is an object.

### Candidate self/body structure

Some latent structures repeatedly improve prediction when conditioned on proprioception, interoception, contact, and issued action. Their special sensorimotor coupling makes them useful explanatory factors.

No `SELF` label is required.

### Candidate other-agent structure

A visible process remains poorly predicted by passive dynamics. A latent history-dependent state improves prediction across situations and transfers across changed surface appearance.

No `AGENT` label is required.

### Candidate causation

Two models predict passive observation equally well. Under intervention they diverge. The model whose learned dependency remains predictive under the relevant action conditions gains support.

No innate `CAUSE` predicate is required.

### Candidate abstraction

A learned transformation explains residual structure across many differently bound factors and contexts. Reusing that transformation predicts novel compositions better than separate memorized cases.

That operator can become an abstract relation before it has a word or human-readable label.

## Stress test 1 — residual guidance can become attention bias

A model only notices residuals in regions receiving compute. Important structure may never generate a proposal if allocation ignores it.

**Requirement:** allocation must retain some exploration/diversity budget and must occasionally sample low-salience regions. Otherwise existing beliefs can become self-sealing.

## Stress test 2 — residuals can be caused by bad perception

A poor continuous representation can create fake structure-search pressure.

**Requirement:** candidate revisions must include both higher-level factor changes and lower-level representation changes. Noema must be able to conclude `my current feature representation is bad` rather than spawning endless latent factors.

## Stress test 3 — Pareto fronts can explode

Maintaining every non-dominated model is computationally impossible in open-ended worlds.

**Requirement:** the frontier itself must be resource-bounded. Diversity-preserving pruning, confidence, expected future usefulness, and decay are needed. Pruning must remain reversible enough that discarded alternatives can be reconstructed from episodic evidence when later anomalies demand it.

## Stress test 4 — generic mutation operators are still inductive bias

`split`, `merge`, `factor`, and `relation` are not assumption-free.

**Requirement:** treat them as explicit admissible computational biases and test alternate operator sets. The project should compare whether the same developmental capabilities appear under materially different generic structure-search grammars.

If success depends on one operator that is effectively a hidden object/agent detector, the claim fails.

## Stress test 5 — structural search may be too slow

Even local graph/model mutations can be expensive in continuous 3D experience.

**Candidate mitigation:** amortize proposal generation. A learned proposal policy can become better at suggesting useful structural edits from residual history, while the candidate still has to earn acceptance through prediction/intervention/transfer evidence.

This creates a possible path to **learning how to form hypotheses** without allowing the proposal policy to become unquestionable.

## Stress test 6 — learned proposal policy can inherit ontology

Once proposal generation is learned, it may overfit to early worlds and start proposing only familiar decompositions.

**Requirement:** later transfer tests must include worlds with materially different organization. The proposal policy must remain corrigible and maintain exploratory mutation capacity.

## Stress test 7 — selection can reward predictive hacks

A candidate can improve prediction through brittle shortcuts rather than useful structure.

**Requirement:** acceptance cannot depend on familiar-data prediction alone. Intervention, recombination, held-out transfer, and ablation must remain decisive evidence.

## Stress test 8 — local provenance can become prohibitive

Tracking every contributing hypothesis through every prediction/action may cost too much.

**Requirement:** preserve approximate causal influence sufficient for credit assignment rather than perfect human-readable provenance. Influence traces can be sparse, thresholded, or compressed, but must support selective revision and evaluation.

## Stronger candidate after stress test

RGSS survives as a plausible mechanism if it is understood as:

> **resource-bounded, residual-guided local structural search over explicit generic mutations, with multiple live hypotheses evaluated by multi-criterion evidence and actively discriminated through intervention.**

A later learned proposal policy may accelerate search, but proposal and acceptance remain distinct: the system may learn what hypotheses are worth trying without being allowed to declare them true.

## Most important new insight

The architecture may need two different kinds of learning:

1. **model learning** — change beliefs/factors/relations about the world;
2. **hypothesis-generation learning** — become better at proposing useful candidate revisions.

That gives a concrete computational interpretation of part of Noema's `learn from my mistakes` requirement. A mistake can teach not only a corrected belief, but a better way to search for explanations next time.

## Immediate falsification experiment

Before a full 3D organism, test RGSS in a synthetic temporal world with no object labels and deliberately ambiguous early evidence.

The evaluator knows two hidden generative structures. Early observations are designed so both fit. Later interventions make their predictions diverge.

Success requires Noema to:

1. preserve both explanations before disambiguating evidence;
2. generate a useful structural distinction without an object/agent-specific rule;
3. choose or exploit an intervention that separates the hypotheses;
4. revise confidence/structure appropriately;
5. transfer the learned relation to a novel surface instantiation;
6. lose the transfer benefit when the relevant learned structure is ablated;
7. improve its later proposal efficiency after similar but non-identical failures.

The seventh requirement is the strongest: it tests whether Noema is beginning to learn **how to hypothesize**, not merely what happened in one world.

## Current verdict

RGSS is the strongest current answer to the candidate-structure search problem, but it remains a hypothesis.

Its central vulnerability is computational tractability. If useful structures cannot be proposed and compared without either combinatorial explosion or semantic proposal heuristics, the DGFW direction weakens substantially.
