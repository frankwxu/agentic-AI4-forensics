# Timeline Reconstruction Case

## Case Overview
- Case ID: `PL-2026-011`
- Scenario: Mobile-phone access and communication timing review after a phone went missing during field visits.
- Device: Google Pixel 8 (`Android 14`)
- Incident window (UTC): `2026-02-11T20:55:00Z` to `2026-02-11T21:25:00Z`
- Analysis timezone: `America/New_York`

## Acquisition and Integrity
- Acquisition type: `full_file_system`
- Acquisition tool: `Cellebrite UFED 7.70`
- Acquisition timestamp (UTC): `2026-02-12T13:11:42Z`
- Original image SHA-256:
  - `4bc2ff573aa8bf3d6b0fb7a81341a7ef34df7b64c1d50368f6dd80e38f4a95ce`

## Narrative Summary
A state benefits caseworker reported that a phone was missing for 30 minutes during evening field visits. The staged artifact package includes device access records, a phone call log, WhatsApp activity, and network status changes. Students must reconstruct the sequence of events, decide which actions happened inside the incident window, and revise the timeline when network evidence changes the interpretation of message delivery.

## Key Observed Event Sequence (UTC)
1. `20:55:03` - device unlocked at the start of the missing period
2. `21:08:14` - outgoing call to `+1-555-0184` lasts `42` seconds
3. `21:10:00` - mobile data drops offline
4. `21:12:07` - WhatsApp chat opened
5. `21:13:12` - deleted image-attachment message event recorded
6. `21:27:04` - mobile data restored after the incident window

## Artifact Files
- Manifest: `artifact_manifest.json`
- Unlock events: `unlock_events.csv`
- Call log: `call_log.csv`
- WhatsApp events: `whatsapp_events.csv`
- Network status: `network_status.csv`
- Chain of custody: `chain_of_custody.csv`

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a planning and replanning workflow:
- define the incident scope
- build an initial timeline from the most direct records
- test the timeline against newly discovered observations
- replan when network status changes the timing interpretation
- produce a final timeline conclusion with cited evidence
