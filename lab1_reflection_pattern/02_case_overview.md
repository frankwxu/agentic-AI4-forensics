# Simulated Mobile Exfiltration Case

## Case Overview
- Case ID: `DF-2026-017`
- Scenario: Suspected customer-data exfiltration from a corporate Android device prior to employee departure.
- Device: Google Pixel 7 (`Android 14`)
- Incident window (UTC): `2026-02-14T20:00:00Z` to `2026-02-16T04:00:00Z`
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `full_file_system`
- Acquisition tool: `Cellebrite UFED 7.64`
- Acquisition timestamp (UTC): `2026-02-18T14:32:11Z`
- Original image SHA-256:
  - `a5f30f7f6a6c95c17117d4ea03f2a618f9380ca379f6f31df96ab53ac49f58a8`

## Narrative Summary
Within the incident window, a file named `customers_q1.csv` appears in Downloads, is modified, then copied into Telegram documents. Shortly after, outgoing Telegram and Gmail activity occurs with elevated outbound network traffic to Telegram and SMTP endpoints. The original file is later deleted. Location events place the device at a stable location during this sequence.

## Key Observed Event Sequence (UTC)
1. `01:05:22` - `customers_q1.csv` created in Downloads
2. `01:06:12` - `customers_q1.csv` modified
3. `01:07:41` - same file hash copied to Telegram documents
4. `01:07:54` - outbound traffic to `api.telegram.org`
5. `01:07:58` - Telegram outbound message: "sending that sheet now"
6. `01:08:15` - Telegram outbound message: "delete after download"
7. `01:09:39` - outbound SMTP traffic via Gmail process
8. `01:09:44` - Gmail outbound message: "see attached export"
9. `01:12:04` - `customers_q1.csv` deleted from Downloads

## Artifact Files
- Manifest: `artifact_manifest.json`
- File events: `file_events.csv`
- App messages: `app_db_messages.csv`
- Network events: `network_events.csv`
- Location events: `location_events.csv`
- Chain of custody: `chain_of_custody.csv`

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a reflection loop:
- Generate an initial forensic report.
- Reflect/critique for provenance, consistency, and overclaiming.
- Revise into a more defensible report.
