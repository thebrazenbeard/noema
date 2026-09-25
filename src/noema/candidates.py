from __future__ import annotations

from dataclasses import dataclass
import math

from .boundary import Prediction


def _check_vector(values: tuple[float, ...], *, name: str) -> None:
    if not values:
        raise ValueError(f"{name} must not be empty")
    if not all(math.isfinite(v) for v in values):
        raise ValueError(f"{name} must contain only finite values")


@dataclass(frozen=True, slots=True)
class GaussianState:
    mean: tuple[float, ...]
    variance: tuple[float, ...]
    count: int

    def __post_init__(self) -> None:
        _check_vector(self.mean, name="mean")
        _check_vector(self.variance, name="variance")
        if len(self.mean) != len(self.variance):
            raise ValueError("mean and variance dimensions must match")
        if any(v <= 0 for v in self.variance):
            raise ValueError("variance must be strictly positive")
        if self.count < 0:
            raise ValueError("count must be nonnegative")


@dataclass(frozen=True, slots=True)
class C1Config:
    alpha: float
    variance_floor: float

    def __post_init__(self) -> None:
        if not math.isfinite(self.alpha) or not (0.0 < self.alpha <= 1.0):
            raise ValueError("alpha must be in (0, 1]")
        if not math.isfinite(self.variance_floor) or self.variance_floor <= 0:
            raise ValueError("variance_floor must be finite and positive")


@dataclass(frozen=True, slots=True)
class ReplayConfig:
    capacity: int
    max_replay_updates_per_event: int

    def __post_init__(self) -> None:
        if self.capacity < 0:
            raise ValueError("capacity must be nonnegative")
        if self.max_replay_updates_per_event < 0:
            raise ValueError("max_replay_updates_per_event must be nonnegative")


@dataclass(frozen=True, slots=True)
class ReplayBuffer:
    items: tuple[tuple[float, ...], ...]
    capacity: int

    def __post_init__(self) -> None:
        if self.capacity < 0:
            raise ValueError("capacity must be nonnegative")
        if len(self.items) > self.capacity:
            raise ValueError("replay buffer exceeds capacity")
        dimensions = {len(item) for item in self.items}
        if len(dimensions) > 1:
            raise ValueError("replay observations must share one dimension")
        for item in self.items:
            _check_vector(item, name="replay observation")

    @classmethod
    def empty(cls, config: ReplayConfig) -> "ReplayBuffer":
        return cls(items=(), capacity=config.capacity)

    def append(self, observation: tuple[float, ...]) -> "ReplayBuffer":
        _check_vector(observation, name="observation")
        if self.capacity == 0:
            return self
        if self.items and len(observation) != len(self.items[0]):
            raise ValueError("replay observation dimension mismatch")
        next_items = (*self.items, tuple(observation))
        if len(next_items) > self.capacity:
            next_items = next_items[-self.capacity :]
        return ReplayBuffer(items=next_items, capacity=self.capacity)


@dataclass(frozen=True, slots=True)
class C2State:
    base: GaussianState
    replay: ReplayBuffer


def predict_gaussian(state: GaussianState) -> Prediction:
    return Prediction(mean=state.mean, variance=state.variance)


def transition_c1(
    state: GaussianState,
    observation: tuple[float, ...],
    config: C1Config,
) -> GaussianState:
    _check_vector(observation, name="observation")
    if len(observation) != len(state.mean):
        raise ValueError("observation dimension mismatch")
    new_mean: list[float] = []
    new_variance: list[float] = []
    for old_mean, old_var, value in zip(state.mean, state.variance, observation, strict=True):
        delta = value - old_mean
        mean = old_mean + config.alpha * delta
        residual = value - mean
        variance = max(
            config.variance_floor,
            (1.0 - config.alpha) * old_var + config.alpha * residual * residual,
        )
        new_mean.append(mean)
        new_variance.append(variance)
    return GaussianState(tuple(new_mean), tuple(new_variance), state.count + 1)


