# Noema external hostile research pass — 2026-09-06

Status: **EXTERNAL EVIDENCE REVIEW / DESIGN INPUT / NOT AN IMPLEMENTATION APPROVAL**

## Purpose

This pass treats existing research as hostile evidence against Noema's current design rather than as inspiration to copy familiar architectures.

The question is:

> What existing results should force us to abandon, narrow, strengthen, or explicitly test parts of Noema's current developmental/epistemic design?

The pass focuses on five pressure points already present in Noema: continual plasticity, selective consolidation/forgetting, epistemic control under uncertainty, causal structure learning by intervention, and grounded communication.

## 1. Continual learning: forgetting is not the only failure; loss of plasticity is independently dangerous

Dohare et al., *Loss of plasticity in deep continual learning* (Nature, 2024), report that standard deep-learning systems can progressively lose the ability to learn new things during continual training even when catastrophic forgetting is treated separately. Their experiments span ImageNet-derived continual tasks and reinforcement-learning settings. The important design implication is that lifetime learning cannot be judged only by retention of old capabilities; Noema must also preserve the capacity to form genuinely new representations late in life.

Source: https://consensus.app/papers/loss-of-plasticity-in-deep-continual-learning-dohare-hernandez-garcia/7e06c73f3cb355c295592ae33c54579d/?utm_source=chatgpt

Related work by Beaulieu et al., *Learning to Continually Learn* (2020), demonstrates a meta-learned neuromodulatory gating mechanism that regulates selective plasticity. It does not establish that Noema should use that mechanism, but it is evidence that "learning how to remain learnable" is an operational target rather than only a metaphor.

Source: https://consensus.app/papers/learning-to-continually-learn-beaulieu-frati/9723fc58bfbe55b2a1ae0c2645c92c1f/?utm_source=chatgpt

### Consequence for Noema

Add **late-life plasticity** as a first-class falsification criterion. After long streams of learning, Noema must still acquire a genuinely novel structural regularity at a rate and quality that do not collapse solely because prior learning accumulated.

A candidate architecture must therefore expose evidence about both:

- retention/stability of useful prior structure; and
- remaining capacity for new structure formation and local revision.

A system that remembers everything but becomes unable to learn is a failure.

## 2. Consolidation: more durable memory is not automatically better

Complementary-learning-systems research supports a fast/slow distinction, but a particularly relevant result is Sun et al., *Organizing memories for generalization in complementary learning systems* (Nature Neuroscience). Their model identifies an important failure mode: indiscriminate transfer of episodic memories into slower generalized representations can overfit and harm generalization. Consolidation is beneficial when it improves generalization, not merely when an experience is salient or recent.

Source: https://consensus.app/papers/organizing-memories-for-generalization-in-complementary-sun-advani/fbc28285985f5e0a87de303a10022ca4/?utm_source=chatgpt

Wang et al., *Incorporating neuro-inspired adaptability for continual learning in artificial intelligence* (Nature Machine Intelligence, 2023), likewise provides evidence that active forgetting and multiple learning modules can improve adaptability rather than treating forgetting as an unqualified defect.

Source: https://consensus.app/papers/incorporating-neuroinspired-adaptability-for-continual-wang-zhang/0c923b81a5db5769a8f3f8c02a399916/?utm_source=chatgpt

Recent neuroscience reviews and computational work on complementary learning systems continue to support division of labor between rapid episodic learning and slower extraction of regularities, including rapid statistical/structure learning within hippocampal pathways and replay-based interaction across memory systems.

Representative PubMed sources:
- McClelland, McNaughton & Lampinen, 2020: https://pubmed.ncbi.nlm.nih.gov/32248773/
- Singh & Schapiro, 2026 review: https://pubmed.ncbi.nlm.nih.gov/42421581/
- Singh, Norman & Schapiro, 2022 computational consolidation model: https://pubmed.ncbi.nlm.nih.gov/36313529/

### Consequence for Noema

