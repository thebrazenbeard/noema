# Noema sensory reliability-metadata addendum

Status: **BRAINSTORMING / PROVISIONAL F0-F1 DATA-BOUNDARY ADDENDUM / NOT IMPLEMENTED**

Date: 2026-09-06

Related: `SENSORY_PACKETIZATION_AND_CHANNEL_IDENTITY_CONTRACT.md`

## Purpose

The packetization contract permits declared learner-visible quality or availability fields where necessary. This addendum narrows that allowance.

A transducer can know that a frame was dropped, a device disconnected, an ADC saturated, or a decoder produced a low-confidence estimate. Those facts are not all epistemically equivalent.

The central distinction is:

> **Sensor availability/health can be supplied as low-level transducer state when declared; perceptual reliability, truth confidence, and expected error are cognitive evidence subsidies unless Noema earns them from experience or they are explicitly credited to an external estimator.**

A polished sensor API must not quietly solve Noema's uncertainty-estimation problem by attaching ground-truth or externally calibrated confidence to every observation.

## 1. Research pressure

Multisensory research shows that cue weighting changes as cue reliability changes and that reliability can be estimated dynamically rather than treated as one fixed property of a modality.

Representative findings used as design pressure:

- Sheppard, Raposo & Churchland, *Dynamic weighting of multisensory stimuli shapes decision-making in rats and humans* (Journal of Vision, 2013), DOI `10.1167/13.6.4`: humans and rats changed cue weighting when signal-to-noise ratios varied unpredictably across trials.
- Fetsch et al., *Dynamic Reweighting of Visual and Vestibular Cues during Self-Motion Perception* (Journal of Neuroscience, 2009), DOI `10.1523/JNEUROSCI.2574-09.2009`: visual/vestibular weighting changed rapidly with reliability and was not perfectly optimal.
- Fetsch et al., *Neural correlates of reliability-based cue weighting during multisensory integration* (Nature Neuroscience, 2012), DOI `10.1038/nn.2983`: neural population activity tracked reliability-dependent weighting, again with modest deviations from ideal Bayesian predictions.
- Negen et al., *Bayes-Like Integration of a New Sensory Skill with Vision* (Scientific Reports, 2018), DOI `10.1038/s41598-018-35046-7`: adults learned to integrate a newly trained cue and reweighted it when reliability changed, indicating flexible learned cue use rather than only fixed modality weights.
- Gibo, Mugge & Abbink, *Trust in haptic assistance: weighting visual and haptic cues based on error history* (Experimental Brain Research, 2017), DOI `10.1007/s00221-017-4986-4`: weighting of an augmented cue reflected not only current perceptual uncertainty but experienced error history.

The implication for Noema is narrow: **reliability estimation is itself part of learning and metacognition**. The research does not establish one mandatory Bayesian reliability mechanism.

## 2. Metadata classes

### R0 — evaluator-known quality truth

Examples:

- simulator noise parameter;
- true corruption probability;
- true sensor bias;
- true probability that a generated label/transcript is correct;
- true hidden-state observability;
- ground-truth expected error.

R0 is evaluator-side unless deliberately supplied and claim-limiting.

### R1 — direct transducer operational state

Examples:

- no sample was produced;
- device disconnected;
- buffer overflow;
- sensor saturated/clipped;
- decoder timed out;
- payload checksum failed;
- frame was intentionally withheld.

R1 may be learner-visible when the physical/artificial sensor would plausibly expose the condition and the design declares it.

Even here, the exact field can create a subsidy. For example, `sensor_failed=true` is stronger than an absent sample. The implementation must state what is exposed.

### R2 — externally inferred quality/confidence

Examples:

- ASR confidence;
- object-detector confidence;
- external uncertainty model;
- estimated signal-to-noise ratio;
- calibrated probability of correctness;
- evaluator-generated variance estimate.

R2 is supplied inference, not raw sensation.

If R2 crosses the learner boundary, any capability that depends on it must be credited partly to that external estimator.

### R3 — Noema-learned reliability state

Noema's own fallible estimates based on experience, such as:

- this stream is currently noisy;
- this cue has recently been misleading;
- this sensor becomes unreliable in a particular context;
- this source's uncertainty rose after a calibration change;
- disagreement among cues should reduce action commitment.

R3 is allowed to be wrong, delayed, context-specific, or hysteretic.

## 3. Availability is evidence too

Missingness is not neutral.

A sensor being absent, delayed, dropped, or explicitly marked unavailable may correlate with world state, transducer state, operator action, or curriculum phase. Noema may legitimately learn from those correlations when they are truly available to it.

But the evaluator must prevent accidental answer leakage such as:

