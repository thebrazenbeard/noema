from __future__ import annotations

from dataclasses import dataclass

from .boundary import PredictionTicket


@dataclass(frozen=True, slots=True)
class ComparatorRecord:
    left_candidate_id: str
    right_candidate_id: str
    step: int
    left_commitment: str
    right_commitment: str
    information_condition_id: str
    opportunity_condition_id: str
    resource_condition_id: str
    representation_version: str


def compare_committed_predictions(
    left: PredictionTicket,
    right: PredictionTicket,
    *,
    information_condition_id: str,
    opportunity_condition_id: str,
    resource_condition_id: str,
    representation_version: str,
) -> ComparatorRecord:
    if left.step != right.step:
        raise ValueError("comparison requires tickets from the same step")
    if left.candidate_id == right.candidate_id:
        raise ValueError("comparison requires distinct candidate IDs")
    values = (
        information_condition_id,
        opportunity_condition_id,
        resource_condition_id,
        representation_version,
    )
    if not all(values):
        raise ValueError("comparison condition identifiers must be nonempty")
    return ComparatorRecord(
        left_candidate_id=left.candidate_id,
        right_candidate_id=right.candidate_id,
        step=left.step,
        left_commitment=left.commitment,
        right_commitment=right.commitment,
        information_condition_id=information_condition_id,
        opportunity_condition_id=opportunity_condition_id,
        resource_condition_id=resource_condition_id,
        representation_version=representation_version,
    )