def transition_c2_once(
    state: C2State,
    observation: tuple[float, ...],
    c1_config: C1Config,
    replay_config: ReplayConfig,
) -> C2State:
    if state.replay.capacity != replay_config.capacity:
        raise ValueError("state replay capacity does not match replay configuration")
    updated_base = transition_c1(state.base, observation, c1_config)
    updated_replay = state.replay.append(observation)
    return C2State(base=updated_base, replay=updated_replay)


def _apply_replay_indices(
    base: GaussianState,
    replay: ReplayBuffer,
    replay_indices: tuple[int, ...],
    c1_config: C1Config,
    replay_config: ReplayConfig,
) -> GaussianState:
    if replay.capacity != replay_config.capacity:
        raise ValueError("state replay capacity does not match replay configuration")
    if len(replay_indices) > replay_config.max_replay_updates_per_event:
        raise ValueError("replay_indices exceed max_replay_updates_per_event")
    updated = base
    for index in replay_indices:
        if isinstance(index, bool) or not isinstance(index, int) or index < 0 or index >= len(replay.items):
            raise ValueError("replay index is outside frozen replay buffer")
        updated = transition_c1(updated, replay.items[index], c1_config)
    return updated


def transition_c2_replay(
    state: C2State,
    replay_indices: tuple[int, ...],
    c1_config: C1Config,
    replay_config: ReplayConfig,
) -> C2State:
    updated_base = _apply_replay_indices(
        state.base,
        state.replay,
        replay_indices,
        c1_config,
        replay_config,
    )
    return C2State(base=updated_base, replay=state.replay)

@dataclass(frozen=True, slots=True)
class RecurrentConfig:
    learning_rate: float
    variance_alpha: float
    variance_floor: float

    def __post_init__(self) -> None:
        if not math.isfinite(self.learning_rate) or not (0.0 < self.learning_rate <= 1.0):
            raise ValueError("learning_rate must be in (0, 1]")
        if not math.isfinite(self.variance_alpha) or not (0.0 < self.variance_alpha <= 1.0):
            raise ValueError("variance_alpha must be in (0, 1]")
        if not math.isfinite(self.variance_floor) or self.variance_floor <= 0:
            raise ValueError("variance_floor must be finite and positive")


@dataclass(frozen=True, slots=True)
class RecurrentGaussianState:
    weights: tuple[tuple[float, ...], ...]
    variance: tuple[float, ...]
    previous: tuple[float, ...] | None
    count: int

    def __post_init__(self) -> None:
        if not self.weights:
            raise ValueError("weights must not be empty")
        dimension = len(self.weights)
        if any(len(row) != dimension for row in self.weights):
            raise ValueError("weights must be a square target-by-context matrix")
        for row in self.weights:
            _check_vector(row, name="weight row")
        _check_vector(self.variance, name="variance")
        if len(self.variance) != dimension:
            raise ValueError("variance dimension must match recurrent state dimension")
        if any(value <= 0 for value in self.variance):
            raise ValueError("variance must be strictly positive")
        if self.previous is not None:
            _check_vector(self.previous, name="previous")
            if len(self.previous) != dimension:
                raise ValueError("previous observation dimension mismatch")
        if self.count < 0:
            raise ValueError("count must be nonnegative")

    @classmethod
    def zeros(cls, *, dimension: int, initial_variance: float) -> "RecurrentGaussianState":
        if dimension < 1:
            raise ValueError("dimension must be at least 1")
        if not math.isfinite(initial_variance) or initial_variance <= 0:
            raise ValueError("initial_variance must be finite and positive")
        return cls(
            weights=tuple(tuple(0.0 for _ in range(dimension)) for _ in range(dimension)),
            variance=tuple(float(initial_variance) for _ in range(dimension)),
            previous=None,
            count=0,
        )


def _matrix_vector(
    weights: tuple[tuple[float, ...], ...],
    context: tuple[float, ...],
) -> tuple[float, ...]:
    return tuple(
        sum(weight * value for weight, value in zip(row, context, strict=True))
        for row in weights
    )


def predict_recurrent(state: RecurrentGaussianState) -> Prediction:
    dimension = len(state.weights)
    mean = (
        tuple(0.0 for _ in range(dimension))
        if state.previous is None
        else _matrix_vector(state.weights, state.previous)
    )
    return Prediction(mean=mean, variance=state.variance)


