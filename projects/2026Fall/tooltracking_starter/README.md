# Tool-tracking project data and additional cases

This synthetic dataset supports the agent tool-calling assignments. The names, devices, and events are fictional. Copy `data/` into the team's controlled VM workspace and GitHub repository, keeping the filenames and contents unchanged. Give the agent read access to that folder. Do not paste the file contents into a prompt: the exercise needs observable file-tool use.

- `data/devices.csv` maps three device IDs to fictional owners and device types.
- `data/auth_events.csv` contains seven fictional login records. Timestamps are UTC; file row order is not strict timestamp order.
- `data/alert_rule.txt` contains the synthetic rule used by F1.

## Required runs

Rerun questions M0, M1, and M2 from the [midterm question guide](../midterm_project_tooltracking/STARTER.md) using their original wording, replacing `DATA_DIR` with the current data-folder path. These must be **new agent runs**. Saved midterm traces may support a comparison, but do not replace final runs. The same prompt can produce a different tool-call sequence, so check each graph against evidence from its own run.

Also run F1 and F2 below. Use each question's wording for the first attempt. Run each question in a fresh agent session or clearly separate run, and save the exact prompt, response, and actual tool-call evidence. F0 and F3 are optional examples. Add runs if the required cases do not produce two actual tool calls or another behavior required by the assignment.

| ID | Additional investigation question | Intended observation |
| --- | --- | --- |
| F0 (optional) | Without reading any files, what is 7 + 5? | Another no-tool control case. |
| F1 | Using `DATA_DIR/devices.csv`, `DATA_DIR/auth_events.csv`, and `DATA_DIR/alert_rule.txt`, identify the owner of any device that meets rule R-1. Cite the relevant event IDs and timestamps. | Three-source investigation. The agent may combine reads into one call; record what it actually does. |
| F2 | Try to read `DATA_DIR/missing_events.csv` and report whether the file exists. Do not create it. | Controlled missing-file case. A refusal or graceful "file not found" response is also a result. |
| F3 (optional) | Using `DATA_DIR/auth_events.csv` and `DATA_DIR/devices.csv`, identify the device and owner with the latest successful login. Cite its event ID and UTC time. | Cross-file lookup with an ordering decision. |

## Expected factual answers

- F0: 12.
- F1: D-101, owned by Elena Ortiz, meets R-1. E-001, E-002, and E-003 are failed logins at 10:00, 10:02, and 10:04 UTC, followed by successful E-004 at 10:06 UTC. No other device meets the rule.
- F2: `missing_events.csv` is intentionally absent.
- F3: D-101, owned by Elena Ortiz, has the latest successful login: E-004 at 2026-09-01 10:06:00 UTC.

These answers check interpretation of the synthetic data. They do **not** specify a correct number or order of tool calls. A graph is correct only when it matches calls actually observed in that run. A factually correct answer without evidence of required tool use does not establish that a file was read.

## Automated outputs and verification

For each required run, process saved evidence with the automated command to produce a machine-readable graph, readable visualization, and validation report. Compare the graph with an independent execution record, report missing or extra nodes and incorrect edges, and deliberately alter a copy of one graph to show that the validator detects an error. Review exported traces before sharing; they may contain local paths or other information beyond this synthetic dataset.

If one tool is called twice, the graph needs two call nodes with different call IDs. A repeated tool name alone does not prove the second call was a retry; use run evidence before adding that label. Demonstrate this with a real repeated-call run when possible. Otherwise, use a clearly labeled synthetic trace fixture to test the graph generator's repeated-call handling, in addition to the required real runs.
