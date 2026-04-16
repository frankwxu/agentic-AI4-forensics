# Agentic AI4 Forensics Labs

<p align="center">
  <img src="assets/readme-cover.svg" alt="Cover banner for Agentic AI4 Forensics Labs" width="100%">
</p>

This repository contains a standalone set of student-facing labs for agentic AI patterns in digital forensics.
It is designed for cybersecurity and digital forensics students, including learners with little or no computer science background.

## Intended Audience

These tutorial labs are written for students who are learning cybersecurity or digital forensics and may be new to programming.
The onboarding sequence starts with a lightweight Python and LLM foundation so students can follow the later agent labs without needing a full computer science background.

## Code Provenance

The agent workflow code in `src/agentic_patterns/` gives credit to The Neural Maze's
[`agentic-patterns-course`](https://github.com/neural-maze/agentic-patterns-course), which provides the upstream course code foundation for several of the labs here.
Parts of that implementation are adapted and reused under the MIT License.

The original copyright and permission notice are preserved in
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

## Get The Repo

Clone the repository to your local machine, then move into the project folder.

```bash
git clone https://github.com/frankwxu/agentic-AI4-forensics.git
cd agentic-AI4-forensics
```

## Quick Start

Most runnable lab folders now have their own `.env.example`. Lab 0-00 (`lab0_00_python_basics`) begins the course with a lightweight Python primer for reading notebook code. Lab 0-01 (`lab0_01_llm_foundations`) covers the basic local Python setup needed for the tiny LLM notebook. Lab 0-02 (`lab0_02_environment_setup`) adds `.env`, Ollama, and Graphviz for the agent workflow labs.

The onboarding labs are paced for cybersecurity and digital forensics students who may only have a little programming experience.

Before running a notebook in one of the later hands-on labs, copy that lab's `.env.example` to `.env` inside the same folder. For example:

```bash
cp lab0_02_environment_setup/.env.example lab0_02_environment_setup/.env
```

On Windows, create `.env` by copying the matching lab-local `.env.example`.

Then update that lab-local `.env` with the `MODEL` and `OLLAMA_BASE_URL` values provided by your instructor.

Repeat that pattern for any lab you plan to run. For example:

```bash
cp lab2_tool_use_pattern/.env.example lab2_tool_use_pattern/.env
```

Lab 2 defaults to `qwen3:8b` in its local example because the `ToolAgent` section has been more stable with that model in the current Ollama setup.

Begin with [lab0_00_python_basics/01_instructions.md](lab0_00_python_basics/01_instructions.md). Then continue to [lab0_01_llm_foundations/01_instructions.md](lab0_01_llm_foundations/01_instructions.md), followed by [lab0_02_environment_setup/01_instructions.md](lab0_02_environment_setup/01_instructions.md). The onboarding sequence now has five parts:

- `Lab 0-00` (`lab0_00_python_basics`): Python primer for reading course notebooks, with a short reading and two small practice notebooks
- `Lab 0-01` (`lab0_01_llm_foundations`): LLM foundations primer with repo clone, base Python setup, and a tiny local training demo
- `Lab 0-02` (`lab0_02_environment_setup`): `.env`, Ollama, Graphviz, and environment checks for the later agent labs
- `Lab 0-03` (`lab0_03_model_warmup`): a small model-comparison exercise
- `Lab 0-04` (`lab0_04_what_is_an_agent`): a hands-on introduction to agent workflows

`lab0_00_python_basics` contains the course-specific primer for:

- reading notebook-style Python without needing a full programming course
- recognizing variables, lists, dictionaries, loops, and helper functions
- practicing tiny JSON and CSV examples that mirror later labs

`lab0_01_llm_foundations` contains the first local setup sequence for:

- repository clone
- virtual environment creation
- Python package installation
- Jupyter launch
- returning to the Python primer notebook after base setup
- LLM foundations reading
- tiny local transformer training demo

`lab0_02_environment_setup` contains the later setup sequence for:

- Graphviz installation
- lab-local `.env` configuration for the instructor-provided Ollama server
- command-line Ollama connectivity testing
- optional local Ollama setup
- Jupyter launch
- environment verification

## Lab Folders

- `lab0_00_python_basics/`: Python primer with a short reading, two small guided notebooks, and tiny JSON/CSV practice data
- `lab0_01_llm_foundations/`: LLM foundations primer with base local setup, a tiny local training demo, reading, figures, and a short public-domain book excerpt
- `lab0_02_environment_setup/`: Setup lab for `.env`, Ollama, Graphviz, and connectivity verification for the later workflow labs
- `lab0_03_model_warmup/`: Warm-up lab for comparing outputs from multiple models and revising prompts for consistency
- `lab0_04_what_is_an_agent/`: Warm-up lab for comparing a plain model prompt with a bounded agent workflow and designing a small agent card
- `lab1_reflection_pattern/`: Reflection lab for suspected customer-data exfiltration
- `lab2_tool_use_pattern/`: Tool-use lab for image metadata, vehicle matching, and sale-draft review
- `lab3_react_pattern/`: ReAct lab for step-by-step communication verification with tool calls
- `lab4_planning_pattern/`: Planning lab for phone access, call timing, and delayed WhatsApp delivery
- `lab5_multiagent_pattern/`: Multiagent lab for transmission assessment and chain-of-custody review

`lab0_00_python_basics/` contains:

- `01_instructions.md` with the primer sequence and handoff to `lab0_01_llm_foundations`
- `02_python_basics_reading.md` with the notebook-reading primer on variables, lists, dictionaries, loops, functions, and small file examples
- `03_python_basics_notebook.ipynb` with the guided Python practice notebook
- `04_python_patterns_for_later_labs.ipynb` with the later-lab Python reading patterns used most often in Labs 2-5
- a `data/` subfolder with the tiny JSON and CSV files used in the notebook

`lab0_01_llm_foundations/` contains:

- `01_instructions.md` with the conceptual primer sequence
- `02_llm_foundations_reading.md` with the main reading on tokens, embeddings, transformer flow, training versus inference, and output limits
- `03_tiny_llm_book_demo.ipynb` with a tiny local word-level transformer training demo
- a `data/` subfolder with the public-domain book excerpt used for training
- a `figures/` subfolder with the LLM teaching diagrams

`lab0_02_environment_setup/` contains:

- `01_instructions.md` with the setup sequence
- `02_setup_checklist.md` with the pre-lab checklist
- `03_environment_check.ipynb` with the runnable environment smoke test
- `04_setup_assignment.ipynb` with the short coding assignment, one student question to the model, and an observation report for setup verification
- `.env.example` with lab-local model settings

`lab0_03_model_warmup/` contains:

- `01_instructions.md` with the warm-up sequence
- `02_model_comparison.ipynb` with the guided baseline model-comparison notebook
- `03_prompt_revision_assignment.ipynb` with the student prompt-revision assignment
- `.env.example` with lab-local model settings

`lab0_04_what_is_an_agent/` contains:

- `01_instructions.md` with the hands-on agent-introduction sequence
- `02_agent_walkthrough.ipynb` with the guided model-vs-agent walkthrough
- `03_agent_design_assignment.ipynb` with the student agent-card assignment
- `.env.example` with lab-local model settings
- a `data/` subfolder with the small synthetic intake packet

Labs 1 through 5 contain:

- `01_instructions.md` with the lab workflow and requirements
- `02_case_overview.md` with the incident background and case context
- one or more `03*.ipynb` notebooks with the interactive walkthroughs for the lab
- `.env.example` with lab-local model settings
- a `data/` subfolder with the staged case artifacts
- a `figures/` subfolder when the lab includes workflow diagrams

Each `data/` folder includes the synthetic evidence artifacts, including an artifact manifest, a chain-of-custody log, and lab-specific files for analysis.

Students should follow this sequence:

1. `lab0_00_python_basics`
2. `lab0_01_llm_foundations`
3. `lab0_02_environment_setup`
4. `lab0_03_model_warmup`
5. `lab0_04_what_is_an_agent`
6. `lab1_reflection_pattern`
7. `lab2_tool_use_pattern`
8. `lab3_react_pattern`
9. `lab4_planning_pattern`
10. `lab5_multiagent_pattern`
