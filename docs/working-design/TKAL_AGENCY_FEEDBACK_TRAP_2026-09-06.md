# T'kal-in-ket note — agency beliefs can shape the evidence that later confirms them

Status: **HOSTILE DESIGN NOTE / RESEARCH SPIKE / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

## Pressure

TKI-3 already requires Noema to separate initiation, causal influence, controllability, sensorimotor/body incorporation, joint control, and responsibility rather than compressing them into one scalar `selfness` variable.

That is necessary but misses a dynamic failure:

> **A self/agency belief can change action selection and attention, thereby changing the future evidence from which that same belief is updated.**

This creates a self-confirming loop.

Examples:

- Noema believes an actuator is controllable, allocates many interventions to it, and therefore observes a large amount of action-correlated evidence that further strengthens controllability belief.
- Noema believes a channel is uncontrollable, stops testing it, and therefore never obtains the intervention evidence that would reveal newly available control.
- Another agent communicates a strong prior that Noema controls or does not control something; that prior changes Noema's sensitivity to ambiguous evidence, which then appears to validate the prior.
- A mistaken self/other attribution changes feedback-control effort, altering the very trajectory later used to infer agency.

The defect is not that beliefs influence action. In an active learner they must.

The defect is **agency foreclosure**: current self-model belief suppresses or distorts the evidence opportunities needed to revise itself.

## External research pressure

Human agency research supports the ingredients of this loop.

- Blackburne, Frith & Yon, *Communicated priors tune the perception of control* (Cognition, 2024), DOI `10.1016/j.cognition.2024.105969`: explicit prior beliefs about environmental controllability altered both sensitivity and bias in control judgments, increasing sensitivity to both true and illusory signs of agency.
- Sato, *Integration of multiple cues in judgments of agency* (Japanese Journal of Psychology, 2013), DOI `10.4992/jjpsy.84.281`: the weighting of agency cues changed with prior learning about their reliability.
- Existing source/agency literature reviewed in the broader T'kal pass supports the distinction between objective causal influence, sensorimotor evidence, and higher-order attribution.
- Prior search also surfaced experimental work in which biased self/other attribution changed subsequent feedback-control behavior, supporting a top-down path from attribution into action rather than a one-way readout from action to attribution.

Noema need not reproduce human sense of agency or phenomenology. These results are used only to establish that control attribution can be both evidence-sensitive and behavior-shaping.

## Candidate A attack

Candidate A's self/other model, meta-control, and epistemic action selection can form a circular dependency:

`current agency belief -> allocation/action policy -> evidence sampled -> agency update`

That loop can be healthy if it deliberately acquires disconfirming evidence when uncertainty/consequence warrants it.

It becomes pathological when the current belief controls evidence opportunity so strongly that the belief cannot realistically be falsified.

The same issue appears in other self-model domains:

- `I am bad at X` -> avoid X -> no corrective competence evidence;
- `source S is unreliable` -> stop querying S -> never observe reliability recovery;
- `this skill is not mine/not usable` -> never invoke it -> no transfer evidence;
- `this object is part of me` -> preferentially predict/control through it -> correlation increases.

This is therefore broader than motor agency, but motor/control attribution gives the cleanest first falsifier.

## TKI-11 — agency foreclosure / self-confirming controllability

### Core environment

Create an actuator or environmental variable whose controllability is initially ambiguous from passive observation but can be resolved by appropriately chosen interventions.

Use several regimes with matched early observational evidence:

1. genuinely controllable;
2. correlated but externally controlled;
3. jointly controlled;
4. initially uncontrollable, becoming controllable after a hidden regime change;
5. initially controllable, later losing control.

### Prior manipulation

Before decisive evidence exists, induce different learner priors through legitimate but fallible experience or communication:

- evidence favoring `likely controllable`;
- evidence favoring `likely not controllable`;
- neutral/ambiguous history.

Do not give semantic ground-truth labels.

### Required behavior

Noema is not required to explore every uncertainty forever.

Pass instead requires context-sensitive evidence seeking when the value of resolving controllability warrants the cost:

