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
- `artifact_manifest.json`: identifies the case and device, explains time handling, and lists the artifacts in the evidence package.
- `file_events.csv`: records when files were created, accessed, copied, or deleted. Use the path and file hash to trace `customers_q1.csv`.
- `app_db_messages.csv`: records selected Telegram and Gmail messages, including their time, direction, contact, and a short text excerpt.
- `network_events.csv`: records connections to remote services, the process responsible, and the amount of outgoing data. Use it to compare network activity with message and file events.
- `location_events.csv`: records approximate device locations from GPS, Wi-Fi, or cell sources. Use it to assess whether the phone stayed in the same general place.
- `chain_of_custody.csv`: records acquisition, hash verification, and later handling of the evidence, helping document its integrity.

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
Use this case overview as your starting point for Lab 1. In the notebook, the model will turn these artifacts into a preliminary incident report, then revise that report after critique for you to inspect.

As you work, keep these questions in mind:

1. What facts are directly supported by the artifacts?
2. What is the strongest defensible conclusion you can make about what happened to `customers_q1.csv`?
3. What remains uncertain, and what can you not claim from this evidence alone?

Your goal is not to make the strongest accusation possible. Your goal is to produce a careful, evidence-bounded report that separates observation from inference and cites the artifacts that support each claim.

## Prepare for the Reflection Workflow

The notebook will generate the initial report from this synthetic case package. Before running it, identify two details you expect a defensible report to include and one stronger conclusion that the current artifacts do **not** prove. You will use those expectations to inspect the model draft, reflection critique, and revised report.

Keep these distinctions in mind:

- A **hypothesis** is a broader explanation of what may have happened, such as “the user likely prepared the file for external sharing.”
- A **claim** is a specific, checkable statement within a report, such as “`customers_q1.csv` was created in Downloads at `01:05:22 UTC`.”

When the evidence is incomplete, prefer cautious phrases such as “the artifacts show,” “this is consistent with,” “this may suggest,” and “the current evidence does not confirm.”

## Worked Reflection Example

This short example shows what to look for when you inspect the notebook’s draft, critique, and revision. It does not replace checking the actual artifacts.

**Model Draft v1**

"The employee exfiltrated `customers_q1.csv` to an outside party through Telegram and Gmail."

**Reflection Critique**

"This conclusion is over-claimed. The artifacts support file preparation, Telegram staging, outbound messaging, outbound network activity, and later deletion of the source file. They do not independently confirm recipient receipt or prove that the same file was successfully transmitted through both Telegram and Gmail. Separate observed events from inferred transmission and explain what remains uncertain."

**Revised Model Draft v2**

"Artifacts show that `customers_q1.csv` was prepared on the device, copied into Telegram application storage, and followed by outbound Telegram and Gmail activity consistent with attempted external sharing. This supports a defensible conclusion that the user engaged in activity consistent with trying to share the file or its contents outside the organization. The current artifacts do not independently confirm completed delivery to a recipient or show that the same file was successfully transmitted through both channels."
