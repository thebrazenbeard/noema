# Noema learning and training research synthesis

Status: WORKING DESIGN RESEARCH / NOT IMPLEMENTATION APPROVAL
Date: 2026-09-06
Base: `main@20f7f699ea15b2300c4aa796b286bdab658f52a3`

Companion causal contract: `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`

Independent convergent contract draft: `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT_DRAFT.md`

Hostile update-order tests: `ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md`

Reconciliation note: `PR31_ONLINE_LEARNING_CONTRACT_RECONCILIATION.md`

## Research question

What should actually change inside Noema after experience, and what training regime best fits a persistent embodied learner that must learn online, preserve prior competence, remain uncertainty-aware under partial observability, and acquire grounded concepts from action rather than semantic labels?

## Short conclusion

The literature does **not** support one canonical training algorithm for Noema. It does support a stronger training architecture than the current vague idea of "continuous learning":

1. immediate recurrent state update from each learner-visible event;
2. continual action-conditioned predictive learning rather than a separate train/deploy split;
3. bounded experience replay as a strong default anti-forgetting baseline;
4. explicit separation between fast adaptation and slower consolidation;
5. calibrated uncertainty / model-inadequacy evidence rather than raw surprise;
6. information-seeking actions based on expected reducible uncertainty, not prediction error alone;
7. structural expansion only if a simpler recurrent predictive learner cannot absorb the evidence;
8. teaching/language as ordinary grounded evidence, not a truth-writing side channel;
9. optimizer mechanics treated as replaceable L4 realization, not part of the intelligence claim.

The first serious realization should therefore be a **recurrent probabilistic predictive learner + bounded replay + explicit online update ordering**, with more elaborate slow structure forced to beat that baseline.

## What the research says

### 1. World-model learning is a credible core, but current high-performing systems are not direct templates

DreamerV3 is strong evidence that an agent can learn a latent world model online and improve behavior through imagined trajectories across many domains. Its world model, actor, and critic are trained concurrently from replayed experience. However, Dreamer also bakes in a reward-learning/control stack and reconstructive representation objective that Noema should not adopt merely because it performs well.

Source: Hafner et al., *Mastering diverse control tasks through world models*, Nature 640 (2025), DOI 10.1038/s41586-025-08744-2.

TD-MPC2 provides another strong existence proof for **decoder-free latent predictive dynamics** used directly for action planning. Its relevance to Noema is narrower: latent action-conditioned prediction can support competent control without requiring full sensory reconstruction. Its task/value assumptions still make it a comparator, not the Noema architecture.

Source: Hansen, Su, Wang, *TD-MPC2: Scalable, Robust World Models for Continuous Control*, ICLR 2024.

### 2. Predictive-state framing remains especially attractive under partial observability

Predictive State Representations model state through predictions of future observable outcomes rather than requiring the learner to recover a privileged hidden world-state ontology. Research on dynamic partially observable environments also shows that predictive-model fit can be used to detect environmental change and reduce catastrophic forgetting.

This supports Noema's existing "predictively anchored, not predictively exhausted" direction: the architecture should require a sufficient revisable predictive state, while PSR-like mathematics remains a candidate realization rather than a semantic ontology.

Source: Dick et al., *Detecting Changes and Avoiding Catastrophic Forgetting in Dynamic Partially Observable Environments*, Frontiers in Neurorobotics 14 (2020), DOI 10.3389/fnbot.2020.578675.

### 3. Replay is too well-supported to omit from the minimal baseline

Online continual-learning literature repeatedly finds catastrophic forgetting under non-IID streams and identifies experience replay as one of the strongest general-purpose mitigations. Reviews place replay alongside regularization and structural plasticity; empirical work commonly finds replay-based systems stronger than otherwise similar systems without replay.

Noema should therefore treat **bounded replay as a mandatory baseline comparator**, even if the eventual architecture uses something better. Replay itself does not prove memory or intelligence; it is a learning mechanism whose information and compute cost must be charged.

Sources:
- Parisi & Lomonaco, *Online Continual Learning on Sequences*, 2020/2022.
- Hayes, Cahill, Kanan, *Memory Efficient Experience Replay for Streaming Learning*, ICRA 2019.
- Jiang, Fan, Li, *Advances in continual learning: A comprehensive review*, Expert Systems with Applications 294 (2025), 128739.

### 4. The optimizer trajectory matters, not only the objective