def predict_reset_reference(*, dimension: int, variance: float) -> Prediction:
    if dimension < 1:
        raise ValueError("dimension must be at least 1")
    if not math.isfinite(variance) or variance <= 0:
        raise ValueError("variance must be finite and positive")
    return Prediction(
        mean=tuple(0.0 for _ in range(dimension)),
        variance=tuple(float(variance) for _ in range(dimension)),
    )


def _learn_recurrent_pair(
    state: RecurrentGaussianState,
    *,
    context: tuple[float, ...],
    outcome: tuple[float, ...],
    config: RecurrentConfig,
    preserve_previous: bool,
) -> RecurrentGaussianState:
    _check_vector(context, name="context")
    _check_vector(outcome, name="outcome")
    dimension = len(state.weights)
    if len(context) != dimension or len(outcome) != dimension:
        raise ValueError("recurrent context/outcome dimension mismatch")

    prediction = _matrix_vector(state.weights, context)
    next_weights: list[tuple[float, ...]] = []
    next_variance: list[float] = []
    for row, old_var, predicted, observed in zip(
        state.weights,
        state.variance,
        prediction,
        outcome,
        strict=True,
    ):
        error = observed - predicted
        next_weights.append(
            tuple(
                weight + config.learning_rate * error * value
                for weight, value in zip(row, context, strict=True)
            )
        )
        residual_variance = error * error
        next_variance.append(
            max(
                config.variance_floor,
                (1.0 - config.variance_alpha) * old_var
                + config.variance_alpha * residual_variance,
            )
        )
    return RecurrentGaussianState(
        weights=tuple(next_weights),
        variance=tuple(next_variance),
        previous=state.previous if preserve_previous else outcome,
        count=state.count + 1,
    )


def transition_recurrent(
    state: RecurrentGaussianState,
    observation: tuple[float, ...],
    config: RecurrentConfig,
) -> RecurrentGaussianState:
    _check_vector(observation, name="observation")
    if len(observation) != len(state.weights):
        raise ValueError("observation dimension mismatch")
    if state.previous is None:
        return RecurrentGaussianState(
            weights=state.weights,
            variance=state.variance,
            previous=tuple(observation),
            count=state.count + 1,
        )
    return _learn_recurrent_pair(
        state,
        context=state.previous,
        outcome=tuple(observation),
        config=config,
        preserve_previous=False,
    )


@dataclass(frozen=True, slots=True)
class RecurrentTransition:
    context: tuple[float, ...]
    outcome: tuple[float, ...]

    def __post_init__(self) -> None:
        _check_vector(self.context, name="replay context")
        _check_vector(self.outcome, name="replay outcome")
        if len(self.context) != len(self.outcome):
            raise ValueError("replay context/outcome dimensions must match")


@dataclass(frozen=True, slots=True)
class RecurrentReplayConfig:
    capacity: int
    max_replay_updates_per_event: int

    def __post_init__(self) -> None:
        if self.capacity < 0:
            raise ValueError("capacity must be nonnegative")
        if self.max_replay_updates_per_event < 0:
            raise ValueError("max_replay_updates_per_event must be nonnegative")


@dataclass(frozen=True, slots=True)
class RecurrentReplayBuffer:
    items: tuple[RecurrentTransition, ...]
    capacity: int

    def __post_init__(self) -> None:
        if self.capacity < 0:
            raise ValueError("capacity must be nonnegative")
        if len(self.items) > self.capacity:
            raise ValueError("recurrent replay buffer exceeds capacity")
        dimensions = {len(item.context) for item in self.items}
        if len(dimensions) > 1:
            raise ValueError("recurrent replay transitions must share one dimension")

    @classmethod
    def empty(cls, config: RecurrentReplayConfig) -> "RecurrentReplayBuffer":
        return cls(items=(), capacity=config.capacity)

    def append(
        self,
        *,
        context: tuple[float, ...],
        outcome: tuple[float, ...],
    ) -> "RecurrentReplayBuffer":
        transition = RecurrentTransition(tuple(context), tuple(outcome))
        if self.capacity == 0:
            return self
        if self.items and len(transition.context) != len(self.items[0].context):
            raise ValueError("recurrent replay transition dimension mismatch")
        next_items = (*self.items, transition)
        if len(next_items) > self.capacity:
            next_items = next_items[-self.capacity :]
        return RecurrentReplayBuffer(items=next_items, capacity=self.capacity)


