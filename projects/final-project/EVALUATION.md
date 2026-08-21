# Instructor Evaluation Guide: Final Project

## Grading Summary

The final project is worth **100 points**. For a two-student team, 95 points are based on shared project artifacts and 5 points measure individual contribution. A student whose documented contribution is materially insufficient may receive fewer individual-contribution points.

| Category | Points | What is evaluated |
|---|---:|---|
| Framework research and selection | 5 | Review quality, credible sources, comparison criteria, and defensible framework choice |
| Five pattern implementations | 35 | Correct, distinct, runnable implementations; 7 points per required pattern |
| Research questions and forensic relevance | 15 | Clear, feasible, distinct questions; suitable scope; well-motivated digital-forensics relevance |
| Experimental evaluation | 20 | Test design, defined success criteria, results, reliability/performance analysis, and limitations |
| Report and reproducibility | 5 | Report quality, citations, code organization, and setup/run instructions |
| Oral presentation | 15 | Clear, accurate explanation of one representative pattern's digital-forensics application, comparison results, and limitations |
| Individual contribution | 5 | Contribution evidence and peer assessment for teams of two |
| **Total** | **100** | |

## Rubric

### 1. Framework Research and Selection — 5 points

| Performance level | Criteria |
|---|---|
| 5 | Reviews at least five relevant frameworks with official documentation and credible sources; comparison addresses required criteria; selection is justified for all five patterns and project constraints. |
| 3–4 | Reviews at least five frameworks with generally appropriate sources; comparison or selection rationale has minor gaps. |
| 1–2 | Framework review is incomplete, weakly sourced, or selection rationale is generic. |
| 0 | Fewer than five frameworks, major factual gaps, or no defensible selection rationale. |

### 2. Five Pattern Implementations — 35 points

Award up to **7 points per pattern**: Reflection, Tool Use, Planning, ReAct, and Multiagent.

| Points per pattern | Criteria |
|---:|---|
| 6–7 | The required pattern notebook is runnable and clearly distinct in the selected AI agent framework; pattern behavior is correctly demonstrated; code, workflow, inputs, outputs, and limitations are documented. |
| 4–5 | Functional implementation with minor gaps in distinctness, documentation, or pattern-specific behavior. |
| 2–3 | Partially functional or weakly evidenced implementation; key pattern behavior is incomplete. |
| 0–1 | Missing, non-runnable, or does not implement the required pattern. |

Apply these pattern checks:

- Reflection includes initial output, critique, and revision.
- Tool Use invokes at least one callable tool and records inputs and outputs.
- Planning includes explicit planning, execution, observations, and replanning.
- ReAct includes iterative reasoning, action, and observation cycles; it is not scored as a duplicate of Planning.
- Multiagent includes at least two role-distinct agents and documented coordination or conflict reconciliation.

### 3. Research Questions and Forensic Relevance — 15 points

| Performance level | Criteria |
|---|---|
| 13–15 | Five clear, distinct, feasible questions; each is well aligned to its pattern, meaningful success criteria, and a digital-forensics task. The questions and answers demonstrate evidence-aware reasoning and appropriate scope. |
| 9–12 | Questions are mostly clear and distinct, with minor alignment, scope, or digital-forensics application issues. |
| 5–8 | Questions are vague, overlapping, weakly connected to digital forensics, or poorly matched to their assigned patterns. |
| 0–4 | Questions are missing or do not support an evaluable implementation. |

Digital forensics is the required project focus. Give credit for precise evidence-to-claim reasoning and appropriate uncertainty language. A non-forensic topic requires instructor approval.

Research questions should be distinct, testable, and assigned one per required pattern. The following are suitable examples:

- **Reflection:** How does a Reflection reimplementation in the selected framework compare with the instructor-provided Reflection implementation when producing a forensic incident summary?
- **Tool Use:** How does a Tool Use reimplementation in the selected framework compare with the instructor-provided implementation for malware identification using a hash-lookup tool?
- **Planning:** How does a Planning reimplementation in the selected framework compare with the instructor-provided implementation for a multi-step evidence-triage task?
- **ReAct:** How does a ReAct reimplementation in the selected framework compare with the instructor-provided implementation when analyzing log files?
- **Multiagent:** How does a Multiagent reimplementation in the selected framework compare with the instructor-provided implementation for evidence-citation completeness?

Students must answer each research question using evidence from their pattern runs and evaluations. Evidence may include saved inputs and outputs, tool-call records, run logs, instructor-baseline versus student-implementation results, measured success criteria, and documented failures. Claims about differences or similarities must be consistent with the reported evidence.

