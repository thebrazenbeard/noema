from noema.candidates import C4Config, C4State, Dependency, GaussianState, StructuralHypothesis, structural_predict


def test_c4_rejects_semantic_relation_names():
    try:
        Dependency(source=0, target=1, weight=0.5, scope="cause")
    except ValueError as exc:
        assert "semantic" in str(exc).lower()
    else:
        raise AssertionError("semantic structural label accepted")


def test_structural_prediction_is_base_plus_bounded_generic_adjustment():
    base = GaussianState(mean=(1.0, 2.0), variance=(1.0, 1.0), count=0)
    hyp = StructuralHypothesis(
        handle="h1",
        dependencies=(Dependency(0, 1, 0.5, "current"),),
        confidence=1.0,
    )
    state = C4State(base=base, hypotheses=(hyp,))
    pred = structural_predict(
        state,
        observation_context=(4.0, 0.0),
        config=C4Config(max_active_hypotheses=2, max_abs_weight=1.0),
    )
    assert pred.mean == (1.0, 4.0)


def test_c4_population_cap_is_enforced():
    base = GaussianState(mean=(0.0,), variance=(1.0,), count=0)
    h1 = StructuralHypothesis(handle="h1", dependencies=(), confidence=0.5)
    h2 = StructuralHypothesis(handle="h2", dependencies=(), confidence=0.5)
    try:
        C4State(base=base, hypotheses=(h1, h2)).validate(C4Config(max_active_hypotheses=1, max_abs_weight=1.0))
    except ValueError as exc:
        assert "population" in str(exc).lower()
    else:
        raise AssertionError("over-cap population accepted")


def test_generic_add_dependency_proposal_is_bounded():
    from noema.candidates import ProposalKind, StructuralProposal, apply_structural_proposal
    base = GaussianState(mean=(0.0, 0.0), variance=(1.0, 1.0), count=0)
    h = StructuralHypothesis(handle="h1", dependencies=(), confidence=1.0)
    state = C4State(base=base, hypotheses=(h,))
    proposal = StructuralProposal(
        kind=ProposalKind.ADD_DEPENDENCY,
        hypothesis_handle="h1",
        dependency=Dependency(0, 1, 0.25, "current"),
    )
    updated = apply_structural_proposal(
        state,
        proposal,
        C4Config(max_active_hypotheses=2, max_abs_weight=1.0),
    )
    assert updated.hypotheses[0].dependencies == (Dependency(0, 1, 0.25, "current"),)


def test_generic_structural_proposal_family_has_no_task_specific_kind():
    from noema.candidates import ProposalKind
    assert {kind.value for kind in ProposalKind} == {
        "add_dependency",
        "remove_dependency",
        "replace_orientation",
        "change_scope",
        "split_hypothesis",
        "merge_retire",
    }


def test_remove_dependency_proposal_removes_exact_generic_edge():
    from noema.candidates import ProposalKind, StructuralProposal, apply_structural_proposal
    dep = Dependency(0, 1, 0.25, "current")
    base = GaussianState(mean=(0.0, 0.0), variance=(1.0, 1.0), count=0)
    state = C4State(base=base, hypotheses=(StructuralHypothesis("h1", (dep,), 1.0),))
    proposal = StructuralProposal(ProposalKind.REMOVE_DEPENDENCY, "h1", dependency=dep)
    updated = apply_structural_proposal(state, proposal, C4Config(2, 1.0))
    assert updated.hypotheses[0].dependencies == ()


def test_split_and_merge_retire_are_bounded_and_deterministic():
    from noema.candidates import ProposalKind, StructuralProposal, apply_structural_proposal
    base = GaussianState(mean=(0.0,), variance=(1.0,), count=0)
    state = C4State(base=base, hypotheses=(StructuralHypothesis("h1", (), 1.0),))
    split = StructuralProposal(ProposalKind.SPLIT_HYPOTHESIS, "h1", new_handle="h2")
    state = apply_structural_proposal(state, split, C4Config(2, 1.0))
    assert tuple(h.handle for h in state.hypotheses) == ("h1", "h2")
    merge = StructuralProposal(ProposalKind.MERGE_RETIRE, "h1", retire_handle="h2")
    state = apply_structural_proposal(state, merge, C4Config(2, 1.0))
    assert tuple(h.handle for h in state.hypotheses) == ("h1",)


def test_c4_can_use_same_base_replay_kernel_as_c2_without_touching_structure():
    from noema.candidates import C1Config, ReplayBuffer, ReplayConfig, transition_c4_base_once
    base = GaussianState(mean=(0.0,), variance=(1.0,), count=0)
    replay = ReplayConfig(capacity=2, max_replay_updates_per_event=1)
    state = C4State(
        base=base,
        hypotheses=(StructuralHypothesis("h1", (), 1.0),),
        replay=ReplayBuffer.empty(replay),
    )
    updated = transition_c4_base_once(
        state,
        (2.0,),
        C1Config(alpha=0.25, variance_floor=0.01),
        replay,
    )
    assert updated.base.mean == (0.5,)
    assert updated.replay.items == ((2.0,),)
    assert updated.hypotheses == state.hypotheses
