# Noema developmental scaffolding contract

Status: **BRAINSTORMING / DEVELOPMENTAL-EVIDENCE CONTRACT / NOT AN APPROVED IMPLEMENTATION**

Level intent: **L2 developmental/evidential constraint.**

## Purpose

Noema is not intended to learn in a featureless void.

A developing learner can receive structured experience, teaching, demonstrations, staged environments, and practical sensory transducers without invalidating the project. The scientific problem is different:

> **Which capabilities were supplied directly, which were made learnable through curriculum/scaffolding, and which were actually acquired by Noema?**

Without this distinction, the project can make two opposite mistakes:

- **purity failure:** demanding Noema reinvent every useful structure from raw physics;
- **attribution failure:** quietly embedding the target answer in training/scaffolding and later calling it emergence.

This contract defines acceptable developmental scaffolding and the evidence required to describe its contribution honestly.

## Core distinction

Use three separate categories.

### Supplied capability

A transformation, representation, skill, semantic label, or policy is directly provided to Noema.

The supplied capability may be useful engineering, but it cannot later be claimed as independently learned.

### Scaffolding / curriculum

The environment, teaching process, or exposure distribution is deliberately arranged to make learning more tractable without directly writing the target representation or answer into Noema.

A scaffold can strongly influence what is learned and when. Its contribution must be documented.

### Acquired capability

Noema's own persistent state/behavior changes from learner-visible experience, and the claimed capability survives appropriate transfer, intervention, ablation, or negative-control tests.

Scaffolding does not disqualify acquisition. It changes the scope of the claim.

## Examples of acceptable scaffolding

### Staged environmental complexity

Start with simpler dynamics before introducing occlusion, multiple agents, noisy sensors, or long delays.

This is analogous to curriculum design. It supplies easier evidence, not the final ontology.

The capability claim must still transfer when the simplifying conditions are relaxed.

### Controlled intervention curriculum

Expose Noema to simple action/efference-consequence relationships before testing ambiguous causal situations.

This may teach the operational significance of intervention channels without telling Noema which causal structure is correct in the later test.

### Human demonstration

Patrick or another agent may demonstrate actions in the shared world.

Noema receives the ordinary observable consequences and communication. It does not receive a hidden semantic statement such as `THIS_IS_THE_CORRECT_SKILL` unless that statement is itself ordinary fallible communication.

### Repeated grounded communication

Patrick may repeatedly use a signal while pointing, presenting, acting, correcting, or coordinating.

The repeated alignment is curriculum. Meaning/reference remains something Noema must infer and generalize.

### Structured exploration opportunities

The evaluator may arrange worlds so useful interventions or informative experiences are reachable.

This does not count as Noema exhibiting autonomous inquiry until Noema itself learns to select those opportunities when alternatives exist.

### Transducer support

Text characters, low-level visual features, or speech transcription may be supplied under the transducer ledger.

The supplied transformation is infrastructure, while higher-level grounding can still be acquired.

## Stronger forms of scaffolding that require explicit attribution

Some curricula can import substantial domain structure without literally supplying labels.

Examples:

- always presenting one object at a time before multi-object scenes;
- always ensuring agents move autonomously while non-agents do not;
- always pairing one word with one referent;
- always making the teacher correct and literal;
- always giving immediate consequences after actions;
- always presenting clean task boundaries;
- always making useful abstractions spatially contiguous.

These may cause Noema to learn a useful prior from the training distribution.

That is legitimate development, but later evaluation must include worlds where the learned regularity changes or fails before claiming a broad concept.

## Curriculum-induced prior versus innate prior

A learned developmental bias is not the same as an innate architectural bias.

For example:

- innate rule: `co-moving features belong to one object`;
- curriculum-induced prior: repeated experience makes co-motion a useful predictor of persistence;
- acquired transfer: Noema uses co-motion when useful but revises when deceptive co-motion is introduced.

The latter two can be legitimate learning, but the project should not confuse a curriculum-shaped prior with a universal truth discovered from first principles.

## Scaffold ledger

Every formal developmental program should record, at minimum:

- **target capability:** what the curriculum is intended to make learnable;
- **starting competencies:** what Noema already possesses;
- **environment restrictions:** what complexity is intentionally absent;
- **teacher behavior policy:** how demonstrations/corrections/examples are selected;
- **hidden evaluator knowledge used to construct curriculum:** if any;
- **learner-visible information:** exactly what crosses the boundary;
- **progression rule:** what causes the curriculum to become harder/change;
- **withdrawal test:** what happens when the scaffold is removed;
- **transfer test:** where the original scaffold regularities no longer hold exactly;
- **claim scope:** what passing the curriculum may and may not establish.

This is parallel to the transducer ledger but applies to experience selection rather than signal transformation.

## Adaptive curriculum risk

