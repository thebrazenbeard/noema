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


def test_durable_state_bytes_uses_pickle_protocol_5():
    import pickle
    from noema.accounting import durable_state_bytes
    state = {"x": (1, 2, 3)}
    assert durable_state_bytes(state) == len(pickle.dumps(state, protocol=5))


def test_measure_operation_returns_result_cpu_and_peak_memory_without_hiding_measurement():
    from noema.accounting import measure_operation
    measured = measure_operation(lambda: sum(range(100)))
    assert measured.result == 4950
    assert measured.cpu_seconds >= 0.0
    assert measured.peak_memory_bytes >= 0


def test_fixed_envelope_fails_closed_on_missing_or_over_budget_measurement():
    from noema.accounting import FixedEnvelope, adjudicate_fixed_envelope
    envelope = FixedEnvelope(
        max_resident_memory_bytes=100,
        max_durable_state_bytes=100,
        max_update_cpu_seconds_per_event=0.1,
        max_query_cpu_seconds_per_event=0.1,
        max_shadow_auditions_per_event=0,
    )
    assert adjudicate_fixed_envelope(
        envelope,
        resident_memory_bytes=None,
        durable_state_bytes=10,
        update_cpu_seconds=0.01,
        query_cpu_seconds=0.01,
        shadow_auditions=0,
    ).valid is False
    result = adjudicate_fixed_envelope(
        envelope,
        resident_memory_bytes=101,
        durable_state_bytes=10,
        update_cpu_seconds=0.01,
        query_cpu_seconds=0.01,
        shadow_auditions=0,
    )
    assert result.valid is False
    assert "resident_memory_bytes" in result.violations
