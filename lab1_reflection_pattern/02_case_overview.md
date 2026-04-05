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
Investigators are reviewing a company-issued Android phone after possible customer-data exfiltration. During the incident window, a file named `customers_q1.csv` appears in Downloads, is modified, and is later copied into Telegram's `Documents` app folder. Soon after, the device shows sent Telegram messages, Gmail activity, and network connections to Telegram and email services. A short time later, the original file disappears from Downloads, while location records suggest the phone stayed in the same general place during this period.

## Key Observed Event Sequence (UTC)
1. `01:05:22` - `customers_q1.csv` created in Downloads
2. `01:06:12` - `customers_q1.csv` modified
3. `01:07:41` - same file hash copied to Telegram's `Documents` app folder
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
| `event_type` | File action such as created, modified, copied, or deleted. |
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

Use the template below:

### 1. Timeline
Fill in 3-5 key events in time order.

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #999; padding: 6px;">Time</th>
      <th style="border: 1px solid #999; padding: 6px;">Event</th>
      <th style="border: 1px solid #999; padding: 6px;">Evidence Source</th>
      <th style="border: 1px solid #999; padding: 6px;">Observation or Inference?</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
  </tbody>
</table>

### 2. Main Conclusion
In 2-3 sentences, state the strongest conclusion you think the evidence supports. Try to separate what you directly observed from what you are inferring.

### 3. Alternative Explanations
Write 1-2 other possible explanations for the observed activity. Briefly explain why each one is still possible or why the current evidence does not fully rule it out.

### 4. Claim-to-Evidence Table
For each major claim in your report, identify the evidence that supports it. If a claim is weakly supported, say so.

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #999; padding: 6px;">Claim</th>
      <th style="border: 1px solid #999; padding: 6px;">Supporting Evidence</th>
      <th style="border: 1px solid #999; padding: 6px;">Confidence (0-1)</th>
      <th style="border: 1px solid #999; padding: 6px;">Limits / Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
  </tbody>
</table>

### 5. What Remains Uncertain
Use this table to name what you still cannot conclude from the evidence alone.

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr>
      <th style="border: 1px solid #999; padding: 6px;">Open Question</th>
      <th style="border: 1px solid #999; padding: 6px;">What Evidence Is Missing?</th>
      <th style="border: 1px solid #999; padding: 6px;">Why It Matters</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
    <tr>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
      <td style="border: 1px solid #999; padding: 6px;"></td>
    </tr>
  </tbody>
</table>

### 6. Confidence and Wording
When the evidence is incomplete, prefer cautious phrases such as:
- "the artifacts show"
- "this is consistent with"
- "this may suggest"
- "the current evidence does not confirm"

Your draft can be brief, but it should show that you are grounding each conclusion in evidence and noticing where the evidence stops.
