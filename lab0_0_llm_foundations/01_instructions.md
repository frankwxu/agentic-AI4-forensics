# Lab 0 Foundations: Train and Inspect a Tiny LLM

## Purpose

Use this primer before [lab0_1_environment_setup/01_instructions.md](../lab0_1_environment_setup/01_instructions.md). The goal is to give you both:

- a plain-language mental model of what a large language model is
- one small runnable example of how a model is trained and then used for next-word prediction

This lab does not require `.env`, Ollama, or Graphviz. It does require the basic local Python setup needed to run the tiny LLM notebook.

## Learning Goals

By the end of this primer, you should be able to:

- explain what an LLM is in plain language
- describe tokens, tokenization, embeddings, and context window at a high level
- explain next-token prediction without using advanced math
- train a tiny word-level transformer on a short book excerpt
- watch training loss and next-word accuracy change during training
- distinguish training from inference
- explain why prompts and temperature can change outputs
- identify at least one reason an LLM can sound confident and still be wrong
- explain why later labs add prompt structure, tools, memory, and human review around the model

## What To Do

Complete the steps in this order:

1. Clone the repo:

   ```bash
   git clone https://github.com/frankwxu/agentic-AI4-forensics.git
   cd agentic-AI4-forensics
   ```

2. Create and activate the virtual environment.

   Linux/macOS:

   ```bash
   python3 -m venv .venv-ai4-forensics
   source .venv-ai4-forensics/bin/activate
   ```

   Windows PowerShell:

   ```powershell
   py -3 -m venv .venv-ai4-forensics
   .\.venv-ai4-forensics\Scripts\Activate.ps1
   ```

   Windows Command Prompt:

   ```cmd
   py -3 -m venv .venv-ai4-forensics
   .venv-ai4-forensics\Scripts\activate.bat
   ```

3. Install the base Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter from the repo root.

5. Read [02_llm_foundations_reading.md](02_llm_foundations_reading.md).
6. Study the five figures in [figures/](figures) as you read:
   - `lab0_llm_pipeline.svg`
   - `lab0_embedding_lookup.svg`
   - `lab0_contextualized_bank.svg`
   - `lab0_weights_regression.svg`
   - `lab0_llm_limits_to_controls.svg`
7. Open [03_tiny_llm_book_demo.ipynb](03_tiny_llm_book_demo.ipynb).
8. Run the notebook from top to bottom.
9. Answer the short reflection questions at the end of the reading and notebook.

The notebook trains a tiny word-level transformer on a repeated public-domain book excerpt so you can see a visible training loop on classroom hardware. It is a teaching model, not a production LLM.

## Success Criteria

You have completed this primer when:

- you can explain what an LLM predicts at each step
- you can distinguish tokens from words
- you can explain the difference between training a model and using a model
- you can explain why prompt wording changes outputs
- you can point to a training loss trend and explain what it means
- you can inspect a next-word prediction and explain why it depends on the prompt context
- you can name at least one limitation of LLM-only behavior that later labs are designed to address

## After This Primer

Continue to [lab0_1_environment_setup/01_instructions.md](../lab0_1_environment_setup/01_instructions.md).
