# Lab 0-04: What Is an AI Agent?

## Purpose

Use this onboarding lab after you complete [lab0_03_model_basics/01_instructions.md](../lab0_03_model_basics/01_instructions.md). The goal is to make the idea of an AI agent concrete before you start the five pattern labs.

## Lab-Specific Environment

Before running the walkthrough notebooks, create a lab-local `.env` in this folder:

```bash
cp .env.example .env
```

This warm-up reads `MODEL` and `OLLAMA_BASE_URL` from `lab0_04_ai_agent/.env`, so you can change settings here without affecting Lab 0-02, Lab 0-03, or the later pattern labs.

This lab is hands-on. You will first see how a simple weather tool works. You will then compare a plain model response with a bounded mobile-device-activity review agent and design a small agent specification of your own.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- explain the difference between a plain model response and an agent workflow
- explain how a tool gives an agent a specific, defined capability
- recognize how a generic `Tool` class and `@tool` decorator can create consistent tool descriptions
- identify the role, goal, approved tools, short memory, stop condition, and human-review boundary in a course agent specification
- run a small agent-style mobile-device-activity review task on a synthetic case packet
- revise an agent specification so the model behaves in a more bounded and inspectable way

## What To Do

Complete the steps in this order:

1. Finish [lab0_02_environment_setup/03_environment_check.ipynb](../lab0_02_environment_setup/03_environment_check.ipynb), [lab0_02_environment_setup/04_setup_assignment.ipynb](../lab0_02_environment_setup/04_setup_assignment.ipynb), and [lab0_03_model_basics/03_prompt_revision_assignment.ipynb](../lab0_03_model_basics/03_prompt_revision_assignment.ipynb).
2. Read [02_what_is_an_agent.md](02_what_is_an_agent.md).
3. Open [03_tools.ipynb](03_tools.ipynb) and run it from top to bottom.
4. Open [04_agent_walkthrough.ipynb](04_agent_walkthrough.ipynb) and run it from top to bottom.
5. Compare the plain-model response with the agent response. Pay attention to which parts of the agent specification change the behavior of the same model.
6. Open [05_agent_design_assignment.ipynb](05_agent_design_assignment.ipynb).
7. Edit the student agent specification so it has a clear role, goal, memory, and human-review rule.
8. Rerun the notebook and review how your agent design changes the output.
9. Complete the short reflection at the end of each notebook.

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

- you run [03_tools.ipynb](03_tools.ipynb) and [04_agent_walkthrough.ipynb](04_agent_walkthrough.ipynb) successfully
- you compare the same model in plain-prompt form and agent form
- you can point to the role, tools, memory, stop condition, and output schema in the agent notebook
- you edit and rerun the student agent specification in [05_agent_design_assignment.ipynb](05_agent_design_assignment.ipynb)
- you complete the reflection sections

## After This Warm-Up

Move on to the main forensic labs in order:

1. `lab1_reflection_pattern`
2. `lab2_tool_use_pattern`
3. `lab3_react_pattern`
4. `lab4_planning_pattern`
5. `lab5_multiagent_pattern`
