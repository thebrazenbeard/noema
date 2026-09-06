# Noema working foundation

Status: **BRAINSTORMING / PROVISIONAL / NOT AN APPROVED ARCHITECTURE**

## Core direction

Build the persistent thing that understands and predicts a world first, then teach that thing to talk.

Language is not assumed to be the substrate of cognition. LLMs, tokenization, semantic/pragmatic models, and existing AI architectures remain optional candidate tools.

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

## Provisional motivational model

Use a hybrid drive system:

- a very small innate drive layer;
- capacity to learn new persistent drives from experience;
- error handling is architectural, not merely an optional drive;
- prediction error is evidence to diagnose, not an automatic command to change the model;
- drive consolidation appears likely to involve persistent salience plus valence, with recurrence/generalization determining whether a temporary state becomes a durable preference or drive;
- primitive valence should be small and tied to innate viability needs; higher-order valence should primarily be learned.

## Current caution

Do not add architecture merely because a familiar AI component exists. The target capabilities should determine the architecture. The design should remain falsifiable and should make it possible to distinguish actual learning, persistent modeling, self-correction, and agency from scripted behavior or response imitation.
