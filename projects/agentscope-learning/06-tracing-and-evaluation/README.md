# Trace an agent run and evaluate its answer

**Time:** 25–30 minutes  
**Outcome:** Record the major events in an agent run, then evaluate whether its final answer is complete and supported by the practice evidence.

## Background story

You are reviewing a practice security note about an internet address. The agent checks a fixed local record, then writes a short conclusion. You need two different kinds of evidence about that run:

1. An execution trace showing whether the agent called the expected tool.
2. An answer evaluation showing whether its conclusion used the record without making an unsupported claim.

The address and record are fictional. The notebook uses no network service or real company data.

## Before you start

Complete [Lesson 05](../05-short-term-memory-state/README.md). This short lab assumes that you already know the individual ReAct event names from [Lesson 04](../04-react-loop-observability/README.md). Then copy this lesson’s settings:

    cp .env.example .env

## Run the notebook

Open and run `01_trace_and_evaluate.ipynb` from top to bottom.

## Two related but different ideas

| Concept | Question it answers | Evidence used in this lesson |
| --- | --- | --- |
| Trace | What did the agent do? | Events from `reply_stream`, such as a model request, tool call, and tool result |
| Evaluation | Was the final answer acceptable? | A visible checklist applied to the final answer and the known practice record |

A successful trace does **not** prove that the answer is correct. For example, the agent may call the correct tool but overstate what a `suspicious` practice-list result means. Likewise, a good-looking answer does not prove that the intended tool was used. Review both.

## How this differs from earlier lessons

Lesson 04 teaches students to read individual ReAct events: model request, tool request, tool result, and final reply. This lesson does not reteach those event names. Instead, it saves selected events as a compact trace and uses that trace with a repeatable checklist to decide whether to accept or reject the run. Lesson 05 showed how one agent retains conversation context across turns.

In short: Lesson 04 explains events; Lesson 05 retains context; Lesson 06 uses run evidence to check behavior and output quality.

## What the notebook demonstrates

1. Create the same kind of read-only Python tool used in Lesson 03.
2. Run the agent with `reply_stream` and save selected event names in `trace_events`.
3. Print a compact trace summary showing model calls, tool use, and completion.
4. Extract the agent’s final answer.
5. Apply three visible checks: correct address, correct `suspicious` label, and no claim that the record proves malicious activity.
6. Accept the run only when the trace and answer checks both support it; otherwise, reject it and review the prompt, tool use, or answer.

The evaluator is intentionally simple. It checks for required wording rather than attempting to judge all possible meanings of the answer. Real evaluations often use a rubric, test cases, human review, or a more capable evaluator; the important habit is to make the criteria explicit and inspectable.

## Expected result

For the normal run, the trace summary should show two model requests, one tool request, one tool start, one tool result, and one completed reply. The evaluation should pass all three checks. A run is accepted only when both conditions are met.

## Checkpoint

Change the system prompt so it omits the instruction to say that a `suspicious` result is not proof of malicious activity. Rerun the notebook. If the model overclaims, the “avoids an unsupported claim” check should fail. Restore the original prompt afterward.
