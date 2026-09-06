# Noema skill, temporal abstraction, and delayed-credit frontier

Status: **BRAINSTORMING / CAPABILITY FRONTIER / NOT AN APPROVED IMPLEMENTATION**

Level intent: **primarily L1 target capability + L3 computational-requirement exploration.**

## Why this deserves separate treatment

The current Noema corpus is much stronger on world modeling, uncertainty, representation, and correction than on a different question:

> How does a learner become *competent* at doing things repeatedly over long periods of time?

Prediction and planning are not enough by themselves.

A system that must rebuild a long action sequence from scratch every time it performs a familiar activity may understand the world but still lack efficient learned skill.

Likewise, a system that only learns from immediate consequences cannot reliably develop long projects, habits, procedures, or delayed causal understanding.

This frontier therefore isolates three linked capabilities:

1. reusable skill acquisition;
2. learned temporal abstraction;
3. delayed credit assignment.

No dedicated `SKILL`, `EPISODE`, or `CREDIT` module is implied.

## 1. Reusable skill acquisition

### Target

Repeated successful interaction should be able to become a reusable competence that:

- invokes with less deliberation than first-time planning;
- remains sensitive to current context;
- can be interrupted or overridden;
- can be decomposed/recombined when useful;
- can be revised when its assumptions stop holding;
- retains enough causal linkage to outcomes for later improvement.

### Failure modes

#### Permanent replanning

Every execution requires expensive fresh search despite extensive successful experience.

#### Cached action script

A fixed sequence replays regardless of changed context.

#### Reward reflex

The system memorizes an action preference without representing conditions under which the behavior works.

#### Skill fossilization

A once-useful routine survives despite systematic failure because its execution became too automatic to re-evaluate.

### Candidate L3 requirement

Some learned structure must compress repeated successful sensorimotor/control organization into reusable policy-like behavior while preserving contextual gating and revisability.

The representation could be:

- a learned policy;
- a generative action operator;
- a temporal latent process;
- a predictive control chunk;
- another representation that earns the same behavioral properties.

No choice is made here.

## 2. Learned temporal abstraction

### Problem

A persistent learner experiences a continuous stream, but useful cognition cannot remain forever at one event-per-step granularity.

Planning, memory, communication, and skill all benefit from discovering temporal organization at scales such as:

- local transitions;
- recurring event patterns;
- episodes;
- procedures;
- routines;
- projects;
- longer contexts/regimes.

These are evaluator examples, not innate labels.

### Target

Noema should be able to discover when a sequence or interval deserves representation as a reusable temporal unit because doing so improves prediction, control, memory, transfer, explanation, or resource use.

### Anti-cheating rule

Do not supply fixed semantic boundaries such as `TASK_START`, `EPISODE_END`, `ROUTINE`, or `PROJECT` and later claim Noema learned temporal abstraction.

Externally imposed experiment boundaries may exist for evaluation/control, but learner-visible temporal organization must be explicitly declared if exposed.

### Candidate L3 requirement

The substrate must be able to represent learned structure with variable temporal extent and hierarchical/overlapping organization where useful.

A fixed universal hierarchy is not assumed.

## 3. Delayed credit assignment

### Problem

Many important consequences are separated from their causes by:

- long delays;
- unrelated intervening events;
- multiple contributing actions;
- hidden state;
- other agents;
- stochastic outcomes;
- later reinterpretation.

Immediate residual update is insufficient.

### Target

When a later outcome matters, Noema should be able to revise earlier implicated behavior/structure proportionally to evidence without globally rewriting everything that happened in between.

### Candidate L3 requirements

Some combination of the following appears necessary, but exact machinery remains open:

- retained influence/eligibility traces;
- episodic reconstruction;
- counterfactual comparison;
- hierarchical temporal structure;
- causal/intervention evidence;
- uncertainty over attribution;
- selective replay/re-examination;
- learned credit horizons.

The important point is not which mechanism is used. It is that long-delay learning must be demonstrated rather than assumed from the existence of memory.

## 4. Why these three capabilities interact

A useful skill compresses temporal structure.

A temporally abstract representation lets Noema reason about a procedure as one candidate unit while retaining access to lower-level details when needed.

Delayed credit can then update:

- one low-level action;
- one substep;
- the whole learned routine;
- the context-selection rule;
- or the higher-level project strategy,

depending on which level evidence implicates.

Without temporal abstraction, delayed credit becomes diffuse.

Without delayed credit, skills become difficult to improve from long-term outcomes.

Without skill consolidation, planning remains unnecessarily expensive.

## 5. Developmental test ladder

These are evaluator concepts, not implementation prescriptions.

### T1 — immediate reusable micro-skill

A short action pattern repeatedly succeeds under varying superficial conditions.

Evidence:

- execution becomes cheaper/faster;
- transfer survives superficial remapping;
- changed conditions interrupt or adapt the behavior rather than triggering blind replay.

### T2 — context-gated skill

The same action pattern succeeds in one context and fails in another.

Evidence:

- Noema learns when to invoke it;
- does not collapse to global `this action is good` preference.

### T3 — compositional reuse

Two learned subskills are useful in a novel sequence not previously demonstrated.

Evidence:

- Noema recombines competence rather than memorizing only whole trajectories.

### T4 — delayed outcome

A sequence produces its important result only after substantial intervening experience.

Evidence:

- relevant earlier decisions change after the delayed outcome;
- unrelated intervening competence remains substantially intact.

### T5 — misleading immediate reward/valence

An immediately attractive sub-action causes a worse delayed consequence than a less attractive alternative.

Evidence:

- Noema learns the temporal consequence structure rather than optimizing only immediate valence.

### T6 — skill regime change

A previously reliable routine becomes wrong because the environment changes.

Evidence:

- automatic competence degrades confidence/reopens;
- Noema returns to deliberation/learning;
- repaired skill can reconsolidate.

### T7 — project-scale behavior

A multi-stage objective requires preserving intent across interruptions and changing subplans.

Evidence:

- Noema can pause, resume, revise, and eventually abandon the project when evidence/valuation warrants;
- continuity is not just replay of a stored action list.

## 6. Baseline comparisons

A future implementation should distinguish at least:

- planner-only system with no reusable skill consolidation;
- cached-sequence system with no contextual revision;
- immediate-credit learner;
- full candidate with temporal abstraction and delayed attribution;
- relevant ablations of replay/eligibility/hierarchical representation where implemented.

The full system earns complexity only if it improves resource use, transfer, delayed learning, or robustness without creating rigid habits.

## 7. Important relationship to Experiment A/B

Experiment A and B remain useful epistemic falsifiers, but they do not meaningfully test this frontier.

Passing A/B would show some uncertainty/intervention competence.

It would not show that Noema can:

- learn skills;
- chunk behavior across time;
- maintain projects;
- assign delayed credit;
- automatize without fossilizing.

These need later experiments designed for their own failure modes.

## Current verdict

Skill learning, temporal abstraction, and delayed credit are not optional polish around a world model.

They are central capabilities for a persistent agent that must become more competent over developmental time.

The exact mechanism remains deliberately open.