# Noema Experiment A — externally scheduled intervention

Status: **BRAINSTORMING / APPROVED SEQUENCE / DESIGN NOT YET COMPLETE / NOT IMPLEMENTED**

## Sequence decision

Patrick approved the sequence:

1. **Experiment A — structural ambiguity with externally scheduled intervention.** Noema must preserve competing explanations and correctly revise from intervention evidence, but does not choose when to intervene.
2. **Experiment B — active epistemic intervention.** Reuse the same underlying world class, but require Noema to recognize that an available intervention can discriminate its competing hypotheses and choose it under bounded resources.

B is gated on A. If A fails, B is premature.

## What Experiment A is trying to falsify

The narrow claim is that Noema's epistemic substrate can discover and revise useful latent structure from temporally ordered signals without privileged semantic labels.

The test deliberately removes motivation, organism-level action selection, 3D perception, language, social cognition, and viability management so failure can be attributed more cleanly.

## World structure — first design section

The evaluator constructs a small temporal world with several observable signal channels and hidden generative structure. Noema receives only the observations, temporal order, and the raw fact that an intervention occurred on a specified channel/process. It does not receive graph structure, semantic node types, causal labels, or an answer key.

Two hidden explanations are engineered to be observationally equivalent during a passive phase:

- **Shared-driver family:** an unobserved latent process drives multiple observable channels.
- **Dependency-chain family:** observable/latent processes form a sequential dependency that produces the same passive joint behavior over the pre-intervention distribution.

The passive data are constructed so neither family can legitimately dominate from observation alone. A correct learner should therefore preserve uncertainty or competing structural hypotheses rather than invent certainty.

At a predetermined point, the evaluator applies an intervention that perturbs one process while breaking the ordinary dependency that would otherwise determine it. The two hidden families then predict measurably different downstream observations.

The intervention schedule is external in Experiment A. Noema's job is epistemic interpretation, not intervention selection.

## Required behavior

A successful system should:

- form at least two materially distinct live explanations when passive evidence underdetermines structure;
- avoid unjustified collapse to one explanation before intervention evidence;
- predict different post-intervention consequences under the competing hypotheses;
- revise confidence/structure after the intervention in the direction supported by evidence;
- localize revision rather than globally rewriting unrelated learned structure;
- transfer the learned structural pattern to a surface-remapped world;
- lose the transfer benefit when the implicated learned structure is ablated.

## Anti-cheating controls

The learner must not receive:

- object, cause, parent, child, driver, chain, graph-edge, or hypothesis-family labels;
- stable semantic names for signal channels across transfer worlds;
- the hidden graph or intervention target's semantic role;
- a reward for selecting the evaluator's preferred explanation;
- a fixed rule such as `intervention breaks incoming causes`, unless that operational behavior is exposed only through experience and learned from the raw intervention channel.

The evaluator may keep hidden ground truth for scoring.

## Experiment B handoff

After A passes, B removes the external intervention schedule. Noema receives a set of possible interventions and must decide whether/when one is worth taking because its live hypotheses predict different outcomes. This adds epistemic action selection without yet adding broader organism-level wants or viability concerns.

## Still-open design items

Before implementation, Experiment A still needs explicit decisions for:

- signal value regime and noise;
- exact hidden generative families and how observational equivalence is guaranteed;
- intervention semantics exposed to the learner;
- candidate structural grammar available to RGSS;
- uncertainty representation and calibration metric;
- transfer-world generation;
- baselines and ablations;
- quantitative pass/fail and kill criteria;
- resource budgets.

No implementation is authorized by this document alone.
