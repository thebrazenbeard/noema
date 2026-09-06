# Noema capability-first design rules

Status: **BRAINSTORMING / DESIGN GOVERNANCE / NOT AN APPROVED IMPLEMENTATION**

Level intent: **L2 design/evidential discipline.**

## Purpose

The project has accumulated enough mechanism vocabulary that future brainstorming needs a simple discipline for preventing architecture from hardening accidentally.

These rules govern design reasoning, not Noema's cognition.

## Rule 1 — capability before mechanism

State the capability or failure being addressed before naming a mechanism.

Bad sequence:

`We need a hypothesis genealogy. What should it contain?`

Better sequence:

`Noema must avoid repeating discarded explanations and selectively reopen useful alternatives. What is the cheapest mechanism that achieves that?`

## Rule 2 — mechanisms must earn their nouns

A named mechanism is provisional until it produces a measurable advantage that simpler competitors cannot provide under fair constraints.

Names such as DGFW, EGSS, anomaly debt, hypothesis genealogy, workspace, factor, operator, or maturation gate do not gain architectural authority through repetition.

## Rule 3 — evaluator vocabulary is not internal ontology

Terms used to score a system may remain external descriptions.

Examples include:

- calibration;
- transfer;
- intervention support;
- confidence maturity;
- model inadequacy;
- skill;
- episode;
- source reliability;
- belief;
- desire.

Do not convert an evaluator category into an internal variable unless a computational reason requires it.

## Rule 4 — experiments isolate; they do not define

A successful solution to one benchmark earns only the capability claim that benchmark actually tests.

Experiment A can support claims about ambiguity, intervention evidence, continual revision, and transfer under its test conditions.

It cannot establish the mature representational format for language, social modeling, skill, or long-term agency.

## Rule 5 — supplied structure is allowed when attributed

Do not fetishize minimality.

An explicit, domain-useful inductive bias or transducer may be supplied when doing so improves tractability or usability.

Its contribution must be recorded and excluded from claims of developmental acquisition.

## Rule 6 — prefer behavioral necessity over inspectability preference

Inspectable explicit structures are attractive for debugging and science, but they must not be forced into Noema merely because humans prefer to read them.

If a distributed representation passes stronger intervention, transfer, ablation, calibration, and resource tests, inspectability alone is not sufficient reason to reject it.

## Rule 7 — no architecture by analogy

Existing neuroscience, cognitive architectures, LLMs, active inference, world models, probabilistic graphs, program induction, and object-centric systems are evidence and candidate tools.

None receives presumptive authority because it sounds biologically plausible, currently fashionable, or philosophically elegant.

## Rule 8 — separate operational constraints from motivational content

Runtime safety, memory limits, compute limits, process liveness, and simulator integrity are engineering facts.

They become Noema motivations only if the design explicitly chooses and justifies that mapping.

## Rule 9 — separate truth, value, and resource allocation

Evidence support, desirability, and compute priority can influence one another through legitimate pathways but should not be collapsed by convenience.

In particular, desired outcomes do not directly become more believed.

## Rule 10 — preserve the option to simplify

When a mechanism becomes unnecessary after a stronger formulation or baseline result, delete/demote it rather than preserving it because work was already invested.

Architectural sunk cost has no evidential weight.

## Rule 11 — add complexity only at demonstrated failure boundaries

If a simpler learner passes the current test, move to the next capability challenge before adding machinery.

Add structure when the simpler system fails in a way that can be localized to a missing computational requirement.

## Rule 12 — keep mature claims level-labeled

Design documents should identify whether their primary claim is:

- L1 target capability;
- L2 developmental/evidential constraint;
- L3 candidate computational requirement;
- L4 candidate mechanism/experiment.

Mixed documents are allowed, but the level of each important claim should remain clear.

## Rule 13 — challenge self-confirming developmental assumptions

If an innate prior makes the later target almost inevitable, test alternate worlds where that prior is wrong or less useful.

The goal is not to eliminate priors; it is to understand what they buy and what they prevent.

## Rule 14 — long-term agency needs more than epistemics

Do not let the first epistemic experiments monopolize design attention.

Future capability coverage must include:

- skill learning;
- temporal abstraction;
- delayed credit;
- planning across interruptions;
- communication development;
- social/source learning;
- motivation/value development;
- continual learning and forgetting;
- self-correction of deeply consolidated structure.

## Rule 15 — failure is architectural evidence

A clean failure that kills a favorite mechanism is a successful experiment.

Do not rescue a failing architecture by adding target-specific semantic heuristics unless the project explicitly chooses to supply that capability and downgrades the corresponding developmental claim.

## Current consequence

The next architecture work should increasingly look like:

`capability -> minimal evidence contract -> simplest candidate -> adversarial test -> baseline/ablation -> keep, split, demote, or kill`

rather than:

`interesting cognitive noun -> document -> subsystem -> another cognitive noun`.

This discipline is intended to keep Noema a falsifiable developmental intelligence project instead of a hand-built cognitive taxonomy.