# Course Setup

Complete this one-time setup before starting Lab 0-00: Python Basics. It prepares your local copy of the course, Python environment, and VS Code notebooks.

## 1. Download the Repository

Choose Git or the ZIP download option below. If you already have a local copy, follow the [update instructions](course_overview/README.md#update-before-each-class), then continue with step 2 in that folder.

### Clone with Git

With Git installed, open a terminal in the folder where you want to keep the course repository, then run:

```bash
git clone https://github.com/frankwxu/agentic-AI4-forensics.git
cd agentic-AI4-forensics
```

- `git clone` downloads the repository from GitHub and creates an `agentic-AI4-forensics` folder inside the terminal's current directory. This folder is your local repository.
- `cd agentic-AI4-forensics` moves the terminal into that folder so subsequent commands run there.

Your local repository is the folder containing `README.md` and `course_overview`. Its location depends on where you ran `git clone`.

### Download without Git

1. Open the [course repository on GitHub](https://github.com/frankwxu/agentic-AI4-forensics).
2. Select the `main` branch, then choose **Code → Download ZIP**.
3. Extract the ZIP into a folder on your computer.
4. Open a terminal inside the extracted repository folder containing `README.md` and `course_overview` before continuing with step 2 below.

A ZIP download does not include Git history, so `git pull` will not update it.

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

Before each class, follow [Update before each class](course_overview/README.md#update-before-each-class) to get the latest course materials.