### 4. Experimental Evaluation — 20 points

| Performance level | Criteria |
|---|---|
| 17–20 | At least three representative cases per pattern, each run with the instructor-provided `src/` baseline implementation and the student reimplementation using the same user question, data, LLM/model, configuration, and success criterion. Student-selected models are fully documented and, when they differ from the instructor-baseline model, compared under the same conditions. Includes clear success criteria, complete comparative results, appropriate quality, reliability, and latency/cost analysis, and specific evidence-based limitations and mitigations. |
| 13–16 | Complete paired test set and generally sound instructor-baseline, student-implementation, and LLM comparison; one area such as reliability, cost, or mitigation is limited. |
| 7–12 | Instructor-baseline, student-implementation, LLM, or classroom-lab comparison, testing, or success criteria is incomplete; analysis is mainly descriptive or lacks key evidence. |
| 0–6 | Minimal testing, no meaningful comparison, or results cannot be verified. |

### 5. Report and Reproducibility — 5 points

| Performance level | Criteria |
|---|---|
| 5 | Clear 6–8 page report; complete citations; organized code; reliable setup/run instructions; all requested artifacts are present. |
| 3–4 | Substantially complete artifacts with minor clarity, organization, citation, or reproducibility gaps. |
| 1–2 | Important documentation, citation, or setup gaps. |
| 0 | Missing report or non-reproducible work. |

### 6. Oral Presentation — 15 points

| Points | Criteria |
|---:|---|
| 13–15 | Clear, well organized presentation that accurately explains one representative pattern in plain language; connects it to the digital-forensics task; presents the instructor-versus-student comparison, results, and limitations; and demonstrates that each presenter understands their contribution. |
| 9–12 | Presentation explains the selected pattern, forensic application, and results with minor omissions, unclear organization, or limited discussion of limitations. |
| 5–8 | Presentation is substantially incomplete, unclear, weakly connected to the forensic task, or contains material inaccuracies. |
| 0–4 | No oral presentation or the presenters cannot explain the submitted work. |

### 7. Individual Contribution — 5 points

Individual projects receive all 5 points when the submitted work demonstrates appropriate authorship and engagement. Two-student teams submit a brief contribution record with role/task assignments, evidence such as commits or work logs, and a confidential peer assessment. Score each student separately:

| Points | Criteria |
|---:|---|
| 5 | Contribution is substantial, documented, and consistent with peer assessment. |
| 3–4 | Contribution is documented but uneven or partially evidenced. |
| 1–2 | Limited documented contribution or material peer-assessment concern. |
| 0 | No credible evidence of contribution. |

## Grading Process and Acceptance Checks

Students may use a dataset previously used in class or their own dataset. Confirm that the dataset source, permitted use, preprocessing, and any applicable citations are documented; data involving private, sensitive, or real-case evidence requires instructor approval.

AI tools and student-selected models may be used, but students must disclose the tool/model, version, source/provider, configuration, purpose, and substantive assistance in the project materials. Verify AI-generated outputs, do not submit undisclosed AI-generated work as original work, and do not upload private, sensitive, real-case, or restricted evidence to an AI service without instructor approval. Use the oral presentation to confirm that students understand and can explain their submitted work.

1. Verify the submission contains all required deliverables and that setup instructions can be followed.
2. Confirm that the required notebook in each of the five pattern folders runs in the selected AI agent framework and that the patterns are meaningfully distinct.
3. Inspect the framework review and source quality before scoring the selected-framework rationale.
4. Confirm that each instructor-baseline versus student-implementation comparison holds the user question, data, LLM/model, configuration, and success criterion constant. When a student-selected model differs from the instructor-baseline model, confirm that the models are compared using the same cases and conditions. Score test materials, results, and classroom-lab comparisons against stated success criteria, rather than rewarding unsupported claims.
5. For forensic work, verify that important conclusions identify their supporting records or artifacts and distinguish evidence from inference.
6. Score the oral presentation and shared project categories once per team; score Individual Contribution separately for each student in a two-student team.

If a required implementation cannot run because of missing credentials, the student may provide a recorded run, sanitized configuration example, saved outputs, and sufficient source code for inspection. This supports partial evaluation but does not replace reproducibility expectations.

## Recommended Feedback Format

Provide one strength, one priority improvement, and one concrete next step for each category. For pattern implementations, name the relevant pattern and identify whether the issue concerns pattern fidelity, implementation quality, evidence quality, or evaluation quality.