def select_most_recent_replay_indices(*, item_count: int, max_updates: int) -> tuple[int, ...]:
    if isinstance(item_count, bool) or not isinstance(item_count, int) or item_count < 0:
        raise ValueError("item_count must be a nonnegative integer")
    if isinstance(max_updates, bool) or not isinstance(max_updates, int) or max_updates < 0:
        raise ValueError("max_updates must be a nonnegative integer")
    count = min(item_count, max_updates)
    return tuple(item_count - 1 - offset for offset in range(count))


@dataclass(frozen=True, slots=True)
class RecurrentC2State:
    base: RecurrentGaussianState
    replay: RecurrentReplayBuffer


def transition_recurrent_c2_once(
    state: RecurrentC2State,
    observation: tuple[float, ...],
    config: RecurrentConfig,
    replay_config: RecurrentReplayConfig,
) -> RecurrentC2State:
    if state.replay.capacity != replay_config.capacity:
        raise ValueError("state replay capacity does not match replay configuration")
    context = state.base.previous
    updated_base = transition_recurrent(state.base, observation, config)
    updated_replay = state.replay
    if context is not None:
        updated_replay = updated_replay.append(context=context, outcome=tuple(observation))
    return RecurrentC2State(base=updated_base, replay=updated_replay)


def transition_recurrent_c2_replay(
    state: RecurrentC2State,
    replay_indices: tuple[int, ...],
    config: RecurrentConfig,
    replay_config: RecurrentReplayConfig,
) -> RecurrentC2State:
    if state.replay.capacity != replay_config.capacity:
        raise ValueError("state replay capacity does not match replay configuration")
    if len(replay_indices) > replay_config.max_replay_updates_per_event:
        raise ValueError("replay_indices exceed max_replay_updates_per_event")
    updated = state.base
    live_previous = state.base.previous
    for index in replay_indices:
        if (
            isinstance(index, bool)
            or not isinstance(index, int)
            or index < 0
            or index >= len(state.replay.items)
        ):
            raise ValueError("replay index is outside frozen recurrent replay buffer")
        transition = state.replay.items[index]
        updated = _learn_recurrent_pair(
            updated,
            context=transition.context,
            outcome=transition.outcome,
            config=config,
            preserve_previous=True,
        )
    if updated.previous != live_previous:
        raise RuntimeError("replay must not alter live recurrent context")
    return RecurrentC2State(base=updated, replay=state.replay)


from enum import Enum

_SEMANTIC_STRUCTURAL_TOKENS = (
    "cause",
    "parent",
    "child",
    "chain",
    "fork",
    "common cause",
)


@dataclass(frozen=True, slots=True)
class Dependency:
    source: int
    target: int
    weight: float
    scope: str

    def __post_init__(self) -> None:
        if self.source < 0 or self.target < 0:
            raise ValueError("dependency endpoints must be nonnegative")
        if self.source == self.target:
            raise ValueError("self-dependency is not allowed in the minimal C4 subject")
        if not math.isfinite(self.weight):
            raise ValueError("dependency weight must be finite")
        normalized = self.scope.strip().lower().replace("_", " ")
        if not normalized:
            raise ValueError("scope must be nonempty")
        if any(token in normalized for token in _SEMANTIC_STRUCTURAL_TOKENS):
            raise ValueError("semantic structural labels are forbidden")


@dataclass(frozen=True, slots=True)
class StructuralHypothesis:
    handle: str
    dependencies: tuple[Dependency, ...]
    confidence: float

    def __post_init__(self) -> None:
        if not self.handle:
            raise ValueError("hypothesis handle must be nonempty")
        if not math.isfinite(self.confidence) or not (0.0 <= self.confidence <= 1.0):
            raise ValueError("hypothesis confidence must be in [0, 1]")
        if len(set(self.dependencies)) != len(self.dependencies):
            raise ValueError("duplicate dependency in one hypothesis")


