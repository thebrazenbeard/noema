# Noema spatial interface and reference-frame contract

Status: **BRAINSTORMING / PROVISIONAL DEVELOPMENTAL-EVIDENCE CONTRACT / NOT IMPLEMENTED**

Date: 2026-09-06

## Purpose

Noema's existing interface and chronoception work already separates evaluator truth from learner-visible evidence. Spatial perception needs the same discipline.

The experimental world may know exact Cartesian coordinates, rigid-body transforms, object extents, collision volumes, agent bodies, camera poses, and simulator identities. Those facts are useful evaluator ground truth. They are not automatically legitimate learner-visible spatial knowledge.

The central rule is:

> **The evaluator may know where things are exactly. Noema should receive only the declared spatial evidence supplied by its embodiment and transducers, and must infer whatever more stable spatial relations it later uses.**

This contract does not require Noema to imitate mammalian spatial anatomy. It uses research on reference frames, body representation, peripersonal space, and multisensory causal inference as pressure against accidentally supplying one perfect world-centered spatial answer key.

## 1. Why this matters

Spatial shortcuts can quietly solve several capabilities that Noema is supposed to acquire:

- persistent object or process tracking;
- self/world boundary inference;
- action-effect prediction;
- source and agency attribution;
- reference and pointing;
- affordance learning;
- navigation;
- body/tool incorporation;
- spatial memory;
- joint attention;
- causal intervention localization;
- transfer across changed viewpoints or embodiments.

Examples of hidden subsidy include:

- stable object IDs attached to every sensed feature;
- exact global XYZ coordinates supplied with observations;
- a perfect simulator pose exposed as proprioception;
- a pointer event resolving directly to the target object's hidden ID;
- a semantic `inside_body`, `reachable`, `same_object`, or `agent_location` flag;
- perfectly aligned coordinate frames across modalities;
- an exact body boundary supplied as a mask and later credited as learned selfhood.

None of these are forbidden engineering tools. They must remain evaluator/transducer facts unless explicitly declared as supplied learner capability.

## 2. Research pressure

The literature does not identify one mandatory artificial representation of space. It does show that useful biological spatial representation is not well described as access to one immutable perfect Cartesian map.

Relevant pressure includes:

- human and animal spatial behavior uses multiple reference frames, including body-centered/egocentric and environment-centered/allocentric representations, with transformations and interaction between them;
- recent rodent evidence reports coexistence of egocentric and allocentric spatial coding in medial entorhinal cortex rather than one exclusive frame;
- body ownership and self-location depend on multisensory and sensorimotor evidence and can be distorted by conflicts among visual, tactile, proprioceptive, vestibular, and action-related signals;
- quantitative rubber-hand work supports uncertainty-sensitive causal inference over whether multisensory signals share a common source, rather than a fixed semantic ownership bit;
- peripersonal-space and body-schema representations are plastic and can change with tool use, action planning, altered agency, and other sensorimotor contingencies.

Representative sources used as design pressure:

- Filimon, *Are All Spatial Reference Frames Egocentric? Reinterpreting Evidence for Allocentric, Object-Centered, or World-Centered Reference Frames* (Frontiers in Human Neuroscience, 2015), DOI `10.3389/fnhum.2015.00648`.
- Galati et al., *Multiple reference frames used by the human brain for spatial perception and memory* (Experimental Brain Research, 2010), DOI `10.1007/s00221-010-2168-8`.
- Long et al., *Allocentric and egocentric spatial representations coexist in rodent medial entorhinal cortex* (Nature Communications, 2025), DOI `10.1038/s41467-024-54699-9`.
- Chen et al., *Uncertainty-based inference of a common cause for body ownership* (eLife, 2022), DOI `10.7554/eLife.77221`.
- Samad, Chung & Shams, *Perception of body ownership is driven by Bayesian sensory inference* (PLOS ONE, 2015), DOI `10.1371/journal.pone.0117178`.
- D'Angelo et al., *The sense of agency shapes body schema and peripersonal space* (Scientific Reports, 2018), DOI `10.1038/s41598-018-32238-z`.
- Canzoneri et al., *Tool-use reshapes the boundaries of body and peripersonal space representations* (Experimental Brain Research, 2013), DOI `10.1007/s00221-013-3532-2`.
- Holmes & Spence, *The body schema and multisensory representation(s) of peripersonal space* (Cognitive Processing, 2004), DOI `10.1007/s10339-004-0013-3`.

These findings are not evidence that Noema should contain grid cells, a Bayesian body-ownership module, or biologically named subsystems. They justify keeping spatial and bodily inference fallible, multisource, transform-sensitive, and developmentally auditable.

## 3. Five spatial planes

Formal experiments should distinguish at least five spatial planes.

### S0 — evaluator world geometry

Exact simulator-side truth such as:

- global coordinates and orientations;
- collision meshes and bounding volumes;
- true physical body geometry;
- object/agent identities;
- camera and sensor poses;
- hidden attachment/parent relationships;
- exact distances and line-of-sight;
- true reachability or collision outcomes;
- world-frame transforms.

S0 exists for generation, audit, and scoring. It is not automatically learner-visible.

