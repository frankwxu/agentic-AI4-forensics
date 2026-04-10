# Incremental Communication Verification Case

## Case Overview
- Case ID: `RA-2026-009`
- Scenario: Quick review of whether a Signal attachment attempt happened during a reported unattended interval, using connectivity records as context to avoid overstating delivery.
- Device: Samsung Galaxy A54 (`Android 14`)
- Incident window (UTC): `2026-02-20T14:10:00Z` to `2026-02-20T14:25:00Z` (`UTC` is a standard global time reference used so timestamps are interpreted consistently.)
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `full_file_system` (a detailed extraction that captures many files and records from the phone)
- Acquisition tool: `Cellebrite UFED 7.70` (a digital forensics tool used to extract device data)
- Acquisition timestamp (UTC): `2026-02-21T10:43:18Z`
- Original image SHA-256: (`SHA-256` is a digital fingerprint used to help verify that the collected evidence image has not been changed)
  - `a7a4db1c2e1d75889f847d0b46a60bf8b84ae4d1533f6f5ce7aa98fb29dcb6ef`

## Narrative Summary
An outreach coordinator reported that a work phone was left unattended on a supply table for a short interval during a community event. In this mini-case, students examine a small set of digital records to reconstruct what happened during that time window. The records include an incident-window record based on staff observation, a messaging record from Signal, and network-status records.

Signal is a messaging app, similar to WhatsApp or iMessage, that people can use to send text messages, photos, and other attachments. In this case, the Signal record shows an attachment attempt, meaning the phone tried to send or prepare a file through the app. The word `event` here means a recorded action or system log entry with a timestamp, such as the start of the unattended interval, a message attempt being logged, or mobile data going offline or coming back online.

`Network-status changes` means changes in the phone's internet connectivity, especially whether mobile data was unavailable or later restored. These records matter because a message attempt can appear in the logs even when the phone is not connected well enough to complete delivery. Students must answer one main timing question: did the attachment attempt happen during the unattended interval? The connectivity record does not prove delivery; it helps students decide whether the evidence supports only an attempt or something stronger.

## Key Observed Event Sequence (UTC)
1. `14:10:00` - staff observation marks the start of the unattended interval
2. `14:15:58` - mobile data drops offline
3. `14:16:11` - Signal attachment attempt recorded
4. `14:25:00` - staff observation marks the end of the unattended interval
5. `14:28:02` - mobile data restored after the unattended interval

## Artifact Files
- Manifest: `artifact_manifest.json` (a summary file describing the contents of the staged evidence package)
- Incident window: `incident_window.csv`
- Messaging events: `messaging_events.csv`
- Network events: `network_events.csv`
- Chain of custody: `chain_of_custody.csv` (a record of how the evidence was collected, handled, and documented)

## What Students Do Next
After reading this overview, students should open `03a_memory_demo.ipynb` for the memory warm-up, then `03b_lab_notebook.ipynb` for the guided ReAct walkthrough, and finally `03c_react_assignment.ipynb` for the less-guided assignment.

1. Restate the forensic question in your own words.
2. Run the notebook's manual ReAct walkthrough one tool call at a time.
3. After each tool call, record the observation and explain how it changes your next step.
4. Wait until you have all needed observations before writing the final answer.
5. In the second half of the notebook, compare your manual ReAct process with the packaged `ReactAgent`.

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a ReAct workflow:
- restate the forensic question
- choose the next tool call
- inspect the returned observation
- decide whether another tool is needed
- produce a bounded final answer that cites the observed evidence
