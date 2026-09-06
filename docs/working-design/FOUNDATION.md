# Noema working foundation

Status: **BRAINSTORMING / PROVISIONAL / NOT AN APPROVED ARCHITECTURE**

## Core direction

Build the persistent thing that understands and predicts a world first, while developing grounded communication as a first-class developmental track rather than making language the substrate of cognition.

Language is not assumed to be the substrate of cognition. LLMs, tokenization, semantic/pragmatic models, and existing AI architectures remain optional candidate tools. Communication may begin early as perceptual and action signals whose meanings must be learned through interaction with the world and other agents.

The current hypothesis is a persistent predictive cognitive architecture, not a proven foundation. Design must remain falsifiable and architecture should follow target capabilities rather than familiar AI components.

## Provisional environment decisions

- Continuous 3D simulated world.
- Structured perception for the target learner.
- Initial perception is clean; noise, occlusion, uncertainty, and mistaken identity are introduced later as controlled challenges.
- Multiple embodied agents exist from the beginning.
- One target learner interacts with multiple **scriptable** agents whose behavioral rules can remain hidden from the learner.
- The learner must be able to distinguish self-caused changes from changes caused by other agents.
- Intracommunication inside the learner is first-class, not an implementation detail.
- Internal communication uses both direct subsystem-to-subsystem messaging and a shared workspace.
- Internal messages are provisionally hybrid: typed/inspectable structure plus learned latent payloads.

## Grounded communication stance

Patrick should be able to communicate with Noema during development. Speech, text, gesture, demonstration, correction, and other agent-produced signals may enter as observations, but their meaning, referents, pragmatic force, reliability, and speaker-specific usage must be learned rather than supplied as privileged semantics.

Noema should eventually produce communicative signals through its own action interface. Text and voice are acceptable modalities, but successful communication must depend on learned world and agent models rather than conversational imitation alone.

Development also needs an operator-facing diagnostic channel so Patrick can inspect Noema before mature language exists. Human-readable diagnostic interpretation must remain separate from Noema's learned communication and must not feed privileged labels or evaluator conclusions back into the learner.

See `COMMUNICATION_INTERFACE.md` for the current communication and operator-interface boundary.

## Provisional motivational / viability model

Use a hybrid drive system:

- physical and cognitive viability both matter;
- viability is homeostatic pressure rather than an absolute survival command;
- a very small innate drive layer;
- capacity to learn new persistent drives from experience;
- error handling is architectural, not merely an optional drive;
- prediction error is evidence to diagnose, not an automatic command to change the model;
- persistent salience is important to learned-drive formation, but salience alone is insufficient; valence and recurrence/generalization also matter;
- primitive valence should be small and tied to innate viability needs; higher-order valence should primarily be learned.

## Developmental stance

Innate machinery should expose signals and learning capabilities while encoding as little interpretation as possible.

Current from-birth access pathways include chronoception, proprioception, interoception, metacognitive access, introspective access, action issuance/efference information, minimal homeostatic viability signals, and learning capacity.

Selfhood and body/world boundaries should be discovered rather than supplied as symbolic ground truth. An efference copy may exist as raw evidence of issued action; a pre-authored `THIS IS ME` fact should not.

The working learned-concept inventory includes nociception meaning, exteroceptive interpretation, somatosensation/body mapping, apperception, neuroception, alloception, affordance, allostasis, mentalization, epistemic drive, salience mapping, mereology, haecceity, substrate independence, beneception, persistent objects/agents, causal structure, higher-order drives, and abstraction/analogy/metaphor.

## Memory stance

Experience is continuous; durable memory should be selective. Decay, forgetting, consolidation, revalidation, and supersession are expected to be necessary cognitive functions rather than storage defects. Exact memory mechanics are intentionally deferred.

## Current caution

Do not add architecture merely because a familiar AI component exists. The target capabilities should determine the architecture. The design should remain falsifiable and should make it possible to distinguish actual learning, persistent modeling, self-correction, agency, developmental emergence, and grounded communication from scripted behavior or response imitation.

See `DEVELOPMENTAL_CONTRACT.md` for the current innate-versus-discovered boundary.
