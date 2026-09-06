# Noema interface research pass — 2026-09-06

Status: **EXTERNAL RESEARCH / PROVISIONAL DESIGN PRESSURE / NOT AN APPROVED IMPLEMENTATION ARCHITECTURE**

## Objective

Pressure-test the current Noema communication/operator-interface design against developmental psychology and neuroscience, embodied/grounded language research, human-interactive robot learning, robot transparency, active clarification, and practical prototyping constraints.

This pass evaluates the current `COMMUNICATION_INTERFACE.md`, `OPERATOR_CONSOLE_SPEC.md`, `INTERACTION_EVENT_CONTRACT.md`, `DIAGNOSTIC_INTERPRETER_BOUNDARY.md`, and `COMMUNICATION_DEVELOPMENTAL_PROGRAM.md`. It does not approve implementation, select a UI framework, or create a Noema runtime.

## Working conclusion

The current interface direction is substantially defensible. The strongest existing choices survive external pressure:

- direct Patrick↔Noema communication should coexist with, but remain distinct from, diagnostic instrumentation;
- language should enter as an ordinary learnable signal rather than a privileged semantic substrate;
- the interface must preserve shared world context, action, correction, and provenance;
- operator controls and diagnostics must remain outside the learner-visible evidence stream unless deliberately routed back through ordinary interaction;
- Patrick must remain a fallible source, not a truth oracle.

The research does, however, expose six missing or under-specified interface requirements: **interactional contingency, mixed initiative, demand-driven transparency, co-adaptation audit, nonsemantic joint-attention affordances, and learner-controlled outward legibility.**

## 1. Interface should be a closed teaching/learning loop, not merely input plus diagnostics

Human-Interactive Robot Learning literature argues that the strongest paradigm is not `human provides data -> robot learns in isolation`, but ongoing bidirectional interaction in which the human and learner adapt to one another. A 2025 ACM THRI overview explicitly frames human-interactive robot learning around the interaction itself and identifies gains in sample efficiency, preference alignment, meaningful exploration, and safe adaptation.

A 2024 International Journal of Robotics Research survey similarly finds that developing learning and communication together can improve human teaching, trust calibration, and human-robot co-adaptation.

### Interface implication

The Noema Console should be designed around an **interaction loop**:

`Patrick acts/communicates -> Noema perceives/updates/acts -> Patrick perceives Noema's outward behavior -> Patrick adapts -> repeat`

Diagnostics are an optional observer aid around this loop, not the loop itself.

This strengthens the existing requirement that Noema have an outbound communication actuator from early development. It also means a future Noema that only answers when prompted would be an incomplete realization of the interface concept. Mixed initiative should eventually be possible.

## 2. Joint attention is useful evidence, but the UI must not manufacture “joint attention” as a primitive event

Developmental research strongly supports the role of caregiver contingency, gaze, pointing, temporal synchrony, and coordinated attention in early communication. A 2024 Annual Review of Developmental Psychology review argues that contingent caregiver adaptation supports attentional control, predictive models, goal-directed behavior, and intentional communication. A 2024 Frontiers in Integrative Neuroscience review similarly links behavioral synchrony and temporally contingent caregiver-child interaction with language development and broader cognitive systems.

Robot-learning studies also show that gaze/pointing and other joint-attention cues can improve learning efficiency. For example, a 2025 classroom robot study with 82 children found an advantage for timely joint-attention cues during vocabulary learning.

But the literature also contains a crucial warning: joint attention is neither universally necessary nor sufficient for word learning, and definitions based only on overt visual attention can be culturally and modality biased.

### Interface correction

The console should **not** expose a learner-visible event equivalent to `joint_attention=true`.

Instead, it should expose ordinary observable ingredients:

- Patrick's gaze or pointing direction when available;
- Noema's own orientation/action state;
- visible gesture trajectories;
- speech/text timing;
- object/world motion and consequences;
- mutual response timing.

“Joint attention” should be an evaluator/diagnostic interpretation of coordinated behavior, or a concept Noema may eventually learn, not an injected sensory label.

The current phrase “pointing/joint-attention tools” should therefore be interpreted as **attention-cue affordances for Patrick**, not semantic joint-attention events delivered to Noema.

## 3. Cross-modal timing is not incidental metadata; it is part of the learnable signal

The developmental literature repeatedly emphasizes contingency and synchrony at fine timescales. Which signal happened with, before, or after another signal can be part of the evidence that lets a learner discover reference, turn-taking, action consequence, and communicative intent.

