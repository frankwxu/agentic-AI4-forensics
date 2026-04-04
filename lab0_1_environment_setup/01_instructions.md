# Lab 0A: Environment Setup and Ollama Connectivity Check

## Purpose

Use this onboarding lab to prepare your machine before starting the forensic pattern labs. The goal is to make sure Python, Jupyter, Graphviz, the configured Ollama endpoint, and the repo layout all work correctly on your system.

## Learning Goals

By the end of Lab 0, you should be able to:

- clone the lab repository to your local machine
- create a local `.env` file from `.env.example`
- configure `.env` with the instructor-provided model and Ollama server URL
- create and activate the lab virtual environment
- install the required Python packages
- install Graphviz and verify the `dot` command works
- test the configured Ollama endpoint from the command line
- optionally run a local Ollama server if you are not using the instructor-managed server
- open Jupyter from the repo root and run a short environment smoke test

## What To Do

Complete the steps in this order:

1. Clone the repo:

   ```bash
   git clone https://github.com/frankwxu/agentic-AI4-forensics.git
   cd agentic-AI4-forensics
   ```

2. Create `.env` from [.env.example](../.env.example).

   Linux/macOS:

   ```bash
   cp .env.example .env
   ```

   Windows PowerShell:

   ```powershell
   Copy-Item .env.example .env
   ```

   Windows Command Prompt:

   ```cmd
   copy .env.example .env
   ```

   The starter [.env.example](../.env.example) currently uses the temporary instructor values below. Only change them if your instructor provides different settings.

   ```text
   MODEL="qwen3:8b"
   OLLAMA_BASE_URL="http://localhost:11434/v1"
   ```

3. Create and activate the virtual environment.

   Linux/macOS:

   ```bash
   python3 -m venv .venv-ai4-forensics
   source .venv-ai4-forensics/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   py -3 -m venv .venv-ai4-forensics
   .\.venv-ai4-forensics\Scripts\Activate.ps1
   ```

   Windows Command Prompt:

   ```cmd
   py -3 -m venv .venv-ai4-forensics
   .venv-ai4-forensics\Scripts\activate.bat
   ```

4. Install the Python packages:

   ```bash
   pip install -r requirements.txt
   ```

5. Install the Graphviz system application.

   Linux (Debian/Ubuntu):

   ```bash
   sudo apt install graphviz
   ```

   macOS (Homebrew):

   ```bash
   brew install graphviz
   ```

   Windows:
   Install Graphviz from https://graphviz.org/download/ and make sure the Graphviz `bin` folder is on your `PATH`.

6. Verify Graphviz:

   ```bash
   dot -V
   ```

7. Test the configured Ollama endpoint from the command line.

   If your `.env` file contains the current temporary instructor endpoint:

   ```text
   OLLAMA_BASE_URL="http://localhost:11434/v1"
   ```

   then test the server at:

   ```bash
   curl http://localhost:11434/api/tags
   ```

   In Windows PowerShell, use:

   ```powershell
   curl.exe http://localhost:11434/api/tags
   ```

   You should receive a JSON response listing available models.

8. Local Ollama setup is optional. Only do this if you are not using the instructor-managed server.

   ```bash
   ollama serve
   ollama pull <model-name>
   ```

9. Launch Jupyter from the repo root.
10. Open [03_environment_check.ipynb](03_environment_check.ipynb) and run all cells from top to bottom.
11. Complete [04_setup_assignment.ipynb](04_setup_assignment.ipynb), including one question to the configured model and the short observation report at the end.
12. After the setup assignment passes, continue to [lab0_2_model_warmup/01_instructions.md](../lab0_2_model_warmup/01_instructions.md).

   If you are using a personal Ollama server, make sure the model in `.env` is available before running the notebook.

## Success Criteria

You have completed Lab 0 when:

- `.env` exists at the repo root and contains the required keys
- `.env` matches the instructor-provided model and Ollama server URL
- the notebook prints the active Python executable and repo paths correctly
- the notebook confirms the required Python libraries import successfully
- the command-line Ollama test returns a valid response
- the notebook can read the repo `.env` values needed by the labs
- the notebook can contact the configured Ollama endpoint
- the notebook can render a small Graphviz diagram
- you complete [04_setup_assignment.ipynb](04_setup_assignment.ipynb), including one question to the configured model and the short observation report
- you are ready to continue to [lab0_2_model_warmup](../lab0_2_model_warmup)

## Troubleshooting

- If `.env` is missing, copy `.env.example` to `.env` before running the notebook.
- If `pip install -r requirements.txt` fails, confirm your virtual environment is activated before retrying.
- If `dot -V` fails, Graphviz is either not installed or not on your system `PATH`.
- If the command-line Ollama test fails, check the `OLLAMA_BASE_URL` in `.env` and confirm you can reach the instructor-managed server from your network.
- If the notebook cannot reach Ollama, make sure the `OLLAMA_BASE_URL` in `.env` matches the running server.
- If you are using the instructor-managed server, you do not need to run `ollama serve` locally.
- If you are using a personal Ollama server, make sure it is running and that the configured model is available.

## After Lab 0

After this setup check passes, continue to:

1. `lab0_2_model_warmup`
2. `lab1_reflection_pattern`
3. `lab2_tool_use_pattern`
4. `lab3_planning_pattern`
5. `lab4_multiagent_pattern`
