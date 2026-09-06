# RLPO minimality and circularity attack

Status: **BRAINSTORMING / L4 HOSTILE MECHANISM REVIEW / NOT AN APPROVED IMPLEMENTATION**

Date: 2026-09-06

Target: `COMPOSITIONAL_TEMPORAL_SUBSTRATE_OPTIONS.md`

## Question

Does the current Reusable Latent Process Operator (RLPO) proposal actually explain how compositional-temporal structure can be learned, or does it move the difficult parts into words such as `applicability`, `binding`, `operator`, `termination`, and `composition`?

This review does not attack the L3 requirement for reusable compositional/temporal structure. It attacks RLPO as the current strongest L4 realization.

## Initial verdict

RLPO remains a useful hypothesis, but the current formulation is **less minimal and more circular than it first appears**.

Four of its defining capabilities are themselves close to the unsolved problem:

1. discovering that two episodes instantiate the "same" reusable transformation;
2. binding different latent content into that transformation without fixed roles;
3. deciding when the transformation begins/continues/ends without supplied boundaries;
4. composing transformations in novel combinations without a supplied compatibility/type system.

If those four capabilities are already available in generic machinery, much of what RLPO claims to solve has already been solved before an RLPO exists.

Therefore RLPO cannot be credited merely for packaging those capabilities into an operator object.

## Attack 1 — recurrence detection may contain the abstraction answer

RLPO consolidation says a transformation earns reuse when it recurs across experience.

But "recurs" is not primitive.

Two trajectories may differ in:

- surface values;
- duration;
- number of participants/features;
- irrelevant distractors;
- coordinate frame;
- action realization;
- temporal warping;
- context;
- which latent variables carry analogous roles.

Recognizing that they instantiate the same transformation requires an equivalence/similarity computation with the right invariances.

If the designer supplies that metric, the metric may contain the abstraction ontology.

If the metric is learned, **that learning mechanism is at least as important as RLPO itself** and must be exposed as a separate candidate requirement/mechanism.

### Falsifier

Give the system recurring useful transformations whose surface statistics differ more than irrelevant distractor patterns do.

RLPO earns credit only if reuse tracks downstream predictive/control/transfer equivalence rather than a designer-chosen surface similarity.

## Attack 2 — dynamic binding may just rename semantic slots

RLPO avoids named argument roles by saying latent content is dynamically routed into an operator's active subspace.

That is not enough.

A routing system can still implement stable hidden slots such as:

- actor-like input;
- patient-like input;
- source/destination;
- object identity;
- controller/controlled variable;
- first/second argument.

Those slots need not have English names to constitute strong ontology priors.

Worse, successful rebinding requires preserving relational correspondence while content changes — exactly the compositionality ability RLPO is intended to explain.

### Falsifiers

- variable arity;
- role permutation;
- symmetric relations where no stable ordered roles are warranted;
- relations whose useful factorization changes by context;
- worlds where slot-like decomposition hurts prediction;
- equivalent behavior produced by distributed non-slot representations.

Passing requires behavioral transfer, not readable slot structure.

## Attack 3 — learned temporal extent risks boundary circularity

RLPO says temporal extent persists while the reusable process remains predictive/compressive/useful and ends under regime or applicability change.

But estimating "the same process is still active" already requires temporal abstraction.

A termination hazard does not remove the problem; it parameterizes it.

There is a circular route:

`need temporal chunks -> create operator with learned termination -> learn termination from whether the same chunk continues`.

The missing computation is what evidence makes persistence versus termination the better explanation without relying on presegmented training episodes.

### Stronger criterion

The candidate must compare at least:

- continue existing process hypothesis;
- terminate and return to unstructured dynamics;
- terminate and invoke another learned process;
- overlap/nest multiple processes;
- treat apparent boundary as noise;
- revise the process itself rather than ending it.

A single scalar hazard attached to one current operator may be too weak if real structure overlaps or nests.

## Attack 4 — composition assumes compatibility without explaining it

The planning sketch:

`B -> O_a -> B' -> O_b -> B''`

looks general, but composition only works if the output state of `O_a` lies in a region where `O_b` has meaningful learned semantics.

Under distribution shift, naive composition can create latent states never encountered during learning. A planner can then exploit model error.

More deeply, some learned transformations may be:

- noncommutative;
- nonassociative;
- mutually exclusive;
- order-sensitive;
- context-dependent;
- only meaningful when jointly active;
- destructive of variables needed by later transformations.

A hidden compatibility/type system would solve much of this — but would also be another supplied structural bias.

### Requirement

Composition must earn itself through predictive consequences and uncertainty under novel combinations, not through designer-declared compatible operator signatures.

## Attack 5 — invocation traces may make delayed credit circular

RLPO proposes compact influence traces based on which operator was invoked, what was bound, and what it predicted/emitted.

This improves credit locality **if the invocation decomposition is already correct**.

But delayed credit is one of the signals that may be needed to discover the useful decomposition in the first place.