Continual-learning work identifies a "stability gap": even an objective approximating joint training can undergo substantial temporary forgetting because the **path of parameter updates** matters. This directly reinforces BT2's concern that Noema needs a causal prediction/update state machine rather than only a list of losses.

Noema must define, at design level, what state predictions are read from and when state, base parameters, candidate parameters, gates, replay, scoring, and optimizer state are mutated. Otherwise a retention/promotion result can depend on incidental scheduling.

Source: Hess, Tuytelaars, van de Ven, *Two Complementary Perspectives to Continual Learning: Ask Not Only What to Optimize, But Also How*, PMLR 249 (2024).

### 5. Fast/slow learning is well motivated, but should remain a functional distinction

Complementary-learning-system work and recent dual-memory continual-learning systems support separating rapid adaptation from slower consolidation. This does **not** justify hardcoding a hippocampus/cortex imitation or a mandatory two-module anatomy.

For Noema, the narrow requirement should be:

- some learner state can change rapidly from current evidence;
- some learned regularity can be protected/consolidated over longer timescales;
- the interaction between them is experimentally attributable;
- the simpler one-timescale baseline is allowed to win.

Recent examples include dual-memory continual systems and online robotics work using short-/long-term memory mechanisms, but these are evidence for the pressure, not for one architecture.

### 6. Structural growth is plausible, but dangerous as a default

Task-agnostic continual-learning work has shown dynamically growing expert populations can work without explicit task labels. That supports the feasibility of Noema's scoped structural expansion idea. It does not prove that Noema needs experts/adapters.

The research makes the current burden of proof sharper: structural growth should occur only when persistent, independently measured predictive inadequacy remains after cheaper repair. A no-explicit-slow-structure recurrent learner must remain a first-class rival.

Source example: *Online continual learning through unsupervised mutual information maximization*, Neurocomputing 578 (2024), 127422.

### 7. Raw surprise is the wrong intrinsic learning signal

Prediction error alone creates the classic "noisy TV" failure: stochastic but unlearnable outcomes can remain perpetually surprising. Research on curiosity under stochasticity explicitly separates reducible epistemic uncertainty from irreducible aleatoric uncertainty.

For Noema, information-seeking pressure should therefore track something closer to **expected information gain / reducible consequential uncertainty / model disagreement that evidence can resolve**, not raw surprise magnitude.

Sources:
- Jarrett et al., *Curiosity in Hindsight*, arXiv:2211.10515.
- Schmitt, Shawe-Taylor, van Hasselt, *Exploration via Epistemic Value Estimation*, AAAI 2023.
- Friston et al., *Active inference and epistemic value*, Cognitive Neuroscience 2015, as a normative reference rather than a required architecture.

### 8. Developmental robotics supports grounding through sensorimotor contingencies

Developmental robotics research strongly supports the idea that progressively richer cognitive and linguistic competence can be grounded in embodied interaction and sensorimotor contingencies. Work on self/other distinction also shows that comparing predicted sensory consequences of self-generated action against incoming sensory evidence can support primitive self/other discrimination without a semantic SELF label.

This is unusually aligned with Noema's developmental contract: communication should begin early, but word meaning, affordances, self/other structure, and causal interpretation should emerge from the coupling of perception, action, prediction, and social evidence.

Sources:
- Cangelosi & Schlesinger, *From Babies to Robots*, Child Development Perspectives 12(3), 2018.
- Jacquey et al., *Sensorimotor Contingencies as a Key Drive of Development: From Babies to Robots*, Frontiers in Neurorobotics 2019.
- Schillaci et al., *Is that me?: sensorimotor learning and self-other distinction in robotics*, HRI 2013.

## Optimizer implications

### Backpropagation / first-order optimization

For an initial differentiable realization, ordinary first-order optimization (for example Adam/AdamW or a simpler SGD-family baseline) should remain the primary engineering comparator because it is mature and data-efficient. The architecture should not depend on a particular optimizer.

Recurrent learning may use truncated temporal credit in an implementation, but the design must make explicit what causal history the learner is allowed to train from and what replay/state is counted in the resource budget.

### MeZO / zeroth-order optimization

MeZO is useful when backpropagation memory is the bottleneck or the objective is non-differentiable. Its published advantages are strongest for adapting **already pretrained language models**, where task alignment and prompts make zeroth-order optimization unusually tractable. That makes it a poor default for Noema's from-scratch fast learner.

