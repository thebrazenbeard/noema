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
        if len(self.seeds) != 8:
            raise ValueError("first-core SVF-0 requires exactly 8 seeds")
        if len(set(self.seeds)) != 8:
            raise ValueError("first-core SVF-0 seeds must be unique")
        if any(isinstance(seed, bool) or not isinstance(seed, int) for seed in self.seeds):
            raise ValueError("all frozen seeds must be integers")
        if self.max_events != 128:
            raise ValueError("first-core SVF-0 max_events must equal 128")


@dataclass(frozen=True, slots=True)
class SVF0SeedResult:
    seed: int
    negative_control: bool
    steps: tuple[SVF0StepResult, ...]


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
        steps=tuple(steps),
    )
