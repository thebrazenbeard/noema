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
