# Lab 0C: What Is an AI Agent?

## Purpose

Use this onboarding lab after you complete [lab0_2_model_warmup/01_instructions.md](../lab0_2_model_warmup/01_instructions.md). The goal is to make the idea of an AI agent concrete before you start the four pattern labs.

This lab is hands-on. You will run the same model in two different ways:

- first as a plain model answering an open-ended prompt
- then as a bounded device-activity review agent with a role, approved tools, short memory, and a stop condition

Then you will design a small agent card of your own and test it on the same mini case packet.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- explain the difference between a plain model response and an agent workflow
- identify the main parts of an instructional AI agent in this course:
  - role
  - goal
  - approved tools
  - short memory
  - stop condition
  - human review boundary
- run a small agent-style device-activity review task on a synthetic case packet
- revise an agent card so the model behaves in a more bounded and inspectable way

## What Each Agent Part Does

In this lab, you will define a simple AI agent using a small agent card in the notebook. The figure below shows the agent itself and the parts that keep its behavior easier to inspect and control:

![Figure 0A. Main parts of a simple AI agent for Lab 0C](./figures/lab0_agent_components.svg)

*Figure 0A. Main parts of a simple AI agent for Lab 0C: role, goal, approved tools, short memory, stop condition, and a human-review boundary work together to keep the agent's behavior bounded and inspectable.*

- `role`: tells the model what job it is performing in this workflow
- `goal`: tells the model what a successful result should accomplish
- `approved tools`: limits which inputs or resources the agent is allowed to use
- `short memory`: keeps the small amount of context the agent should carry across steps
- `stop condition`: tells the agent when it should stop instead of continuing to generate more steps
- `human review boundary`: marks the decisions or judgments that should stay with a person

## Instructional Figure

To make the comparison in this lab easier to see, use Figure 0 as a quick map. The top path shows a plain prompt sent directly to a model. The bottom path shows the same model bounded by an agent card, a small case packet, approved inputs, and a human-review step.

![Figure 0. Plain model versus bounded agent workflow for Lab 0C](./figures/lab0_agent_workflow.svg)

*Figure 0. Plain model versus bounded agent workflow for Lab 0C: a single plain prompt can lead to an open-ended answer, while an agent card plus a mini case packet turns the same model into a bounded workflow that produces structured output for human review.*

## What To Do

Complete the steps in this order:

1. Finish [lab0_1_environment_setup/03_environment_check.ipynb](../lab0_1_environment_setup/03_environment_check.ipynb), [lab0_1_environment_setup/04_setup_assignment.ipynb](../lab0_1_environment_setup/04_setup_assignment.ipynb), and [lab0_2_model_warmup/03_prompt_revision_assignment.ipynb](../lab0_2_model_warmup/03_prompt_revision_assignment.ipynb).
2. Open [02_agent_walkthrough.ipynb](02_agent_walkthrough.ipynb).
3. Run the notebook from top to bottom.
4. Compare the plain-model response with the agent response.
5. Pay attention to which parts of the agent card change the behavior of the same model.
6. Open [03_agent_design_assignment.ipynb](03_agent_design_assignment.ipynb).
7. Edit the student agent card in the notebook so it has a clear role, goal, memory, and human-review rule.
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

## Success Criteria

You have completed this warm-up lab when:

- you run [02_agent_walkthrough.ipynb](02_agent_walkthrough.ipynb) successfully
- you compare the same model in plain-prompt form and agent form
- you can point to the role, tools, memory, stop condition, and output schema in the agent notebook
- you edit and rerun the student agent card in [03_agent_design_assignment.ipynb](03_agent_design_assignment.ipynb)
- you complete the reflection sections

## After This Warm-Up

Move on to the main forensic labs in order:

1. `lab1_reflection_pattern`
2. `lab2_tool_use_pattern`
3. `lab3_planning_pattern`
4. `lab4_multiagent_pattern`
