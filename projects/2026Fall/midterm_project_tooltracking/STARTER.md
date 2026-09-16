# Midterm starter case

The device and login records are entirely synthetic. Copy the three files from [`../tooltracking_starter/data/`](../tooltracking_starter/data/) into your controlled VM workspace, keeping their filenames and contents unchanged. Give the agent read access to the copied folder. Do not paste file contents into the prompt: the exercise needs observable file-tool use.

- `devices.csv` maps fictional device IDs to owners and device types.
- `auth_events.csv` contains seven fictional login records. Timestamps are UTC; file row order is not strict timestamp order.
- `alert_rule.txt` contains a synthetic rule. You may inspect it while exploring functions, but the required questions below do not depend on it.

## Questions

Run M0, M1, and M2 in separate agent sessions or clearly separated runs. M3 is an optional limitation case. `DATA_DIR` stands for the path to your copied data folder; replace it before running each prompt. Use the question wording as written on the first attempt. Save the exact prompt, response, and evidence of actual tool calls. If the agent does not call a tool, record that result before changing the prompt or tool configuration.

| ID | Investigation question | Intended observation |
| --- | --- | --- |
| M0 | Without reading any files, what is 2 + 2? | Basic model-response check. |
| M1 | Using `DATA_DIR/devices.csv`, who owns device D-101? Cite the device ID you used. | Simple file lookup. |
| M2 | First identify the owner of D-102 from `DATA_DIR/devices.csv`. Then use `DATA_DIR/auth_events.csv` to report the outcome and UTC time of event E-005. | Cross-file task. The agent may use one or multiple tool calls; report what happened. |
| M3 (optional) | Using `DATA_DIR/devices.csv`, who owns D-999? Do not invent a record. | Missing-record limitation; no file is missing. |

## Expected factual answers

- M0: 4.
- M1: Elena Ortiz owns D-101.
- M2: Maya Chen owns D-102; E-005 is a successful login at 2026-09-01 10:01:00 UTC.
- M3: D-999 is absent from `devices.csv`.

These answers check interpretation of the data. They do not specify a correct number or order of tool calls. An answer that is factually correct without tool-use evidence does not establish that a file was read. Review screenshots and run records for credentials or private paths before sharing them.