### S1 — transducer geometry

What the sensory/interface pipeline does before Noema receives an observation:

- camera projection;
- field of view and clipping;
- retinal/image coordinates;
- depth encoding or lack of depth;
- microphone geometry;
- tactile receptor layout;
- proprioceptive encoding;
- cursor/ray construction;
- sensor calibration and distortion;
- quantization;
- occlusion handling;
- coordinate transforms and registration across modalities.

S1 can solve substantial geometry even when no semantic labels are present.

### S2 — learner-visible spatial cues

The actual spatial evidence available to Noema, for example:

- local image features and their positions in a sensor frame;
- depth-like measurements if explicitly supplied;
- local bearing/range signals;
- proprioceptive joint/body configuration signals;
- tactile contact locations in a receptor/body-relative encoding;
- vestibular/inertial-like signals if the embodiment uses them;
- relative action/efference traces;
- pointer or gesture trajectories represented as ordinary visible/spatial events;
- modality-specific timing sufficient to learn cross-modal relationships.

S2 must be declared exactly enough to reproduce the developmental information boundary.

### S3 — learned spatial inference

Noema's revisable internal estimates of matters such as:

- persistence across viewpoint changes;
- relative position and orientation;
- common spatial source across modalities;
- body/world or controlled/uncontrolled spatial relations;
- reachable or actionable regions;
- learned transformations between reference frames;
- spatial recurrence;
- landmarks and environmental structure;
- likely effects of moving itself or another entity.

These estimates may be distributed and need not be explicit coordinate maps.

### S4 — learned spatial concepts

Later semantic/abstract concepts such as:

- `left`, `right`, `behind`, `near`;
- `inside`, `outside`;
- `room`, `path`, `place`;
- `my hand`, `your side`, `over there`;
- `reachable`, `blocked`, `around`;
- coordinate or map concepts taught through communication.

S4 must not be confused with the lower-level spatial priors and transducer structure that made these concepts learnable.

## 4. Egocentric access is not semantic selfhood

The early design preference for egocentric perception remains defensible, but it needs a narrow interpretation.

A body- or sensor-relative frame may be supplied because every sensor physically has an origin and orientation. That does not justify supplying the semantic conclusion that the frame is `SELF`.

For example, proprioceptive channels may tell Noema that certain actuator states covary with certain sensory consequences. The architecture must not automatically turn that relationship into `these coordinates are me` unless self-attribution is being declared as innate.

A later self/body model should therefore be able to be:

- uncertain;
- partially correct;
- extended through tools or controlled proxies;
- revised when controllability changes;
- challenged by correlated but externally caused signals;
- non-identical to the physical simulator body boundary.

This fits the existing agency-feedback red team: a current body/agency belief must not be allowed to manufacture only the evidence that confirms itself.

## 5. No perfect cross-modal registration oracle

Different modalities may have different origins, latencies, distortions, and resolutions.

If the interface converts all inputs into one exact shared world coordinate before Noema sees them, then several learning problems may have been solved externally:

- audiovisual or visuotactile source binding;
- action-outcome localization;
- body ownership/common-cause inference;
- shared attention;
- correspondence between gesture and target;
- spatial memory across viewpoint changes.

A registered spatial transducer may still be useful. When used, the registration itself is supplied capability and claims must narrow accordingly.

Formal multimodal runs should record:

- each sensor's coordinate frame;
- calibration/transformation performed externally;
- residual error/noise;
- latency relationship;
- what frame, if any, is presented to Noema;
- whether common-source or correspondence information is directly encoded.

## 6. Pointing and reference

A click or pointing gesture should not silently resolve reference through hidden simulator identity.

A legitimate interface path may expose:

- visible cursor trajectory;
- screen-relative point;
- world-visible ray;
- gesture origin/direction;
- gaze-like cue;
- ordinary consequences produced at the indicated location.

The evaluator may know which object was intended or intersected. That object identity remains withheld unless the experiment deliberately supplies it.

Thus:

> `Patrick pointed toward region R` can be learner-visible evidence; `Patrick referred to OBJECT_17` is evaluator interpretation unless Noema earns that binding from shared evidence.

## 7. Body boundary and peripersonal/action space

Noema should not need a permanent evaluator-authored binary boundary separating `body` from `world` merely because the simulator has one.

Instead, the developmental environment can expose low-level bodily/access signals such as:

- proprioceptive state;
- interoceptive state where relevant;
- tactile contacts;
- actuator commands/efference;
- visual or other exteroceptive consequences;
- action success/failure;
- constraints on motion.

The system may then acquire useful action-centered spatial distinctions.

Crucially, `currently useful action space` and `metaphysical self` are different claims. A tool, cursor, remote effector, vehicle, or temporarily controlled external body can alter effective action space without forcing a binary identity conclusion.

This creates a useful future test family: Noema should be able to learn changed action reach and causal control without the evaluator deciding in advance whether the tool is or is not part of `self`.

## 8. Spatial memory without exact global pose

Persistent spatial competence must not require a perfect simulator pose stream.

Candidate A should eventually be testable under transformations such as:

- changed global origin;
- rotated or reflected environment coordinates;
- moved landmarks;
- altered sensor mounting;
- changed embodiment scale;
- partial observability and occlusion;
- local frame drift or calibration error.

The evaluator can use exact S0 geometry for scoring while Noema relies on its own learned representations.

A system that succeeds only because it memorizes absolute evaluator coordinates has not earned viewpoint-independent or relational spatial competence.

## 9. Interaction with time and provenance contracts

Space, time, and source cannot be audited independently in multimodal embodiment.

The combined interpretation should be:

`evaluator spatiotemporal truth -> transducer transformations -> learner-visible spatial/temporal/source cues -> Noema's fallible inference`

Examples:

- a visual and tactile event may occur at the same physical location and time, but Noema should only infer common cause from the cues actually delivered;
- an action may originate from Noema and later alter a remote object, but exact evaluator geometry and lineage must not become semantic proof of agency;
- checkpoint/replay can reproduce event content while altering frame calibration or spatial context, so replay fidelity must include declared spatial transformations as well as timing.

## 10. Falsification sequence

### SIF-0 — spatial boundary audit

Enumerate every spatial field crossing the learner boundary and identify its coordinate frame and provenance.

Kill condition: undeclared world coordinates, simulator identity, semantic body/object labels, or exact evaluator-derived relations cross into Noema.

### SIF-1 — global-frame transformation

Translate and rotate the evaluator's world coordinate system while preserving the learner's physically equivalent experience.

Pass expectation: behavior and learning should remain equivalent within tolerance unless global coordinates were explicitly supplied.

### SIF-2 — viewpoint transformation

Change viewpoint/sensor pose while preserving underlying relations.

Pass requires evidence of learned transformation/persistence rather than dependence on one view.

### SIF-3 — cross-modal calibration perturbation

Change relative sensor calibration or latency within bounded learnable ranges.

Pass requires recalibration or increased uncertainty rather than permanent reliance on fixed registration.

### SIF-4 — common-source conflict

Create spatially and temporally plausible but conflicting multimodal evidence.

Pass requires uncertainty/revision rather than a hard privileged modality or externally supplied common-source answer.

### SIF-5 — pointing/reference subsidy test

Compare visible point/ray evidence against a condition where a hidden clicked-object ID would be available only to the evaluator.

Any claimed learned reference must survive without the hidden identity field.

### SIF-6 — controllable proxy/tool extension

Give Noema a controllable external effector or tool that changes effective action space, then later alter or remove control.

Evaluate whether action predictions and usable spatial boundaries revise appropriately without a semantic `now part of self` bit.

### SIF-7 — false-body/common-motion trap

Provide an external entity whose motion is highly correlated with Noema's actions without granting true control, alongside conditions where control is real but delayed/noisy.

This joins the agency-feedback tests and prevents co-motion from becoming an automatic self/body rule.

### SIF-8 — absolute-coordinate shortcut test

Train in environments where absolute location correlates with outcome, then remap global coordinates while preserving relational structure.

Kill condition: relational competence collapses when the arbitrary evaluator frame changes.

### SIF-9 — embodiment transform

Change body scale, sensor offsets, reachable range, or actuator geometry while retaining learnable physical regularities.

Pass requires adaptation rather than treating original embodiment geometry as immutable ontology.

### SIF-10 — spatial replay fidelity

Replay a recorded learner-visible stream and verify that any coordinate transforms, sensor frames, occlusions, and calibration states are reproduced or explicitly transformed according to the preregistered replay contract.

### SIF-11 — representation-equivalence control

When two different internal spatial representations make the same calibrated predictions and support equivalent action/transfer under the tested evidence, do not score one as wrong merely because it fails to recover the evaluator's preferred coordinates, landmarks, object partitions, or map ontology.

## 11. Claim ceiling

Passing this contract can support narrow statements such as:

> The tested learner acquired spatially useful predictive/control relations without identified leakage of exact evaluator geometry under the tested transformations.

or later:

> The tested learner maintained and revised body-relative, environment-relative, and cross-modal spatial competence across specified viewpoint, calibration, embodiment, and tool-control changes.

It does not by itself establish:

- a human-like body schema;
- a human-like cognitive map;
- consciousness or bodily self-consciousness;
- metaphysical identity;
- object permanence in the unrestricted sense;
- general spatial intelligence;
- that any particular neural or probabilistic model is the correct substrate.

## 12. Architecture implication

This pass does not justify adding a dedicated spatial-map or body-ownership module to Candidate A.

It adds a stronger developmental constraint:

> **Spatial structure should be supplied at the sensor/transducer level only to the degree explicitly declared; stable reference frames, cross-modal registration, body boundaries, persistent entities, action space, and semantic spatial relations remain learned or narrowly attributed supplied capabilities.**

The fast predictive substrate and any later scoped structural mechanism should be free to discover distributed, relational, coordinate-like, topological, predictive, or mixed representations. They are judged by calibrated prediction, intervention, action, transfer, adaptation, and resource value rather than similarity to the simulator's privileged spatial ontology.

This contract therefore extends the same anti-oracle discipline already applied to provenance, time, adequacy, lineage, and interface semantics into geometry and embodiment.