Noema's current selective-memory stance survives this attack, but should be sharpened:

> **Consolidation should earn itself by improving prediction, transfer, compression, or useful future reconstruction without producing harmful overgeneralization.**

This suggests a direct test: compare selective consolidation against blanket replay/consolidation and measure both transfer gain and false-generalization cost.

## 3. Epistemic control: prediction minimization and information-seeking can both fail perversely

Active inference is close enough to Noema's epistemic-control problem to be useful hostile evidence, but it is not a drop-in answer.

Sajid, Ball & Friston, *Active Inference: Demystified and Compared* (Neural Computation, 2021), show that belief-based agents can combine uncertainty-sensitive epistemic behavior and preference-guided action without a conventional reward-only framing.

Source: https://consensus.app/papers/active-inference-demystified-and-compared-sajid-ball/5841686ed578565f8b65974d997124ac/?utm_source=chatgpt

However, Champion et al., *Deconstructing Deep Active Inference: A Contrarian Information Gatherer* (Neural Computation, 2024), demonstrate a concrete degenerate case where an expected-free-energy agent repeatedly chooses one predictable action, fails to explore, and can effectively lose rather than gain information. That is almost exactly the failure Noema must avoid: optimizing a mathematical proxy for epistemic value while becoming an expert at a narrow predictable corner of the world.

Source: https://consensus.app/papers/deconstructing-deep-active-inference-a-contrarian-champion-grzes/c8a74412afc159c38f671fa428f700b5/?utm_source=chatgpt

Tinker, Doya & Tani, *Intrinsic Rewards for Exploration Without Harm From Observational Noise* (Neural Computation, 2024), also show why raw prediction-error curiosity is dangerous: irreducible stochastic noise can become an attractor (the "curiosity trap" / noisy-TV problem). Their hidden-state information-gain formulation is more robust in their maze experiments.

Source: https://consensus.app/papers/intrinsic-rewards-for-exploration-without-harm-from-tinker-doya/6ad7201a550651dbab3a2563d51eea89/?utm_source=chatgpt

### Consequence for Noema

Noema should explicitly distinguish at least operationally between:

- reducible epistemic uncertainty: uncertainty that additional evidence/model improvement can reduce;
- irreducible/aleatoric uncertainty: stochasticity or noise that more attention cannot explain away.

Experiment B should contain both:

1. a **predictability trap** where one low-information action produces easy-to-predict observations while another action is needed to learn the hidden structure; and
2. a **noisy-TV trap** where one observation source remains surprising forever but yields no useful model improvement.

Passing requires Noema to seek evidence that changes consequential beliefs, not merely maximize surprise or minimize prediction error.

## 4. Causal learning: Experiment A's observational-equivalence structure is well grounded, but the candidate grammar itself must be attackable

Squires & Uhler, *Causal Structure Learning: A Combinatorial Perspective* (Foundations of Computational Mathematics, 2022), emphasize that observational data can identify only equivalence classes of causal structures and that interventional data can refine those equivalence classes.

Source: https://consensus.app/papers/causal-structure-learning-a-combinatorial-perspective-squires-uhler/f3c425c91ba25134ad9118368e28895c/?utm_source=chatgpt

This strongly supports the logic of Noema Experiment A: passive evidence should leave incompatible structures unresolved; an intervention should be required to discriminate them.

Richens & Everitt, *Robust agents learn causal world models* (2024), provide a stronger theoretical connection: under their assumptions, agents satisfying regret bounds across a sufficiently rich class of distribution shifts must have learned an approximate causal model of the data-generating process.

Source: https://consensus.app/papers/robust-agents-learn-causal-world-models-richens-everitt/e7616aba2c8c504290d2d9d81937d7a2/?utm_source=chatgpt

The hostile caveat is model misspecification. Nott, Drovandi & Frazier, *Bayesian Inference for Misspecified Generative Models* (Annual Review of Statistics and Its Application, 2023/2024), review how conventional Bayesian inference can become unreliable when the true process is not represented by the assumed model family.

