# Noema objective reexamination — 2026-09-06

Status: **BRAINSTORMING / ARCHITECTURE AUDIT / NOT AN APPROVED IMPLEMENTATION**

## Purpose

Step back from the accumulated mechanism-level design and reexamine Noema objectively from first principles.

This document deliberately distinguishes:

1. target capabilities;
2. developmental/evidential constraints;
3. candidate computational requirements;
4. candidate mechanisms and experiments.

The goal is to prevent useful provisional machinery from silently becoming the definition of Noema.

## 1. Target capabilities — strongest surviving layer

Noema should be a persistent embodied learner that can:

- build and revise a model of itself and its environment from experience;
- predict consequences across multiple timescales;
- learn from observation and action;
- preserve and appropriately revise uncertain beliefs;
- form durable but revisable memory;
- develop action-relevant preferences, concerns, and commitments;
- plan and act under uncertainty;
- learn reusable skills rather than recompute every successful behavior from scratch;
- learn reusable representations and abstractions that transfer across changed surface form;
- model other agents and their differing information/history;
- communicate with Patrick and other agents through grounded interaction rather than inherited language semantics;
- improve not only what it knows, but aspects of how it learns, investigates, allocates effort, and corrects itself;
- remain capable of continued development without catastrophic forgetting, permanent self-sealing, or unrestricted self-rewrite.

These are capability targets. They do not imply a specific cognitive architecture.

## 2. Developmental and evidential constraints — strong, but must avoid purity traps

The central developmental rule remains useful:

> Do not claim Noema learned a capability when the architecture silently supplied the answer.

However, the stricter formulation is now:

> **Minimize unacknowledged semantic structure, not structure itself.**

Zero inductive bias is impossible. A useful innate bias is not a failure merely because it makes learning easier. The scientific obligation is to expose, document, ablate, and correctly attribute what the bias contributes.

Therefore:

- supplied low-level structure is allowed when explicit;
- semantic target concepts must not be credited as developmental achievements when they were materially encoded by the substrate;
- transducers may solve lower-level perceptual problems, but whatever they solve must be declared as supplied capability;
- evaluator labels, stable environment identities, hidden answers, or semantic role names must not leak into the learner unless an experiment explicitly changes that contract;
- acquisition, intervention, transfer, and ablation remain primary evidence for learned capability.

## 3. Current functional decomposition — useful, not established primitives

The existing five-part reduction remains a good checklist:

- provenanced signal flow;
- generative/modeling capacity;
- valuation/concern;
- competition/allocation/selection;
- plasticity across timescales.

But these should no longer be spoken of as established primitive organs.

Reasons:

- provenanced signal flow is partly an interface/data-integrity requirement;
- generative structure currently contains representation, inference, prediction, uncertainty, counterfactual simulation, compositionality, and more;
- competition/selection currently bundles attention, hypothesis selection, compute allocation, and motor/action choice, which may require different mechanisms;
- plasticity currently contains ordinary learning, consolidation, structural change, reopening, forgetting, proposal-policy learning, and metaplasticity.

Current status:

> **five functional pressures / responsibilities, not five proven computational primitives.**

Experiments may split or collapse them.

## 4. DGFW, EGSS, bounded hypothesis populations, graph bindings, and genealogy

These remain candidate mechanisms only.

The project should resist promoting any of the following into architectural truth before evidence forces the move:

- Dynamic Generative Factor Workspace (DGFW);
- Evidence-Guided Structure Search (EGSS);
- latent-process hypotheses;
- graph-like explicit slow structure;
- learned reusable operators/bindings;
- bounded populations of explicit hypotheses;
- hypothesis genealogy;
- anomaly-debt bookkeeping;
- explicit multidimensional confidence fields.

Each is useful insofar as it produces a measurable advantage in uncertainty handling, intervention learning, transfer, compositionality, local correction, sample efficiency, planning, or continual learning.

If a simpler continuous/distributed learner achieves the same relevant behavior under comparable resources, the explicit machinery has not earned itself.

## 5. Correction to the maturation idea

Patrick's `N_min` / `N_max` proposal exposed two legitimate problems:

