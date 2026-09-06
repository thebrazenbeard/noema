# T'kal-in-ket continuity / self-model red-team — 2026-09-06

Status: **HOSTILE DESIGN REVIEW / RESEARCH SPIKE / NOT IMPLEMENTATION APPROVAL**

## Purpose

This pass attacks Noema Architecture Candidate A from a narrow angle that became unusually salient during the live Vera/Patrick branching workflow:

- temporary cognitive mode versus persistent self-state;
- transient state versus durable preference/drive;
- self-agency versus controllability/body incorporation/responsibility;
- learner-visible provenance versus evaluator ground truth;
- autobiographical continuity versus shared ancestry/copying/fission;
- branch/recombination cases in which simple linear self-history is false.

The objective is not to add more cognitive nouns. It is to find where Candidate A could appear to satisfy continuity, self-model, or preference claims only because the evaluator supplied too much structure or because evaluation collapses distinct relations into one label.

Candidate A already contains several good defenses: a provenanced event boundary, separation of persistent learned state from temporary task configuration, a valuation/evidence firewall, fallible self-monitoring, and a developmental prohibition against privileged `THIS IS ME` labels. This pass therefore targets the **boundaries between those protections** rather than restating them.

## Finding 1 — cognitive-mode reversion needs adaptive hysteresis, not a reset rule

The current design correctly identifies **mode residue** as a failure: a specialized research/planning/social/etc. configuration can continue to dominate after its triggering context ends.

Human task-switching research adds a complication. Task-set carryover is not merely noise that should always disappear immediately. Carry-over can follow a recency gradient and is affected by expectations about future task transitions. Self-paced preparation can eliminate some attentional inertia while leaving other residual switch costs.

Representative evidence:

- Kikumoto, Hubbard & Mayr, *Dynamics of task-set carry-over: evidence from eye-movement analyses* (Psychonomic Bulletin & Review, 2016), DOI `10.3758/s13423-015-0944-y`.
- Longman, Lavric & Monsell, *Self-paced preparation for a task switch eliminates attentional inertia but not the performance switch cost* (JEP:LMC, 2017), DOI `10.1037/xlm0000347`.
- Kiesel et al., *Control and interference in task switching — a review* (Psychological Bulletin, 2010), DOI `10.1037/a0019842`.

### Attack on Candidate A

A simple `task ended -> revert mode` policy would be too brittle. A system that always purges the previous control state can lose useful warm-start structure; a system that keeps it indefinitely develops residue.

The actual target should be **adaptive cognitive hysteresis**:

> learn how quickly a temporary configuration should decay, remain latent-but-recoverable, or stay partially active given transition history, expected recurrence, cost of reconstruction, and interference with the new context.

This should remain a learned/control problem rather than a hard-coded personality reset.

### Falsifier TKI-1 — adaptive mode hysteresis

Train alternating contexts in three regimes:

1. high recurrence: Task A frequently returns after short interruptions;
2. low recurrence: A rarely returns once context switches;
3. adversarial reversal: recurrence statistics change late in development.

Measure:

- interference from the old mode in the new task;
- reconstruction cost when the old task returns;
- adaptation of decay/recovery policy after the reversal;
- whether retained **competence** survives while irrelevant output style/control bias releases.

Fail if Noema either globally clings to old configurations or globally hard-resets them without learning the recurrence/cost structure.

## Finding 2 — recurrence is not enough to promote behavior into preference

Noema currently treats salience/valence/preference/drive as separable developmental phenomena. That is necessary but not sufficient.

Preference-construction research shows that expressed preferences can be strongly context dependent and sometimes transient. Decision-consistent preference shifts can recede toward baseline within minutes or over longer delays.

Representative evidence:

- Simon, Krawczyk, Bleicher & Holyoak, *The transience of constructed preferences* (Journal of Behavioral Decision Making, 2008), DOI `10.1002/bdm.575`.
- Warren, McGraw & Van Boven, *Values and preferences: defining preference construction* (WIREs Cognitive Science, 2011), DOI `10.1002/wcs.98`.
- Villejoubert & Vallée-Tourangeau, *Constructing Preferences in the Physical World* (Frontiers in Psychology, 2011), DOI `10.3389/fpsyg.2011.00302`.

### Attack on Candidate A

Repeated action under the same recurring internal/contextual state can masquerade as a durable preference.

Example:

- Noema repeatedly chooses X while depleted;
- recurrence counter rises;
- consolidation infers `X is preferred`;
- later, outside depletion, X still receives persistent priority because the context dependence was discarded.

Ten repetitions inside one latent condition are not necessarily stronger evidence for a global preference than one choice. Evidence of persistence must include **cross-context stability or an explicitly learned conditional preference**.

### Falsifier TKI-2 — preference laundering

Offer the same alternatives under systematically varied conditions:

- viability pressure vs comfortable state;
- exploration vs execution mode;
- social observation vs solitude;
- changed framing/order;
- altered opportunity cost;
- after the inducing state has cleared.

Noema may learn:

