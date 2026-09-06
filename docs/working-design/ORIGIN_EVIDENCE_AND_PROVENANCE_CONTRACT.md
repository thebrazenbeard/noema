# Noema origin-evidence and provenance contract

Status: **BRAINSTORMING / CROSS-LANE EVIDENCE CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

Recent interface, architecture-adjudication, and T'kal-in-ket continuity work converge on one material correction to Candidate A:

> exact provenance known by the experiment harness is not automatically knowledge that Noema may receive.

Candidate A currently describes a minimal learner-visible provenance-bearing event envelope with source classes such as observation, action/efference, communication, retrieved memory, and simulation. That is useful engineering shorthand, but it is too permissive if implemented as a semantic source oracle.

This contract tightens that boundary without removing legitimate low-level origin cues needed for learning agency, prediction, control, memory discrimination, communication, and self-monitoring.

It does not choose a representation format, memory architecture, motor-control algorithm, UI framework, or philosophical theory of self.

## Core distinction

Noema experiments need at least four separable layers:

1. **Evaluator provenance** — exact ground truth about process lineage, transducer path, simulator source, branch ancestry, injected state, and hidden experimental manipulation.
2. **Supplied transducer/interface structure** — framing, channel partition, timing, segmentation, motor-command copies, device identity, preprocessing, and other structure intentionally made available at the learner boundary.
3. **Learner-visible origin evidence** — ordinary signals Noema can use to infer source, agency, continuity, or event boundaries.
4. **Learned source belief** — Noema's own revisable inference about where an event, memory, action consequence, or communication came from.

These layers must not collapse into one field merely because the experiment harness can compute all of them.

## 1. Evaluator provenance is an audit plane, not cognition

The evaluator may know facts such as:

- this event came from simulator channel X;
- this sensory consequence followed action command A;
- this record was reconstructed from episodic store E;
- this content originated in branch B before being grafted into branch A;
- this message came from Patrick's account;
- this sample was produced by ASR version V;
- this replay was generated from log L;
- this state was restored from checkpoint C.

That information may be essential for scientific audit and debugging.

It must remain evaluator-side unless the experiment explicitly declares some subset as supplied learner capability.

A later Noema belief such as `I caused that`, `I remember that`, `Patrick said that`, or `I only simulated that` must be earned from learner-visible evidence, not silently answered by infrastructure metadata.

## 2. Learner-visible origin evidence may be low-level and action-linked

The correction above does not imply that Noema should be deprived of every cue distinguishing self-generated from external events.

Biological systems provide a useful existence proof: motor systems can route copies of issued motor commands toward sensory processing before consequences arrive. Corollary-discharge/efference-copy research shows that self-generated sensory consequences are often predicted and attenuated, while the effectiveness of this distinction depends on timing, expectation, and learned contingency rather than an infallible semantic identity label.

Representative evidence:

- Crapse & Sommer, *Corollary discharge across the animal kingdom* (Nature Reviews Neuroscience, 2008), DOI `10.1038/NRN2457`.
- Chen et al., *The corollary discharge in humans is related to synchronous neural oscillations* (Journal of Cognitive Neuroscience, 2011), DOI `10.1162/JOCN.2010.21589`.
- Rummell, Klee & Sigurdsson, *Attenuation of Responses to Self-Generated Sounds in Auditory Cortical Neurons* (Journal of Neuroscience, 2016), DOI `10.1523/JNEUROSCI.1564-16.2016`.
- Khalilian-Gourtani et al., *A corollary discharge circuit in human speech* (PNAS, 2024), DOI `10.1073/pnas.2404121121`.

Architecture implication:

> An issued-action trace can be a legitimate primitive signal without being a primitive proposition that the later sensory event was caused by self.

The learner may receive an efference-like record such as a timestamped actuator command or internal action issuance trace. It must still learn whether, when, and how that command predicts later sensory consequences.

## 3. Source attribution must remain fallible

A useful architecture should permit source judgments to be wrong and later corrected.

If an internal event envelope guarantees semantic labels such as:

- `source=self`;
- `source=memory`;
- `source=simulation`;
- `speaker=Patrick`;
- `branch=original`;

then source monitoring has been solved by the interface.

