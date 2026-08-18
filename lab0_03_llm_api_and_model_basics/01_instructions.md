# Lab 0-03: LLM API, Structured Output, and Model Comparison

## Purpose

Use this warm-up lab after you complete [Lab 0-02: Environment Setup](../lab0_02_environment_setup/01_instructions.md). You will practice LLM API requests, structured output, model comparison, and prompt revision.

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

This warm-up reads `MODEL` and `OLLAMA_BASE_URL` from `lab0_03_llm_api_and_model_basics/.env`, so you can change settings here without affecting Lab 0-02, Lab 0-04, or the later pattern labs.

## Learning Goals

By the end of this warm-up lab, you should be able to:

- discover available models from the configured Ollama endpoint
- send a request to one configured model through the OpenAI-compatible API
- use a JSON Schema to request, parse, and check structured output
- run the same prompt on 3 different models
- compare model outputs using a simple comparison summary
- revise a prompt to make results more consistent
- notice differences in structure, accuracy, and response time

## Lab Sequence

1. Complete [02_llm_api_and_structured_output.ipynb](02_llm_api_and_structured_output.ipynb), including the short schema-field exercise.
2. Run [03_model_comparison.ipynb](03_model_comparison.ipynb) using the fixed class model set.
3. Complete [04_prompt_revision_assignment.ipynb](04_prompt_revision_assignment.ipynb) and compare the baseline and revised prompts.
4. Complete [05_pii_ground_truth_assignment.ipynb](05_pii_ground_truth_assignment.ipynb) by comparing the model answers with the synthetic ground truth.

## Success Criteria

You have completed this warm-up lab when:

- you complete the API and structured-output tutorial, including its schema-field exercise
- you compare the three class models and review the comparison summary
- you revise the prompt, rerun the same models, and complete the reflection
- you compare the model answers with the five-person synthetic ground truth

## Next

Continue with [Lab 0-04: What Is an AI Agent?](../lab0_04_ai_agent/01_instructions.md).