@dataclass(frozen=True, slots=True)
class C4Config:
    max_active_hypotheses: int
    max_abs_weight: float

    def __post_init__(self) -> None:
        if self.max_active_hypotheses < 1:
            raise ValueError("max_active_hypotheses must be at least 1")
        if not math.isfinite(self.max_abs_weight) or self.max_abs_weight <= 0:
            raise ValueError("max_abs_weight must be finite and positive")


@dataclass(frozen=True, slots=True)
class C4State:
    base: GaussianState
    hypotheses: tuple[StructuralHypothesis, ...]
    replay: ReplayBuffer | None = None

    def validate(self, config: C4Config) -> "C4State":
        if len(self.hypotheses) > config.max_active_hypotheses:
            raise ValueError("structural hypothesis population exceeds configured cap")
        handles = tuple(h.handle for h in self.hypotheses)
        if len(set(handles)) != len(handles):
            raise ValueError("structural hypothesis handles must be unique")
        dimension = len(self.base.mean)
        for hypothesis in self.hypotheses:
            for dependency in hypothesis.dependencies:
                if dependency.source >= dimension or dependency.target >= dimension:
                    raise ValueError("dependency endpoint outside base dimension")
                if abs(dependency.weight) > config.max_abs_weight:
                    raise ValueError("dependency weight exceeds configured cap")
        return self


def transition_c4_base_once(
    state: C4State,
    observation: tuple[float, ...],
    c1_config: C1Config,
    replay_config: ReplayConfig,
) -> C4State:
    if state.replay is None:
        raise ValueError("C4 replay state is required for matched C2/C4 replay conditions")
    if state.replay.capacity != replay_config.capacity:
        raise ValueError("state replay capacity does not match replay configuration")
    return C4State(
        base=transition_c1(state.base, observation, c1_config),
        hypotheses=state.hypotheses,
        replay=state.replay.append(observation),
    )


def transition_c4_replay(
    state: C4State,
    replay_indices: tuple[int, ...],
    c1_config: C1Config,
    replay_config: ReplayConfig,
) -> C4State:
    if state.replay is None:
        raise ValueError("C4 replay state is required for matched C2/C4 replay conditions")
    updated_base = _apply_replay_indices(
        state.base,
        state.replay,
        replay_indices,
        c1_config,
        replay_config,
    )
    return C4State(
        base=updated_base,
        hypotheses=state.hypotheses,
        replay=state.replay,
    )


class ProposalKind(str, Enum):
    ADD_DEPENDENCY = "add_dependency"
    REMOVE_DEPENDENCY = "remove_dependency"
    REPLACE_ORIENTATION = "replace_orientation"
    CHANGE_SCOPE = "change_scope"
    SPLIT_HYPOTHESIS = "split_hypothesis"
    MERGE_RETIRE = "merge_retire"


@dataclass(frozen=True, slots=True)
class StructuralProposal:
    kind: ProposalKind
    hypothesis_handle: str
    dependency: Dependency | None = None
    new_scope: str | None = None
    new_handle: str | None = None
    retire_handle: str | None = None

    def __post_init__(self) -> None:
        if not self.hypothesis_handle:
            raise ValueError("hypothesis_handle must be nonempty")


def structural_predict(
    state: C4State,
    observation_context: tuple[float, ...],
    config: C4Config,
) -> Prediction:
    state.validate(config)
    _check_vector(observation_context, name="observation_context")
    if len(observation_context) != len(state.base.mean):
        raise ValueError("observation_context dimension mismatch")
    adjusted = list(state.base.mean)
    total_confidence = sum(h.confidence for h in state.hypotheses)
    if total_confidence > 0.0:
        for hypothesis in state.hypotheses:
            share = hypothesis.confidence / total_confidence
            for dependency in hypothesis.dependencies:
                adjusted[dependency.target] += (
                    share * dependency.weight * observation_context[dependency.source]
                )
    return Prediction(mean=tuple(adjusted), variance=state.base.variance)


