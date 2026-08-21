# Final Project Submission Template

Use this template to write the **final research report**. Replace bracketed text with project-specific content. The completed report should be 6–8 pages, excluding references and appendices, and should be included in the GitHub repository with the supporting code, test materials, run records, and presentation materials. The framework review, research questions, implementation descriptions, evaluation, AI-use disclosure, and reproducibility information are sections of this one final report, not separate reports.

## Project Information

- Title: `[Project title]`
- Student(s): `[Name(s)]`
- Selected framework and version: `[Framework/version]`
- Model(s), provider/source, version, and access method: `[For example: API, local, or open-source]`
- Model configuration and any fine-tuning/adaptation: `[Settings, prompt configuration, or none]`
- Theme/domain: `[Domain]`
- Dataset(s): `[Classroom dataset or own dataset; source, permitted use, preprocessing, and citation]`
- GitHub repository: `[Link to repository containing the entire final-project folder]`

### AI-Use Disclosure

Document every AI tool or model used for substantive assistance. Include code, writing, analysis, data preparation, debugging, and similar assistance. Attach or link substantive prompts and outputs when appropriate.

| AI tool/model | Purpose and project component | Substantive prompt/output or record location | How output was verified |
|---|---|---|---|
| `[Tool/model]` | | | |

## 1. Framework Review and Selection

### Framework Comparison

| Framework | Pattern support | Tools/orchestration | Observability/testing | Model/provider support | Learning curve and limitations | Sources |
|---|---|---|---|---|---|---|
| `[Framework 1]` | | | | | | |
| `[Framework 2]` | | | | | | |
| `[Framework 3]` | | | | | | |
| `[Framework 4]` | | | | | | |
| `[Framework 5]` | | | | | | |

### Selection Rationale

State your criteria, explain the tradeoffs, and justify why the selected framework is appropriate for all five pattern implementations.

## 2. Pattern Implementations

Repeat the following subsection for Reflection, Tool Use, Planning, ReAct, and Multiagent.

### `[Pattern Name]`

- Research question: `[Question]`
- Evidence-based answer to the research question: `[Answer supported by run records and evaluation results]`
- Selected-framework notebook and run record: `[Notebook path, how it uses the selected framework, run command, and output/log link]`
- Intended task/user: `[Description]`
- Architecture or workflow: `[Diagram link or concise description]`
- Prompts, roles, tools, and state: `[Description/link]`
- Source location and run command: `[Path/command]`
- Dependencies/configuration: `[Requirements and safe configuration steps]`
- Sample input and output: `[Include or link]`
- Pattern-specific evidence:
  - Reflection: `[Initial response, critique, and revision]`
  - Tool Use: `[Tool schema, calls, and outputs]`
  - Planning: `[Initial plan, execution observations, and replan]`
  - ReAct: `[Reasoning/action/observation iterations]`
  - Multiagent: `[Agent roles and coordination/conflict-resolution record]`
- Limitations and failure modes: `[Description]`
- Proposed mitigations: `[Description]`

## 3. Experimental Evaluation

### Required Instructor and Student Implementation Comparison Evidence

For every pattern and test case, include or link to all of the following:

- The shared user question and input/data reference.
- The instructor-baseline implementation path or command in `src/` and its saved output.
- The student notebook path and its saved output.
- The LLM/model name and version, configuration, and any relevant tool, plan, reasoning/action/observation, or multiagent coordination record.
- The success-criterion score or determination for both implementations.
- A brief evidence-based comparison that explains the result, differences, and limitations.

### Success Criteria

Define measurable success criteria before interpreting results. A criterion must state what is being assessed, the metric or scoring method, the passing threshold, and the evidence or reference answer used to judge it. For every pattern, run the same cases with the **instructor-provided baseline implementation** in `src/` and with the **student reimplementation** in the selected agent framework. Use the user question, input/data, LLM/model, configuration, and criterion identically in both conditions. Students may use multiple LLMs, but must run the same cases and conditions for every LLM being compared. Use one row for each pattern; add rows when a pattern has more than one criterion.

| Pattern | Criterion ID and success criterion | Metric/scoring method | Pass threshold | Evidence, reference answer, or scoring guide | Reliability method and run count | Latency/cost collection method |
|---|---|---|---|---|---|---|
| Reflection | | | | | | |
| Tool Use | | | | | | |
| Planning | | | | | | |
| ReAct | | | | | | |
| Multiagent | | | | | | |

| Pattern | Controlled variables: question, data, LLM/model, configuration, and criterion | Instructor baseline implementation in `src/` | Student reimplementation in selected framework |
|---|---|---|---|
| Reflection | `[State identical values]` | `[Path/command]` | `[Path/command]` |
| Tool Use | `[State identical values]` | `[Path/command]` | `[Path/command]` |
| Planning | `[State identical values]` | `[Path/command]` | `[Path/command]` |
| ReAct | `[State identical values]` | `[Path/command]` | `[Path/command]` |
| Multiagent | `[State identical values]` | `[Path/command]` | `[Path/command]` |

For deterministic workflows, state why repeat runs are unnecessary. For stochastic workflows, run each test case at least three times using the same configuration, then report the number of successful runs and any meaningful variation. Record latency and cost when they are available; otherwise state `not available` and why.

