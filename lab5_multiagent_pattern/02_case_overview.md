# Transmission and Custody Review Case

## Case Overview
- Case ID: `MA-2026-022`
- Scenario: Possible transmission of a sensitive image from a public-health outreach phone, combined with a chain-of-custody gap.
- Device: Motorola Edge 2024 (`Android 14`)
- Incident window (UTC): `2026-03-01T18:35:00Z` to `2026-03-01T19:10:00Z`
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `full_file_system`
- Acquisition tool: `Cellebrite UFED 7.70`
- Acquisition timestamp (UTC): `2026-03-03T12:04:55Z`
- Original image SHA-256:
  - `2ef6f6d371459ce23d3953196b03f979f8d2d440d4e8f1bf13d1712d7bf7f3a1`

## Narrative Summary
A county public-health outreach phone was unattended during a vaccination event. The staged artifact package includes device state records, file creation evidence, a messaging attach attempt, network activity, and a chain-of-custody log with a missing transfer entry. Students must decide both whether the file was likely transmitted and whether the evidence-handling record is complete enough to support confidence in that conclusion.

## Key Observed Event Sequence (UTC)
1. `18:35:02` - device locked at the start of the unattended interval
2. `18:44:11` - `patients_contacts.png` created on the device
3. `18:45:02` - attach attempt recorded in the messaging app
4. `18:45:07` - network upload started
5. `19:10:08` - device unlocked after the unattended interval
6. `2026-03-05T11:02:44Z` - analyst review begins without a documented transfer from the prior handler

## Artifact Files
- Manifest: `artifact_manifest.json`
- Device state: `device_state.csv`
- File events: `file_events.csv`
- Messaging events: `messaging_events.csv`
- Network events: `network_events.csv`
- Chain of custody: `chain_of_custody.csv`

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a multiagent workflow:
- assign specialized review roles
- compare technical evidence and evidence-handling findings
- resolve disagreements across agent outputs
- decide whether the transmission claim is confirmed, likely, or unconfirmed
- decide whether the custody record strengthens or weakens confidence