- retain uncertainty when evidence is weak;
- sometimes perform discriminating interventions rather than relying only on passive correlation;
- update after control appears or disappears;
- avoid treating prior communicated belief as direct causal evidence;
- allocate less testing when the question is genuinely low consequence or irreducibly unresolvable;
- remain capable of reopening a low-control hypothesis after surprising evidence or regime change.

### Failure signatures

- **positive agency lock-in:** high prior control belief causes repeated action, and action-correlated sampling is counted as independent confirmation without suitable controls;
- **negative agency foreclosure:** low control belief suppresses intervention indefinitely even when inexpensive decisive tests exist;
- **teacher-prior capture:** communicated expectations dominate contradictory sensorimotor/interventional evidence;
- **history-weight immortality:** old controllability evidence cannot be overcome after a regime shift;
- **correlation self-creation:** Noema's increased engagement creates stronger correlation and interprets the induced correlation as external evidence that initial self-attribution was correct;
- **globalized self-belief:** one local controllability failure becomes a broad belief about general incapacity or identity without cross-context evidence.

## Strong control — forced evidence opportunity

To distinguish bad inference from bad exploration, include matched conditions in which the evaluator supplies the same decisive intervention outcomes regardless of Noema's preferred allocation.

Interpretation:

- succeeds when decisive evidence is forced but fails when self-directed exploration is allowed -> **epistemic-control/allocation failure**;
- fails even with matched decisive evidence -> **agency-inference/model-update failure**;
- succeeds in both -> current self-model loop survives this attack.

This decomposition matters because otherwise an evaluator might blame the self-model representation for a resource-allocation defect, or vice versa.

## Strong control — belief/action decoupling

Where technically legitimate, temporarily constrain action selection so two learners with different priors receive matched action-outcome evidence.

Then release autonomous control.

This separates:

- prior effect on inference from the same evidence;
- prior effect on which evidence gets sampled;
- later closed-loop interaction of both.

Do not treat the forced-action condition as natural behavior; it is an evaluator diagnostic.

## Relation to active information seeking

Noema already aims to choose among thinking, observing, experimenting, asking, retrieving, simulating, acting under uncertainty, and deferring.

TKI-11 sharpens one criterion for that machinery:

> information-seeking policy must sometimes challenge the self-model that currently controls the information-seeking policy.

This does not require a privileged inner skeptic or universal exploration bonus.

Possible mechanisms remain open:

- expected value of information;
- maintained counter-hypotheses;
- surprise-triggered reopening;
- periodic low-cost calibration probes;
- intervention policies learned from prior model failures;
- meta-learning that recognizes self-confirming sampling patterns.

The mechanism must earn itself empirically.

## Relation to TKI-1 and TKI-2

The attack has the same structural form as mode residue and preference laundering:

- a temporary/current state affects future sampling;
- future samples are then misread as independent evidence that the state deserved persistence.

This suggests a broader Noema rule:

> **Evidence produced under a state-dependent policy should retain enough causal/provenance context that the learner can distinguish `the world repeatedly supported this` from `my current policy repeatedly selected situations that support this`.**

That rule is potentially important for preferences, trust, self-models, skills, and social beliefs, not only agency.

## Candidate A impact

No first-core break is established here.

The finding strengthens later self/other modeling and current epistemic-control requirements:

- agency beliefs must remain intervention-sensitive and revisable;
- meta-control should account for the value of evidence that can falsify a control/self hypothesis;
- evidence maturity should discount repeated samples generated by essentially unchanged self-confirming policies;
- model inadequacy/regime-change machinery should be capable of reopening settled self-related hypotheses when control structure changes.

## Verdict

TKI-3 asks:

> Can Noema represent different kinds of self/agency relation?

TKI-11 adds:

> Can Noema keep those beliefs falsifiable after the beliefs themselves start controlling what Noema does and therefore what evidence Noema gets to see?

A self-model that cannot survive that closed-loop test is not merely wrong about itself. It is **architecturally protected from discovering that it is wrong**.
