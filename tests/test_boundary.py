from noema.boundary import LearnerEvent, EvaluatorRecord, Prediction, commit_prediction


def test_learner_event_has_no_evaluator_truth_fields():
    event = LearnerEvent(step=3, channels=(1.0, 2.0), intervention=None)
    assert not hasattr(event, "hidden_family")
    assert not hasattr(event, "score")


def test_prediction_ticket_commitment_is_stable():
    pred = Prediction(mean=(0.0, 1.0), variance=(1.0, 2.0))
    a = commit_prediction("c2", 7, pred)
    b = commit_prediction("c2", 7, pred)
    assert a.commitment == b.commitment
    assert len(a.commitment) == 64


def test_evaluator_record_is_separate_type():
    record = EvaluatorRecord(step=3, hidden_family="F", realized_score=None)
    assert record.hidden_family == "F"
