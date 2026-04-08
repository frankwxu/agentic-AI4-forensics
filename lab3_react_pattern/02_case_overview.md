# Incremental Communication Verification Case

## Case Overview
- Case ID: `RA-2026-009`
- Scenario: Quick review of whether a messaging attachment attempt happened during an unattended-device interval and whether connectivity returned before that interval ended.
- Device: Samsung Galaxy A54 (`Android 14`)
- Incident window (UTC): `2026-02-20T14:10:00Z` to `2026-02-20T14:25:00Z`
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `full_file_system`
- Acquisition tool: `Cellebrite UFED 7.70`
- Acquisition timestamp (UTC): `2026-02-21T10:43:18Z`
- Original image SHA-256:
  - `a7a4db1c2e1d75889f847d0b46a60bf8b84ae4d1533f6f5ce7aa98fb29dcb6ef`

## Narrative Summary
An outreach coordinator reported that a work phone was unattended for a short interval during a community event. The staged artifact package includes device-state records, a Signal attachment-attempt event, and network-status changes. Students must answer a narrow timing question: did the attachment attempt happen during the unattended interval, and did the phone reconnect before that interval ended?

## Key Observed Event Sequence (UTC)
1. `14:10:04` - device locked at the start of the unattended interval
2. `14:15:58` - mobile data drops offline
3. `14:16:11` - Signal attachment attempt recorded
4. `14:25:11` - device unlocked at the end of the unattended interval
5. `14:28:02` - mobile data restored after the unattended interval

## Artifact Files
- Manifest: `artifact_manifest.json`
- Device state: `device_state.csv`
- Messaging events: `messaging_events.csv`
- Network events: `network_events.csv`
- Chain of custody: `chain_of_custody.csv`

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a ReAct workflow:
- restate the forensic question
- choose the next tool call
- inspect the returned observation
- decide whether another tool is needed
- produce a bounded final answer that cites the observed evidence
