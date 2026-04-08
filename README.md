# Agentic AI4 Forensics Labs

This repository contains a standalone set of student-facing labs for agentic AI patterns in digital forensics.

## Code Provenance

Parts of the Python implementation in `src/agentic_patterns/` are adapted from The Neural Maze's
[`agentic-patterns-course`](https://github.com/neural-maze/agentic-patterns-course) and are reused under the MIT License.

Primary upstream source references:

- `ReflectionAgent`: <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/reflection_pattern/reflection_agent.py>
- `ToolAgent`: <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/tool_pattern/tool_agent.py>
- `Tool`: <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/tool_pattern/tool.py>
- `ReactAgent` (local path: `src/agentic_patterns/react_pattern/react_agent.py`): <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/planning_pattern/react_agent.py>
- `PlanningAgent` (repo-owned abstraction): `src/agentic_patterns/planning_pattern/planning_agent.py`
- `Agent`: <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/multiagent_pattern/agent.py>
- `Crew`: <https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/multiagent_pattern/crew.py>
- Utilities: <https://github.com/neural-maze/agentic-patterns-course/tree/main/src/agentic_patterns/utils>

The original copyright and permission notice are preserved in
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Get The Repo

Clone the repository to your local machine, then move into the project folder.

```bash
git clone https://github.com/frankwxu/agentic-AI4-forensics.git
cd agentic-AI4-forensics
```

## Quick Start

Create a local `.env` from the example file:

```bash
cp .env.example .env
```

On Windows, create `.env` by copying `.env.example`.

Then update `.env` with the `MODEL` and `OLLAMA_BASE_URL` values provided by your instructor.

Then begin with [lab0_1_environment_setup/01_instructions.md](lab0_1_environment_setup/01_instructions.md). The onboarding sequence now has three parts:

- `lab0_1_environment_setup`: environment and connectivity setup
- `lab0_2_model_warmup`: a small model-comparison exercise
- `lab0_3_what_is_an_agent`: a hands-on introduction to agent workflows

`lab0_1_environment_setup` contains the full setup sequence for:

- virtual environment creation
- Python package installation
- Graphviz installation
- `.env` configuration for the instructor-provided Ollama server
- command-line Ollama connectivity testing
- optional local Ollama setup
- Jupyter launch
- environment verification

## Lab Folders

- `lab0_1_environment_setup/`: Setup lab for Python, Jupyter, Graphviz, and Ollama connectivity verification
- `lab0_2_model_warmup/`: Warm-up lab for comparing outputs from multiple models and revising prompts for consistency
- `lab0_3_what_is_an_agent/`: Warm-up lab for comparing a plain model prompt with a bounded agent workflow and designing a small agent card
- `lab1_reflection_pattern/`: Reflection lab for suspected customer-data exfiltration
- `lab2_tool_use_pattern/`: Tool-use lab for image metadata, vehicle matching, and sale-draft review
- `lab3_react_pattern/`: ReAct lab for step-by-step communication verification with tool calls
- `lab4_planning_pattern/`: Planning lab for phone access, call timing, and delayed WhatsApp delivery
- `lab5_multiagent_pattern/`: Multiagent lab for transmission assessment and chain-of-custody review

`lab0_1_environment_setup/` contains:

- `01_instructions.md` with the setup sequence
- `02_setup_checklist.md` with the pre-lab checklist
- `03_environment_check.ipynb` with the runnable environment smoke test
- `04_setup_assignment.ipynb` with the short coding assignment, one student question to the model, and an observation report for setup verification

`lab0_2_model_warmup/` contains:

- `01_instructions.md` with the warm-up sequence
- `02_model_comparison.ipynb` with the guided baseline model-comparison notebook
- `03_prompt_revision_assignment.ipynb` with the student prompt-revision assignment

`lab0_3_what_is_an_agent/` contains:

- `01_instructions.md` with the hands-on agent-introduction sequence
- `02_agent_walkthrough.ipynb` with the guided model-vs-agent walkthrough
- `03_agent_design_assignment.ipynb` with the student agent-card assignment
- a `data/` subfolder with the small synthetic intake packet

Labs 1 through 5 contain:

- `01_instructions.md` with the lab workflow and requirements
- `02_case_overview.md` with the incident background and case context
- `03_lab_notebook.ipynb` with the interactive notebook for the lab
- a `data/` subfolder with the staged case artifacts
- a `figures/` subfolder when the lab includes workflow diagrams

Each `data/` folder includes the synthetic evidence artifacts, including an artifact manifest, a chain-of-custody log, and lab-specific files for analysis.

Students should follow this sequence:

1. `lab0_1_environment_setup`
2. `lab0_2_model_warmup`
3. `lab0_3_what_is_an_agent`
4. `lab1_reflection_pattern`
5. `lab2_tool_use_pattern`
6. `lab3_react_pattern`
7. `lab4_planning_pattern`
8. `lab5_multiagent_pattern`