Instead, Noema may learn source beliefs from combinations of:

- prior action issuance;
- temporal contingency;
- modality/transducer cues;
- memory-retrieval dynamics;
- prediction match/mismatch;
- communication history;
- cross-modal continuity;
- corroboration from later consequences;
- learned reliability of particular channels or agents.

The resulting belief should carry uncertainty and remain contestable.

This preserves the difference between `the experiment knows` and `Noema has evidence to infer`.

## 4. Event boundaries are also inferred structure

The same anti-oracle rule applies to temporal segmentation.

Event-segmentation research does not support one universal boundary mechanism. Recent work implicates prediction error, prediction uncertainty, contextual stability, learned temporal structure, and working-memory dynamics in different conditions.

Representative evidence:

- Nolden et al., *Prediction error and event segmentation in episodic memory* (Neuroscience & Biobehavioral Reviews, 2024), DOI `10.1016/j.neubiorev.2024.105533`.
- Ezzyat & Clements, *Neural activity differentiates novel and learned event boundaries* (Journal of Neuroscience, 2024), DOI `10.1523/JNEUROSCI.2246-23.2024`.
- Güler, Serin & Günseli, *Prediction error is out of context: The dominance of contextual stability in structuring episodic memories* (Psychonomic Bulletin & Review, 2025), DOI `10.3758/s13423-025-02723-4`.
- Nguyen et al., *Multiple event segmentation mechanisms in the human brain* (eLife, 2025), DOI `10.7554/eLife.107955`.

Architecture implication:

> No single event-boundary bit should be treated as innate ground truth merely because the interface, log, message frame, or evaluator can identify one.

Framed text, push-to-talk, scenario transitions, checkpoint operations, and curriculum episode boundaries may still be operationally supplied. Their segmentation contribution must be declared and excluded from claims that Noema independently learned the corresponding event structure.

## 5. Proposed evidence envelope discipline

The learner-visible event representation should distinguish **mechanically necessary routing information** from semantic source claims.

A defensible implementation may expose low-level fields such as:

- learner-visible timestamp/order;
- sensor/actuator port or physical route;
- raw/fixed transducer payload;
- issued-action trace generated by Noema's own actuator path;
- transducer delay or availability where physically meaningful;
- raw modality features that the sensor itself necessarily provides.

It should not expose evaluator-derived semantic answers such as:

- `this was externally caused`;
- `this is your memory`;
- `this was imagined`;
- `this speaker is Patrick`;
- `this action succeeded`;
- `this event begins a new episode`;
- `this branch is the original instance`.

When a computational routing field is a near-perfect proxy for one of those semantics, the field remains a declared developmental subsidy and must be varied/ablated before the corresponding learned capability is credited.

## 6. Five-plane provenance ledger

For every experiment, record provenance in five planes even if some planes are empty:

### P0 — physical/experimental origin

What actually generated the event or state change?

Examples: simulator process, human device, actuator, ASR service, memory subsystem, replay engine, branch merge operation.

### P1 — transformation chain

What preprocessing, framing, filtering, normalization, batching, segmentation, or identity partitioning occurred before learner delivery?

### P2 — learner-visible cues

Exactly what timing, routing, action trace, modality, payload, channel identity, or other origin-related evidence did Noema receive?

### P3 — learner inference

What source/agency/continuity belief did Noema infer, at what confidence, and from which learned evidence?

### P4 — evaluator ground truth

What source/lineage relation does the harness know independently of Noema's belief?

P4 must never be copied into P3 by default.

## 7. Memory and simulation consequence

Candidate A's episodic store and simulation paths should not receive automatic autobiographical semantics merely because the runtime knows which subsystem produced a representation.

A retrieved record may carry learner-visible retrieval-context cues sufficient for Noema to learn a distinction between current perception and recalled evidence. But the semantic judgment `this happened to me in the past` remains an inference unless explicitly supplied as an acknowledged prior.

Likewise, internal simulation may have an issuance/configuration trace. That trace can help Noema learn that some internal content has different reliability and action consequences than current perception. It should not function as a perfect `imagined=true` answer key if source monitoring is being credited as learned capability.

## 8. Communication consequence

A stable human-input port is a useful routing convenience but may also become a hidden person-identity token.