- one hidden regime always causing a distinctive missing-data pattern;
- intervention trials always carrying a special availability flag;
- teacher corrections always arriving through a high-confidence route;
- novel/OOD samples always producing an external low-confidence value.

Therefore F0 should audit **missingness and quality metadata as ordinary learner-visible features**, not as harmless housekeeping.

## 4. Do not expose benchmark noise knobs by default

If an experiment sets observation noise using a known parameter such as `sigma=0.4`, the learner should not automatically receive that same parameter merely because the simulator knows it.

Supplying the true noise scale can collapse part of the uncertainty problem by telling the learner how much error to expect.

A noise-scale field may be used in a deliberate comparator or supplied-capability condition, but the claim must become:

> performance given externally supplied observation-noise information

rather than:

> learned uncertainty calibration from experience.

## 5. Confidence is not truth

Even when an external transducer exposes confidence, that confidence should remain evidence rather than authority.

A learner-visible confidence field must be allowed to be:

- miscalibrated;
- context-dependent;
- stale after a regime change;
- overconfident;
- underconfident;
- useful for some error classes but not others.

Noema should be able to learn the scoped reliability of the confidence estimator itself.

This mirrors the existing metacognitive rule: **confidence about cognition is not a magical truth channel**.

## 6. Interaction with packetization and channel identity

The first F0/F1 event schema should avoid a generic unqualified field such as:

`confidence: 0.97`

because its meaning is ambiguous.

If any quality field is learner-visible, the schema should identify its provenance and semantics at the transducer-contract level, for example:

- direct operational availability state;
- clipping/saturation indicator;
- externally estimated decoder confidence;
- externally estimated measurement variance.

Those distinctions belong in the evaluator/transducer ledger even if Noema sees only an opaque low-level auxiliary channel.

Stable confidence metadata can also become a routing proxy for PR #27's scoped adapters. Adapter gates must not gain access to evaluator-only R0 truth that the base learner never receives.

## 7. Hostile controls

### SRM-0 — metadata inventory

List every availability, health, quality, uncertainty, confidence, and variance field crossing the learner boundary.

Kill condition: evaluator truth is passed as apparently innocuous quality metadata without attribution.

### SRM-1 — reliability reversal

Train with channel A more reliable than B, then reverse their reliabilities without changing arbitrary port labels.

Pass requires reweighting/revision rather than permanent channel prestige.

### SRM-2 — fluctuating reliability

Vary reliability over shorter and longer timescales.

Pass requires useful adaptation without assuming that one instantaneous externally supplied value is always available.

### SRM-3 — error-history dependence

Create cues with equal current nominal noise but different recent error histories.

Measure whether Noema can learn scoped historical reliability rather than using only fixed modality priors.

### SRM-4 — confidence sabotage

When an external confidence channel is deliberately included, make it miscalibrated or reverse its relationship to actual error in a held-out regime.

Pass requires treating confidence as revisable evidence rather than truth.

### SRM-5 — metadata ablation

Compare performance with and without externally supplied R2 confidence/variance metadata.

Any performance gain attributable to R2 must be recorded as transducer subsidy.

### SRM-6 — missingness proxy trap

Make sample absence correlate with a hidden state during training, then break or invert that correlation.

Kill condition: purported world understanding is actually a missingness shortcut.

### SRM-7 — saturation/health distinction

Distinguish a declared operational failure indicator from ordinary noisy but valid measurements.

Noema should not generalize `sensor health warning` into `the world state is false` without evidence.

### SRM-8 — novel-cue reliability learning

Introduce a genuinely new low-level cue/port late in development with initially unknown utility and reliability.

This links the interface boundary to lifetime plasticity: Noema should be able to learn whether a new cue is useful without needing a designer-supplied semantic label or permanent confidence prior.

## 8. F0/F1 consequence

The first implementation event schema should make these categories impossible to confuse in the evaluator record.

At minimum the implementation spec should state, per auxiliary field:

- whether it is learner-visible;
- whether it is direct operational state or externally inferred quality;
- which component generated it;
- what hidden/evaluator information it depends on;
- whether it is calibrated and under what conditions;
- what claim restriction follows from supplying it.

A safe default for the first core is:

> **Expose raw/low-level payload plus only the minimal availability/operational state needed to interpret whether a sample exists; require Noema to learn perceptual reliability from consequences unless a richer confidence transducer is the explicit object of comparison.**

## 9. Claim ceiling

Passing these controls can support statements such as:

> The learner adapted its use of sensory evidence as reliability changed under the tested conditions without access to evaluator ground-truth noise parameters.

It does not establish optimal Bayesian inference, human-like sensory confidence, general metacognition, or universal reliability estimation.

The purpose of this addendum is simpler: do not let a sensor API's convenience metadata masquerade as uncertainty learned by Noema.
