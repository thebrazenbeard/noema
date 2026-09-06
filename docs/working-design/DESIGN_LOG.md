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

## Open design frontier

Do not choose implementation architecture yet.

The next design task is to build a **developmental capability ladder**: an ordered set of increasingly demanding capabilities that Noema must acquire through experience, with a falsification test for each rung showing how success differs from hidden scripting, privileged labels, memorization, or evaluator leakage.

Candidate early rungs to challenge rather than accept blindly:

- experience temporal change;
- form short-horizon predictions;
- discover persistent entities;
- discover controllability and self/world structure;
- distinguish self-caused from externally caused change;
- discover causal regularities;
- track individual other agents across time;
- learn agent-specific behavioral models;
- form and revise preferences;
- seek information to reduce consequential uncertainty;
- recognize and diagnose its own prediction/model errors;
- transfer learned relations to novel situations;
- form abstractions and analogies;
- develop higher-order drives and self-directed development.

The ordering is provisional. The next conversation should challenge dependencies between these capabilities before treating the ladder as architecture.