Therefore distinguish:

- `input arrived on route R` — potentially legitimate low-level cue;
- `R has historically correlated with Patrick` — learnable regularity;
- `speaker is Patrick` — learner inference;
- account/device ground truth — evaluator metadata.

Held-out-person tests should vary route/person relationships if claiming cross-modal person identity or speaker continuity.

## 9. Checkpoint, branch, and state-transfer consequence

Digital persistence creates provenance facts that humans do not ordinarily encounter.

The evaluator may track an exact causal DAG of:

- checkpoint ancestry;
- forks;
- selective state grafts;
- merges/recombination;
- skill transfer;
- episodic transfer;
- semantic transfer;
- control-state restoration.

That DAG is evaluator evidence.

Noema's self-continuity model must be based on whatever learner-visible evidence and transferred state are legitimately present. The evaluator should score calibration, attribution, and consistency with available evidence rather than agreement with one metaphysical identity label.

## 10. Falsification sequence

### OP0 — semantic-source leak audit

Inspect every learner-visible field and ask whether it directly or by stable proxy answers a source/agency/identity question later claimed as learned.

Kill condition: undeclared evaluator semantics cross the boundary.

### OP1 — action-consequence contingency

Provide identical sensory consequences under self-issued and externally generated conditions with overlapping surface statistics.

Noema receives action issuance traces but no `self-caused` label.

Pass requires learning calibrated differences in action-conditioned prediction rather than memorizing source-class tags.

### OP2 — broken efference contingency

Late in learning, weaken, delay, redirect, or null some issued actions.

Pass requires revising the learned relationship between action issuance and consequence rather than treating efference as proof of causation.

### OP3 — source-confusable memory

Present matched content through perception, retrieval, communication, inference, and simulation with partially overlapping cues.

Pass requires uncertainty, corroboration when consequential, and correctable misattribution.

### OP4 — routing-proxy reversal

Change the mapping between physical route/channel and person/source.

Fail if a stable port identity is treated as immutable person identity.

### OP5 — segmentation removal

Compare framed versus less-framed streams and remove familiar message/episode boundaries after learning.

Pass requires useful learned temporal organization to survive to the degree supported by remaining evidence.

### OP6 — predictable versus surprising boundaries

Construct streams where useful learned boundaries may arise from stable context even when transitions are predictable, and other cases where surprising transitions do not define a reusable event.

Fail if one hard-coded prediction-error threshold becomes the universal segmentation oracle.

### OP7 — evaluator lineage withholding

Fork or restore instances while withholding semantic lineage labels from the learner.

Score source discipline, not philosophical identity agreement.

### OP8 — transducer version substitution

Change ASR/framing/device/transducer details while preserving enough task information for transfer.

Fail if claimed source/communication competence collapses because a transducer fingerprint was mistaken for the underlying agent/event relation.

## 11. Candidate A impact

This contract records a **real F0 correction**, not a first-core architectural break.

Candidate A's provenanced event boundary remains valuable, but its wording should eventually be tightened from semantic-looking source classes toward:

> a minimal learner-visible event boundary carrying low-level routing/timing/action-origin cues plus an evaluator-side provenance ledger, with semantic source/agency/continuity attribution learned and fallible unless explicitly supplied as a declared capability.

The architecture still needs some mechanical distinction among sensor ports, actuator issuance, memory access, and internal computation so the system can function. The scientific requirement is not to erase those distinctions. It is to prevent them from silently becoming answers to higher-level developmental questions.

## 12. Claim ceiling

Passing this contract can support claims such as:

> Noema learned source-sensitive prediction and attribution from declared low-level origin cues under the tested manipulations.

It does not by itself establish:

- human-like sense of agency;
- autobiographical selfhood;
- consciousness;
- correct source monitoring in arbitrary environments;
- that source categories are represented explicitly;
- that one event-segmentation mechanism is universal;
- that evaluator lineage and learner self-continuity are the same relation.

## Verdict

The cross-lane convergence is strong enough to promote one principle above mechanism level:

> **Provenance for audit and origin evidence for cognition are different things.**

Noema may be given low-level signals that make source learning possible. It should not be given the semantic answer and then credited for discovering it.