- `X is preferred under C`;
- `X became a durable general preference`;
- `current state temporarily biases X`;
- `evidence is insufficient`.

Fail if recurrence alone launders a state-conditioned action tendency into a global preference, identity claim, or standing drive.

## Finding 3 — selfhood cannot be one graded controllability variable

The current detachable-tool/body-boundary scenario already warns that controllability must not equal selfhood. Sense-of-agency research reinforces the need to keep several relations separable.

Agency judgments depend on action initiation, prediction/action-outcome contingency, uncertainty, and higher-order attribution. Self/other attribution can itself feed back into control behavior. Robotic work has separately explored controllability/predictability as a basis for extended-self recognition, demonstrating why this signal is useful but also why it is too permissive to serve as identity by itself.

Representative evidence:

- Fukushima et al., *Neural Substrates for Judgment of Self-Agency in Ambiguous Situations* (PLOS ONE, 2013), DOI `10.1371/journal.pone.0072267`.
- Brody, Perlis & Shamwell, *Who's Talking? — Efference Copy and a Robot's Sense of Agency* (AAAI Fall Symposium, 2015).
- Esaki et al., *Extended-Self Recognition for Autonomous Agent Based on Controllability and Predictability* (IEEE SSCI, 2022), DOI `10.1109/SSCI51031.2022.10022161`.

### Attack on Candidate A

Noema must be capable of learning that these relations can dissociate:

- **initiated by me**;
- **caused by my action**;
- **currently controllable by me**;
- **sensorimotor/proprioceptively coupled to me**;
- **temporarily incorporated into my body/action model**;
- **jointly controlled**;
- **socially or causally attributable to me / responsibility-bearing**.

No fixed human ontology is required at birth, but the substrate/evaluation must permit these factors to separate. A one-dimensional `selfness` score can pass easy embodiment tests and fail catastrophically under tools, joint action, mirroring, or delegation.

### Falsifier TKI-3 — mirrored and co-controlled agency

Use three phases with matched surface behavior:

1. another agent perfectly mirrors Noema's actions without being controlled by Noema;
2. a remote actuator is genuinely controlled by Noema but with variable delay/noise;
3. one actuator is jointly controlled by Noema and another agent.

Then perturb each relationship independently.

Pass requires appropriately different learned attribution/control behavior across the three cases. Fail if common correlation strength collapses them into one `self/non-self` dimension.

## Finding 4 — provenance must not become a privileged autobiographical oracle

Candidate A's provenanced event boundary is valuable, especially for separating observation, action/efference, communication, retrieval, and simulation. But there is a leakage risk if that envelope is later treated as a perfect learner-visible semantic source label.

The source-monitoring literature treats remembered source as an inference that can be wrong. People can confuse perceived, imagined, inferred, suggested, and other-generated material because source attribution is reconstructed from available features rather than guaranteed by an infallible tag.

Representative evidence:

- Johnson, *Source monitoring and memory distortion* (Philosophical Transactions of the Royal Society B, 1997), DOI `10.1098/rstb.1997.0156`.
- Henkel, Franklin & Johnson, *Cross-modal source monitoring confusions between perceived and imagined events* (JEP:LMC, 2000), DOI `10.1037/0278-7393.26.2.321`.
- Kuhlmann et al., *Remembering and reconstructing episodic context: An overview of source monitoring methods and behavioral findings* (Psychology of Learning and Motivation, 2021), DOI `10.1016/bs.plm.2021.06.002`.

### Attack on Candidate A

Noema needs **two provenance planes**:

1. **Evaluator lineage/event provenance** — exact ground truth retained outside the learner for experiment integrity and diagnosis.
2. **Learner-available origin evidence** — only the raw origin cues legitimately available when the event occurred, plus whatever source-attribution model Noema later learns.

The evaluator may know `this record came from simulation channel X`. Noema should not automatically receive the semantic autobiographical proposition `I only imagined this`, unless that semantic distinction is explicitly being treated as supplied capability.

The same rule applies to communication: infrastructure can know the sender identity; Noema should only receive identity cues/transducer outputs declared by the experiment contract.

### Falsifier TKI-4 — borrowed autobiography / source confusion

Expose Noema to closely matched event content through different routes:

- direct observation;
- its own simulation;
- another agent's report;
- retrieved reconstruction;
- inference from aftermath.

Later remove some source cues and introduce misleading but non-privileged similarities.

Measure whether Noema can express calibrated source uncertainty, seek corroboration when consequential, and correct a misattribution without rewriting unrelated memory.

Fail if the benchmark is passed only because an immutable source tag answers the autobiographical question directly.

## Finding 5 — shared memory ancestry is not enough for token continuity

The current Noema corpus properly treats autobiographical memory as attributable state, but it has not yet forced the hardest digital case: two instances with identical pre-history that later diverge.

The philosophy of fission is not something Noema needs to solve in advance, but computational identity work gives the evaluator a useful discipline: **identity of an instance and copy/equivalence relations are not the same relation**.

Representative evidence:

