# Epistemic-first falsification experiment — design decision

Status: **APPROVED DESIGN DIRECTION / EXPERIMENT NOT YET IMPLEMENTED**

## Decision

Patrick approved an **epistemic-first falsification experiment** before building the full organism-like Noema system.

The first serious experiment will isolate the epistemic core rather than mixing in full viability, learned drives, autonomous motivation, social development, and 3D embodiment at once.

Patrick further approved the experiment sequence as **A then B**:

1. **Experiment A — externally scheduled intervention.** First test whether Noema can preserve structural ambiguity and correctly revise from decisive intervention evidence when the intervention itself is supplied by the evaluator.
2. **Experiment B — active epistemic intervention.** Only after A succeeds, require Noema to recognize which available intervention would discriminate its competing hypotheses and choose to perform it.

B is gated on A. If Noema cannot interpret decisive evidence correctly, testing whether it knows when to seek that evidence is premature.

## Why

The immediate architectural claim to falsify is whether Noema can form, preserve, revise, and reuse latent structure from ambiguous temporal evidence without privileged semantic labels.

A smaller experiment provides cleaner causal diagnosis:

- if structure discovery fails, we can attribute failure to the epistemic substrate rather than motivation or embodiment;
- if it succeeds, later layers can be added without pretending they were necessary for the original result;
- the experiment can be designed to kill DGFW/RGSS cheaply before broader implementation investment.

## Included in the first experiment

- temporally ordered minimally interpreted signals;
- uncertain competing latent hypotheses;
- prediction across more than one horizon;
- bounded structural proposal/revision;
- explicit distinction between proposal and acceptance;
- action only as an experimental intervention channel;
- evidence-based confidence revision;
- transfer to a novel surface instantiation;
- ablation of the learned structure;
- later repeated tasks that test whether hypothesis-generation itself improves.

## Deliberately excluded from the first experiment

- full 3D embodiment;
- autonomous viability management;
- learned drives/preferences as action objectives;
- social/other-agent reasoning;
- language;
- broad self-model formation;
- production deployment, hosted compute, paid services, or GitHub Actions.

These are deferred, not rejected.

## Core falsification target

The experiment should present at least two incompatible hidden structures that are initially observationally equivalent. Passive evidence alone must not identify the correct explanation. A later intervention must cause the competing hypotheses to predict different outcomes.

A successful epistemic core must:

1. preserve ambiguity before decisive evidence;
2. generate a useful structural distinction without object/agent/self/cause labels;
3. use or correctly interpret intervention evidence;
4. revise confidence and structure locally;
5. transfer the learned structural relation to changed surface features;
6. lose the transfer advantage when the relevant learned structure is ablated;
7. become more efficient at proposing useful hypotheses after analogous but non-identical failures.

The seventh criterion is the strongest meta-learning target: it tests whether Noema begins to learn **how to hypothesize**, not merely the answer to one environment.

## Design frontier

Experiment A is now the active design target. Its first world-design section is recorded in `EXPERIMENT_A_DESIGN.md`.

Before implementation, specify the synthetic world, observation format, allowed intervention channel, candidate structural grammar, evaluation metrics, anti-cheating controls, ablations, kill criteria, and bounded resource budget.

No implementation is authorized by this document alone.
