# Setup Checklist

Use this checklist before starting `lab0_03_model_warmup`.

- Lab 0-01 is completed:
  - repository cloned locally
  - virtual environment created: `.venv-ai4-forensics`
  - virtual environment activated in the current shell
  - `pip install -r requirements.txt` completed successfully
  - Jupyter launches from the repo root
  - the tiny LLM reading and notebook are completed
- `lab0_02_environment_setup/.env` created from `lab0_02_environment_setup/.env.example`
- `lab0_02_environment_setup/.env` updated with the instructor-provided `MODEL` and `OLLAMA_BASE_URL`
- Graphviz system application installed
- `dot -V` runs successfully
- Command-line request to the configured Ollama endpoint succeeds
- If using a personal Ollama server, the configured model is available there
- [03_environment_check.ipynb](03_environment_check.ipynb) runs without blocking errors
- [04_setup_assignment.ipynb](04_setup_assignment.ipynb) is completed, including one student question to the configured model and the short observation report

If any item above is incomplete, fix it before moving to `lab0_03_model_warmup`.
