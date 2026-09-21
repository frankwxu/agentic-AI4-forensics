# Optional Supplement 01: Vision Transformer Foundations

## Purpose

This optional supplement introduces the Vision Transformer (`ViT`) through a short reading and a tiny implementation. It shows how the Transformer ideas used for text can also be applied to images by representing image patches as a sequence of tokens.

The notebook trains a small ViT from scratch to distinguish handwritten `3`s from `8`s in a balanced subset of MNIST. It is an educational demonstration, not a forensic image-validation system. This supplement is not required for Labs 1 through 5 or for the final project.

## Prerequisite

Complete [Lab 0-01: LLM Foundations](../lab0_01_llm_foundations/01_instructions.md) first. You should already have a high-level understanding of tokens, embeddings, positional information, attention, and Transformer blocks.

## Learning Goals

By the end of this supplement, you should be able to:

- trace an image from fixed-size patches to a predicted class
- explain patch embeddings, position embeddings, and the `[CLS]` token
- recognize ViT as an encoder-based Transformer
- contrast ViT image classification with decoder-only next-token generation
- implement and train a tiny ViT on a small image-classification task
- visualize how masking individual patches changes the model's predicted probability
- explain how TCAV tests sensitivity to a human-defined concept across many images
- explain why a confident image classification is not sufficient forensic evidence

## Supplement Sequence

1. Read [02_vit_introduction.md](02_vit_introduction.md).
2. Follow the ViT architecture figure from the input image to the predicted class.
3. Open [03_tiny_vit_digits_demo.ipynb](03_tiny_vit_digits_demo.ipynb) and run it from top to bottom. The first run downloads MNIST into this supplement's `data/` folder.
4. After Notebook 03 saves the trained checkpoint, open [04_visualize_vit_decision.ipynb](04_visualize_vit_decision.ipynb) and run it from top to bottom.
5. For an advanced concept-level analysis, run [05_tcav_concept_analysis.ipynb](05_tcav_concept_analysis.ipynb).
6. Compare the ViT pipeline with the decoder-only LLM pipeline from Lab 0-01.
7. Answer the reflection questions in the reading and notebooks.

## Completion Criteria

You have completed this supplement when you can:

- describe how an image becomes a sequence of patch tokens
- explain why ViT adds position information to those tokens
- state what the `[CLS]` token contributes to image classification
- identify the encoder blocks and classification head in the architecture
- interpret the demo's loss, accuracy, confusion matrix, and example predictions
- interpret a patch-occlusion heatmap as model sensitivity rather than proof of reasoning
- contrast local patch occlusion with class-level concept sensitivity from TCAV
- name at least two reasons a ViT prediction requires human and evidentiary validation in a forensic investigation

## Next

Return to the required course sequence. If you completed this supplement immediately after Lab 0-01, continue with [Lab 0-02: Environment Setup](../lab0_02_environment_setup/01_instructions.md).
