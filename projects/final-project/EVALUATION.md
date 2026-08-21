# Instructor Evaluation Guide: Final Project

## Grading Summary

The final project is worth **100 points**. For a two-student team, 95 points are based on shared project artifacts and 5 points measure individual contribution. A student whose documented contribution is materially insufficient may receive fewer individual-contribution points.

| Category | Points | What is evaluated |
|---|---:|---|
| Framework research and selection | 15 | Review quality, credible sources, comparison criteria, and defensible framework choice |
| Five pattern implementations | 40 | Correct, distinct, runnable implementations; 8 points per required pattern |
| Research questions and forensic relevance | 10 | Clear, feasible, distinct questions; suitable scope; well-motivated forensic relevance when used |
| Experimental evaluation | 20 | Test design, defined success criteria, results, reliability/performance analysis, and limitations |
| Report, reproducibility, and presentation | 10 | Report quality, citation, code organization, instructions, and demonstration |
| Individual contribution | 5 | Contribution evidence and peer assessment for teams of two |
| **Total** | **100** | |

## Rubric

### 1. Framework Research and Selection — 15 points

| Performance level | Criteria |
|---|---|
| 13–15 | Reviews at least five relevant frameworks with official documentation and credible sources; comparison addresses required criteria; selection is well justified for all five patterns and project constraints. |
| 9–12 | Reviews at least five frameworks with generally appropriate sources; comparison or selection rationale has minor gaps. |
| 5–8 | Framework review is incomplete, weakly sourced, or selection rationale is generic. |
| 0–4 | Fewer than five frameworks, major factual gaps, or no defensible selection rationale. |

### 2. Five Pattern Implementations — 40 points

Award up to **8 points per pattern**: Reflection, Tool Use, Planning, ReAct, and Multiagent.

| Points per pattern | Criteria |
|---:|---|
| 7–8 | Runnable and clearly distinct implementation; pattern behavior is correctly demonstrated; code, workflow, inputs, outputs, and limitations are documented. |
| 5–6 | Functional implementation with minor gaps in distinctness, documentation, or pattern-specific behavior. |
| 3–4 | Partially functional or weakly evidenced implementation; key pattern behavior is incomplete. |
| 0–2 | Missing, non-runnable, or does not implement the required pattern. |

Apply these pattern checks:

- Reflection includes initial output, critique, and revision.
- Tool Use invokes at least one callable tool and records inputs and outputs.
- Planning includes explicit planning, execution, observations, and replanning.
- ReAct includes iterative reasoning, action, and observation cycles; it is not scored as a duplicate of Planning.
- Multiagent includes at least two role-distinct agents and documented coordination or conflict reconciliation.

### 3. Research Questions and Forensic Relevance — 10 points

| Performance level | Criteria |
|---|---|
| 9–10 | Five clear, distinct, feasible questions; each is well aligned to its pattern and has meaningful success criteria. Forensic questions are evidence-aware and appropriately scoped. |
| 6–8 | Questions are mostly clear and distinct, with minor alignment or scope issues. |
| 3–5 | Questions are vague, overlapping, or poorly matched to their assigned patterns. |
| 0–2 | Questions are missing or do not support an evaluable implementation. |

Digital-forensics relevance is encouraged, not mandatory. When a forensic question is used, give credit for precise evidence-to-claim reasoning and appropriate uncertainty language.

### 4. Experimental Evaluation — 20 points

| Performance level | Criteria |
|---|---|
| 17–20 | At least three representative cases per pattern; clear success criteria; complete results; appropriate quality, reliability, and latency/cost analysis; limitations and mitigations are specific and evidence-based. |
| 13–16 | Complete test set and results with generally sound analysis; one area such as reliability, cost, or mitigation is limited. |
| 7–12 | Testing or success criteria is incomplete; analysis is mainly descriptive or lacks key evidence. |
| 0–6 | Minimal testing, no meaningful criteria, or results cannot be verified. |

### 5. Report, Reproducibility, and Presentation — 10 points

| Performance level | Criteria |
|---|---|
| 9–10 | Clear 6–8 page report; complete citations; organized code; reliable setup/run instructions; all requested artifacts; effective demonstration. |
| 6–8 | Substantially complete artifacts with minor clarity, organization, or reproducibility gaps. |
| 3–5 | Important documentation, citation, setup, or presentation gaps. |
| 0–2 | Missing report, non-reproducible work, or no demonstration. |

### 6. Individual Contribution — 5 points

Individual projects receive all 5 points when the submitted work demonstrates appropriate authorship and engagement. Two-student teams submit a brief contribution record with role/task assignments, evidence such as commits or work logs, and a confidential peer assessment. Score each student separately:

| Points | Criteria |
|---:|---|
| 5 | Contribution is substantial, documented, and consistent with peer assessment. |
| 3–4 | Contribution is documented but uneven or partially evidenced. |
| 1–2 | Limited documented contribution or material peer-assessment concern. |
| 0 | No credible evidence of contribution. |

## Grading Process and Acceptance Checks

1. Verify the submission contains all required deliverables and that setup instructions can be followed.
2. Confirm that all five patterns run and are meaningfully distinct.
3. Inspect the framework review and source quality before scoring the selected-framework rationale.
4. Score test materials and reported results against stated success criteria, rather than rewarding unsupported claims.
5. For forensic work, verify that important conclusions identify their supporting records or artifacts and distinguish evidence from inference.
6. Score shared categories once per team; score Individual Contribution separately for each student in a two-student team.

If a required implementation cannot run because of missing credentials, the student may provide a recorded run, sanitized configuration example, saved outputs, and sufficient source code for inspection. This supports partial evaluation but does not replace reproducibility expectations.

## Recommended Feedback Format

Provide one strength, one priority improvement, and one concrete next step for each category. For pattern implementations, name the relevant pattern and identify whether the issue concerns pattern fidelity, implementation quality, evidence quality, or evaluation quality.
