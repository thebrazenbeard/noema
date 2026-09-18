from __future__ import annotations

from dataclasses import dataclass

from .candidates import (
    RecurrentC2State,
    RecurrentGaussianState,
    RecurrentReplayBuffer,
)
from .svf0 import (
    SVF0NegativeControlConfig,
    SVF0WorldConfig,
    svf0_negative_control_point,
    svf0_point,
)
from .provenance import canonical_json_bytes, sha256_hex
from .svf0_runner import (
    SVF0RunnerConfig,
    SVF0RuntimeState,
    SVF0StepResult,
    SealedLearnerEvent,
    execute_svf0_step,
)


@dataclass(frozen=True, slots=True)
class E0ExecutionAuthority:
    authorization_id: str
    logical_subject_id: str

    def __post_init__(self) -> None:
        if not self.authorization_id:
            raise ValueError("authorization_id must be nonempty")
        if not self.logical_subject_id:
            raise ValueError("logical_subject_id must be nonempty")


_FROZEN_SEEDS = (101, 202, 303, 404, 505, 606, 707, 808)


@dataclass(frozen=True, slots=True)
class SVF0ExperimentPlan:
    logical_subject_id: str
    seeds: tuple[int, ...]
    max_events: int
    world: SVF0WorldConfig
    negative_control: SVF0NegativeControlConfig
    runner: SVF0RunnerConfig

    def __post_init__(self) -> None:
        if not self.logical_subject_id:
            raise ValueError("logical_subject_id must be nonempty")
        if self.seeds != _FROZEN_SEEDS:
            raise ValueError("first-core SVF-0 requires the exact frozen ordered 8 seeds")
        if self.max_events != 128:
            raise ValueError("first-core SVF-0 max_events must equal 128")
        world_tuple = (
            self.world.change_point,
            self.world.coefficient_before,
            self.world.coefficient_after,
            self.world.stable_coefficient,
            self.world.noise_half_width,
        )
        if world_tuple != (64, 0.8, -0.4, 0.3, 0.05):
            raise ValueError("primary world configuration differs from the frozen first-core plan")
        negative_tuple = (
            self.negative_control.coefficient,
            self.negative_control.stable_coefficient,
            self.negative_control.noise_half_width,
        )
        if negative_tuple != (0.4, -0.2, 0.05):
            raise ValueError("negative-control configuration differs from the frozen first-core plan")
        recurrent_tuple = (
            self.runner.recurrent.learning_rate,
            self.runner.recurrent.variance_alpha,
            self.runner.recurrent.variance_floor,
        )
        if recurrent_tuple != (0.1, 0.05, 0.0025):
            raise ValueError("recurrent configuration differs from the frozen first-core plan")
        replay_tuple = (
            self.runner.replay.capacity,
            self.runner.replay.max_replay_updates_per_event,
        )
        if replay_tuple != (32, 1):
            raise ValueError("replay configuration differs from the frozen first-core plan")
        if self.runner.reset_variance != 1.0:
            raise ValueError("reset variance differs from the frozen first-core plan")
        envelope = self.runner.envelope
        envelope_tuple = (
            envelope.max_resident_memory_bytes,
            envelope.max_durable_state_bytes,
            envelope.max_update_cpu_seconds_per_event,
            envelope.max_query_cpu_seconds_per_event,
            envelope.max_shadow_auditions_per_event,
        )
        if envelope_tuple != (268435456, 1048576, 0.05, 0.01, 0):
            raise ValueError("resource envelope differs from the frozen first-core plan")


def experiment_plan_commitment(plan: SVF0ExperimentPlan) -> str:
    payload = {
        "logical_subject_id": plan.logical_subject_id,
        "seeds": list(plan.seeds),
        "max_events": plan.max_events,
        "world": {
            "change_point": plan.world.change_point,
            "coefficient_before": plan.world.coefficient_before,
            "coefficient_after": plan.world.coefficient_after,
            "stable_coefficient": plan.world.stable_coefficient,
            "noise_half_width": plan.world.noise_half_width,
        },
        "negative_control": {
            "coefficient": plan.negative_control.coefficient,
            "stable_coefficient": plan.negative_control.stable_coefficient,
            "noise_half_width": plan.negative_control.noise_half_width,
        },
        "runner": {
            "recurrent": {
                "learning_rate": plan.runner.recurrent.learning_rate,
                "variance_alpha": plan.runner.recurrent.variance_alpha,
                "variance_floor": plan.runner.recurrent.variance_floor,
            },
            "replay": {
                "capacity": plan.runner.replay.capacity,
                "max_replay_updates_per_event": plan.runner.replay.max_replay_updates_per_event,
            },
            "reset_variance": plan.runner.reset_variance,
            "envelope": {
                "max_resident_memory_bytes": plan.runner.envelope.max_resident_memory_bytes,
                "max_durable_state_bytes": plan.runner.envelope.max_durable_state_bytes,
                "max_update_cpu_seconds_per_event": plan.runner.envelope.max_update_cpu_seconds_per_event,
                "max_query_cpu_seconds_per_event": plan.runner.envelope.max_query_cpu_seconds_per_event,
                "max_shadow_auditions_per_event": plan.runner.envelope.max_shadow_auditions_per_event,
            },
        },
    }
    return sha256_hex(canonical_json_bytes(payload))


