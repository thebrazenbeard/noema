from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable

from .accounting import (
    FixedEnvelope,
    adjudicate_fixed_envelope,
    durable_state_bytes,
    measure_operation,
)
from .boundary import LearnerEvent, PredictionTicket, commit_prediction
from .candidates import (
    RecurrentC2State,
    RecurrentConfig,
    RecurrentGaussianState,
    RecurrentReplayConfig,
    predict_recurrent,
    predict_reset_reference,
    select_most_recent_replay_indices,
    transition_recurrent,
    transition_recurrent_c2_once,
    transition_recurrent_c2_replay,
)
from .svf0 import gaussian_nll


@dataclass(frozen=True, slots=True)
class SealedLearnerEvent:
    step: int
    reveal: Callable[[], LearnerEvent]

    def __post_init__(self) -> None:
        if self.step < 0:
            raise ValueError("sealed step must be nonnegative")
        if not callable(self.reveal):
            raise ValueError("reveal must be callable")


@dataclass(frozen=True, slots=True)
class SVF0RuntimeState:
    c1: RecurrentGaussianState
    c2: RecurrentC2State

    def __post_init__(self) -> None:
        if len(self.c1.weights) != len(self.c2.base.weights):
            raise ValueError("C1 and C2 dimensions must match")
        if self.c1.previous != self.c2.base.previous:
            raise ValueError("C1 and C2 must enter a step with identical live context")


@dataclass(frozen=True, slots=True)
class SVF0RunnerConfig:
    recurrent: RecurrentConfig
    replay: RecurrentReplayConfig
    reset_variance: float
    envelope: FixedEnvelope

    def __post_init__(self) -> None:
        if not math.isfinite(self.reset_variance) or self.reset_variance <= 0:
            raise ValueError("reset_variance must be finite and positive")


@dataclass(frozen=True, slots=True)
class StepResources:
    query_cpu_seconds: float
    update_cpu_seconds: float
    resident_memory_bytes: int
    durable_state_bytes: int
    python_peak_allocated_bytes: int
    envelope_valid: bool
    violations: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CandidateStepRecord:
    ticket: PredictionTicket
    outcome: tuple[float, ...]
    score: float
    resources: StepResources
    replay_updates: int


@dataclass(frozen=True, slots=True)
class SVF0StepResult:
    state: SVF0RuntimeState
    learner_event: LearnerEvent
    candidate_records: tuple[CandidateStepRecord, ...]

    @property
    def point_valid(self) -> bool:
        return all(record.resources.envelope_valid for record in self.candidate_records)

    @property
    def invalid_candidate_ids(self) -> tuple[str, ...]:
        return tuple(
            record.ticket.candidate_id
            for record in self.candidate_records
            if not record.resources.envelope_valid
        )


def _resources(
    *,
    envelope: FixedEnvelope,
    query_measurement,
    update_measurement,
    durable_bytes: int,
    shadow_auditions: int = 0,
) -> StepResources:
    query_cpu = query_measurement.cpu_seconds
    update_cpu = 0.0 if update_measurement is None else update_measurement.cpu_seconds
    resident = query_measurement.resident_memory_bytes
    python_peak = query_measurement.python_peak_allocated_bytes
    if update_measurement is not None:
        resident = max(resident, update_measurement.resident_memory_bytes)
        python_peak = max(python_peak, update_measurement.python_peak_allocated_bytes)
    adjudication = adjudicate_fixed_envelope(
        envelope,
        resident_memory_bytes=resident,
        durable_state_bytes=durable_bytes,
        update_cpu_seconds=update_cpu,
        query_cpu_seconds=query_cpu,
        shadow_auditions=shadow_auditions,
    )
    return StepResources(
        query_cpu_seconds=query_cpu,
        update_cpu_seconds=update_cpu,
        resident_memory_bytes=resident,
        durable_state_bytes=durable_bytes,
        python_peak_allocated_bytes=python_peak,
        envelope_valid=adjudication.valid,
        violations=adjudication.violations,
    )


def execute_svf0_step(
    *,
    sealed: SealedLearnerEvent,
    state: SVF0RuntimeState,
    config: SVF0RunnerConfig,
) -> SVF0StepResult:
    if state.c2.replay.capacity != config.replay.capacity:
        raise ValueError("C2 replay capacity does not match runner configuration")

    c1_query = measure_operation(lambda: predict_recurrent(state.c1))
    c2_query = measure_operation(lambda: predict_recurrent(state.c2.base))
    reset_query = measure_operation(
        lambda: predict_reset_reference(
            dimension=len(state.c1.weights),
            variance=config.reset_variance,
        )
    )

    c1_ticket = commit_prediction("c1_recurrent", sealed.step, c1_query.result)
    c2_ticket = commit_prediction("c2_recurrent_replay", sealed.step, c2_query.result)
    reset_ticket = commit_prediction("reset_ref", sealed.step, reset_query.result)

    event = sealed.reveal()
    if event.step != sealed.step:
        raise ValueError("revealed event step does not match sealed step")
    if event.intervention is not None:
        raise ValueError("SVF-0 runner rejects intervention packets")
    outcome = tuple(event.channels)

    c1_score = gaussian_nll(
        outcome=outcome,
        mean=c1_ticket.prediction.mean,
        variance=c1_ticket.prediction.variance,
    )
    c2_score = gaussian_nll(
        outcome=outcome,
        mean=c2_ticket.prediction.mean,
        variance=c2_ticket.prediction.variance,
    )
    reset_score = gaussian_nll(
        outcome=outcome,
        mean=reset_ticket.prediction.mean,
        variance=reset_ticket.prediction.variance,
    )

    c1_update = measure_operation(
        lambda: transition_recurrent(state.c1, outcome, config.recurrent)
    )

    def _c2_update():
        live = transition_recurrent_c2_once(
            state.c2,
            outcome,
            config.recurrent,
            config.replay,
        )
        replay_indices = select_most_recent_replay_indices(
            item_count=len(live.replay.items),
            max_updates=config.replay.max_replay_updates_per_event,
        )
        updated = transition_recurrent_c2_replay(
            live,
            replay_indices,
            config.recurrent,
            config.replay,
        )
        return updated, len(replay_indices)

    c2_update = measure_operation(_c2_update)
    next_c2, replay_updates = c2_update.result

    c1_resources = _resources(
        envelope=config.envelope,
        query_measurement=c1_query,
        update_measurement=c1_update,
        durable_bytes=durable_state_bytes(c1_update.result),
    )
    c2_resources = _resources(
        envelope=config.envelope,
        query_measurement=c2_query,
        update_measurement=c2_update,
        durable_bytes=durable_state_bytes(next_c2),
    )
    reset_resources = _resources(
        envelope=config.envelope,
        query_measurement=reset_query,
        update_measurement=None,
        durable_bytes=0,
    )

    records = (
        CandidateStepRecord(
            ticket=c1_ticket,
            outcome=outcome,
            score=c1_score,
            resources=c1_resources,
            replay_updates=0,
        ),
        CandidateStepRecord(
            ticket=c2_ticket,
            outcome=outcome,
            score=c2_score,
            resources=c2_resources,
            replay_updates=replay_updates,
        ),
        CandidateStepRecord(
            ticket=reset_ticket,
            outcome=outcome,
            score=reset_score,
            resources=reset_resources,
            replay_updates=0,
        ),
    )

    return SVF0StepResult(
        state=SVF0RuntimeState(c1=c1_update.result, c2=next_c2),
        learner_event=event,
        candidate_records=records,
    )
