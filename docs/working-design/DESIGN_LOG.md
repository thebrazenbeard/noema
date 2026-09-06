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

## Open design frontier

The next design problem is to define the smallest innate motivational/viability substrate that can support learning, endogenous drive formation, initiative, and self-correction without pre-programming a personality or desired high-level values.
