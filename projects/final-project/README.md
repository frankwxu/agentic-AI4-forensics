# Final Project: Agentic AI Patterns

## Overview

Design, implement, and evaluate five agentic-AI patterns using **one agent framework** that your team selects after a documented framework review. This is a 100-point final project and may be completed individually or by a team of two students.

Your five implementations must address five distinct, student-defined questions:

1. **Reflection** — improve an initial response through structured critique and revision.
2. **Tool Use** — select and invoke one or more callable tools to answer a question.
3. **Planning** — create an explicit plan, execute it, and revise the plan when observations require it.
4. **ReAct** — use an iterative reasoning, action, and observation loop.
5. **Multiagent** — coordinate at least two agents with distinct responsibilities.

Questions may come from any domain. Digital-forensics questions are strongly encouraged, especially questions that require evidence-based conclusions, clear uncertainty language, and a distinction between observed evidence and inference.

## Learning Objectives

By completing this project, you will be able to:

- Compare agent frameworks using credible evidence and select one that fits a stated technical goal.
- Implement and distinguish five core agentic-AI patterns.
- Design testable research questions and evaluate agent behavior with documented evidence.
- Analyze accuracy or task quality, reliability, latency or cost when available, limitations, and failure modes.
- Build reproducible agentic-AI software and communicate its design and results clearly.

## Required Workflow

1. Form an individual or two-student team and choose a project theme.
2. Review at least five agent frameworks using official documentation and credible technical sources.
3. Compare the reviewed frameworks and justify your selection of one framework.
4. Define five distinct research questions, one for each required pattern.
5. Implement all five patterns in the selected framework.
6. Create and run a documented test set with at least three representative cases for each pattern.
7. Analyze results, limitations, and mitigations; submit the report, runnable implementation, and demonstration.

## Agent Framework Review

Review at least five frameworks. The following are starting points; you may propose a different framework with instructor approval.

| Framework | Official reference |
|---|---|
| LangChain / LangGraph | [LangChain documentation](https://python.langchain.com/docs/) and [LangGraph documentation](https://langchain-ai.github.io/langgraph/) |
| AutoGen | [Microsoft AutoGen documentation](https://microsoft.github.io/autogen/) |
| CrewAI | [CrewAI documentation](https://docs.crewai.com/) |
| Semantic Kernel | [Microsoft Semantic Kernel documentation](https://learn.microsoft.com/semantic-kernel/) |
| LlamaIndex | [LlamaIndex documentation](https://docs.llamaindex.ai/) |
| Haystack | [Haystack documentation](https://docs.haystack.deepset.ai/) |
| OpenAI Agents SDK | [OpenAI Agents SDK documentation](https://openai.github.io/openai-agents-python/) |

For each reviewed framework, compare:

- Support for the five required patterns and agent orchestration.
- Tool integration and structured-output support.
- Observability, tracing, testing, and debugging support.
- Model/provider compatibility and deployment considerations.
- Learning curve, documentation quality, licensing, and known limitations.

State the criteria you used to select your framework, cite your sources, and explain why the selected framework is appropriate for all five implementations. The framework review is documentation/literature based; you do **not** need to implement the project in every reviewed framework.

## Pattern Implementation Requirements

Each pattern implementation must include the following in its code and report section:

- A clear research question and intended user/task.
- Architecture diagram or workflow description.
- Prompts, roles, tools, state, and orchestration logic used.
- Runnable source code, dependency list, sample inputs, and representative outputs.
- At least three documented test cases with expected success criteria.
- Results, limitations, failure modes, and proposed mitigations.

Additional requirements:

- **Reflection:** show an initial output, critique/reflection, and revised output.
- **Tool Use:** invoke at least one real or simulated callable tool and preserve tool inputs and outputs in the run record.
- **Planning:** demonstrate explicit plan creation, execution, and observation-driven replanning.
- **ReAct:** demonstrate repeated reasoning, action, and observation cycles. It must be implemented and analyzed separately from Planning.
- **Multiagent:** use at least two agents with distinct roles and explain how their outputs are coordinated, checked, or reconciled.

For forensic questions, identify the source artifact or record behind each important factual claim. Do not present an inference as if it were directly observed evidence.

## Evaluation Requirements

For each pattern, evaluate at least three representative cases. Define success before or while designing the test set; acceptable measures include task accuracy, evidence-citation completeness, valid tool-call rate, plan quality, conflict-resolution quality, or a justified domain-specific measure.

Report:

- Per-case result and whether it met the stated success criterion.
- Reliability across repeated runs, when stochastic behavior is relevant.
- Latency and/or cost when the framework or provider makes it available.
- Failure modes, including unsupported claims, invalid tool use, faulty plans, or unresolved agent disagreements.
- A mitigation or next-step improvement for each material failure mode.

## Deliverables

Submit one project package containing:

1. **Research report** — 6–8 pages, excluding references and appendices.
2. **Runnable implementation** — a source repository link or compressed source package with all five pattern implementations.
3. **README** — setup, configuration, dependency, execution, and reproduction instructions.
4. **Framework review** — comparison table, sources, selection criteria, and selection rationale; this may be part of the report or a separate appendix.
5. **Test materials and results** — questions, inputs/data references, expected criteria, outputs, and evaluation results.
6. **Demonstration** — short recorded or live demonstration showing the five implementations and one representative result from each.
7. **Team contribution record** — required only for two-student teams; see `EVALUATION.md`.

Use the suggested structure in [`submission-template.md`](submission-template.md).

## Data, Ethics, and Academic Integrity

- Prefer synthetic, public, or instructor-approved data.
- Do not submit private, sensitive, or real-case evidence unless the instructor explicitly approves its use and sharing.
- Protect identifiers and credentials. Do not place API keys, tokens, personal data, or restricted evidence in source control or the submission.
- Cite frameworks, models, datasets, code, and external materials. Clearly identify generated content and all substantive external assistance.
- Your team is responsible for understanding, testing, and explaining every submitted component. Work that cannot be explained or reproduced may not receive full credit.

## Submission Details

| Item | Placeholder |
|---|---|
| Proposal/checkpoint due | `[Instructor will provide]` |
| Final package due | `[Instructor will provide]` |
| Demonstration format/date | `[Instructor will provide]` |
| Submission location | `[Instructor will provide]` |

See [`EVALUATION.md`](EVALUATION.md) for the complete 100-point rubric and grading process.