### Test Results

Document at least three representative cases for **each** pattern, for a minimum of 15 cases. Run every case with the instructor baseline and the student reimplementation. Use one row per case. If a case is run repeatedly, record the run count and the number of runs that met the criterion. Copy the three-row block below for Reflection, Tool Use, Planning, ReAct, and Multiagent.

| Pattern | Case ID | Input/data reference | LLM/model and version | Criterion ID | Instructor baseline result/score | Student implementation result/score | Instructor baseline runs meeting criterion / total | Student implementation runs meeting criterion / total | Baseline vs. student latency/cost | Comparative finding, failure mode, or evidence citation |
|---|---|---|---|---|---|---|---|---|---|---|
| `[Pattern]` | 1 | | | | | | | | | |
| `[Pattern]` | 2 | | | | | | | | | |
| `[Pattern]` | 3 | | | | | | | | | |

### Findings

Summarize the instructor-baseline-versus-student-implementation comparison by pattern, including the number and proportion of cases that met each criterion in each condition, task quality, reliability, and latency/cost where available. State how the selected-framework implementation differed from the instructor baseline. Interpret material failure modes; for each one, identify a mitigation or next-step improvement. For forensic work, distinguish observations from conclusions and cite source artifacts or records.

### LLM/Model Comparison

Required when more than one LLM/model is used, including when the student-selected model differs from the instructor-baseline model. Compare models using the same implementation condition, pattern, cases, user question, data, configuration, and success criterion. Do not interpret a difference as a framework or pattern effect when the LLM/model changed.

| Pattern | LLM/model and version | Same cases and conditions used? | Quality/success-rate comparison | Reliability and latency/cost comparison | Limitations and evidence |
|---|---|---|---|---|---|
| `[Pattern]` | | | | | |

### Instructor Baseline and Classroom Lab Comparison

For each pattern, compare your selected-framework implementation's results with the corresponding classroom lab result or instructor-provided baseline in `src/`. Use the same user question, task, data, LLM/model, configuration, and success criterion whenever feasible. If a direct comparison is not valid, describe the differences and provide a justified qualitative comparison; do not make an unsupported performance claim.

| Pattern | Corresponding lab/result or `src/` baseline reference | Comparable question/task/data/model/criterion? | Comparison of results and forensic usefulness | Differences, limitations, and evidence |
|---|---|---|---|---|
| Reflection | | | | |
| Tool Use | | | | |
| Planning | | | | |
| ReAct | | | | |
| Multiagent | | | | |

## 4. Report, Reproducibility, and Oral Presentation

- Research report (6–8 pages, excluding references and appendices): `[Filename or link]`
- Environment and dependency setup: `[Instructions]`
- Configuration without secrets: `[Instructions]`
- Commands to run each pattern: `[Instructions]`
- Test data/materials location: `[Instructions]`
- Oral-presentation materials: `[Slides, recording, or link, if applicable]`
- Oral-presentation outline: `[Selected representative pattern; its forensic application; instructor-versus-student comparison; results; limitations; and each presenter's contribution]`

## 5. Presentation Reference Outline

Use the following outline as a guide for the oral presentation. Demonstrate one representative pattern only; the other four patterns only need to be identified as completed.

- **Project title and team:** State the project title, student name(s), and digital-forensics topic.
- **Selected agent framework:** Briefly introduce the framework and explain why the team chose it based on the framework review.
- **Project overview:** State that all five patterns were implemented. Identify the five notebooks, but do not explain or demonstrate the other four patterns in detail.
- **Selected pattern and research question:** Identify the one pattern being presented and describe its forensic task, user question, data, and success criterion.
- **Implementation comparison:** Explain the instructor implementation in `src/` and the student notebook in the selected framework. Identify the shared inputs, LLM/model, and configuration.
- **Demonstration:** Run or show the selected pattern notebook. Demonstrate only this one pattern.
- **Results and answer:** Compare outputs and results, then answer the research question using the recorded evidence.
- **Limitations and takeaway:** Describe important limitations or failures, lessons learned, and each presenter's contribution.

## 6. Submission Checklist

- [ ] The GitHub repository contains the entire `final-project` folder, including code, report, framework review, test materials/results, and presentation materials.
- [ ] Each student submitted the GitHub repository link individually through Sakai.
- [ ] The project package and oral presentation will be submitted/presented during the last class meeting.
- [ ] Dataset source, permitted use, preprocessing, and citations are documented. Private, sensitive, or real-case data has instructor approval.
- [ ] AI tools/models, their purpose, substantive assistance, and verification are disclosed. No private, sensitive, real-case, or restricted evidence was uploaded to an AI service without instructor approval.

## 7. References

List all framework documentation, technical sources, datasets, models, code, and other external materials in a consistent citation format.

## 8. Two-Student Contribution Record

Required only for two-student teams.

| Student | Responsibilities | Evidence of contribution | Approximate contribution |
|---|---|---|---:|
| `[Student 1]` | | | |
| `[Student 2]` | | | |

Each student must separately submit the instructor-requested confidential peer assessment.
