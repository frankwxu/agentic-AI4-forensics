# Course overview

**Before each class, download the latest course materials.** Follow the Git instructions below if you have Git installed, or use the ZIP download option.

## First download with Git

Open a terminal in the folder where you want to keep the course repository, then run:

```bash
git clone https://github.com/frankwxu/agentic-AI4-forensics.git
cd agentic-AI4-forensics
```

- `git clone` downloads the repository from GitHub and creates an `agentic-AI4-forensics` folder inside the terminal's current directory. This folder is your local repository.
- `cd agentic-AI4-forensics` moves the terminal into that folder so subsequent commands run there.

Your local repository is the folder containing `README.md` and `course_overview`. Its location depends on where you ran `git clone`.

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

## Download without Git

1. Open the [course repository on GitHub](https://github.com/frankwxu/agentic-AI4-forensics).
2. Select the `main` branch, then choose **Code → Download ZIP**.
3. Extract the ZIP into a new, separate folder. For each update, download it again and use a different folder so your previous work is preserved.
4. Use the newly extracted folder for the latest course materials. A ZIP download does not include Git history, so `git pull` will not update it.

## Run the bot demo

After getting the latest materials, follow the [Bot Demo: Memory and Tools instructions](BOT_DEMO_INSTRUCTIONS.md) to install dependencies, configure credentials, and start the Telegram bot.
