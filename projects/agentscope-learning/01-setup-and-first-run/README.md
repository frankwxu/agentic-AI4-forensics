# Setup and first run

**Time:** 20–30 minutes  
**Outcome:** A working AgentScope environment that can make one model call.

This is a setup check, not a programming lesson. Finish it before Lesson 02.

## 1. Create a separate Python workspace

Run these commands from this folder:

```bash
python3 -m venv .venv
source .venv/bin/activate              # macOS/Linux
# .venv\\Scripts\\Activate.ps1          # Windows PowerShell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

AgentScope requires Python 3.10 or later. This lesson uses AgentScope 2.x because its code differs from older examples online. See the [official installation guide](https://doc.agentscope.io/tutorial/quickstart_installation.html).

## 2. Set the course model details

This course uses the same local Ollama address as the other labs. Copy the example settings; do **not** commit `.env`.

```bash
cp .env.example .env
```

The defaults are:

- `MODEL=qwen3:8b`
- `OLLAMA_BASE_URL=http://localhost:11434/v1`

If your instructor provides a different model address, use those values. The default local Ollama setup does not need a key.

## 3. Verify the installation

Open and run `01_verify_installation.ipynb`.

You should see an AgentScope version and `Installation check passed.` This performs no model request and costs nothing.

## 4. Make a first model request

Open and run `02_first_model_call.ipynb`.

Expected result: a short answer to `Reply with exactly: AgentScope is ready.` This is a very small request to the local model.

If it fails:

- `ModuleNotFoundError`: activate `.venv`, then reinstall `requirements.txt`.
- model-not-found error: run `ollama pull qwen3:8b`, or update `MODEL` to an installed model.
- connection error: start Ollama, then check `OLLAMA_BASE_URL`.

## Checkpoint

Before moving on, you can:

1. Start the course’s separate Python workspace.
2. Explain where the model name and Ollama address are set.
3. Run both notebooks successfully.

The next lesson turns this model request into an agent.
