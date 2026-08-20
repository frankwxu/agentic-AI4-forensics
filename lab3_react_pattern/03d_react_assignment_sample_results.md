# Lab 3 Assignment: Sample Results

## Use This Guide After Completing the Assignment

Complete `03c_react_assignment.ipynb` first. This guide shows one possible set of results so you can compare your reasoning; it is not an answer key to copy.

The artifact observations below are fixed by the staged evidence. The manual ReAct sequence and `ReactAgent` wording are representative examples: a model may choose a different valid order or phrasing if it uses the evidence carefully and keeps the final conclusion evidence-bounded.

## Fixed Artifact Observations

- The reported unattended interval starts at `2026-02-20T14:10:00Z` and ends at `2026-02-20T14:25:00Z`.
- Signal records an image attachment attempt at `2026-02-20T14:16:11Z`.
- Mobile data goes offline at `2026-02-20T14:15:58Z` and is restored at `2026-02-20T14:28:02Z`.
- The attempt is inside the reported unattended interval. The records do not confirm image delivery.

## One Possible Completed Response

### Task 1

- **Question in my own words:** Determine whether the phone tried to send an image through Signal while it was unattended, and state what the network records do and do not show about delivery.
- **Evidence I need:** The unattended interval, the Signal attempt time, and the network restoration time.
- **Response structure:** ReAct step log; unattended-interval evidence; Signal image-sending timing evidence; connectivity context and evidence-bounded conclusion.

### Task 2

- **Reported unattended interval:** `14:10:00Z` to `14:25:00Z`.
- **Two relevant artifact files:** `incident_window.csv` and `messaging_events.csv`.
- **Evidence limit:** A recorded attempt and later network restoration do not prove delivery.

### Task 3

- **Interval tool:** `get_incident_window()`.
- **Signal-attempt tool and input:** `get_message_attempt(app="Signal")`.
- **Connectivity tool:** `get_network_restore_time()`.

### Task 4

- **First tool and why:** `get_incident_window`, because the other event times need a comparison window.
- **Second tool and why:** `get_message_attempt(app="Signal")`, because it supplies the event time to compare with the interval.
- **Third tool and why:** `get_network_restore_time`, because it adds connectivity context without claiming delivery.

### Task 5

- **Prompt goal:** Reason, request one tool, inspect its observation, and respond only after collecting the required evidence.
- **Chat-history memory:** The case question, each model response, and each returned observation.
- **Evidence needed before a conclusion:** The interval, Signal attempt, and network-restoration observations.

### Task 6

- **Predicted first tool:** `get_incident_window`.
- **Representative model first tool:** `get_incident_window`.
- **Why it makes sense:** It establishes the time window before comparing the Signal event.

### Task 7

- **First observation:** The phone was unattended from `14:10:00Z` through `14:25:00Z`.
- **Representative next tool:** `get_message_attempt(app="Signal")`.
- **Why it follows:** The next question is whether the recorded Signal attempt falls inside that interval.

### Task 8

- **Second observation:** A Signal image attachment attempt was recorded at `14:16:11Z`.
- **Representative next tool:** `get_network_restore_time`.
- **Why it follows:** The attempt is inside the interval; connectivity context is still needed to avoid overstating delivery.

### Task 9

**ReAct step log**

1. Checked the reported unattended interval.
2. Checked the Signal image-sending attempt.
3. Checked when mobile data was restored.

**Unattended-interval evidence**

The reported unattended interval was `2026-02-20T14:10:00Z` to `2026-02-20T14:25:00Z`.

**Signal image-sending timing evidence**

The Signal image attachment attempt was recorded at `2026-02-20T14:16:11Z`, which is inside the reported unattended interval.

**Connectivity context and evidence-bounded conclusion**

Mobile data was restored at `2026-02-20T14:28:02Z`, after the unattended interval. The evidence supports that the phone attempted to send an image through Signal during the interval, but it does not confirm that the image was delivered.

### Task 10

- **Predicted order:** `get_incident_window -> get_message_attempt -> get_network_restore_time`.
- **Representative manual order:** `get_incident_window -> get_message_attempt -> get_network_restore_time`.
- **Reason for difference:** No difference in this example; each observation supports the next step.

### Task 11

- **Representative `ReactAgent` order:** `get_incident_window -> get_message_attempt -> get_network_restore_time`.
- **Possible variation:** A different model run could choose another order. Evaluate whether it still collects all required evidence and uses it logically.
- **Evidence-bounded conclusion:** A suitable agent conclusion identifies the in-window attempt and avoids claiming confirmed delivery.

### Task 12

- **Was the manual order reasonable?** Yes. It established the comparison window, located the Signal event, then checked connectivity context.
- **Observation that changed the next step:** The `14:16:11Z` Signal attempt was inside the interval, so the next step was to check network context rather than write a delivery conclusion.
- **Manual and agent delivery conclusions:** Both should say delivery is unconfirmed.
- **Evidence-bounded claim kept:** The phone attempted to send an image through Signal during the unattended interval.
- **Report I trust more and why:** I trust the report that clearly names the three observations and avoids claiming delivery, whether it came from the manual walkthrough or `ReactAgent`.

## What May Differ in Your Run

- The wording of the model's Reason text and final response.
- The exact `ReactAgent` tool order.
- The amount of explanation returned with each tool request.

Your work remains sound if it gathers the required observations, explains how they support the next step, and does not treat an attempt as confirmed delivery.