An adaptive teacher can accidentally become an external cognitive controller.

Suppose the evaluator observes Noema's hidden state and selects exactly the next example needed to repair the correct latent concept.

The resulting system may look highly developmental while relying on an omniscient external process to perform diagnosis and curriculum selection.

Adaptive curricula are allowed, but their role must be isolated.

### Required controls

When adaptive teaching is important to a claim, compare against at least one of:

- fixed curriculum;
- teacher using only ordinary observable behavior;
- randomized but matched exposure;
- removal of hidden-state access from the curriculum controller.

If capability disappears when omniscient curriculum control is removed, the claim belongs partly to the external teacher system.

## Patrick as teacher

Patrick can be a rich developmental influence without becoming a truth oracle.

His teaching may include:

- demonstration;
- naming;
- correction;
- explanation;
- questions;
- joint attention;
- social reinforcement;
- collaboration;
- deliberate challenge or misleading cases during evaluation.

But Patrick's communication enters as ordinary agent-produced evidence.

Noema may learn Patrick-specific reliability, conventions, preferences, and history.

A capability should eventually survive periods without Patrick where the capability does not logically require his presence.

## Reward/valence scaffolding

External reward shaping deserves the same scrutiny as semantic labels.

If every intermediate step toward a complex behavior receives hand-authored reward, the project has supplied substantial procedural guidance.

That may be useful for bootstrapping, but it weakens claims of self-generated goal formation or skill discovery.

Prefer, where feasible:

- sparse consequences grounded in the developmental world;
- primitive valence whose scope is explicit;
- learned intermediate structure rather than a designer-authored reward for every desired substep.

When shaping is used, record exactly what it specifies.

## Task-boundary scaffolding

Evaluator-defined episodes are useful for experiments but can become hidden semantic structure if Noema receives them.

A hard learner-visible `episode reset` or `task ID` may simplify memory, credit, and context inference dramatically.

Therefore distinguish:

- evaluator-only run boundary;
- physical/perceptual world reset Noema can observe;
- learner-visible explicit task identifier;
- internally learned context/episode boundary.

Claims about temporal abstraction, continual learning, or context inference must account for which of these were supplied.

## Scaffold withdrawal test

A developmental scaffold earns legitimacy when Noema can continue functioning after the support is reduced or removed, within the scope of the claimed capability.

Examples:

- a learned term remains usable when Patrick stops repeating demonstrations;
- a skill survives new surface conditions;
- object-like persistence survives clutter after clean single-entity training;
- causal learning survives longer delays after immediate-consequence curriculum;
- social reliability learning survives a less predictable teacher.

Failure after withdrawal does not automatically invalidate the curriculum; it narrows the claim to scaffold-dependent performance.

## Anti-curriculum-overfitting tests

A mature developmental benchmark should sometimes reverse or violate early curriculum regularities.

Examples:

- contiguous features belong to different processes;
- one entity splits or merges;
- autonomous motion comes from a non-agent mechanism;
- an apparently controllable process is produced by another agent;
- a familiar speaker becomes mistaken;
- a familiar word is used metaphorically or differently by another speaker;
- immediate positive valence predicts a later bad outcome;
- a once-useful skill becomes harmful after a regime change.

The purpose is not trickery. It tests whether Noema learned revisable evidence-sensitive structure rather than fossilizing its childhood curriculum as universal law.

## Developmental ordering is a hypothesis

The eventual curriculum sequence should itself remain falsifiable.

If a later capability is easier or more natural to develop concurrently with an earlier one, the project should not preserve a stage order merely because the evaluator roadmap is sequential.

The evaluator isolates capabilities for scientific clarity.

The developing Noema may legitimately co-develop:

- world modeling;
- communication;
- skill;
- social learning;
- value;
- memory;
- self/world organization.

Do not mistake experimental gating for a claim about how cognition must develop.

## Claim language examples

Weak/overstated:

> Noema learned language from scratch.

Stronger:

> With character-level text supplied as a transducer and repeated grounded interaction with Patrick, Noema acquired reference and repair behavior that transferred to held-out referents and degraded when grounding was removed.

Weak/overstated:

> Noema discovered objects.

Stronger:

> After curriculum exposure to simple continuous scenes without learner-visible object IDs or segmentation, Noema acquired a persistent entity-like representation that improved occlusion prediction and transferred to cluttered scenes; performance degraded under the relevant ablation.

The second form is less dramatic and much more scientifically useful.

## Current consequence

Future developmental designs should carry both:

- a **transducer ledger** for what transformations enter Noema;
- a **scaffold ledger** for how experience is deliberately arranged.

Together these establish a clean boundary among infrastructure, curriculum, and acquired cognition.

The project should use scaffolding aggressively when it makes learning tractable, but never hide what the scaffold contributed.