The existing event contract already preserves timing, but the interface specification currently treats timing mostly as provenance/audit metadata.

### Research-driven strengthening

The interface should make **cross-modal temporal alignment an explicit contract**:

- one monotonic learner-visible event clock;
- preserved event onset and duration where meaningful;
- measured input/output latency at the transducer boundary;
- explicit recording of dropped, delayed, unavailable, or reordered events;
- replay that preserves learner-visible temporal relationships;
- no UI smoothing that silently changes temporal contingency during formal developmental tests.

Latency/jitter introduced by ASR, rendering, networking, buffering, or input devices is not merely a performance issue if Noema is expected to learn temporal relations from experience.

## 4. Grounded communication should remain multimodal and interactive

Embodied-language research supports the current decision not to make text the mind. Work on crossmodal language grounding shows that interacting with objects while receiving caregiver language can produce integrated perceptual/linguistic representations; broader grounded-language work argues that shared physical and social experience is central to meaning in communication.

This supports the current architecture boundary:

- typed text may be the first practical communication transducer;
- voice, gesture, gaze/pointing, demonstrations, and action context should eventually coexist;
- external transcription may be useful operationally but imports speech segmentation/spelling and cannot be credited to Noema as learned speech perception.

### Important falsifier

If Noema's apparent word/reference competence disappears whenever the specific pointing/gaze channel used in training is removed, that is evidence of shortcut dependence, not robust grounding.

Formal evaluation should therefore include modality substitution and cue-conflict tests.

## 5. Noema should eventually be able to ask, not merely receive

Interactive-learning and grounded-dialogue research consistently finds value in active querying. Agents can learn faster when they influence the teaching interaction, and clarification questions are especially useful when competing interpretations remain consequentially different. Recent grounded-dialog work ties the decision to ask for clarification to predictive uncertainty rather than a fixed supervised “ask now” classifier.

### Interface implication

Mixed initiative should be an explicit eventual capability of the same ordinary communication/action channel:

- Noema may request repetition, contrast, demonstration, or more evidence;
- Noema may redirect attention toward what would be informative;
- Patrick may answer or refuse;
- the response remains ordinary fallible evidence;
- querying has a cost so the learner cannot replace world learning with constant interrogation.

The console should not require a privileged internal `ASK_CLARIFICATION` API visible to the learner. It may expose operator-side diagnostics showing that an emitted behavior is interpreted as a query, but Noema's query behavior itself should emerge through learned action/communication.

## 6. Transparency should be demand-driven and provenance-aware, not maximal by default

The strongest pressure on the existing console layout comes from human-agent transparency research.

More transparency can improve team performance and trust calibration, but more is not automatically better. Demand-driven transparency—letting the human request deeper detail when needed—has been shown to improve trust/usability while avoiding information overload. Research on robot learning transparency also finds that outward cues can help teachers understand learning, but uncertainty cues can be misinterpreted.

### Interface amendment

The existing three diagnostic classes remain strong:

1. direct instrumentation;
2. deterministic derived diagnostics;
3. external interpretive gloss.

But the presentation should use **progressive disclosure**:

- default: compact state/uncertainty summary and major anomaly/change indicators;
- drill-down: underlying predictions, provenance, memory references, candidate alternatives, temporal traces;
- deepest layer: raw instrumentation and replay.

Full persistent diagnostics remain available in development mode, but the console should not assume that displaying every internal variable simultaneously is the best human interface.

This also creates a cleaner natural-interaction mode: Noema's own behavior dominates, diagnostics are requested when Patrick wants them.

## 7. Learner-controlled outward behavior must not be confused with wrapper-generated “social expressivity”

Human teachers respond to robot gaze, gesture, and expressive behavior, and some studies report that such cues improve teaching. But this creates a major Noema-specific trap.

A wrapper could generate a friendly face, gaze shift, “confused” animation, or uncertainty cue from diagnostic state and thereby improve Patrick's teaching—even if Noema itself never learned to communicate that state.

That would put part of the social intelligence in the interface.

### Boundary

Any outward cue claimed as Noema communication must be generated through Noema's own learned action/communication policy.

Operator-side visualization may render diagnostic state, but it must remain visibly diagnostic. It cannot masquerade as Noema's facial expression, tone, gaze, or communicative act.

This is the social equivalent of the existing “interpreter gloss is not Noema speech” rule.

