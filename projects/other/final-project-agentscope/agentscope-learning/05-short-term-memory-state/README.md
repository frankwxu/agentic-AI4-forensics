# Keep context during one investigation

**Time:** 40–50 minutes  
**Outcome:** Use an AgentScope agent’s short-term conversation state, inspect the stored messages, and clear them when the case context should no longer be used.

## Background story

You are on a practice security team reviewing a workstation alert. A colleague gives the agent an incident number and a preliminary assessment. In a later question, the colleague refers to “that incident” without repeating the details. The agent needs the earlier exchange to answer correctly.

All case details in this lesson are fictional. The agent uses a local model and no tools.

## Before you start

Complete [Lesson 04](../04-react-loop-observability/README.md), then copy this lesson’s settings:

    cp .env.example .env

## Run the notebook

Open and run `01_short_term_memory_state.ipynb` from top to bottom.

## New term: short-term memory

Short-term memory is the conversation history held by the current agent while it works. In the current AgentScope 2 API, this history is the `context` list inside an `AgentState` object. The state holds the user messages and agent replies in the computer’s working memory. When the agent receives the next question, it can use that stored history as context.

Short-term memory is useful for a multi-turn conversation, but it is not a permanent case record:

| It does | It does not do |
| --- | --- |
| Keeps context for later turns in the current agent run | Verify facts or replace an evidence record |
| Lets the agent resolve references such as “that incident” | Persist automatically after the program stops |
| Can be inspected and cleared by the developer | Guarantee that the model will draw a correct conclusion |

### What AgentScope saves automatically

When an `Agent` is created with `state=case_state`, AgentScope automatically adds each incoming user message and each agent reply to `case_state.context`. The next `reply()` call uses that stored context when preparing the model request. After the notebook’s two turns, the context normally contains this sequence:

    user: first question
    assistant: first response
    user: follow-up question
    assistant: follow-up response

The notebook prints this list in the **Inspect the stored conversation** cell. The messages remain only in the current state object until they are cleared or the program ends.

## How this differs from earlier lessons

Lesson 03 gave an agent a tool. Lesson 04 showed the ReAct events produced while the agent used that tool. Lesson 05 does not add a tool or a new ReAct loop. Instead, it changes what the agent receives on its second turn: the earlier messages are available through short-term memory.

In short: Lesson 04 observes one agent run; Lesson 05 connects several turns of one conversation.

## What the notebook demonstrates

1. Create an empty `AgentState` object.
2. Pass it to an `Agent` when the agent is created.
3. Ask a first question that gives the agent the incident number and assessment.
4. Ask a second question that relies on the first question’s context.
5. Print the stored messages so that the conversation state is visible.
6. Clear the memory when the practice case is finished.

The second question should identify `INC-204` and describe its preliminary assessment without being given those details again. Exact wording can vary by model.

## Why clearing matters

Do not carry one case’s context into an unrelated case. Calling `case_state.context.clear()` removes the stored conversation messages. Setting `case_state.summary = ""` also removes any compressed summary of earlier context. A question asked afterward should be treated as a fresh conversation unless the needed facts are supplied again.

Later lessons cover persistence, tracing, and long-term memory. This lesson stays focused on the simplest form of state: messages retained only during the current run.

## Checkpoint

Change the first message so the incident number is `INC-319` and the assessment is `needs review`. Then rerun the conversation cells. The follow-up answer should use the new incident number and assessment. Finally, run the clear-memory cell and confirm that the printed memory count is zero.
