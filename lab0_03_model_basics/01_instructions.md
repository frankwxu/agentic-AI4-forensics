# Lab 0-03: LLM API, Structured Output, and Model Comparison

## Purpose

Use this warm-up lab after you complete [lab0_02_environment_setup/01_instructions.md](../lab0_02_environment_setup/01_instructions.md). The goal is to practice one LLM API request and structured output before comparing models, moving to the AI-agent warm-up, and then starting the five forensic pattern labs.

## Lab-Specific Environment

Before running the warm-up notebooks, create a lab-local `.env` in this folder:

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

This warm-up reads `MODEL` and `OLLAMA_BASE_URL` from `lab0_03_model_basics/.env`, so you can change settings here without affecting Lab 0-02, Lab 0-04, or the later pattern labs.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- discover available models from the configured Ollama endpoint
- send a request to one configured model through the OpenAI-compatible API
- use a JSON Schema to request, parse, and check structured output
- run the same prompt on 3 different models
- compare model outputs using a simple comparison summary
- revise a prompt to make results more consistent
- notice differences in structure, accuracy, and response time

## What To Do

Complete the steps in this order:

1. Finish [lab0_02_environment_setup/03_environment_check.ipynb](../lab0_02_environment_setup/03_environment_check.ipynb) and [lab0_02_environment_setup/04_setup_assignment.ipynb](../lab0_02_environment_setup/04_setup_assignment.ipynb).
2. Open [02_llm_api_and_structured_output.ipynb](02_llm_api_and_structured_output.ipynb) and run it from top to bottom.
3. Complete the short structured-output exercise by adding the requested schema field.
4. Open [03_model_comparison.ipynb](03_model_comparison.ipynb).
5. Run the notebook from top to bottom using the fixed class model set shown in the notebook.
6. Compare the three models on the synthetic PII and device-identifier extraction task.
7. Open [04_prompt_revision_assignment.ipynb](04_prompt_revision_assignment.ipynb).
8. Revise the prompt so the three models return more consistent results.
9. Compare the baseline and revised results, then complete the reflection.
10. Open [05_pii_ground_truth_assignment.ipynb](05_pii_ground_truth_assignment.ipynb).
11. Compare each model's answer with the five-person synthetic ground truth and complete the assignment questions.

In [04_prompt_revision_assignment.ipynb](../lab0_03_model_basics/04_prompt_revision_assignment.ipynb), Steps 1 through 5 keep the same models, case note, and baseline prompt flow from [03_model_comparison.ipynb](../lab0_03_model_basics/03_model_comparison.ipynb). The new work begins in Steps 6 and 7, where you revise the prompt and compare the before/after results.

## Success Criteria

You have completed this warm-up lab when:

- you run all four notebooks successfully
- you send one ordinary request and one schema-constrained request to the configured model
- you parse the structured response and complete the schema-field exercise
- you compare 3 different models on the same task
- you review the comparison summary
- you revise the prompt and rerun the same 3 models
- you complete the reflection section
- you compare all three models with the five-person synthetic ground truth and explain whether they agree

## After This Warm-Up

Continue with [Lab 0-04: What Is an AI Agent?](../lab0_04_ai_agent/01_instructions.md). After that, move on to the main forensic labs in order:

1. `lab1_reflection_pattern`
2. `lab2_tool_use_pattern`
3. `lab3_react_pattern`
4. `lab4_planning_pattern`
5. `lab5_multiagent_pattern`
