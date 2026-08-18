# Lab 0-01: LLM Foundations

## Purpose

Use this primer before [lab0_02_environment_setup/01_instructions.md](../lab0_02_environment_setup/01_instructions.md). The goal is to give you both:

- a plain-language mental model of what a large language model is
- one small runnable example of how a model is trained and then used for next-word prediction

This lab does not require `.env`, Ollama, or Graphviz. Complete [Course Setup](../course_setup.md) and [Lab 0-00: Python Basics](../lab0_00_python_basics/01_instructions.md) before you begin.

## Learning Goals

By the end of this primer, you should be able to:

- explain what an LLM is in plain language
- describe tokens, tokenization, embeddings, and context window at a high level
- explain next-token prediction without using advanced math
- identify the causal mask that makes the tiny model a decoder-only Transformer
- train a tiny word-level decoder-only Transformer on a short book excerpt
- interpret training and validation loss and next-word accuracy graphs
- distinguish training from inference
- explain why prompts and temperature can change outputs
- identify at least one reason an LLM can sound confident and still be wrong
- explain why later labs add prompt structure, tools, memory, and human review around the model

## Lab Sequence

1. Read [02_llm_foundations_reading.md](02_llm_foundations_reading.md).
2. Study the figures embedded in the reading. Pay particular attention to the decoder-only Transformer, contextualized `bank` embeddings, and the next-token generation loop.
3. Open [03_tiny_llm_book_demo.ipynb](03_tiny_llm_book_demo.ipynb).
4. Run the notebook from top to bottom. Notice the initial random embeddings, the decoder-only architecture diagram, the training and validation loss/accuracy graphs, the next-word predictions, and the generated continuation.
5. Answer the short reflection questions at the end of the reading and notebook.

The notebook trains a tiny word-level decoder-only Transformer on a repeated public-domain book excerpt so you can see a visible training loop on classroom hardware. It is a teaching model, not a production LLM.

## Success Criteria

You have completed Lab 0-01 when:

- you can explain what an LLM predicts at each step
- you can distinguish tokens from words
- you can explain why the tiny model is decoder-only and how its causal mask limits attention to prior tokens
- you can explain the difference between training a model and using a model
- you can explain why prompt wording changes outputs
- you can point to training and validation loss/accuracy trends and explain what they mean
- you can inspect a next-word prediction and explain why it depends on the prompt context
- you can name at least one limitation of LLM-only behavior that later labs are designed to address

## Optional Extension

At the end of the notebook, complete **Optional Assignment: Train on a Different Text** to observe how a different training excerpt changes the vocabulary, learned parameters, predictions, and generated output. This is an extension, not a required completion criterion.

## Next

Continue to [lab0_02_environment_setup/01_instructions.md](../lab0_02_environment_setup/01_instructions.md).
