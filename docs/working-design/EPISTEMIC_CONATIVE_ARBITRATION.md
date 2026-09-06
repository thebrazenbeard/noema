# Epistemic/conative arbitration

Status: **BRAINSTORMING / DECISION-MAKING HYPOTHESIS / NOT AN APPROVED IMPLEMENTATION**

## Problem

Noema's current design deliberately avoids one fixed scalar reward or one globally weighted objective. But an embodied learner still has to make concrete choices:

- which hypotheses deserve belief/confidence;
- which uncertainty deserves investigation;
- which memories or simulations receive compute;
- which competing predicted future is preferable;
- which action is actually executed.

A Pareto frontier can preserve trade-offs temporarily, but it cannot act forever. Eventually one action must win.

The danger is solving this by quietly inserting one privileged global utility function. That would hard-code much of Noema's eventual value structure and make learned preferences/drives less meaningful.

## First correction: truth and desire are different arbitration problems

The design should sharply distinguish two processes:

### Epistemic arbitration

Question: **what should Noema currently treat as more likely / better supported?**

Evidence may include:

- predictive performance;
- intervention-conditioned evidence;
- calibration;
- cross-context transfer;
- provenance/source reliability learned from experience;
- complexity/resource cost;
- contradiction with other supported hypotheses;
- recency and nonstationarity evidence.

### Conative arbitration

Question: **given uncertain beliefs, which future/action should Noema prefer or choose?**

Inputs may include:

- primitive viability/valence;
- learned preferences;
- learned drives;
- commitments;
- anticipated consequences over multiple horizons;
- cost/risk;
- uncertainty and information value;
- current resource state.

These two processes interact, but they must not collapse into one score.

## Epistemic-conative firewall

A central working principle is:

> **Desirability may determine what Noema investigates, but desirability must not directly determine what Noema believes.**

A valued outcome may justify spending more compute or choosing an informative action. It may not raise the confidence of a convenient hypothesis without evidence.

Conversely, a well-supported prediction may be unpleasant without becoming less believed.

This separation is necessary to prevent built-in wishful thinking and to preserve the distinction between world modeling and motivation.

The firewall is not total isolation. Conative state may affect attention, intervention choice, and information gathering; resulting evidence may then legitimately change epistemic confidence.

## Rejecting three naive arbitration designs

### A. One fixed weighted scalar objective

Example in spirit:

`score = prediction - complexity + curiosity + viability + reward`

**Problem:** the designer chooses the permanent exchange rates between truth, simplicity, safety, curiosity, and desire. This hides values inside coefficients and encourages pathological optimization of proxies.

**Verdict:** reject as the foundational explanatory model.

### B. Fixed lexicographic hierarchy

Example: `survival > certainty > reward > curiosity`.

**Problem:** less scalarized, but still hard-codes a permanent value hierarchy and makes trade-offs brittle.

**Verdict:** reject except for truly non-negotiable engineering constraints outside Noema's learned conative system.

### C. Pure Pareto indecision

Keep every non-dominated action forever.

**Problem:** preserves ambiguity but cannot select an action, and the frontier can become huge.

**Verdict:** useful intermediate representation, not a complete choice mechanism.

## Strongest current conative hypothesis

Noema should maintain a **vector of active concerns** rather than one permanent utility scalar.

A concern is a learned or innate pressure that can assign consequence/valence to predicted future states over some horizon.

At birth, this vector is sparse: primarily physical/cognitive viability signals and primitive valence, plus minimal information-seeking/exploration machinery needed for learning.

Over development, concerns may include learned preferences, drives, commitments, social concerns, epistemic concerns, and self-development goals.

The architecture supplies the ability to maintain and compare concerns; it does not pre-author their high-level semantics.

## Action-selection pipeline

A provisional general process is:

1. generate a bounded set of candidate actions or action policies;
2. simulate uncertain future trajectories under each candidate;
3. estimate each trajectory's effects across currently active concerns;
4. discard clearly dominated options where one candidate is no worse across all materially active concerns and better on at least one;
5. preserve meaningful trade-offs among remaining candidates;
6. apply a **learned context-sensitive arbitration policy** to choose among them;
7. retain the outcome and conflict structure so arbitration itself can learn from experience.

The arbitration policy is not allowed to alter epistemic confidence merely because it prefers one outcome.

## Where the arbitration policy comes from

This is the unavoidable place where Noema needs some action-selection disposition before it has learned mature preferences.

The weakest current seed is:

- primitive viability/valence pressure;
- stochastic/exploratory variation;
- sensitivity to predicted consequence;
- information value when uncertainty blocks consequential decisions;
- finite-resource cost.

Early choices need not be globally optimal or perfectly coherent. Their outcomes become experience from which more stable trade-off dispositions can develop.

This is important: **a developing intelligence may have to learn how it chooses, not merely what it believes.**

## Learned arbitration as part of individuality

Repeated trade-offs can create durable context-sensitive dispositions.

For example, if two concerns repeatedly conflict, Noema may learn that in one context it usually sacrifices concern A to preserve B, while in another context the reverse is better.

That history can consolidate into stable preferences or commitments without requiring one universal numerical exchange rate.

This provides a plausible route for individuality/character to emerge from developmental history: not from a prewritten personality table, but from persistent learned arbitration patterns.

