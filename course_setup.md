# Course Setup

Complete this one-time setup before starting Lab 0-00: Python Basics. It prepares your local copy of the course, Python environment, and VS Code notebooks.

## 1. Clone the Repository

```bash
git clone https://github.com/frankwxu/agentic-AI4-forensics.git
cd agentic-AI4-forensics
```

## 2. Create and Activate the Virtual Environment

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

## 3. Install the Python Packages

With the virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

## 4. Open the Course in VS Code

1. Open the `agentic-AI4-forensics` repository folder in Visual Studio Code.
2. Install the **Python** and **Jupyter** extensions if they are not already installed.
3. Select the `.venv-ai4-forensics` Python interpreter. In VS Code, open the Command Palette (`Ctrl+Shift+P`), choose **Python: Select Interpreter**, then select the virtual environment created in step 2.
4. Open a lab's `.ipynb` notebook. When prompted to select a notebook kernel, choose `.venv-ai4-forensics`.

VS Code starts and manages the Jupyter kernel for the notebook, so you do not need to run `jupyter notebook` in a terminal.

## Next Step

Continue to [Lab 0-00: Python Basics](lab0_00_python_basics/01_instructions.md).
