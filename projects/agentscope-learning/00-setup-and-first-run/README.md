# Setup and first run

**Time:** 20–30 minutes  
**Outcome:** A working AgentScope environment that can make one model call.

This is onboarding, not an AgentScope API lesson. Finish it before Lesson 01.

## 1. Create and activate a virtual environment

Run these commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate              # macOS/Linux
# .venv\\Scripts\\Activate.ps1          # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

AgentScope requires Python 3.10 or later. This lesson uses AgentScope 2.x. Pinning the major version matters because many online examples use a different API. See the [official installation guide](https://doc.agentscope.io/tutorial/quickstart_installation.html).

## 2. Configure the course model

This course uses the same OpenAI-compatible Ollama endpoint as the other labs. Copy the example configuration; do **not** commit `.env`.

```bash
cp .env.example .env
```

The defaults are:

- `MODEL=qwen3:8b`
- `OLLAMA_BASE_URL=http://localhost:11434/v1`

If your instructor provides a different model server, use their values. An API key is not required for the default local Ollama configuration.

## 3. Verify the installation

Open and run `01_verify_installation.ipynb`.

You should see an AgentScope version and `Installation check passed.` This performs no model request and costs nothing.

## 4. Run the model smoke test

Open and run `02_first_model_call.ipynb`.

Expected result: a short answer to `Reply with exactly: AgentScope is ready.` The call is intentionally small, but it does use your provider account.

If it fails:

- `ModuleNotFoundError`: activate `.venv`, then reinstall `requirements.txt`.
- model-not-found error: run `ollama pull qwen3:8b`, or update `MODEL` to an installed model.
- connection error: start Ollama, then check `OLLAMA_BASE_URL`.

## Checkpoint

Before moving on, you can:

1. Activate the course virtual environment.
2. Explain where the model name and Ollama endpoint are configured.
3. Run both notebooks successfully.

The next lesson turns this model call into a `ReActAgent`.
