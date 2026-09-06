# Noema operator console — concrete interaction design

Status: **BRAINSTORMING / PROVISIONAL INTERFACE SPEC / NOT IMPLEMENTED**

## Purpose

Patrick needs a concrete answer to a practical question: **how does he actually interact with Noema while Noema is developing?**

The interface must satisfy two competing requirements:

1. Patrick must be able to communicate with and teach Noema from early development.
2. The interface must not smuggle human semantic ground truth into Noema merely to make the UI convenient.

The current answer is a local **Noema Console** with three sharply separated surfaces: direct communication, shared world interaction, and read-only diagnostics.

## 1. Direct Patrick ↔ Noema communication

This is the ordinary learned communication channel.

Patrick should have a persistent conversation pane that feels operationally similar to a chat/voice interface, but the data delivered to Noema are treated as ordinary perceptual signals rather than privileged semantic facts.

### Patrick → Noema

Initial modalities:

- **typed text** as the first practical channel;
- **microphone/voice** as an additional channel once the sensory front end is defined;
- later gesture, pointing, shared attention, and other embodied signals from the world interface.

For typed text, Noema should receive minimally interpreted symbol sequences plus low-level timing/channel provenance. The interface must not inject pretrained semantic embeddings, ontology labels, hidden intent labels, or evaluator conclusions.

A practical early representation is raw UTF-8 bytes or characters with temporal boundaries sufficient to observe sequences. Word meanings, referents, pragmatics, reliability, speaker models, and conversational conventions remain learned.

The interface may know that input arrived through `human_input_channel_1`; that is sensor provenance, not the semantic fact `Patrick said this` or `trusted teacher said this`. Personal identity and source reliability are developmental inferences.

### Voice

Voice is desirable because Patrick should eventually be able to simply speak to Noema.

There are two conceptually different routes:

- **developmentally pure acoustic route:** microphone audio or low-level acoustic features become Noema sensory input; phonetic/word structure must be learned;
- **external transcription route:** speech-to-text converts Patrick's voice into the same text signal channel used above.

The transcription route is much easier operationally but imports a substantial perceptual prior: word segmentation and spelling have already been solved by another model. If used, that fact must remain explicit in experiments. It can be acceptable as an external sensory transducer without giving semantic meaning, but it must not be cited as evidence that Noema independently learned speech perception.

The first usable console should therefore support typed text immediately and reserve microphone input behind an explicit modality boundary rather than blocking all interaction until speech perception is solved.

### Noema → Patrick

Noema receives a communication actuator: a channel through which it may emit learned symbol sequences/signals.

Early output may be sparse, malformed, repetitive, or meaningless. The console displays it anyway. Noema does not receive a pre-authored answer generator merely because Patrick needs readable output.

As Noema learns communication, this same channel can become text and later voice.

## 2. Shared world interface

Direct language grounding requires shared context.

The console therefore includes a world pane showing the environment in which Noema is currently operating. Patrick can interact with that world as an external agent/operator.

Examples:

- move or present something;
- point toward a location or perceptual region;
- demonstrate an action;
- place a barrier;
- reveal or hide information;
- offer alternatives;
- create a correction situation;
- later inhabit/control another embodied agent in the same world.

This makes interactions such as the following possible without a semantic database:

Patrick types or says a signal while presenting something.
Noema observes the signal and the surrounding event.
Patrick repeats the signal in other contexts.
Noema forms hypotheses about what the signal predicts/refers to.
Noema acts or communicates based on that interpretation.
Patrick corrects it through another ordinary interaction.

The UI may let Patrick select or point at a region for convenience, but Noema should receive the corresponding observable pointing/attention event, not an injected hidden object ID or semantic label.

## 3. Read-only diagnostic instrumentation

Patrick also needs to understand what the developing system is doing before its communication is mature.

A separate diagnostics pane exposes inspectable state such as:

- current live hypotheses and their maturity/state;
- confidence dimensions and strongest challenger;
- current `N_min`/`N_max` deliberation state where applicable;
- whether Noema currently regards its model set as inadequate;
- current predictions and prediction error;
- intervention/counterfactual disagreement;
- recently retrieved memories/episodes;
- high-allocation/salient signals;
- candidate actions and predicted outcomes;
- structure created, reopened, split, merged, made dormant, or retired;
- hypothesis genealogy;
- evidence provenance/source mode;
- active uncertainty and known-unknown conditions.

This pane is for Patrick, not for Noema.

### Diagnostic provenance labels

The console must distinguish at least three things visually:

1. **Noema emitted this** — actual learned communication from Noema.
2. **Noema internal state contains this inspectable quantity/structure** — direct instrumentation.
3. **Interpreter says this probably means X** — a human-readable gloss generated outside Noema.

These must never be collapsed into one conversational transcript.