It remains potentially interesting later for slow, sparse, bounded adaptation where memory pressure or non-differentiable objectives matter.

Source: Malladi et al., *Fine-Tuning Language Models with Just Forward Passes*, NeurIPS 2023.

### Meta-learned optimizers

Recent work shows that optimizers themselves can be meta-learned to improve continual learning. That should be a later Noema capability experiment, not a birth assumption: a pretrained optimizer can silently inject task-family priors and confuse "Noema learned how to learn" with "the designer pretrained the learning strategy."

Source: Vettoruzzo et al., *Learning to learn without forgetting using attention*, Conference on Lifelong Learning Agents / PMLR 274 (2025).

## Recommended first training stack to test

This is a **research recommendation**, not an approved implementation specification.

### Fast path

At every learner-visible event:

1. update bounded recurrent predictive state;
2. emit pre-update predictions for selected future learner-visible quantities conditioned on candidate actions/interventions;
3. observe the next event;
4. score predictive distribution/calibration before mutation;
5. update fast learner parameters from current evidence plus a bounded replay sample;
6. record uncertainty, provenance class, and resource cost.

The predictive targets should be learner-visible consequences, not evaluator semantic labels.

### Memory / replay

Use a small fixed-budget replay store with explicit policy and attribution. Compare at least:

- recency-biased replay;
- reservoir-style replay;
- error/novelty-prioritized replay with safeguards against noisy-TV capture;
- no-replay baseline.

Replay records must carry enough legitimate learner-side provenance to reproduce causal update ordering without adding hidden semantics.

### Slow path

Do **not** start by assuming adapters or a model population. First test whether the recurrent learner + replay can retain and revise sufficiently.

If persistent out-of-family failure remains, allow a bounded slow repair path to compete:

- regularized consolidation;
- a probationary soft-gated adapter;
- a growing expert/fragment mechanism;
- or another learned structural repair.

Each must beat the simpler learner on held-out prediction, intervention prediction, transfer, sample efficiency, or total resource cost.

### Information-seeking path

When action choice is underdetermined, compare interventions by predicted reduction in consequential epistemic uncertainty, while discounting irreducible stochasticity. Raw surprise must never be sufficient intrinsic reward.

## Mandatory comparators

The first empirical package should compare at minimum:

1. simple incremental predictive model / online system-identification baseline;
2. recurrent probabilistic predictor with no replay;
3. recurrent probabilistic predictor + bounded replay;
4. stochastic latent state-space/world-model realization;
5. only after those: scoped structural extension.

Dreamer-like and TD-MPC2-like systems are useful engineering reference families, not identity-level requirements. PSR-like predictive sufficiency is a particularly important conceptual comparator. A simple online shallow world model that avoids forgetting by construction should be allowed to embarrass the deep architecture if it performs better under equal information and resource budgets.

## Training claims Noema should avoid

- "from scratch" if pretrained semantic encoders, language models, or meta-optimizers contribute materially;
- "learned self" if self/action identity is supplied by interface metadata;
- "learned causality" if interventions are tagged with evaluator causal truth;
- "continual learning" if the system periodically resets or batch-refits from full history;
- "curiosity" if behavior is driven by raw prediction error in noisy environments;
- "memory" if success depends only on evaluator replay rather than persistent learner state;
- "meta-learning" if adaptation policy was pretrained and not independently attributed.

## Design consequence

The research strengthens one architecture boundary rather than adding a module:

> **Noema requires an explicit online learning-state transition contract.**

For every event, the design must define which predictive state is read, what is scored before learning, what can update immediately, what can replay, what can consolidate later, what survives checkpoint/restore, and which compute/information belongs to the learner versus evaluator.

That contract now exists as `ONLINE_LEARNING_STATE_TRANSITION_CONTRACT.md`, with `ONLINE_UPDATE_ORDER_HOSTILE_ATTACK.md` supplying the adversarial test layer. A concurrent independent draft is retained and explicitly reconciled rather than overwritten.

This directly addresses the strongest BT2 implementation-realizability pressure in the successor lane without retroactively repairing the frozen R1 subject or prematurely implementing anything.

## Open research frontier

The next high-value comparison is not "Adam vs MeZO." It is:

**PSR-like predictive state vs stochastic latent state-space/recurrent probabilistic state under the same online/replay/update contract.**

Only after that comparison is well specified should optimizer choice become the dominant question.
