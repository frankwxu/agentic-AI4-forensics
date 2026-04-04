# Agentic AI4 Forensics Labs

This repository contains a standalone set of student-facing labs for agentic AI patterns in digital forensics.

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

Then begin with [lab0_1_environment_setup/01_instructions.md](lab0_1_environment_setup/01_instructions.md). The onboarding sequence now has two parts:

- `lab0_1_environment_setup`: environment and connectivity setup
- `lab0_2_model_warmup`: a small model-comparison exercise

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
- `lab0_2_model_warmup/`: Warm-up lab for comparing outputs from multiple models
- `lab1_reflection_pattern/`: Reflection lab for suspected customer-data exfiltration
- `lab2_tool_use_pattern/`: Tool-use lab for image metadata, vehicle matching, and sale-draft review
- `lab3_planning_pattern/`: Planning lab for phone access, call timing, and delayed WhatsApp delivery
- `lab4_multiagent_pattern/`: Multiagent lab for transmission assessment and chain-of-custody review

`lab0_1_environment_setup/` contains:

- `01_instructions.md` with the setup sequence
- `02_setup_checklist.md` with the pre-lab checklist
- `03_environment_check.ipynb` with the runnable environment smoke test
- `04_setup_assignment.ipynb` with the short coding assignment, one student question to the model, and an observation report for setup verification

`lab0_2_model_warmup/` contains:

- `01_instructions.md` with the warm-up sequence
- `02_model_comparison.ipynb` with the student model-comparison assignment

Labs 1 through 4 contain:

- `01_instructions.md` with the lab workflow and requirements
- `02_case_overview.md` with the incident background and case context
- `03_lab_notebook.ipynb` with the interactive notebook for the lab
- a `data/` subfolder with the staged case artifacts
- a `figures/` subfolder when the lab includes workflow diagrams

Each `data/` folder includes the synthetic evidence artifacts, including an artifact manifest, a chain-of-custody log, and lab-specific files for analysis.

Students should follow this sequence:

1. `lab0_1_environment_setup`
2. `lab0_2_model_warmup`
3. `lab1_reflection_pattern`
4. `lab2_tool_use_pattern`
5. `lab3_planning_pattern`
6. `lab4_multiagent_pattern`
