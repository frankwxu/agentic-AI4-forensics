# Course overview

**Start here: [Course Setup](../course_setup.md).** Complete this one-time setup to download the repository, prepare your Python environment, and configure VS Code before starting [Lab 0-00: Python Basics](../lab0_00_python_basics/01_instructions.md).

**Before each class, download the latest course materials.** If you cloned the repository with Git, follow the update commands below. If you downloaded a ZIP, follow [Update a ZIP download](#update-a-zip-download).

## Update before each class

Open a terminal and move into your existing local repository. For example, if you cloned it into your `Documents` folder:

```bash
cd ~/Documents/agentic-AI4-forensics
git switch main
git pull --ff-only origin main
```

- `cd ~/Documents/agentic-AI4-forensics` moves into the repository. Here, `~` means your home folder. This path is an example; replace it with the actual location on your computer. If you open a terminal directly inside the repository, skip this command.
- `git switch main` selects your local `main` branch, the branch used for the course materials.
- `git pull --ff-only origin main` gets the latest course materials from GitHub and updates the local branch you selected.

### Why does the command include both `origin` and `main`?

They answer two different questions:

| Name | Question it answers | Meaning in this course |
| --- | --- | --- |
| `origin` | Where should Git get updates? | A saved nickname for `https://github.com/frankwxu/agentic-AI4-forensics.git`. Git creates this nickname when you clone the repository. |
| `main` | Which branch should Git get? | The branch containing the course materials. A repository can contain multiple branches, each with its own line of development. |

Read `git pull --ff-only origin main` as: **“Get updates from the `main` branch in the GitHub repository called `origin`, and apply them to my current local branch.”** The preceding `git switch main` makes sure your current local branch is also `main`.

The `--ff-only` option allows Git to move your local branch forward when no merge is needed. If your local branch and the GitHub branch have developed separately, Git stops so you can ask for help.

If Git says **Already up to date**, no updates are needed. If Git reports local changes that prevent switching or updating, or says the histories have diverged, preserve your work and ask the instructor for help. Do not delete your changes to force an update.

## Update a ZIP download

Download a fresh ZIP using the [Course Setup ZIP instructions](../course_setup.md#download-without-git). Extract each update into a new, separate folder to preserve your previous work, and use the newly extracted folder for the latest course materials.

## Run the bot demo

After getting the latest materials, follow the [Bot Demo: Memory and Tools instructions](BOT_DEMO_INSTRUCTIONS.md) to install dependencies, configure credentials, and start the Telegram bot.
