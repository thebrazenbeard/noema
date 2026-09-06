# Noema design log

Status: **LIVE BRAINSTORMING NOTES**

## 2026-09-06

Initial direction established:

1. Start from first principles rather than assuming LLM/SPM/tokenizer architecture.
2. Primary target: a persistent system that understands and predicts a world, then later learns to communicate.
3. Environment: continuous 3D simulation.
4. Perception: structured and initially clean; harder perceptual uncertainty is added later as a controlled test.
5. Social environment: multiple embodied agents from the beginning.
6. Counterpart agents: scriptable agents with simple hidden rules, so the learner's inferences can be checked against known ground truth.
7. Intracommunication is at least as important as inter-agent communication.
8. Internal communication should support both direct messages and a shared workspace.
9. Internal messages should combine typed/inspectable structure with learned latent payloads.
10. Architecture work was deliberately paused to define observable intelligence criteria before adding more components.
11. Motivation: hybrid innate + learned drives.
12. Built-in error principle refined from "learn from my mistakes" to: treat error as evidence, determine what actually deserves to change, then revise and test.
13. Persistent salience is important to learned-drive formation, but salience alone is insufficient; valence and recurrence/generalization also matter.
14. Primitive valence should be minimal and tied to innate viability; higher-order valence should be learned.
15. Viability includes both physical and cognitive dimensions and should create homeostatic pressure rather than an absolute survive-at-any-cost command.
16. Selfhood should be discovered. The system may receive action-issuance/efference information, but should not be born with a symbolic `THIS IS ME` fact.
17. From-birth access pathways: chronoception, proprioception, interoception, metacognitive access, introspective access, action issuance/efference information, minimal viability signals, and general learning capacity.
18. Learned interpretations/concepts include nociception meaning, exteroceptive interpretation, somatosensation/body mapping, apperception, neuroception, alloception, affordance, allostasis, mentalization, epistemic drive, salience mapping, mereology, haecceity, substrate independence, beneception, persistent objects/agents, causal structure, higher-order drives, abstraction, analogy, and metaphor.
19. Working design rule: innate machinery should expose signals and learning capabilities while encoding as little interpretation as possible.
20. Memory: continuous experience does not imply permanent retention. Decay, forgetting, consolidation, revalidation, and selective persistence are treated as necessary cognitive functions. Exact mechanics are deferred.
21. Metaphor understanding is treated as a special case of analogical abstraction: learn relational structure, transfer it across domains, and later map figurative language onto that structure.
22. A developmental contract is now the primary framing device: distinguish innate machinery, learned concepts, and capabilities that must never be handed over as privileged ground truth.
23. Noema should eventually learn not only world facts but **how to learn from mistakes**: experience should be able to change evidence gathering, confidence formation, hypothesis revision, and testing strategy.
24. Perception is not identity. Stable object IDs are prohibited as privileged perceptual metadata; percept-instance IDs, if operationally required, expire with the observation.
25. Objecthood is also learned. Structured perception may expose organized sensory features, but should not pre-group them into privileged `OBJECT` records. Noema must learn both feature grouping/object formation and later persistent identity across time.
26. Initial spatial perception is egocentric. Noema should not receive privileged world coordinates; stable places, trajectories, and allocentric/world-relative maps are learned from movement, temporal continuity, and sensorimotor regularity.
27. A strictly linear developmental ladder is likely the wrong abstraction. Several capabilities should co-develop, so the working model is now a **developmental capability dependency graph**.
28. Candidate graph clusters: temporal prediction/sensorimotor contingency/feature binding; self-world/persistence/spatial mapping; causal intervention/affordance/error diagnosis; social agent modeling; learned salience/preferences/drives; meta-learning/transfer/abstraction/self-development.
29. Every developmental claim should ultimately require acquisition, ablation, intervention, and transfer evidence, with privileged labels/IDs/scripted policies/evaluator leakage treated as disqualifying explanations.
30. A proposed general substrate based on one persistent recurrent predictive latent state was adversarially stress-tested rather than accepted.
31. Stress-test result: **prediction appears necessary but is not sufficient**. A single point latent state collapses uncertainty; next-step prediction can reward surface shortcuts; prediction alone does not establish causation, exploration, wants, empathy, abstraction, planning, durable memory, or correct credit assignment.
32. Stronger surviving hypothesis: an evolving **belief state** over possible latent world states/explanations, preserving competing hypotheses and uncertainty, learning reusable structure through multi-horizon predictive compression, and treating Noema's own interventions as special evidence.
33. Independent pressures still appear necessary: primitive viability/valence, multiple memory timescales, selective salience/attention, and the capacity for information-seeking when uncertainty matters.
34. Controllability is evidence for selfhood but not identical to selfhood; tools, remote effectors, attachments, and other controllable structures require learned, potentially layered self/body/agency boundaries.
35. Agenthood must not be credited merely because behavior prediction improves. Social tests must require latent agent-specific state/history/information models to outperform surface dynamical prediction.
36. Abstraction should be tested as reusable compression and transfer across changed surface form, not merely good prediction on familiar cases.
37. Full adversarial review is recorded in `PREDICTIVE_SUBSTRATE_STRESS_TEST.md`.
38. A second functional review found **allocation/attention is functionally fundamental** because finite cognition must decide where scarce sensory, modeling, memory, learning, and planning resources go. The content of salience should largely be learned even if allocation capacity exists from birth.
39. `Homeostasis` was broadened to **valuation/motivation**: primitive viability and valence seed the system, while later preferences, drives, commitments, and values can become learned and multi-timescale.
40. The current functional skeleton is: **model/simulate; value/motivate; allocate/attend; act/intervene; learn/adapt**. Persistence/memory, uncertainty/provenance, multi-timescale operation, internal integration, and anti-cheating constraints remain cross-cutting requirements.
41. Concrete adversarial scenarios exposed a major substrate requirement not captured by the five loops: **dynamic relational binding/compositionality**. False-belief reasoning, analogy, role transfer, nested agent models, and later language require reusable relations that can bind arbitrary learned entities/states without a pre-authored ontology.
42. A second substrate requirement is **epistemic source/mode separation**. Observed, remembered, inferred, predicted, simulated, intended, and desired states may share representational machinery but must not silently collapse into one evidential status.
43. Learning must support **structural locality of revision** so a correction can change the implicated belief, relation, or learning policy without indiscriminate global drift.
44. Valuation likely cannot be a single scalar reward. Noema should eventually support multiple learned concerns over different timescales and construct derived goals over predicted future states.
45. Intracommunication/integration should preserve disagreement, confidence, provenance, and causal influence instead of flattening subsystem outputs into premature consensus.
46. Full functional review is recorded in `FUNCTIONAL_CORE_STRESS_TEST.md`; concrete scenario attacks are recorded in `ADVERSARIAL_DEVELOPMENTAL_SCENARIOS.md`.

## Open design frontier

Do not choose implementation architecture merely because a familiar AI family already provides some of these pieces.

The current functional skeleton survives, but the representational substrate now has strong constraints:

- open-ended latent structure;
- dynamic relational binding/compositionality;
- persistent uncertain state;
- epistemic source/mode separation;
- counterfactual simulation;
- localizable continual learning and metaplasticity;
- multi-timescale persistence and forgetting;
- contestable internal integration;
- intervention-sensitive learning;
- learned valuation and allocation.

The next design step is to compare broad implementation families against these requirements and reject families that need privileged labels or bespoke cognitive modules to fake the developmental capabilities Noema is supposed to acquire.
