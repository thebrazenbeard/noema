from noema.accounting import ResourceLedger, SupportClass, SupportRecord
from noema.boundary import Prediction, commit_prediction
from noema.comparator import compare_committed_predictions


def test_consumed_unmeasured_resource_is_not_zero():
    ledger = ResourceLedger()
    ledger = ledger.consume("structural_compute", amount=None)
    assert "structural_compute" in ledger.unmeasured_classes
    assert ledger.measured_total("structural_compute") is None


def test_zero_support_cannot_claim_strong_confidence():
    try:
        SupportRecord(SupportClass.ZERO_OR_UNKNOWN_SUPPORT, confidence=0.9)
    except ValueError:
        pass
    else:
        raise AssertionError("zero support accepted strong confidence")


def test_comparator_record_binds_preoutcome_ticket_commitments_and_conditions():
    left = commit_prediction("c2", 4, Prediction((0.0,), (1.0,)))
    right = commit_prediction("c4", 4, Prediction((0.1,), (1.0,)))
    record = compare_committed_predictions(
        left,
        right,
        information_condition_id="info-1",
        opportunity_condition_id="opp-1",
        resource_condition_id="res-1",
        representation_version="rep-1",
    )
    assert record.left_commitment == left.commitment
    assert record.right_commitment == right.commitment
    assert record.step == 4
    assert record.resource_condition_id == "res-1"
