# Transmission and Custody Review Case

## Case Overview
- Case ID: `MA-2026-022`
- Scenario: A public-health outreach phone was left unattended during a vaccination event. Investigators must determine whether a file containing patient-related information, `patients_contacts.png`, was likely transmitted from the device and whether a gap in the chain-of-custody record weakens confidence in that conclusion.
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
The case materials show when the phone was locked and unlocked, when `patients_contacts.png` was created, when a messaging app tried to attach that file, when network upload activity began, and how the phone was handled after collection. One transfer between handlers is missing from the chain-of-custody log. Students must evaluate both the transmission evidence and the evidence-handling record before deciding how confident they can be in the final conclusion.

## Investigation Goal
The investigation goal in this lab is to make one careful final judgment about the evidence. Students should answer:

1. Does the available technical evidence support that `patients_contacts.png` was transmitted?
2. Should that conclusion be labeled `confirmed`, `likely`, or `unconfirmed`?
3. Does the missing chain-of-custody transfer weaken confidence in that conclusion?

Students are not being asked to identify a suspect or prove intent. The task is to evaluate the strength of the transmission evidence and the completeness of the evidence-handling record.

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
