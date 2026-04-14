# Python Basics for Reading Course Notebooks

This reading is for students who may be new to Python but still need to work through notebook-based labs. The goal is not to make you a programmer in one sitting. The goal is to help you recognize the Python patterns that appear in the rest of this course.

## 1. Why You Need Python in This Course

Later labs use short Python notebook cells to:

- load case files
- build prompts
- call helper functions
- inspect model outputs
- loop through tool results

You do not need advanced programming for this course. You do need to be comfortable reading small pieces of code without freezing when you see them.

## 2. Reading Notebook Cells

Here is a small notebook-style example:

```python
from pathlib import Path

case_id = "DF-2026-001"
report_path = Path("report.md")
print(case_id)
```

How to read it:

- `from pathlib import Path` brings in a tool named `Path`
- `case_id = "DF-2026-001"` stores a string in a variable
- `report_path = Path("report.md")` creates a path object
- `print(case_id)` displays the value

Another common pattern is a function call:

```python
response = ask_model(prompt)
```

Read this as:

- call the function `ask_model`
- give it the value `prompt`
- store the returned value in `response`

You will also see method calls like:

```python
agent.run(user_msg)
```

Read this as:

- `agent` is an object
- `.run(...)` is an action attached to that object
- the notebook is asking the object to do its job

## 3. Lists and Dictionaries

Two of the most common data structures in this course are lists and dictionaries.

### Lists

```python
artifacts = ["messages.csv", "network_log.csv", "chain_of_custody.csv"]
```

Read this as:

- `artifacts` stores an ordered list
- the first item is `artifacts[0]`
- the second item is `artifacts[1]`

Example:

```python
first_file = artifacts[0]
```

### Dictionaries

```python
response = {
    "model": "tiny-demo",
    "seconds": 1.2,
    "summary": "Practice output"
}
```

Read this as:

- a dictionary stores key-value pairs
- you look up a value by key

Example:

```python
model_name = response["model"]
```

This pattern appears often in the labs:

```python
response["model"]
rows[0]["timestamp"]
```

## 4. `if` and `for`

### `if`

```python
if confidence < 0.5:
    print("Confidence is still low.")
```

Read this as:

- check whether the condition is true
- if it is true, run the indented line below it

### `for`

```python
for name in toolbox:
    print(name)
```

Read this as:

- take one item at a time from `toolbox`
- store that item in `name`
- run the indented block for each item

You will see this pattern often in the course:

```python
for name in toolbox:
    print(f"- {name}: {toolbox[name]}")
```

That means:

- loop through the tool names
- print each tool name and its description

## 5. Reading JSON- and CSV-Shaped Data

Many later labs use evidence data stored in JSON and CSV files.

### JSON Usually Loads Into Dictionaries and Lists

```python
import json

with open("case_packet.json", "r", encoding="utf-8") as handle:
    case_packet = json.load(handle)
```

After loading, you might read values like:

```python
case_packet["case_id"]
case_packet["question"]
case_packet["artifacts"][0]
```

### CSV Often Becomes a List of Rows

```python
import csv

with open("timeline.csv", "r", encoding="utf-8", newline="") as handle:
    rows = list(csv.DictReader(handle))
```

After loading, you might read values like:

```python
rows[0]["timestamp"]
rows[0]["event"]
```

In this course, it is enough to remember:

- JSON often becomes nested dictionaries and lists
- CSV often becomes a list of row dictionaries

## 6. How To Read Later Notebook Code

Here are a few patterns you will see later:

```python
case_packet = {...}
toolbox = {...}
for name in toolbox:
    print(name)
response["model"]
rows[0]["timestamp"]
```

Quick translation:

- `case_packet = {...}` means a dictionary is being created
- `toolbox = {...}` means another dictionary is being created
- `for name in toolbox:` means loop through the dictionary keys
- `response["model"]` means get the value stored under the key `"model"`
- `rows[0]["timestamp"]` means get the first row, then get its `"timestamp"` value

The most important skill is not memorizing syntax names. It is learning to slow down and read code one line at a time.

## 7. Short Reflection Questions

Use these questions to check your understanding:

1. What is the difference between a list and a dictionary?
2. What does `response["model"]` mean?
3. What does `rows[0]["timestamp"]` mean?
4. What does a `for` loop do in plain language?
5. What usually happens when a notebook cell calls a function like `ask_model(prompt)`?

## Notebook Bridge

When you open [03_python_basics_notebook.ipynb](03_python_basics_notebook.ipynb), watch for these patterns:

- variables storing strings, numbers, lists, and dictionaries
- simple `if` and `for` blocks
- a helper function that returns a dictionary
- loading a tiny JSON file and a tiny CSV file
- printing a few values that look like later course notebook outputs

Then open [04_python_patterns_for_later_labs.ipynb](04_python_patterns_for_later_labs.ipynb) to practice the extra notebook-reading patterns that show up often in Labs 2-5:

- `with` blocks for file reading
- `sorted(...)`
- list and dictionary comprehensions
- `enumerate(...)`
- imports from the course code
- `@tool` and simple type hints as reading aids
