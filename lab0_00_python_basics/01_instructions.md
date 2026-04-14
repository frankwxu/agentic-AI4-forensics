# Lab 0-00: Python Basics for Reading Course Notebooks

## Purpose

Use this primer before [lab0_01_llm_foundations/01_instructions.md](../lab0_01_llm_foundations/01_instructions.md). The goal is not to teach full Python. The goal is to teach just enough Python for you to read the notebook code used throughout the rest of the course.

This primer has three parts:

- a short reading you can do first
- a first practice notebook on variables, lists, dictionaries, loops, functions, JSON, and CSV
- a second practice notebook on later-lab patterns such as `sorted(...)`, comprehensions, `enumerate(...)`, and `@tool`

## Learning Goals

By the end of this primer, you should be able to:

- recognize variables, strings, numbers, lists, and dictionaries
- read simple `if` statements and `for` loops
- follow a small function definition and function call
- recognize common notebook patterns such as `response['model']` and `for name in toolbox:`
- read tiny JSON- and CSV-shaped examples without getting lost
- recognize later-lab helper patterns such as `with`, `sorted(...)`, comprehensions, and `enumerate(...)`
- understand `@tool` as a course-specific pattern for turning a function into something an agent can call
- feel more comfortable reading the code cells in the later labs

## What To Do

Complete the steps in this order:

1. Read [02_python_basics_reading.md](02_python_basics_reading.md) now.
2. Do not run the notebook yet if you have not completed the base local setup.
3. Start [lab0_01_llm_foundations/01_instructions.md](../lab0_01_llm_foundations/01_instructions.md) and complete its setup steps 1-4:

   - clone the repo
   - create and activate the virtual environment
   - install `requirements.txt`
   - launch Jupyter

4. Return here and open [03_python_basics_notebook.ipynb](03_python_basics_notebook.ipynb).
5. Run the notebook from top to bottom.
6. Open [04_python_patterns_for_later_labs.ipynb](04_python_patterns_for_later_labs.ipynb).
7. Run that notebook from top to bottom.
8. Then continue with the rest of [lab0_01_llm_foundations/01_instructions.md](../lab0_01_llm_foundations/01_instructions.md).

## Success Criteria

You have completed this primer when:

- you can explain what a variable stores
- you can read a list and a dictionary without confusion
- you can follow a small `if` statement and a small `for` loop
- you can read a function call and understand what value it returns
- you can inspect a tiny JSON file and a tiny CSV file in a notebook
- you can read later-lab helper patterns such as `sorted(...)`, list/dictionary comprehensions, and `enumerate(...)`
- you can explain in plain language what `@tool` is doing in the course notebooks
- you can read later course notebook cells with much less anxiety

## After This Primer

Continue into [lab0_01_llm_foundations/01_instructions.md](../lab0_01_llm_foundations/01_instructions.md).
