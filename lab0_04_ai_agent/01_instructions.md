# Lab 0-04: What Is an AI Agent?

## Purpose

Complete this onboarding lab after [Lab 0-03: LLM API and Model Basics](../lab0_03_llm_api_and_model_basics/01_instructions.md). It introduces the bounded AI-agent workflow used throughout the five pattern labs.

An LLM is the reasoning component of an agent, not the entire agent. The surrounding program defines the role, goal, approved tools, limits, and human-review boundary. In this lab, you trace those parts in small examples before running a bounded review of synthetic mobile-device activity.

## Learning Outcomes

By the end of this lab, you will be able to:

1. Explain how a bounded agent combines an LLM, instructions, tools, memory, and program-controlled steps.
2. Distinguish a tool description from a tool request, and explain why the program validates a requested tool before running it.
3. Identify an agent’s role, goal, approved tools, working memory, stop condition, structured result, and human-review boundary.
4. Trace how an agent uses approved evidence to produce an evidence-bounded device-activity summary.
5. Explain why an agent’s output is a review aid, not the evidence itself or a final investigative decision.

## The General Bounded-Agent Workflow

A bounded agent follows a repeatable loop:

`Question -> LLM reasoning -> approved tool request -> program validation -> tool result -> updated context -> bounded response -> human review`

- **Question:** States the narrow task the agent should address.
- **LLM reasoning:** Uses instructions and current context to decide what information is needed next.
- **Approved tool request:** Names one allowed tool and supplies its inputs in a structured format.
- **Program validation:** Checks that the request uses an approved tool and valid inputs before local code runs.
- **Tool result:** Returns information from the approved evidence package or service.
- **Updated context:** Keeps useful prior messages or observations available for a later step.
- **Bounded response:** Summarizes only what the available materials support and states remaining uncertainty.
- **Human review:** Leaves investigative, legal, or disciplinary decisions to a qualified person.

Read [02_what_is_an_agent.md](02_what_is_an_agent.md) for the detailed concepts and diagrams behind this workflow.

## The Mini Case Scenario

The final walkthrough uses a small synthetic case packet about a clinic-issued Android phone. During an after-hours interval, records show a screenshot named `staff_schedule_monday.png` was created, a message conversation was opened, a message said “sending that image now,” an outgoing mobile-data connection occurred, and the screenshot was later deleted.

Your task is not to prove who acted, what the screenshot contained, whether it was delivered, or whether misconduct occurred. Summarize what the approved records show, identify what remains unknown, and recommend one next human-review step.

## Workflow in This Lab

Work through the lab in this order:

1. **Read the agent concepts.** Open [02_what_is_an_agent.md](02_what_is_an_agent.md) to learn the difference between an LLM, an agent, tools, memory, boundaries, and human review.
2. **Learn what tools do.** Run [03_tools.ipynb](03_tools.ipynb) to see how a function becomes a tool with a name, description, and inputs.
3. **Trace tool selection and validation.** Run [04_tool_selection_and_validation.ipynb](04_tool_selection_and_validation.ipynb). The LLM receives a question and tool descriptions, returns a structured request, and the program checks that request before running the selected tool.
4. **Compare manual and packaged tool use.** Run [05_reusable_toolagent_weather_demo.ipynb](05_reusable_toolagent_weather_demo.ipynb) to compare one visible tool call with a reusable `ToolAgent` workflow.
5. **See how memory changes later steps.** Run [06_memory.ipynb](06_memory.ipynb) to see how an agent can retain useful context across a conversation or evidence review.
6. **Run the bounded forensic walkthrough.** Run [07_forensic_agent_walkthrough.ipynb](07_forensic_agent_walkthrough.ipynb), inspect its tool decisions and working memory, then complete its reflection.

## What to Notice in the Final Walkthrough

- **Role and goal:** What narrow review task is the agent performing?
- **Approved inputs and tools:** Which case files may the agent read, and which helpers may it call?
- **Validation:** Where does the program prevent an unapproved tool request from running?
- **Working memory:** Which prior observations are retained for the next step?
- **Stop condition:** What tells the workflow that it has enough information to stop?
- **Structured result:** How does the output separate observed activity, uncertainty, and a next review step?
- **Human-review boundary:** Which conclusions must remain with a human reviewer?

## Mini Case Packet

The synthetic packet in [data/](data) is intentionally small so you can focus on the agent workflow rather than a long forensic analysis.

- `case_brief.md`: States the scenario, review question, and evidence limit.
- `artifact_manifest.json`: Identifies the device, time window, and allowed packet contents.
- `triage_events.csv`: Provides the short, plain-language event timeline used in the walkthrough.
- `chain_of_custody.csv`: Optional supporting record of basic evidence handling.

## Lab-Specific Environment

Before running the notebooks, create a lab-local `.env` file:

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

The notebooks read `MODEL` and `OLLAMA_BASE_URL` from `lab0_04_ai_agent/.env`, so you can change these settings without affecting the other labs.

## Success Criteria

You have completed this warm-up lab when you can:

- run notebooks 03 through 07 successfully;
- identify the bounded-agent components in the final walkthrough;
- explain why the mini-case records support a careful summary but not a claim of confirmed delivery or misconduct; and
- complete the reflection in the forensic-agent walkthrough.

## Next

Continue with [Lab 1: Reflection Pattern](../lab1_reflection_pattern/01_instructions.md).
