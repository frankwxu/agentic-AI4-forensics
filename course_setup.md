# Course Setup

Complete this one-time setup before starting Lab 0-00: Python Basics. It prepares your local copy of the course, Python environment, and Jupyter notebooks.

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

## 4. Launch Jupyter

Start Jupyter from the repository root while the virtual environment is still active:

```bash
jupyter notebook
```

## Next Step

Continue to [Lab 0-00: Python Basics](lab0_00_python_basics/01_instructions.md).
