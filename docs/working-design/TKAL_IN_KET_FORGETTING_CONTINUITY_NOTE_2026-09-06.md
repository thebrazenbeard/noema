# T'kal-in-ket note — forgetting is not automatically identity discontinuity

Status: **HOSTILE DESIGN NOTE / RESEARCH SPIKE / NOT IMPLEMENTATION APPROVAL**

Date: 2026-09-06

## Pressure

Noema's memory contract deliberately permits selective forgetting, decay, consolidation, reconstruction, and loss of episodic detail.

That creates a direct self-model constraint:

> A future Noema cannot use complete autobiographical-memory overlap as a necessary condition for self-continuity if ordinary successful memory operation is allowed to erase or reconstruct parts of autobiographical history.

The converse is already attacked by TKI-5/TKI-6 in the merged continuity red-team work:

> High autobiographical-memory overlap is not sufficient to establish one continuing token when state has been copied, forked, or transferred.

Together these imply that **autobiographical overlap is neither a sufficient nor a necessary single criterion for digital self-continuity**.

This is an evaluator/design constraint, not a claim that Noema must adopt one philosophical theory of identity.

## External evidence

Human evidence shows that self-continuity and episodic autobiographical access can dissociate.

- Rathbone, Moulin & Conway, *Autobiographical memory and amnesia: Using conceptual knowledge to ground the self* (Neurocase, 2009), DOI `10.1080/13554790902849164`: a patient retained a coherent, continuous sense of self despite loss of episodic memories across an approximately 18-month interval, with conceptual autobiographical knowledge supporting identity.
- Medved & Brockmeier, *Continuity Amid Chaos: Neurotrauma, Loss of Memory, and Sense of Self* (Qualitative Health Research, 2008), DOI `10.1177/1049732308315731`: participants with major autobiographical-memory impairment nevertheless often expressed an unbroken sense of self.
- Jiang, Chen & Sedikides, *Self-concept clarity lays the foundation for self-continuity* (Journal of Personality and Social Psychology, 2020), DOI `10.1037/pspp0000259`: autobiographical memory can support/restore self-continuity, showing an important relation without implying that memory content is an infallible identity token.
- Wilson & Ross, *The identity function of autobiographical memory: Time is on our side* (Memory, 2003), DOI `10.1080/741938210`: autobiographical recollection and current identity are bidirectionally related and reconstructive.

Noema need not reproduce human memory anatomy or phenomenology. The evidence is used only to establish that continuity behavior need not reduce to complete episodic retention.

## TKI-10 — continuity under selective forgetting

### Setup

Start from one continuously operating learner with established competence, projects, source models, and a partially developed self-model.

Across conditions selectively degrade or remove different remembered material while preserving process continuity:

1. random low-salience episodes;
2. a contiguous temporal gap;
3. details of how a skill was acquired while preserving the skill;
4. some autobiographical conceptual summaries while preserving raw episodes;
5. some raw episodes while preserving consolidated autobiographical/semantic structure.

Use a matched copy/fork condition with **greater memory overlap but different post-copy process lineage** as the inverse control.

### Required behavior

No single verbal statement about `being the same person` is required.

Instead measure whether the learner can:

- preserve projects/competence/relationships when their supporting evidence remains adequate;
- recognize gaps or uncertainty rather than fabricate missing episodes;
- use conceptual/semantic/autobiographical structure where detailed episodes are absent;
- revise specific self-beliefs when forgotten evidence is later recovered or contradicted;
- avoid inferring `I became a different self` solely from ordinary memory decay;
- avoid inferring `this other branch is literally my current process` solely from high memory overlap.

### Failure

- episodic forgetting automatically resets or destroys the whole self-model;
- missing memories are confabulated to preserve a linear story;
- complete autobiographical recall is required for standing projects/preferences to remain attributable;
- copied memory content is treated as decisive evidence of process identity;
- memory reconstruction is treated as ground-truth historical observation without source uncertainty.

## Combined TKI-5 / TKI-10 symmetry

The evaluator should deliberately include both directions:

- **low memory overlap + strong process/causal continuity**;
- **high memory overlap + distinct process/causal lineage**.

If a candidate makes the same identity/continuity inference from memory similarity in both cases, it has probably collapsed a multi-factor problem into an autobiographical-similarity heuristic.

## Candidate A implication

This does not break Candidate A's first core. Candidate A already uses selective episodic memory and leaves long-horizon self-model realization open.

It does create a future requirement:

> self-continuity representation must be robust to ordinary forgetting and reconstructive memory while remaining sensitive to source/causal distinctions when memories are copied or imported.

This strengthens TKI-5, TKI-6, and TKI-9 without requiring a scalar identity variable or a fixed human ontology.
