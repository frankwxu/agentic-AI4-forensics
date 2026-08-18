# Lab 0-04: What Is an AI Agent?

## Purpose

Use this onboarding lab after you complete [lab0_03_llm_api_and_model_basics/01_instructions.md](../lab0_03_llm_api_and_model_basics/01_instructions.md). The goal is to make the idea of an AI agent concrete before you start the five pattern labs.

## Lab-Specific Environment

Before running the walkthrough notebooks, create a lab-local `.env` in this folder:

```bash
cp .env.example .env
```

On Windows, use the command for your terminal:

```powershell
# PowerShell
Copy-Item .env.example .env
```

```bat
:: Command Prompt
copy .env.example .env
```

This lab reads `MODEL` and `OLLAMA_BASE_URL` from `lab0_04_ai_agent/.env`, so you can change settings here without affecting Lab 0-02, Lab 0-03, or the later pattern labs.

This lab is hands-on. You will first see how a simple weather tool works. You will then compare a plain model response with a bounded mobile-device-activity review agent and design a small agent specification of your own.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- explain the difference between a plain model response and an agent workflow
- explain how a tool gives an agent a specific, defined capability
- recognize how a generic `Tool` class and `@tool` decorator can create consistent tool descriptions
- identify the role, goal, approved tools, short memory, stop condition, and human-review boundary in a course agent specification
- run a small agent-style mobile-device-activity review task on a synthetic case packet
- revise an agent specification so the model behaves in a more bounded and inspectable way

## Lab Sequence

1. Read [02_what_is_an_agent.md](02_what_is_an_agent.md).
2. Run [03_tools.ipynb](03_tools.ipynb), [04_tool_selection_demo.ipynb](04_tool_selection_demo.ipynb), and [05_memory.ipynb](05_memory.ipynb).
3. Run [06_agent_walkthrough.ipynb](06_agent_walkthrough.ipynb) and compare the plain-model and agent responses.
4. Complete [07_agent_design_assignment.ipynb](07_agent_design_assignment.ipynb), including its reflection.

## Mini Case Packet

This lab uses a small synthetic mini case packet in [data/](data):

- `case_brief.md`
- `artifact_manifest.json`
- `triage_events.csv`

Optional supporting file:

- `chain_of_custody.csv`

The packet is intentionally small so you can focus on the agent concept rather than a long forensic analysis. In this lab, the main task is to summarize simple device activity, note what is still unknown, and recommend one next human review step.

The `triage_events.csv` file is written in plain language on purpose. Read each row as a short timeline note about what happened on the device.

## Success Criteria

You have completed this warm-up lab when:

- you run [03_tools.ipynb](03_tools.ipynb), [04_tool_selection_demo.ipynb](04_tool_selection_demo.ipynb), [05_memory.ipynb](05_memory.ipynb), and [06_agent_walkthrough.ipynb](06_agent_walkthrough.ipynb) successfully
- you compare the same model in plain-prompt form and agent form
- you can point to the role, tools, memory, stop condition, and output schema in the agent notebook
- you edit and rerun the student agent specification in [07_agent_design_assignment.ipynb](07_agent_design_assignment.ipynb)
- you complete the reflection sections

## Next

Continue with [Lab 1: Reflection Pattern](../lab1_reflection_pattern/01_instructions.md).