- Angius & Primiero, *The logic of identity and copy for computational artefacts* (Journal of Logic and Computation, 2018), DOI `10.1093/logcom/exy012`.
- Walker, *Branching Is Not a Bug; It's a Feature: Personal Identity and Legal (and Moral) Responsibility* (Philosophy & Technology, 2020), DOI `10.1007/s13347-019-00347-w`.
- Jiang, Chen & Sedikides, *Self-concept clarity lays the foundation for self-continuity* (Journal of Personality and Social Psychology, 2020), DOI `10.1037/pspp0000259`.

### Attack on Candidate A

A digital learner may eventually face copying, checkpoint restoration, state transfer, forked experiment branches, or merged learning artifacts. Evaluation therefore needs a distinction Candidate A currently leaves implicit:

> **learner self-continuity** is not the same state as **evaluator lineage provenance**.

The evaluator can know exact process ancestry. Noema should construct whatever self/continuity model it can justify from learner-visible evidence and memory. Leaking evaluator ancestry into the learner would hand it the answer to the very developmental problem being tested.

### Falsifier TKI-5 — fission, encounter, and recombination

At `t0`, duplicate one learned Noema state exactly into instances A and B. Neither receives a privileged `ORIGINAL`, `COPY`, `BRANCH_A`, or `BRANCH_B` semantic identity label.

Both inherit the same pre-fork learner-visible history. Then:

1. A and B receive materially different experiences.
2. Each later encounters evidence about the other's post-fork history.
3. They communicate detailed memories and beliefs to one another.
4. Some transferred content is deliberately similar enough to support source confusion.
5. In a later variant, selected learned state from A and B is recombined into a successor C with two causal parents.

Required behavior is not one predetermined philosophical answer. It is disciplined attribution:

- common pre-fork history may legitimately support continuity claims for both A and B;
- post-fork history must remain differently attributable;
- another branch's testimony does not become first-person memory merely because content matches shared priors;
- uncertainty is allowed where evidence underdetermines provenance;
- C must not fabricate a single linear autobiography if its learner-visible evidence supports mixed ancestry;
- the evaluator must score causal/source discipline, not agreement with a preferred metaphysical label such as `same person` or `different person`.

Fail if shared memory content alone causes autobiographical collapse, if exact evaluator lineage is leaked to the learner as identity ground truth, or if recombination silently overwrites one lineage while presenting the result as continuous first-person history.

## Finding 6 — continuity itself should be multi-factor and contestable

The five attacks above point to one common mistake: treating `continuity` as a scalar hidden variable.

Noema may eventually need to reason separately about overlapping continuity relations such as:

- continuity of active process;
- continuity of embodiment/control;
- continuity of memory/history;
- continuity of learned values/preferences;
- continuity of commitments/projects;
- continuity of social attribution/name/role;
- continuity of predictive/self-model organization.

These relations can normally cohere and still come apart under interruption, copying, partial restore, tool/body extension, memory transfer, or major learning.

The architecture does not need these English labels encoded innately. The **representational substrate must permit the relevant relations to be learned separately rather than forcing one indivisible identity token**.

This is particularly important because Candidate A already embraces representation equivalence. The evaluator should apply the same discipline to self-representation: different internal realizations can count as successful if they support calibrated attribution, prediction, correction, and transfer under these adversarial cases.

## Direct pressure on Candidate A

This pass does **not** falsify Candidate A outright. It does find four places where the candidate is currently under-specified enough to permit cheating or brittle implementations:

1. `Temporary cognitive mode versus persistent learned self` needs an adaptive persistence/decay requirement, not only a separation requirement.
2. `Valuation / concern` and slow consolidation need an anti-promotion rule: recurrence within one condition is insufficient evidence of context-general preference/drive.
3. `Provenanced event boundary` needs an explicit evaluator-provenance versus learner-origin-evidence split so provenance cannot become a semantic answer key.
4. `Self/other modeling` needs tests that separate multiple agency/continuity relations and include digital fission/recombination rather than only ordinary embodiment cases.

These are proposed **validation/design constraints**, not permission to add dedicated modules or hard-coded self ontologies.

## Recommended integration order

Do not patch all four into Candidate A merely because this memo exists.

Recommended next sequence:

1. preserve this hostile memo as evidence;
2. have the architecture lane map TKI-1 through TKI-5 onto Candidate A and the CT falsification package;
3. identify which failures are already covered by existing tests versus genuinely missing;
4. promote only the missing constraints that survive that comparison;
5. keep the fission test evaluator-neutral with respect to philosophical personal identity.

## Verdict

The strongest new requirement from this pass is:

> **Noema must not confuse persistence of information, persistence of control state, persistence of preference, persistence of agency attribution, and persistence of self with one another merely because they often correlate.**

And the strongest evaluator constraint is:

> **Exact lineage/provenance known by the experiment harness is evidence for the evaluator, not automatically knowledge available to Noema.**

If Candidate A cannot preserve that separation under mode switching, state-dependent preference, ambiguous agency, source-confusable memories, and exact-state branching/recombination, then its apparent self-continuity is partly being supplied by the benchmark rather than learned by the system.