- do not consolidate too early;
- do not deliberate forever.

But a literal loop count should not become the epistemic principle.

### N_min

A fixed minimum number of hypothesis loops can become bureaucracy:

- one highly diagnostic intervention may deserve rapid confidence movement;
- fifty repetitions of the same dependent evidence should not create fifty times the epistemic maturity.

The stronger principle is **evidence maturity**.

A candidate belief becomes eligible for consolidation based on the quality and diversity of evidence, opportunities for meaningful contradiction, relevant scope, calibration, and consequence of error—not merely repeated processing cycles.

A loop/event count may remain an engineering safeguard or benchmark control, but it should not create confidence or be treated as a universal cognitive law.

### N_max

Bounded deliberation survives the review more strongly.

The general requirement is contextual bounded cognition: additional inference, observation, intervention, memory retrieval, simulation, asking, action, or deferral competes for finite resources according to expected usefulness and cost.

A universal fixed number is unlikely to be mature architecture. Different problems should earn different amounts of cognition.

## 6. Confidence — do not hard-code a human epistemology spreadsheet

Predictive support, intervention support, calibration, scope, transfer, stability, challenger margin, and model-set adequacy are excellent **evaluation dimensions**.

They are not yet proven to require separate native confidence variables.

A future uncertainty representation is acceptable if those properties can be behaviorally or diagnostically recovered without explicitly storing each as a dedicated field.

The requirement is that Noema not collapse materially different epistemic situations into one misleading scalar—not that the implementation must contain the evaluator's chosen taxonomy.

## 7. Model inadequacy / none-of-the-above survives

One important concept from the latest work survives the audit:

> Noema must not assume that one member of its current explanatory set is correct merely because it is the least bad.

This is best treated as a capability requirement:

- detect when the current representational family is collectively failing;
- preserve unresolved inadequacy instead of false certainty;
- broaden or alter learning/search behavior when current forms cannot explain the evidence;
- keep useful existing substructure where possible rather than globally resetting.

The exact internal representation of `model inadequacy` remains open.

## 8. Underdesigned capability: skill learning

The current design spends much more attention on world understanding than on reusable competence.

Noema should eventually support a developmental path like:

`experience -> successful action sequence -> reusable skill/policy -> context-sensitive invocation -> adaptation when the skill stops working`

A system that must perform expensive counterfactual planning from scratch for every familiar activity has not developed efficient competence.

This does not yet imply a dedicated skill module. A skill may be a learned predictive/control structure, policy, operator, or another form that experiments justify.

## 9. Underdesigned capability: temporal abstraction

Noema currently has temporal order, multi-horizon prediction, latent processes, and memory, but it still risks representing life too granularly.

It must eventually learn useful temporal organization such as:

- short events;
- episodes;
- routines;
- procedures;
- projects;
- longer-lived contexts/regimes.

These levels should not require a fixed human hierarchy. The requirement is that repeated temporal organization can be compressed, recalled, planned with, and revised at useful scales.

Temporal abstraction is likely important to memory, skill learning, planning, language, and long-term identity continuity.

## 10. Underdesigned capability: delayed credit assignment

Tiny intervention worlds mostly test short-latency consequence learning.

Noema also needs to learn when a materially important consequence appears long after the action or belief that contributed to it.

The architecture must eventually demonstrate credit assignment across delay, intervening events, uncertainty, and competing causal explanations without retaining every raw event forever.

This is not currently solved merely by saying `provenance + memory + plasticity`.

## 11. General transducer principle

The project should stop deciding sensory purity modality by modality.

Use the general rule:

> **A transducer may supply a lower-level transformation, but the transformation's contribution must be explicit and may not be credited to Noema as a learned cognitive achievement.**

Examples:

- keyboard/UTF-8 encoding may be supplied without claiming Noema learned orthography;
- speech-to-text may be used operationally without claiming Noema learned speech perception;
- low-level visual features may be supplied without claiming Noema learned the sensor physics that produced them;
- later end-to-end sensory learning can be evaluated separately if scientifically useful.

This prevents unnecessary reinvention of sensors while keeping capability claims honest.

