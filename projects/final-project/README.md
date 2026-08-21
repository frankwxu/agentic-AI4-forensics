# Final Project: Agentic AI Patterns

## Overview

Design, implement, and evaluate five agentic-AI patterns using **one agent framework** that your team selects after a documented framework review. This is a 100-point final project and may be completed individually or by a team of two students.

Your five implementations must address five distinct, student-defined questions:

1. **Reflection** — improve an initial response through structured critique and revision.
2. **Tool Use** — select and invoke one or more callable tools to answer a question.
3. **Planning** — create an explicit plan, execute it, and revise the plan when observations require it.
4. **ReAct** — use an iterative reasoning, action, and observation loop.
5. **Multiagent** — coordinate at least two agents with distinct responsibilities.

Questions should address digital-forensics tasks, especially tasks that require evidence-based conclusions, clear uncertainty language, and a distinction between observed evidence and inference. A non-forensic topic requires instructor approval.

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

All five patterns must be implemented and run using the **one AI agent framework** selected through the framework review. Do not substitute standalone scripts, unrelated libraries, or a different framework for an individual pattern without instructor approval.

Pattern-specific requirements are in the `PATTERN-INSTRUCTIONS.md` file within each pattern folder. This top-level `README.md` is the main guide for the complete final-project submission.

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

For each pattern, evaluate at least three representative cases under two conditions: the **instructor-provided baseline implementation** in `src/` and the **student reimplementation** in the selected agent framework. Use the same user question, input/data, LLM/model, configuration, and success criterion in both conditions. Define success before or while designing the test set; acceptable measures include task accuracy, evidence-citation completeness, valid tool-call rate, plan quality, conflict-resolution quality, or a justified domain-specific measure.

Students may use their own selected LLMs/models, including local or open-source models. For every model used, the report must identify the model name and version, provider or source, access method, relevant configuration, and any fine-tuning or adaptation. When a student-selected model differs from the model used by the instructor baseline, run a controlled model comparison using the same cases, implementation condition, user question, data, configuration, and success criterion. Compare quality, success rate, reliability, latency/cost, and limitations. Do not attribute a difference to the implementation framework when the LLM/model also changed.

Report:

- Per-case instructor-baseline and student-implementation result, and whether each met the stated success criterion.
- Comparative conclusion explaining how the selected-framework reimplementation differed from the instructor-provided implementation.
- For each pattern, use the corresponding classroom lab result or documented instructor baseline as the comparison reference. Identify any differences in task, data, model, or criterion and provide a justified qualitative comparison rather than an unsupported direct performance claim.
- Reliability across repeated runs, when stochastic behavior is relevant.
- Latency and/or cost when the framework or provider makes it available.
- Failure modes, including unsupported claims, invalid tool use, faulty plans, or unresolved agent disagreements.
- A mitigation or next-step improvement for each material failure mode.

## Deliverables

Submit one GitHub repository containing the entire `final-project` folder. The repository must contain one **final research report** and the supporting materials listed below. The final research report must follow [`submission-template.md`](submission-template.md); it is not a separate assignment from the framework review, evaluation, or reproducibility documentation.

1. **Final research report** — 6–8 pages, excluding references and appendices. Use `submission-template.md` as its required structure. Include the framework review, research questions and evidence-based answers, implementation descriptions, evaluation results, model/AI-use disclosure, and reproducibility information in the report or its appendices.
2. **Runnable implementations** — complete and run the notebook in each pattern folder using the selected agent framework: `01-reflection/reflection.ipynb`, `02-tool-use/tool-use.ipynb`, `03-planning/planning.ipynb`, `04-react/react.ipynb`, and `05-multiagent/multiagent.ipynb`. Include any supporting code, data, dependencies, and safe configuration needed to reproduce each notebook.
3. **Instructor and student implementation comparison evidence** — document this in the **“Required Instructor and Student Implementation Comparison Evidence”** section of `submission-template.md`. For each pattern and test case, include the shared user question and data, instructor-baseline output from `src/`, student-notebook output, LLM/model and configuration, run logs or pattern artifacts, success results, and an evidence-based comparison.
4. **Pattern-specific documentation** — complete the `PATTERN-INSTRUCTIONS.md` file in each pattern folder with setup, dependencies, execution, reproduction, and evidence-location instructions for that pattern.
5. **Presentation materials** — slides, recording (if used), or other materials supporting the oral presentation. Demonstrate only one representative pattern, including its instructor-versus-student comparison, results, and limitations. The other four patterns only need to be identified as completed; students do not need to demonstrate or discuss them in detail. Start with `your_presentation.pptx` and rename it for your project before submitting. See the presentation reference outline in `submission-template.md`.
6. **Team contribution record** — required only for two-student teams; see `EVALUATION.md`.

Each student must submit the repository link individually through Sakai.

## Data, Ethics, and Academic Integrity

- Students may use a dataset previously used in class or provide their own dataset for implementing and evaluating the patterns. Document the dataset source, contents, permitted use, and any preprocessing; cite external datasets.
- Prefer synthetic, public, or instructor-approved data.
- Do not submit private, sensitive, or real-case evidence unless the instructor explicitly approves its use and sharing.
- Protect identifiers and credentials. Do not place API keys, tokens, personal data, or restricted evidence in source control or the submission.
- AI tools may be used for this project, including to generate or revise code, text, analyses, and other project materials. Disclose every AI tool/model used, the purpose of its use, and any substantive prompts, outputs, or assistance in the report or appendix.
- Cite frameworks, models, datasets, code, AI-generated content, and other external materials. Do not present undisclosed AI-generated work as your own.
- Verify all AI outputs. Your team is responsible for their accuracy, unsupported claims, security implications, and appropriate use of evidence.
- Do not upload private, sensitive, real-case, or restricted forensic evidence to an AI service unless the instructor explicitly approves both the data and service.
- Your team must be able to explain and modify every submitted component during the oral presentation. Work that cannot be explained or reproduced may not receive full credit.

## Submission Details

Upload the **entire `final-project` folder** to a GitHub repository so that all required code, documentation, test materials, and results are available in one place. Each student must submit the link to that GitHub repository individually through the Sakai website.

All final-project submissions and oral presentations are due during the **last class meeting**.

| Item | Placeholder |
|---|---|
| Final package due | Last class meeting |
| Oral presentation date | Last class meeting |
| Submission location | Sakai — each student submits the GitHub repository link individually |

See [`EVALUATION.md`](EVALUATION.md) for the complete 100-point rubric and grading process.