@dataclass(frozen=True, slots=True)
class SVF0SeedResult:
    seed: int
    negative_control: bool
    logical_subject_id: str
    plan_commitment: str
    steps: tuple[SVF0StepResult, ...]

    def __post_init__(self) -> None:
        if not self.logical_subject_id:
            raise ValueError("logical_subject_id must be nonempty")
        if len(self.plan_commitment) != 64 or any(
            character not in "0123456789abcdef" for character in self.plan_commitment
        ):
            raise ValueError("plan_commitment must be a lowercase SHA-256 hex digest")


@dataclass(frozen=True, slots=True)
class SVF0ExperimentResult:
    logical_subject_id: str
    plan_commitment: str
    authorization_id: str
    primary_results: tuple[SVF0SeedResult, ...]
    negative_control_results: tuple[SVF0SeedResult, ...]


def initial_runtime_state(plan: SVF0ExperimentPlan) -> SVF0RuntimeState:
    base = RecurrentGaussianState.zeros(
        dimension=3,
        initial_variance=plan.runner.reset_variance,
    )
    return SVF0RuntimeState(
        c1=base,
        c2=RecurrentC2State(
            base=base,
            replay=RecurrentReplayBuffer.empty(plan.runner.replay),
        ),
    )


def _require_e0(
    *,
    plan: SVF0ExperimentPlan,
    authority: E0ExecutionAuthority | None,
) -> E0ExecutionAuthority:
    if authority is None:
        raise PermissionError("E0 execution authority is required")
    if authority.logical_subject_id != plan.logical_subject_id:
        raise PermissionError("E0 authority subject does not match frozen experiment subject")
    return authority


def _require_frozen_seed(plan: SVF0ExperimentPlan, seed: int) -> None:
    if seed not in plan.seeds:
        raise ValueError("seed is not in the frozen seed manifest")


def execute_primary_seed(
    *,
    plan: SVF0ExperimentPlan,
    seed: int,
    authority: E0ExecutionAuthority | None,
) -> SVF0SeedResult:
    _require_e0(plan=plan, authority=authority)
    _require_frozen_seed(plan, seed)

    state = initial_runtime_state(plan)
    steps: list[SVF0StepResult] = []
    for step in range(plan.max_events):
        point = svf0_point(seed=seed, step=step, config=plan.world)
        result = execute_svf0_step(
            sealed=SealedLearnerEvent(
                step=step,
                reveal=lambda point=point: point.learner_event,
            ),
            state=state,
            config=plan.runner,
        )
        steps.append(result)
        state = result.state
    return SVF0SeedResult(
        seed=seed,
        negative_control=False,
        logical_subject_id=plan.logical_subject_id,
        plan_commitment=experiment_plan_commitment(plan),
        steps=tuple(steps),
    )


def execute_negative_control_seed(
    *,
    plan: SVF0ExperimentPlan,
    seed: int,
    authority: E0ExecutionAuthority | None,
) -> SVF0SeedResult:
    _require_e0(plan=plan, authority=authority)
    _require_frozen_seed(plan, seed)

    state = initial_runtime_state(plan)
    steps: list[SVF0StepResult] = []
    for step in range(plan.max_events):
        point = svf0_negative_control_point(
            seed=seed,
            step=step,
            config=plan.negative_control,
        )
        result = execute_svf0_step(
            sealed=SealedLearnerEvent(
                step=step,
                reveal=lambda point=point: point.learner_event,
            ),
            state=state,
            config=plan.runner,
        )
        steps.append(result)
        state = result.state
    return SVF0SeedResult(
        seed=seed,
        negative_control=True,
        logical_subject_id=plan.logical_subject_id,
        plan_commitment=experiment_plan_commitment(plan),
        steps=tuple(steps),
    )


def execute_frozen_experiment(
    *,
    plan: SVF0ExperimentPlan,
    authority: E0ExecutionAuthority | None,
) -> SVF0ExperimentResult:
    _require_e0(plan=plan, authority=authority)
    primary_results = tuple(
        execute_primary_seed(plan=plan, seed=seed, authority=authority)
        for seed in plan.seeds
    )
    negative_control_results = tuple(
        execute_negative_control_seed(plan=plan, seed=seed, authority=authority)
        for seed in plan.seeds
    )
    assert authority is not None
    return SVF0ExperimentResult(
        logical_subject_id=plan.logical_subject_id,
        plan_commitment=experiment_plan_commitment(plan),
        authorization_id=authority.authorization_id,
        primary_results=primary_results,
        negative_control_results=negative_control_results,
    )
