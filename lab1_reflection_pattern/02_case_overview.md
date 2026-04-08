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
Investigators are reviewing a company-issued Android phone after possible customer-data exfiltration. During the incident window, a file named `customers_q1.csv` appears in Downloads, is accessed, and is later copied into Telegram's `Telegram/Documents` storage folder. Soon after, the device shows sent Telegram messages, Gmail activity, and network connections to Telegram and email services. A short time later, the original file disappears from Downloads, while location records suggest the phone stayed in the same general place during this period.

## Key Observed Event Sequence (UTC)
1. `01:05:22` - `customers_q1.csv` created in Downloads
2. `01:06:12` - `customers_q1.csv` accessed
3. `01:07:41` - same file hash copied to Telegram's `Telegram/Documents` storage folder
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

### Artifact Guide
Use the notes below to understand what each file contains before you begin your draft.

| File | What It Contains | Important Columns |
|------|------------------|-------------------|
| `artifact_manifest.json` | High-level case metadata about the device, time handling, dataset purpose, and available artifacts. | JSON fields rather than fixed columns |
| `file_events.csv` | File-system activity during the incident window. | `timestamp_utc`, `path`, `event_type`, `sha256` |
| `app_db_messages.csv` | Selected app messages relevant to the case. | `timestamp_utc`, `app`, `contact`, `direction`, `text_excerpt` |
| `network_events.csv` | Network connections associated with the device during the incident window. | `timestamp_utc`, `domain`, `ip`, `bytes_out`, `process` |
| `location_events.csv` | Location records associated with the device. | `timestamp_utc`, `lat`, `lon`, `source` |
| `chain_of_custody.csv` | Handling and integrity log for the acquired evidence. | `timestamp_utc`, `handler`, `action`, `notes` |

#### Column Notes by File

`artifact_manifest.json` uses JSON fields rather than a fixed table layout. Focus on the device details, time-handling notes, dataset purpose, and artifact inventory.

`file_events.csv`

| Column | Meaning |
|--------|---------|
| `timestamp_utc` | Time of the file event in UTC. |
| `path` | File location on the device. |
| `event_type` | File action such as created, accessed, copied, or deleted. |
| `sha256` | File hash used to compare whether files have the same contents. |

`app_db_messages.csv`

| Column | Meaning |
|--------|---------|
| `timestamp_utc` | Time of the message in UTC. |
| `app` | App where the message was recorded. |
| `contact` | Other party in the conversation. |
| `direction` | Whether the message was sent from the device (`OUT`) or received by it (`IN`). |
| `text_excerpt` | Short excerpt of message content. |

`network_events.csv`

| Column | Meaning |
|--------|---------|
| `timestamp_utc` | Time of the network event in UTC. |
| `domain` | Remote service contacted by the device. |
| `ip` | Remote IP address for that service. |
| `bytes_out` | Amount of data sent from the device. |
| `process` | App or process tied to the network connection. |

`location_events.csv`

| Column | Meaning |
|--------|---------|
| `timestamp_utc` | Time of the location record in UTC. |
| `lat` | Approximate latitude of the device. |
| `lon` | Approximate longitude of the device. |
| `source` | How the location was obtained, such as GPS or Wi-Fi. |

`chain_of_custody.csv`

| Column | Meaning |
|--------|---------|
| `timestamp_utc` | Time of the handling step in UTC. |
| `handler` | Person responsible for the evidence at that step. |
| `action` | Handling step such as acquisition or hash verification. |
| `notes` | Short explanation of the handling step. |

## Intended Educational Use
This dataset is synthetic and designed to demonstrate a reflection loop:
- Generate an initial forensic report.
- Reflect/critique for provenance, consistency, and overclaiming.
- Revise into a more defensible report.

## What You Should Do Next
Use this case overview as your starting point for Lab 1. In the notebook, you will turn these artifacts into a preliminary incident report, then revise that report after critique.

As you work, keep these questions in mind:

1. What facts are directly supported by the artifacts?
2. What is the strongest defensible conclusion you can make about what happened to `customers_q1.csv`?
3. What remains uncertain, and what can you not claim from this evidence alone?

Your goal is not to make the strongest accusation possible. Your goal is to produce a careful, evidence-bounded report that separates observation from inference and cites the artifacts that support each claim.

## Student Draft v0
Before using the notebook, write a short first-pass report based on the case overview and the listed artifacts. Spend about 5-10 minutes on this draft. It does not need to be perfect. The purpose is to capture your initial reasoning before you revise it through the reflection workflow.

Use the same wording and order that the notebook will request later:

`Return these five parts in order: (1) timeline = key events in time order, (2) primary hypothesis = best-supported explanation, (3) two alternative hypotheses = other plausible explanations not fully ruled out, (4) confidence score 0-1 per claim = how strongly each claim is supported, (5) explicit evidence mapping = exact artifacts that support each claim, plus limits.`

`Hypothesis` and `claim` are not the same thing. A hypothesis is your broader explanation of what may have happened in the case. A claim is one specific statement inside your report that can be checked against the artifacts. One hypothesis usually contains several claims. For example, "the user likely prepared the file for external sharing" is a hypothesis, while "`customers_q1.csv` was created in Downloads at `01:05:22 UTC`" is a claim.

### (1) timeline
List the key events in time order.

| Time | Event | Evidence Source |
|------|-------|-----------------|
| `01:05:22 UTC` | `customers_q1.csv` created in Downloads | `file_events.csv` |
| `[enter time]` | `[enter event]` | `[enter artifact]` |
| `[enter time]` | `[enter event]` | `[enter artifact]` |

### (2) primary hypothesis
State the main explanation that best fits the available artifacts.

`[Write 2-3 sentences here.]`

### (3) two alternative hypotheses
- Alternative hypothesis 1: `[Write one other possible explanation and why it is still possible.]`

- Alternative hypothesis 2: `[Write a second possible explanation and why the current evidence does not fully rule it out.]`

### (4) confidence score 0-1 per claim
For each claim in your report, assign a confidence score from 0 to 1 and briefly explain why.

| Claim | Confidence (0-1) | Why This Score? |
|------|-------------------|-----------------|
| ``customers_q1.csv` was copied into Telegram's `Telegram/Documents` storage folder.` | `0.95` | `This is directly supported by a copied event in file_events.csv with a matching file hash and Telegram storage path.` |
| `[enter claim]` | `[0.0-1.0]` | `[explain why]` |
| `[enter claim]` | `[0.0-1.0]` | `[explain why]` |

### (5) explicit evidence mapping
For each claim in your report, identify the specific evidence that supports it. If a claim is weakly supported, say so.

| Claim | Supporting Evidence | Limits / Notes |
|------|----------------------|----------------|
| ``customers_q1.csv` was copied into Telegram's `Telegram/Documents` storage folder.` | `file_events.csv` copied event at `01:07:41 UTC`; matching `sha256` for the Downloads file and the Telegram-stored file | `This supports file staging inside Telegram storage, but it does not by itself confirm that the file was successfully sent to a recipient.` |
| `[enter claim]` | `[cite artifact(s)]` | `[note limits]` |
| `[enter claim]` | `[cite artifact(s)]` | `[note limits]` |

When the evidence is incomplete, prefer cautious phrases such as:
- "the artifacts show"
- "this is consistent with"
- "this may suggest"
- "the current evidence does not confirm"

Your draft can be brief, but it should separate observation from inference, ground each major claim in evidence, and note when the current artifacts do not confirm a stronger conclusion.