A diagnostic interpreter may eventually translate internal structures into sentences such as `current evidence favors hypothesis H7 over H12, but the model remains unresolved under intervention class I3`.

That sentence is the interpreter's rendering, not necessarily Noema's own linguistic thought or statement.

## 4. Concrete console layout

A first practical desktop/local-browser console can use four persistent regions.

### Left: World

- current simulation/experiment viewport;
- controls for Patrick's ordinary world actions;
- visible Noema embodiment/state only to the degree intended by the scenario;
- pointing/joint-attention tools.

### Bottom or center: Talk to Noema

- text input;
- optional push-to-talk microphone input;
- Noema's outbound communication stream;
- timestamps and raw modality/source-channel markers;
- clear separation from diagnostic text.

### Right: Noema state

- current hypothesis population;
- confidence/maturation state;
- uncertainty / none-of-the-above state;
- prediction and counterfactual panels;
- memory/provenance inspection;
- allocation/salience;
- current action candidates.

### Top/operator strip

- pause/resume learner;
- checkpoint/save state;
- load a registered experiment;
- start/stop recording;
- reset only the experiment state allowed by the test protocol;
- toggle diagnostics without changing what Noema perceives;
- clearly marked experimenter-only interventions.

These controls operate outside Noema's world unless a test explicitly routes their consequence into normal perceptual channels.

## 5. Interaction modes

The same console should support distinct modes rather than separate applications.

### Development mode

Patrick sees full diagnostics while communicating/interacting with Noema.

Purpose: debug learning, inspect failures, understand grounding, test architecture.

### Blind evaluation mode

Diagnostics that would bias Patrick's behavior can be hidden or frozen while the underlying learner continues normally.

Purpose: prevent the human experimenter from unconsciously teaching toward internal answers during formal tests.

### Natural interaction mode

World + communication dominate the display; diagnostics are optional/background.

Purpose: approximate what living with or working with Noema would eventually feel like rather than permanently operating a laboratory instrument.

## 6. Early communication should not wait for mature world cognition

The console does not wait until Noema has mastered objects, agents, causation, or language.

Patrick can communicate from the beginning. The difference is that early Noema may have little or no grounded interpretation of the signals.

This is analogous at the architectural level to exposing a developing learner to recurring communication while grounding grows through shared history.

Communication and world modeling therefore co-develop.

## 7. Important anti-cheating boundaries

The console may provide Patrick with rich controls while still restricting what crosses into Noema.

Do not inject:

- hidden object IDs because Patrick clicked an object;
- semantic class names from the simulator;
- `Patrick`, `teacher`, `trusted`, or `truth` metadata as source meaning;
- interpreter-generated English as internal state;
- evaluator-known correct hypotheses;
- pre-labeled intents, commands, referents, emotions, agent goals, or dialogue acts.

Low-level provenance such as timing, modality, sensor channel, efference/action source, and ordinary physical consequences is allowed where the developmental contract permits it.

## 8. Practical first usable version

The first interface does not need the eventual 3D organism to become useful.

A minimal but real console can appear during the Experiment A/B era with:

- a simple experiment/world viewport;
- text input to a generic communication signal stream;
- raw outbound symbol stream from Noema;
- live hypothesis/confidence instrumentation;
- a timeline showing observations, interventions, predictions, revisions, and communication events;
- pause/checkpoint/reset controls.

Experiment A itself remains language-free for epistemic isolation. The console can still exist; its direct communication channel is simply disabled for that formal run.

This allows operator/UI work to mature in parallel without contaminating the causal-learning benchmark.

## 9. Concrete answer to Patrick's question

Patrick is not expected to interact with Noema through GitHub, logs, notebooks, or a command line as the normal user experience.

The target interaction is:

> open Noema Console → see the world Noema is inhabiting → talk/type directly to Noema → watch Noema act/respond → optionally inspect what it currently believes, predicts, remembers, doubts, or is reconsidering in the diagnostic pane.

During development the console looks partly like a lab instrument. As grounded communication matures, it should increasingly feel like interacting with the agent itself while the diagnostics recede into an optional debugger.

## 10. Design implications that now become explicit requirements

The cognitive architecture should expose enough stable inspection hooks to support the diagnostic pane without letting the pane become a privileged controller.

Communication events need provenance and temporal alignment with world events so grounding can be learned.

The world interface needs a non-semantic way to express joint attention/pointing.

Noema needs an outbound communication actuator even before it knows how to use it.

The eventual UI must distinguish direct Noema communication from diagnostic interpretation at all times.

## Open implementation questions

These remain implementation questions rather than reasons to leave the user experience undefined:

- exact desktop/web framework;
- whether early voice uses acoustic input, external ASR, or both experimental modes;
- how raw symbol streams are encoded internally;
- how diagnostic structures are serialized;
- which inspectable states are deterministic readouts versus interpreter-generated glosses;
- how 3D rendering and world interaction are eventually hosted locally.
