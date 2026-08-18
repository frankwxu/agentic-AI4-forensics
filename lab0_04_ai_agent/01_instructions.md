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

This lab is hands-on. You will first see how a simple weather tool works. You will then run and inspect a bounded mobile-device-activity review agent.

## Learning Goals

By the end of this introductory lab, you should be able to:

- explain how a bounded agent combines a role and goal with program-controlled steps
- explain how a tool gives an agent a specific, defined capability
- recognize how a generic `Tool` class and `@tool` decorator can create consistent tool descriptions
- identify the role, goal, approved tools, tool validation, working memory, stop condition, structured result, and human-review boundary in a course agent specification
- run a bounded mobile-device-activity review task on a synthetic case packet
- trace how an agent specification makes a model workflow more bounded and inspectable

## Lab Sequence

1. Read [02_what_is_an_agent.md](02_what_is_an_agent.md).
2. Run [03_tools.ipynb](03_tools.ipynb), [04_tool_selection_demo.ipynb](04_tool_selection_demo.ipynb), and [05_memory.ipynb](05_memory.ipynb).
3. Run [06_forensic_agent_walkthrough.ipynb](06_forensic_agent_walkthrough.ipynb), inspect its tool decisions, working memory, and final review, and complete its reflection.

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

- you run [03_tools.ipynb](03_tools.ipynb), [04_tool_selection_demo.ipynb](04_tool_selection_demo.ipynb), [05_memory.ipynb](05_memory.ipynb), and [06_forensic_agent_walkthrough.ipynb](06_forensic_agent_walkthrough.ipynb) successfully
- you can point to the role, goal, approved tools, validation, working memory, stop condition, structured result, and human-review boundary in the agent notebook
- you complete the reflection sections

## Next

Continue with [Lab 1: Reflection Pattern](../lab1_reflection_pattern/01_instructions.md).
