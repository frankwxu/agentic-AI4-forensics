# Agentic AI4 Forensics Labs

## Setup

From the `agentic-AI4-forensics` folder, create and activate a virtual environment, then install the required Python packages:

```bash
python3 -m venv .venv-ai4-forensics
source .venv-ai4-forensics/bin/activate
pip install -r requirements.txt
```

Make sure `.env` is present at the repo root with the model configuration used by the notebooks, then open Jupyter from this folder so the local `src/` package and lab paths resolve correctly.

This directory is organized into four self-contained lab folders. Each lab folder contains:

- `01_instructions.md` with the lab workflow and requirements
- `02_case_overview.md` with the incident background and case context
- `03_lab_notebook.ipynb` with the interactive notebook for the lab
- a `data/` subfolder with the staged case artifacts
- a `figures/` subfolder when the lab includes workflow diagrams
- a local `src/` folder with the `agentic_patterns` package used by the notebooks

## Lab Folders

- `lab1_reflection_pattern/`: Reflection lab for suspected customer-data exfiltration
- `lab2_tool_use_pattern/`: Tool-use lab for image metadata, vehicle matching, and sale-draft review
- `lab3_planning_pattern/`: Planning lab for phone access, call timing, and delayed WhatsApp delivery
- `lab4_multiagent_pattern/`: Multiagent lab for transmission assessment and chain-of-custody review

Each `data/` folder includes the synthetic evidence artifacts, including an artifact manifest, a chain-of-custody log, and lab-specific files for analysis.

Students should follow the files in order: `01_instructions.md` -> `02_case_overview.md` -> `03_lab_notebook.ipynb`.