def _replace_hypothesis(
    state: C4State,
    replacement: StructuralHypothesis,
) -> C4State:
    return C4State(
        base=state.base,
        hypotheses=tuple(
            replacement if h.handle == replacement.handle else h for h in state.hypotheses
        ),
        replay=state.replay,
    )


def apply_structural_proposal(
    state: C4State,
    proposal: StructuralProposal,
    config: C4Config,
) -> C4State:
    state.validate(config)
    by_handle = {h.handle: h for h in state.hypotheses}
    if proposal.hypothesis_handle not in by_handle:
        raise ValueError("proposal references unknown hypothesis")
    current = by_handle[proposal.hypothesis_handle]

    if proposal.kind is ProposalKind.ADD_DEPENDENCY:
        if proposal.dependency is None:
            raise ValueError("add_dependency requires dependency")
        replacement = StructuralHypothesis(
            current.handle,
            (*current.dependencies, proposal.dependency),
            current.confidence,
        )
        return _replace_hypothesis(state, replacement).validate(config)

    if proposal.kind is ProposalKind.REMOVE_DEPENDENCY:
        if proposal.dependency is None or proposal.dependency not in current.dependencies:
            raise ValueError("remove_dependency requires an existing dependency")
        replacement = StructuralHypothesis(
            current.handle,
            tuple(d for d in current.dependencies if d != proposal.dependency),
            current.confidence,
        )
        return _replace_hypothesis(state, replacement).validate(config)

    if proposal.kind is ProposalKind.REPLACE_ORIENTATION:
        if proposal.dependency is None or proposal.dependency not in current.dependencies:
            raise ValueError("replace_orientation requires an existing dependency")
        reversed_dep = Dependency(
            source=proposal.dependency.target,
            target=proposal.dependency.source,
            weight=proposal.dependency.weight,
            scope=proposal.dependency.scope,
        )
        replacement = StructuralHypothesis(
            current.handle,
            tuple(reversed_dep if d == proposal.dependency else d for d in current.dependencies),
            current.confidence,
        )
        return _replace_hypothesis(state, replacement).validate(config)

    if proposal.kind is ProposalKind.CHANGE_SCOPE:
        if proposal.dependency is None or proposal.dependency not in current.dependencies:
            raise ValueError("change_scope requires an existing dependency")
        if proposal.new_scope is None:
            raise ValueError("change_scope requires new_scope")
        changed = Dependency(
            source=proposal.dependency.source,
            target=proposal.dependency.target,
            weight=proposal.dependency.weight,
            scope=proposal.new_scope,
        )
        replacement = StructuralHypothesis(
            current.handle,
            tuple(changed if d == proposal.dependency else d for d in current.dependencies),
            current.confidence,
        )
        return _replace_hypothesis(state, replacement).validate(config)

    if proposal.kind is ProposalKind.SPLIT_HYPOTHESIS:
        if not proposal.new_handle or proposal.new_handle in by_handle:
            raise ValueError("split_hypothesis requires a unique new_handle")
        retained = StructuralHypothesis(
            current.handle,
            current.dependencies,
            current.confidence / 2.0,
        )
        branch = StructuralHypothesis(
            proposal.new_handle,
            current.dependencies,
            current.confidence / 2.0,
        )
        replaced = tuple(retained if h.handle == current.handle else h for h in state.hypotheses)
        return C4State(base=state.base, hypotheses=(*replaced, branch), replay=state.replay).validate(config)

    if proposal.kind is ProposalKind.MERGE_RETIRE:
        if not proposal.retire_handle or proposal.retire_handle == current.handle:
            raise ValueError("merge_retire requires a distinct retire_handle")
        if proposal.retire_handle not in by_handle:
            raise ValueError("retire_handle is unknown")
        retired = by_handle[proposal.retire_handle]
        merged = StructuralHypothesis(
            current.handle,
            current.dependencies,
            min(1.0, current.confidence + retired.confidence),
        )
        remaining = tuple(
            merged if h.handle == current.handle else h
            for h in state.hypotheses
            if h.handle != proposal.retire_handle
        )
        return C4State(base=state.base, hypotheses=remaining, replay=state.replay).validate(config)

    raise ValueError(f"unsupported proposal kind: {proposal.kind}")
