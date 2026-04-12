# Lab 0A: Environment Setup and Ollama Connectivity Check

Work through [lab0_0_llm_foundations/01_instructions.md](../lab0_0_llm_foundations/01_instructions.md) before this lab. Lab 0 Foundations covers repo clone, virtual environment creation, base Python package installation, Jupyter launch, and the tiny LLM notebook. This lab focuses on the remaining setup needed for the later agent workflow labs: `.env`, Ollama connectivity, Graphviz, and environment verification.

## Purpose

Use this onboarding lab after Lab 0 Foundations to finish the setup needed for the later forensic pattern labs. The goal is to make sure Graphviz, the configured Ollama endpoint, the lab-local `.env` file, and the later environment-check notebooks all work correctly on your system.

## Learning Goals

By the end of Lab 0, you should be able to:

- create a lab-local `.env` file from `lab0_1_environment_setup/.env.example`
- configure that `.env` with the instructor-provided model and Ollama server URL
- install Graphviz and verify the `dot` command works
- test the configured Ollama endpoint from the command line
- optionally run a local Ollama server if you are not using the instructor-managed server
- run a short environment smoke test for the later labs

## What To Do

Complete the steps in this order:

1. Create `lab0_1_environment_setup/.env` from [lab0_1_environment_setup/.env.example](./.env.example).

   Linux/macOS:

   ```bash
   cp lab0_1_environment_setup/.env.example lab0_1_environment_setup/.env
   ```

   Windows PowerShell:

   ```powershell
   Copy-Item lab0_1_environment_setup/.env.example lab0_1_environment_setup/.env
   ```

   Windows Command Prompt:

   ```cmd
   copy lab0_1_environment_setup\.env.example lab0_1_environment_setup\.env
   ```

   The starter [lab0_1_environment_setup/.env.example](./.env.example) currently uses the temporary instructor values below. Only change them if your instructor provides different settings.

   ```text
   MODEL="qwen3:8b"
   OLLAMA_BASE_URL="http://localhost:11434/v1"
   ```

2. Install the Graphviz system application.

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

3. Verify Graphviz:

   ```bash
   dot -V
   ```

4. Test the configured Ollama endpoint from the command line.

   If `lab0_1_environment_setup/.env` contains the current temporary instructor endpoint:

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

5. Local Ollama setup is optional. Only do this if you are not using the instructor-managed server.

   ```bash
   ollama serve
   ollama pull <model-name>
   ```

6. Open [03_environment_check.ipynb](03_environment_check.ipynb) and run all cells from top to bottom.
7. Complete [04_setup_assignment.ipynb](04_setup_assignment.ipynb), including one question to the configured model and the short observation report at the end.
8. After the setup assignment passes, create `lab0_2_model_warmup/.env` from `lab0_2_model_warmup/.env.example`, then continue to [lab0_2_model_warmup/01_instructions.md](../lab0_2_model_warmup/01_instructions.md).

   If you are using a personal Ollama server, make sure the model in this lab's `.env` is available before running the notebook.

## Success Criteria

You have completed Lab 0 when:

- `lab0_1_environment_setup/.env` exists and contains the required keys
- `lab0_1_environment_setup/.env` matches the instructor-provided model and Ollama server URL
- the notebook confirms the required Python libraries import successfully
- the command-line Ollama test returns a valid response
- the notebook can read the lab-local `.env` values needed by the labs
- the notebook can contact the configured Ollama endpoint
- the notebook can render a small Graphviz diagram
- you complete [04_setup_assignment.ipynb](04_setup_assignment.ipynb), including one question to the configured model and the short observation report
- you are ready to continue to [lab0_2_model_warmup](../lab0_2_model_warmup)

## Troubleshooting

- If `.env` is missing, copy `lab0_1_environment_setup/.env.example` to `lab0_1_environment_setup/.env` before running the notebook.
- If `pip install -r requirements.txt` fails, confirm your virtual environment is activated before retrying.
- If `dot -V` fails, Graphviz is either not installed or not on your system `PATH`.
- If the command-line Ollama test fails, check the `OLLAMA_BASE_URL` in `lab0_1_environment_setup/.env` and confirm you can reach the instructor-managed server from your network.
- If the notebook cannot reach Ollama, make sure the `OLLAMA_BASE_URL` in `lab0_1_environment_setup/.env` matches the running server.
- If you are using the instructor-managed server, you do not need to run `ollama serve` locally.
- If you are using a personal Ollama server, make sure it is running and that the configured model is available.

## After Lab 0

After this setup check passes, continue to:

1. `lab0_2_model_warmup`
2. `lab0_3_what_is_an_agent`
3. `lab1_reflection_pattern`
4. `lab2_tool_use_pattern`
5. `lab3_react_pattern`
6. `lab4_planning_pattern`
7. `lab5_multiagent_pattern`