## 12. Reexamine cognitive viability as primitive motivation

Physical and cognitive viability were previously grouped together as primitive homeostatic pressures.

That conflates two distinct things:

- **operational integrity:** conditions under which Noema can continue functioning correctly;
- **motivational concern:** states that influence what Noema seeks or avoids.

Operational integrity can be an engineering constraint without being an innate desire.

The design should not assume that intelligence requires an intrinsic motivation to preserve its own software substrate. Whether and how self-preservation-like concerns emerge should remain a separate question.

Physical simulated homeostasis may still be useful as a minimal source of directional valence in embodied developmental worlds, but its exact role also remains empirical.

## 13. Epistemic/conative separation survives strongly

The principle remains:

> **Desirability may influence what Noema investigates or chooses, but desirability must not directly manufacture evidential confidence.**

This remains one of the cleanest architectural constraints currently identified.

The exact implementation of the separation remains open.

## 14. Experiment A survives, but only as a narrow falsifier

Experiment A remains useful because:

- passive evidence is deliberately non-identifying;
- intervention adds decisive information;
- the learner is evaluated as a streaming persistent system;
- calibration matters before evidence permits commitment;
- transfer and ablation are required;
- continuous baselines are allowed to defeat explicit-structure candidates.

But Experiment A must not determine Noema's mature representation.

It tests a narrow claim:

> Can a candidate remain appropriately uncertain under observational ambiguity and revise from intervention evidence under bounded continual-learning conditions?

A simple mechanism winning A should be preferred over a sophisticated one unless later capabilities force added structure.

## 15. Communication and operator-interface work survives

The strongest part is not the visual layout. It is the information-flow separation among:

- ordinary world/perceptual events;
- ordinary communication events;
- operator-only controls and diagnostics.

Patrick can communicate with Noema from early development without language becoming the substrate of cognition.

Human-readable diagnostic interpretation must remain distinguishable from Noema's own emitted communication and must not leak semantic answers back into the learner.

Patrick's testimony and correction remain evidence rather than privileged truth.

## 16. Strongest current architecture thesis

After removing mechanisms that have not earned foundational status, the strongest current thesis is:

> **Noema is a persistent embodied learner that maintains revisable predictive state about itself and its environment, learns from the consequences of observation and action across multiple timescales, allocates finite cognitive resources, develops action-relevant valuation without confusing desire with evidence, and can acquire reusable representations, skills, communication, memory, and learning strategies from experience.**

This is a target-level architectural thesis, not an implementation description.

## 17. Required hierarchy from this point forward

Future design material should explicitly classify claims into four levels:

### Level 1 — target capability

What Noema must demonstrably be able to do.

### Level 2 — developmental/evidential constraint

What must or must not be supplied, and what evidence counts as learning.

### Level 3 — candidate computational requirement

A kind of computation/state that appears necessary across multiple capabilities, still subject to falsification.

### Level 4 — candidate mechanism / experiment

DGFW, EGSS, graph-like binding, bounded hypothesis populations, maturation controls, specific uncertainty representations, experiment designs, etc.

A Level 4 mechanism moves upward only when competing implementations repeatedly fail without the underlying requirement.

## 18. Immediate design consequences

1. Do not add further mechanism-level architecture until the existing corpus has been classified against the four-level hierarchy.
2. Treat the five-function/five-primitive vocabulary as provisional functional decomposition, not established anatomy.
3. Keep DGFW/EGSS and explicit structural machinery fully contestable by simpler baselines.
4. Revise maturation language away from literal-loop certainty toward evidence maturity; retain bounded deliberation as a contextual resource principle.
5. Add skill learning, temporal abstraction, delayed credit assignment, and transducer attribution to the capability/evaluation frontier.
6. Reopen the assumption that cognitive operational integrity must be innately valenced.
7. Preserve the epistemic/conative firewall and interaction-information boundaries unless evidence exposes a better formulation.

## Current verdict

Noema has a strong and increasingly falsifiable **research program**.

It does not yet have a justified final cognitive architecture.

That is the correct state at this stage.

The next useful work is consolidation and classification, not another named mechanism.