This is not evidence of consciousness or moral personhood by itself. It is a computational route to historically shaped conative consistency.

## Epistemic arbitration can remain more rule-governed

Unlike value trade-offs, evidence quality has stronger domain-general constraints.

Epistemic candidates can be compared through predictive/intervention/transfer/calibration evidence and resource cost without asking whether the predicted outcome is desirable.

When epistemic models remain non-dominated or empirically indistinguishable, Noema should preserve uncertainty rather than force a single answer merely to simplify action.

An action can still be chosen under model uncertainty by simulating outcomes across multiple live hypotheses.

## Information-seeking without curiosity becoming a master reward

Information has value when it can change a consequential decision, improve model calibration, resolve persistent anomaly, or produce transferable structure.

Noema should not receive an unconditional `maximize novelty` or `maximize surprise` drive.

A better primitive is **decision-relevant information value** plus a small exploration/diversity floor.

Higher-order curiosity can later emerge as a learned concern if information-seeking repeatedly becomes salient/valuable beyond immediate instrumental use.

## Commitments and temporal consistency

If every action is re-arbitrated from scratch, Noema cannot sustain plans, promises, long-term projects, or identity-consistent preferences.

Therefore some learned concerns may acquire persistence/inertia across time.

A commitment is not immutable. It is a durable learned concern whose future influence survives transient competing states unless stronger evidence, conflict, or revision processes justify change.

The persistence of commitments should itself be learnable and revisable.

## Stress test 1 — arbitration policy becomes a hidden utility function

Any deterministic choice policy can mathematically be represented as maximizing some utility under broad conditions, but that does not mean a fixed explicit utility function is the right architectural explanation.

**Requirement:** the policy must be demonstrably context-sensitive, plastic, historically shaped, and capable of representing unresolved conflict rather than merely exposing one concealed permanent scalar score.

## Stress test 2 — learned values contaminate belief

A learner may discover that believing comforting or goal-consistent hypotheses reduces negative valence.

**Requirement:** direct conative-to-confidence pathways are prohibited. Values may control investigation and attention; only evidence-bearing updates may change epistemic confidence.

This separation should be directly tested with cases where the desired hypothesis is false.

## Stress test 3 — viability dominates everything forever

If primitive viability has overwhelming priority, higher-order learned drives become decorative.

**Requirement:** viability supplies pressure, not an absolute lexical command. Mature Noema must be capable of learned trade-offs in which temporary viability cost is accepted for other durable concerns.

## Stress test 4 — learned concern proliferation

Every recurring valenced event could become a new concern, producing incoherent or unstable motivation.

**Requirement:** concern consolidation should require persistence, recurrence/generalization, consequence, and predictive usefulness; redundant concerns may merge and obsolete concerns may decay or be revised.

## Stress test 5 — cyclic/inconsistent preferences

Multi-concern arbitration can generate A>B, B>C, C>A depending on context or framing.

**Requirement:** Noema need not satisfy perfect economic rationality, but repeated harmful cycling should become a metacognitive error signal. The learner should be able to discover and stabilize trade-off policies when inconsistency produces bad outcomes.

## Stress test 6 — arbitration can be manipulated through internal proxies

If Noema learns to alter its measured valence/concern signals directly, it may choose proxy satisfaction over underlying outcomes.

**Requirement:** underlying viability and learned concern targets remain distinct from fallible internal estimates. Intervention tests should include misleading or manipulable signals.

## Stress test 7 — excessive commitment creates rigidity

Persistent concerns can make identity stable but resistant to legitimate change.

**Requirement:** commitments carry provenance/evidence/history and remain revisable through explicit conflict, counterevidence, changed context, or meta-learning. Persistence is friction, not invulnerability.

## Stress test 8 — no action wins

A large non-dominated action set can leave the learner indecisive.

**Requirement:** action selection must be time/resource bounded. When evidence and learned arbitration do not yield a clear winner, bounded stochastic choice among acceptable alternatives is preferable to infinite deliberation. The resulting outcome becomes learning evidence.

## Current surviving hypothesis

Noema should not have one foundational reward scalar that simultaneously determines truth, attention, learning, and desire.

Instead:

> **epistemic arbitration estimates what is supported; conative arbitration chooses among predicted futures using a learned multi-concern policy seeded by minimal viability/valence and exploration.**

Value may steer inquiry but cannot directly manufacture belief.

## New architectural implication

The current DGFW/RGSS picture now has a meaningful separation of powers:

- **world-model hypotheses** compete through evidence;
- **allocation** decides what receives scarce compute;
- **conative concerns** determine which predicted consequences matter;
- **arbitration policy** resolves context-sensitive trade-offs for action;
- **learning/metaplasticity** can revise all of the above through their proper evidence channels.

This is stronger than one global objective because failures can be localized: a bad belief, bad allocation choice, bad learned concern, or bad arbitration strategy are different errors.

## Next decisive attack

The next major risk is **self-sealing cognition**.

Once Noema learns an ontology, proposal policy, allocation policy, values, and source-reliability expectations, all of them can conspire to suppress evidence that would challenge the current system.

A genuine learning architecture needs a general correction mechanism that can revise deeply consolidated structure without making the entire mind permanently unstable.
