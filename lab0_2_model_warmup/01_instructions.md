# Lab 0B: Model Warm-Up and Comparison

## Purpose

Use this warm-up lab after you complete [lab0_1_environment_setup/01_instructions.md](../lab0_1_environment_setup/01_instructions.md). The goal is to give you one small hands-on AI task before you start the four forensic pattern labs.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- discover available models from the configured Ollama endpoint
- run the same prompt on 3 different models
- compare model outputs using a simple comparison summary
- revise a prompt to make results more consistent
- notice differences in structure, accuracy, and response time

## What To Do

Complete the steps in this order:

1. Finish [lab0_1_environment_setup/03_environment_check.ipynb](../lab0_1_environment_setup/03_environment_check.ipynb) and [lab0_1_environment_setup/04_setup_assignment.ipynb](../lab0_1_environment_setup/04_setup_assignment.ipynb).
2. Open [02_model_comparison.ipynb](02_model_comparison.ipynb).
3. Run the notebook from top to bottom.
4. Use the fixed class model set shown in the notebook.
5. Compare the three models on the synthetic PII and device-identifier extraction task.
6. Open [03_prompt_revision_assignment.ipynb](03_prompt_revision_assignment.ipynb).
7. Revise the prompt so the three models return more consistent results.
8. Compare the baseline and revised results, then complete the reflection.

In [03_prompt_revision_assignment.ipynb](../lab0_2_model_warmup/03_prompt_revision_assignment.ipynb), Steps 1 through 5 keep the same models, case note, and baseline prompt flow from [02_model_comparison.ipynb](../lab0_2_model_warmup/02_model_comparison.ipynb). The new work begins in Steps 6 and 7, where you revise the prompt and compare the before/after results.

## Success Criteria

You have completed this warm-up lab when:

- you run the notebook successfully
- you compare 3 different models on the same task
- you review the comparison summary
- you revise the prompt and rerun the same 3 models
- you complete the reflection section

## After This Warm-Up

Move on to the main forensic labs in order:

1. `lab1_reflection_pattern`
2. `lab2_tool_use_pattern`
3. `lab3_planning_pattern`
4. `lab4_multiagent_pattern`