## 8. Human input is useful precisely because it is imperfect

Interactive machine-learning research increasingly treats human feedback as noisy, uncertain, state-dependent evidence rather than ground truth.

The current teacher-dependence contract already gets the important epistemic rule right: Patrick is evidence, not truth.

The interface should preserve enough ordinary interaction information for Noema to learn source reliability and uncertainty cues if useful—speech hesitation, timing, contradiction, repeated correction, gaze/head behavior, etc.—without handing Noema an externally computed `patrick_confidence=0.63` field.

An explicit statement such as “I'm not sure” is acceptable because it is ordinary communication. A hidden operator confidence label is a different thing and should remain outside the learner stream unless the experiment explicitly studies such a transducer.

## 9. Co-adaptation creates an evaluator confound

If Patrick sees diagnostics and adapts his teaching to Noema's exact internal failure mode, Noema may improve partly because the teacher has become a bespoke external optimizer.

That is legitimate during development, but it contaminates claims about independent capability.

### Interface/evaluation requirement

The console should log not only learner-visible events but also **operator exposure state**:

- which diagnostics Patrick could see at each moment;
- when Patrick drilled into deeper instrumentation;
- when an interpreter gloss was shown;
- which operator-only controls were used.

Formal evaluation should compare at least some runs with diagnostics hidden/delayed and/or with held-out human teachers. This tests whether competence survives outside a highly co-adapted Patrick↔Noema dyad.

## 10. Proposed interface architecture after this research pass

The evidence supports a refinement of the existing console, not a replacement.

### Plane A — shared world/perception

Contains only ordinary learner-visible world consequences and transducer outputs. Includes multimodal timing and observable attention cues. Does not contain semantic object IDs, speaker roles, correctness, or “joint attention” labels.

### Plane B — learned social/communication loop

Patrick and Noema can both initiate signals/actions. Text may be first, but voice/gesture/gaze/demonstration can join later. Noema's questions, requests, repairs, and expressive actions must use the same learned action/communication machinery.

### Plane C — operator diagnostics

Direct instrumentation, deterministic derivatives, and explicitly separate interpreter gloss. Uses demand-driven/progressive disclosure and records what Patrick could see.

### Plane D — experiment/control

Pause/checkpoint/reset/scenario/recording controls remain outside Noema by default. Their learner-visible consequences, if any, re-enter through Plane A or B.

This is conceptually four operator-facing planes even though the current interaction contract groups world and communication as separate learner-visible event classes and operator controls as a third event plane. The distinction is UI/analysis-oriented, not a proposal to add a new semantic channel to Noema.

## 11. Interface-specific falsification tests worth adding later

1. **Temporal-contingency ablation** — jitter or decorrelate communication/world timing while preserving content; grounded reference should degrade if timing was genuinely informative.
2. **Cue substitution** — train with gaze/pointing and test with alternative shared-context cues; competence should not reduce to one hard-coded modality.
3. **Cue conflict** — make gaze, speech, and world evidence disagree; Noema should preserve uncertainty/source conflict rather than follow a privileged channel.
4. **Teacher fallibility** — Patrick or another teacher is occasionally mistaken; Noema should learn scoped reliability rather than obedience.
5. **Mixed-initiative value** — allow versus suppress active clarification; questions should concentrate where they reduce consequential uncertainty, not become compulsive.
6. **Diagnostic observer-effect test** — compare Patrick teaching with full diagnostics, demand-driven diagnostics, and blind diagnostics.
7. **Wrapper-expressivity kill test** — disable interface-generated social cues while preserving Noema-controlled outputs; claimed social communication should survive.
8. **ASR attribution test** — compare transcription and raw-acoustic routes; success through transcription cannot be counted as learned speech perception.
9. **Held-out-teacher test** — evaluate whether grounded communication survives interaction with a human who did not co-adapt throughout development.
10. **Replay fidelity test** — replay learner-visible multimodal events with preserved timing and verify equivalent learner updates within deterministic/stochastic tolerance.

## 12. Replit feasibility probe

A read-only search of Patrick's editable Replit apps found no existing app named/matching `Noema` at the time of this pass.

No Replit app was created. That was intentional: interface research should not quietly become implementation or consume build/hosting quota before the architecture/prototype gate is chosen.