A bad early operator boundary creates bad traces; bad traces reinforce bad credit; bad credit may fossilize the operator.

Required control:

- retain lower-level evidence sufficient to challenge operator-level attribution;
- compare operator-level credit against a less-structured trace baseline;
- allow later outcomes to split/merge/reassign earlier operator explanations;
- never make "active operator" an unquestionable causal parent simply because the controller invoked it.

## Attack 6 — universal substrate may become a bottleneck ideology

RLPO is attractive partly because one representation species could support perception, action, memory, planning, and communication.

But nature does not owe us architectural elegance.

A single universal operator substrate may be worse than heterogeneous learned structures that share only interfaces and evidence rules.

Forcing all reusable knowledge into RLPO form could:

- discretize phenomena better represented continuously;
- create artificial boundaries;
- make simple prediction more expensive;
- privilege procedural structure over static/distributed constraints;
- distort social/language structures to fit a control-oriented representation;
- increase catastrophic coupling because one substrate serves too many functions.

Candidate A should therefore permit **non-operator knowledge to remain first-class**.

RLPO must be an optional learned compression/reuse layer over a viable continuous substrate, not the obligatory representational form of everything Noema knows.

## Attack 7 — operator proposal may relocate intelligence into meta-control

Who decides that an RLPO should be created, split, merged, tested, invoked, or retired?

If a hand-designed meta-controller contains rules tailored to recurring transformations, compositional novelty, task success, transfer, and anomaly structure, the meta-controller may be doing the hard abstraction work while RLPOs merely store its decisions.

This is the same "meta-controller becomes the real intelligence" failure already identified for Candidate A, now sharpened for the compositional-temporal layer.

A credible implementation must separate generic resource/search operators from learned proposal strategy and ablate fixed versus learned proposal policy.

## Attack 8 — operator identity is not necessarily identifiable

Multiple decompositions can yield equivalent predictions and behavior:

- one long operator versus three short ones;
- overlapping operators versus one conjunctive operator;
- distributed continuous dynamics versus explicit operator sequence;
- different latent coordinate systems;
- different binding decompositions.

Evaluation must not reward the evaluator's preferred number or shape of operators.

The target is functional equivalence under prediction, intervention, transfer, recombination, cost, and revision.

Therefore "recovered the correct operators" is not a legitimate success criterion unless the environment construction uniquely identifies them under the available evidence.

## Stronger competing baseline

The current falsification package should include a deliberately simple rival that is stronger than a flat recurrent baseline:

> **continuous recurrent substrate + learned local transition adapters**

This rival may learn low-rank/context-gated local transition modifications without explicit operator identity, termination objects, or persistent argument bindings.

It can potentially provide:

- local reuse;
- context-sensitive prediction;
- efficient adaptation;
- some compositional behavior;
- action-conditioned dynamics;

while carrying fewer ontological commitments.

If this simpler realization matches RLPO on rebinding, transfer, novel combination, long-delay credit, and resource cost, RLPO's explicit operator machinery has not earned itself.

## Revised minimal L3 target

This attack suggests the common substrate requirement should remain phrased more weakly than RLPO:

> Noema needs a learnable means to discover and reuse **conditionally applicable transformations/dependencies across time and content**, and to combine them when doing so improves prediction/control/transfer under bounded resources.

This wording does not require:

- explicit operator identities;
- single initiation/termination boundaries;
- argument slots;
- a hierarchy;
- symbolic composition;
- one universal representation species.

## What RLPO must demonstrate to survive

RLPO should remain L4 unless it beats simpler alternatives on all of the following:

1. **equivalence discovery** — identifies reusable transformation structure despite stronger irrelevant surface similarity;
2. **rebinding** — applies learned structure to novel content without fixed semantic slots;
3. **boundary discovery** — learns useful temporal extent from continuous streams without curriculum segmentation;
4. **novel composition** — combines learned structure outside training combinations while calibrating unsupported extrapolation;
5. **credit improvement** — operator-level traces improve delayed attribution beyond equally budgeted unstructured/local baselines;
6. **representation mismatch** — declines or weakens explicit operatorization when the world is better represented as distributed/symmetric continuous structure;
7. **late revision** — old decomposition can be split/merged/replaced after regime change;
8. **resource value** — added machinery produces measurable benefit worth its memory/search/control cost.

## Effect on Candidate A

Classification: **MECHANISM CHALLENGE, not a Candidate A break.**

Candidate A already keeps RLPO at L4 and permits the continuous substrate to win. That design discipline survives this attack.

However, the phrase "strongest current L4 hypothesis" should be treated cautiously. RLPO currently describes the desired behavior more clearly than it explains the four hardest generative computations: equivalence discovery, binding, temporal persistence, and compatibility-aware composition.

Until those are resolved empirically or computationally, RLPO is best understood as a **structured research target / candidate packaging**, not yet a strong explanatory mechanism.

The cross-lane T'kal-in-ket attack may independently break Candidate A at a deeper level; this review should not pre-empt or dilute those findings.