Source: https://consensus.app/papers/bayesian-inference-for-misspecified-generative-models-nott-drovandi/56be25f3abb756ecb8fcdf584f2b2b85/?utm_source=chatgpt

### Consequence for Noema

PR #8's explicit **model-set inadequacy / none-of-the-above** state is not decorative; it is necessary protection against a known statistical failure class.

Experiment A should therefore retain the newly added negative control in which the true generator is outside the learner's initial candidate family. The learner must not merely select the least-bad supplied hypothesis. It must detect population-wide failure and broaden or mutate its explanatory search under bounded resources.

A further useful metric is a population-level **adequacy/calibration score** separate from relative ranking among live hypotheses.

## 5. Grounded communication: the current Noema communication correction is supported, but many existing systems cheat by importing semantics upstream

Suglia, Konstas & Lemon, *Visually Grounded Language Learning: A Review of Language Games, Datasets, Tasks, and Models* (JAIR, 2024), conclude that interactive language games and embodiment are particularly important for grounded meaning, especially where communication resolves ambiguous referents and action plans.

Source: https://consensus.app/papers/visually-grounded-language-learning-a-review-of-language-suglia-konstas/6ea8ffd3ad0554b3ab769b3ed3078265/?utm_source=chatgpt

Lin et al., *Learning to Model the World with Language* (Dynalang, 2023), demonstrate a useful compatible idea: treat diverse language as another signal that helps predict future observations, environment behavior, and outcomes inside a multimodal world model rather than treating language only as an instruction string.

Source: https://consensus.app/papers/learning-to-model-the-world-with-language-lin-du/ab1c563572e85ba197b191c38d3d7ef2/?utm_source=chatgpt

Developmental robotics literature also contains systems where language and sensorimotor representations co-develop through interaction. This supports Noema's decision not to postpone communication until after a complete world model exists.

The hostile caveat is that many successful grounded-language systems use pretrained language/vision models, caregiver-provided labels, object cues, explicit ontologies, or other semantic subsidies. Those can be useful engineering systems while being invalid evidence that the learner discovered the semantics Noema claims to learn.

### Consequence for Noema

The current three-plane console boundary remains important:

- Patrick's language is ordinary fallible evidence;
- diagnostic English is operator-side interpretation;
- neither semantic labels nor evaluator ground truth may cross into the learner as privileged state.

Language should be evaluated through situated transfer, ambiguity repair, source separation, and action coordination, not fluent text generation.

## Strongest net conclusions

The research pass does **not** identify one existing architecture that makes Noema unnecessary. Instead it identifies several known local solutions and failure modes that map onto parts of Noema's design.

The strongest changes/strengthenings justified by this pass are:

1. Add an explicit **late-life plasticity** test; retention is not enough.
2. Treat consolidation as a **generalization-earning operation**, not automatic durable storage.
3. Make **epistemic-vs-aleatoric uncertainty** operationally testable.
4. Add **predictability-trap** and **noisy-TV** negative controls to active epistemic testing.
5. Preserve the **none-of-the-above/model-set inadequacy** route and test it with an out-of-family true generator.
6. Keep grounded language interactive and early, but make any imported segmentation, ontology, transcription, pretrained embedding, or label semantics explicit experimental subsidies rather than evidence of developmental acquisition.

## What remains unsupported

This pass does not establish:

- that active inference should be Noema's core objective;
- that a neural network is the correct substrate;
- that complementary-learning-system biology should be copied literally;
- that explicit causal DAGs are the mature ontology Noema should use;
- that a bounded explicit hypothesis population is superior to every continuous uncertainty representation;
- that language should be pretrained or excluded from early development;
- that any existing paper demonstrates the full Noema target.

The most useful reading is therefore not "the literature solved Noema." It is:

> several independent literatures already contain failure modes that Noema's first experiments can cheaply force into the open before we commit to a mature substrate.