When a UI prototype is justified, Replit is suitable for a **non-cognitive console mock/prototype** using synthetic or replayed learner data. Such a prototype can test layout, progressive diagnostics, event timelines, shared-world interaction affordances, and human workflow without being treated as evidence that Noema cognition exists.

## Net change to the current Noema concept

**Survives:**

- local Noema Console;
- early Patrick↔Noema communication;
- language as grounded signal, not mind;
- shared-world interaction;
- separate diagnostic interpreter;
- no privileged reverse diagnostic path;
- source fallibility and teacher independence;
- development/blind/natural modes.

**Strengthen:**

- fine-grained cross-modal timing contract;
- mixed initiative and active querying;
- demand-driven/progressive transparency;
- operator-exposure/co-adaptation logging;
- modality substitution/conflict testing;
- learner-controlled outward social cues.

**Correct wording/assumption:**

- do not treat a UI pointing tool as a semantic “joint attention” event;
- do not assume maximal diagnostic visibility is always the best interface;
- do not let wrapper-generated expressivity count as Noema communication.

## Selected evidence

- Baraka K, Faulkner TK, Biyik E, et al. **Human-Interactive Robot Learning: Definition, Challenges, and Recommendations.** ACM Transactions on Human-Robot Interaction. 2025;15:1–31. Consensus record: https://consensus.app/papers/humaninteractive-robot-learning-definition-challenges-baraka-faulkner/2c5d07fd41af54dca97e467431bf5470/
- Habibian S, Alvarez Valdivia A, Blumenschein LH, Losey DP. **A survey of communicating robot learning during human-robot interaction.** International Journal of Robotics Research. 2024/2025. DOI: 10.1177/02783649241281369.
- Wass SV, Phillips EM, Haresign IM, Amadó MP, Goupil L. **Contingency and Synchrony: Interactional Pathways Toward Attentional Control and Intentional Communication.** Annual Review of Developmental Psychology. 2024. DOI: 10.1146/annurev-devpsych-010923-110459.
- Eulau K, Hirsh-Pasek K. **From behavioral synchrony to language and beyond.** Frontiers in Integrative Neuroscience. 2024. DOI: 10.3389/fnint.2024.1488977.
- Akhtar N, Gernsbacher MA. **Joint Attention and Vocabulary Development: A Critical Look.** Language and Linguistics Compass. 2007. DOI: 10.1111/j.1749-818X.2007.00014.x.
- Jouen A, Matsunaka R, Hiraki K. **Once Upon a Time… Acquisition of Second Language Vocabulary Through Robotic Storytelling in Classroom Settings.** International Journal of Social Robotics. 2025;17:955–988.
- Heinrich S, Yao Y, Hinz T, et al. **Crossmodal Language Grounding in an Embodied Neurocognitive Model.** Frontiers in Neurorobotics. 2020. DOI: 10.3389/FNBOT.2020.00052.
- Bisk Y, Holtzman A, Thomason J, et al. **Experience Grounds Language.** EMNLP 2020. DOI: 10.18653/V1/2020.EMNLP-MAIN.703.
- Vered M, Howe PDL, Miller T, Sonenberg L, Velloso E. **Demand-Driven Transparency for Monitoring Intelligent Agents.** IEEE Transactions on Human-Machine Systems. 2020. DOI: 10.1109/THMS.2020.2988859.
- Matarese M, Sciutti A, Rea F, Rossi S. **Toward Robots’ Behavioral Transparency of Temporal Difference Reinforcement Learning With a Human Teacher.** IEEE Transactions on Human-Machine Systems. 2021. DOI: 10.1109/THMS.2021.3116119.
- Phaijit O, Sammut C, Johal W. **User Interface Interventions for Improving Robot Learning from Demonstration.** 2023. DOI: 10.1145/3623809.3623848.
- Gervits F, Roque A, Briggs G, Scheutz M, Marge M. **How Should Agents Ask Questions For Situated Learning?** SIGDIAL 2021 / arXiv:2106.06504.
- Naszádi K, Manggala P, Monz C. **Aligning Predictive Uncertainty with Clarification Questions in Grounded Dialog.** Findings of EMNLP 2023. DOI: 10.18653/v1/2023.findings-emnlp.999.

## Claim ceiling

This research supports interface requirements and test design. It does **not** establish that joint attention, multimodal fusion, active querying, transparency, any specific diagnostic layout, or any human-robot-learning algorithm is a cognitive primitive required by Noema. Those remain implementation hypotheses or interface constraints until experiments justify stronger claims.
