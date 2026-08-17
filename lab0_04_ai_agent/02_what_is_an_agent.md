# Agent Concepts: From Models to Bounded Workflows

This short reading uses a familiar task to show what an AI agent does. You do not need to memorize technical terms at the start. First, focus on what the agent is trying to accomplish; later sections name the parts that help it work safely and predictably.

## A Travel-Planning Agent Example

Imagine asking a digital assistant: “Find me a hotel near the conference venue for two nights under $200 per night.” The assistant checks available hotels, compares options that meet the request, and returns the reservation result. With the user's approval, it can also make the booking.

<img src="./figures/travel_planning_agent.png" alt="Travel-planning agent loop" style="width: 120%; height: auto;">

*Figure 0A. A travel-planning agent helps with a complete task: it starts with a request, searches and compares hotels, and returns a booking result.*

Read Figure 0A from left to right:

- The user explains what they need: a hotel near the venue, for two nights, within a budget.
- The agent works out what to look for and checks the available options.
- The agent uses the hotel service to compare choices and, after approval, make a reservation.
- The hotel system returns a confirmation, or explains a problem such as no available rooms. That result helps the agent decide what to do next.

The key idea is simple: an agent can use information and tools to help complete a task, rather than only write an answer.

## Classical AI Definition of an Agent

A foundational definition of an agent is simple: it perceives an environment and acts on that environment. In classical AI, the environment provides percepts to the agent, and the agent produces actions that affect the environment.

At a high level, the agent receives information, decides what to do, acts, and then uses the result to guide what happens next. The travel example follows that same general loop.

**The travel example in agent terms.** The same story can now be described more precisely:

- **User objective:** “Book me a hotel near the conference venue for two nights under $200 per night.”
- **Reason / plan:** The agent identifies the dates, location, budget, and other constraints, then decides to search for and compare available hotels.
- **Act:** It uses hotel-search and booking tools to check availability, compare options, and make the reservation after the required approval.
- **Environment:** The hotel reservation system is updated, and the booking confirmation is returned to the user.

In compact form:

```text
Find hotel → evaluate options → select/book → reservation system updated
```

This example makes both reasoning and tool use visible. The next sections explain the general agent architecture behind it.

Figure 0B shows the classical version of this idea: the agent receives information from the environment, chooses an action, and that action changes the environment. Notice that the arrows form a loop rather than a one-time question-and-answer exchange.

![Figure 0B. Classical AI agent-environment view](https://artint.info/3e/html/x6.png)

*Figure 0B. Classical AI agent-environment view from Poole and Mackworth, [Agents and Environments](https://artint.info/3e/html/ArtInt3e.Ch2.S1.html): the agent receives percepts from the environment and produces actions that affect the environment.*

## A Modern LLM-Based Agent

An `LLM`-based agent is a system that uses an `LLM` to interact with its environment and achieve a user-defined objective. It combines the model's reasoning and planning with actions—often through external tools—to complete tasks.

The `LLM` is the reasoning core, not the entire agent. Instructions set the agent's role and limits. Memory retains useful context between steps, and tools let the agent gather information or act in its environment.

Figure 0C shows these parts working together. Configuration and instructions set the agent's role and boundaries; inputs give it information to work with; the `LLM`, memory, and tools support its decisions and actions; and the results become observations that can guide a later step.

![Figure 0C. Agent and key components](./figures/agent_components_with_config.png)

*Figure 0C. Agent and key components: configuration and instructions define the agent's role and boundaries; it then receives inputs, uses a reasoning model, memory, and tools to act in an environment, and observes results in a repeating thought–action–observation loop.*

The labels in Figure 0C have these meanings:

- `inputs`: user requests, system events, messages from other agents or systems, and files or data that give the agent something to work on
- `agent configuration / instructions`: persistent guidance that defines the agent's role and goal, rules and constraints, output format, and safety or human-review boundaries
- `brain / reasoning engine`: the AI model or `LLM` that understands inputs, reasons about goals and context, plans steps, and selects the next action
- `memory`: information the agent keeps while working, such as conversation history, intermediate notes, stored documents, databases, or a knowledge base
- `tools / capabilities`: the ways an agent interacts with the outside world, including retrieval or search, code execution, APIs and services, external actions, and file or data operations
- `environment`: the external world the agent can observe or act on, such as websites, databases, services, users, events, and devices
- `outputs`: responses and artifacts the agent produces, plus external effects such as sent messages, system changes, or completed actions
- `agent loop`: the repeating cycle of reasoning or planning, acting with a selected tool, and observing the result until the goal or stop condition is reached

**Inputs versus instructions.** Inputs are the current materials the agent works on. For example, “Summarize this mobile-device event log” is a user input. Instructions are the persistent guidance that controls how it works. For example, “Use only approved case materials, do not determine misconduct, and recommend one human-review step” is part of the agent configuration.

## Classical and LLM-Based Agents

Figure 0C is a modern version of the same basic agent idea in Figure 0B. Both receive information from an environment, decide what to do, act, and use the result to guide later behavior. The main difference is the component that makes the decisions and the interface used to act:

| Classical AI agent                                                          | LLM-based agent                                                                                                     |
| --------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **sensors** receive percepts from the environment                           | **inputs** include user requests, events, messages, and files or data                                               |
| a **controller** uses rules, search, planning, or a learned policy to decide | an **LLM reasoning engine** interprets the context, reasons, plans, and selects a next action                      |
| **actuators** carry out actions in the environment                          | **tools and capabilities** retrieve information, run code, call APIs, edit files, or take approved external actions |

Both types follow an observe–decide–act loop. In an LLM-based agent, the `LLM` takes the controller role and can work with natural-language instructions and external tools.

## How Much Control Does an AI Agent Have?

An `LLM` can be part of a workflow without controlling it. The term **agency** describes how much the model's output is allowed to control the next step in the surrounding program. Here, **control flow** means what the program does next: for example, choosing a path, calling a tool, or running another step.

**Reasoning and planning do not determine agency by themselves.** An `LLM` can reason about a problem and return text, but remain a simple processor if the program only displays or saves that response. The workflow gives the model agency when it allows the response to affect a path, tool, or later step.

The patterns below are simplified pseudocode, not code you need to run.

| Agency level | What the model output controls | What that is called | Example pattern |
| --- | --- | --- | --- |
| ☆☆☆ | It does not choose the program's next path, tool, or iteration. | Simple processor | `process_llm_output(llm_response)` |
| ★☆☆ | It chooses between predefined paths. | Router | `if llm_decision(): path_a() else: path_b()` |
| ★★☆ | It selects an approved function and its arguments. | Tool caller | `run_function(llm_chosen_tool, llm_chosen_args)` |
| ★★★ | It controls whether another step runs and what that step is. | Multi-step agent | `while llm_should_continue(): execute_next_step()` |
| ★★★ | It can delegate work to another agentic workflow. | Multi-agent workflow | `if llm_trigger(): execute_agent()` |

The final row is a coordination pattern, not automatically a higher level of agency than a multi-step agent. In digital forensics, greater workflow control makes clear boundaries, activity logs, authorization checks, and human review increasingly important.

## What Is a Bounded Agent?

Being bounded is not a separate agency level. **Agency** asks what the `LLM` is allowed to control in a workflow; **boundaries** define the limits on that control. A bounded agent can be a router, a tool caller, or a multi-step agent. As an agent is allowed to control more of a workflow, its boundaries become more important.

A bounded agent has a limited job and clear operating limits. A bounded-agent specification has two parts: a purpose and boundaries. The purpose defines the job to perform and what a useful result looks like. The boundaries define the permitted scope—what the agent may read, use, and produce—as well as prohibited actions, the stopping point, and decisions reserved for human review.

The core parts of a bounded-agent specification are:

- **purpose:** `role` tells the model what job it is performing, and `goal` tells it what a useful result should accomplish
- **permitted scope:** approved inputs and `approved tools` limit the materials and resources the agent may use
- **operational limits:** prohibited actions and a `stop condition` define what the agent must not do and when it must stop instead of continuing to generate more steps
- **human authority:** a `human review boundary` marks the decisions or judgments that must remain with a person
- **optional working context:** `short memory` is a limited amount of context the agent carries across steps

Memory is optional, not part of the definition of a bounded agent. If an agent uses memory, limiting its scope is another useful boundary. Memory is not the same as a tool call; memory is what the agent keeps, while tools are what it uses to gather information or do work.

Figure 0C uses broader architecture terms for these boundaries and optional design choices:

| Bounded-agent boundary or design choice | AI-agent component in Figure 0C |
| --- | --- |
| `role`, `goal`, approved inputs, prohibited actions, `stop condition`, `human review boundary` | agent configuration / instructions |
| `approved tools` | tools / capabilities |
| optional `short memory` | memory |

The `LLM` is the reasoning core that uses these configured components.

**Why bounded agents matter in digital forensics.** Digital-forensic work depends on being able to explain what information was examined, how it was handled, and what supports a conclusion. A bounded agent can help with a narrow, repeatable task—such as organizing approved artifacts, summarizing an event log, or identifying a question for the next review step—without becoming the source of the evidence or the final decision-maker.

Its limits make that assistance easier to audit: approved inputs define the evidence scope, approved tools define what the workflow may do, and a stop condition prevents an open-ended investigation. The agent's output is a lead or a structured summary for an examiner to check against the original materials. A qualified human must still assess reliability, preserve required documentation, and make investigative or legal conclusions.

Some actions have real consequences. For example, a booking agent should follow its approval and payment rules before it commits a reservation.

## A Course Example: Mobile Device Activity Summary Agent

Assume a synthetic case packet from a clinic-issued Google Pixel 7 running Android 14. A clinic supervisor submitted the phone after noticing after-hours activity involving a screenshot of a staff schedule.

The `Mobile Device Activity Summary Agent` is one example of a bounded agent. It does not examine the physical phone directly. It reads only the approved case brief, artifact manifest, and short event log. Its narrow job is to summarize the activity those materials show, identify what remains unknown, and recommend one next step for a human reviewer. It must not decide whether misconduct or a security incident occurred.

Figure 0D shows this course example. Its role, approved tools, short memory, stop condition, and human-review boundary make its first-pass review limited and inspectable:

![Figure 0D. Mobile Device Activity Summary Agent specification](./figures/lab0_agent_components.svg)

*Figure 0D. A course example of a bounded-agent specification: the LLM is the reasoning core, while role, goal, approved tools, short memory, stop condition, and a human-review boundary keep the device-activity review limited and inspectable.*

## Plain Model or Bounded Workflow?

Figure 0E is a quick map of the comparison you will make in the walkthrough. The top path shows a plain prompt sent directly to a model. The bottom path shows the same model bounded by an agent specification, a small case packet, approved inputs, and a human-review step.

![Figure 0E. Plain model versus bounded agent workflow for Lab 0-04](./figures/lab0_agent_workflow.svg)

*Figure 0E. Plain model versus bounded agent workflow for Lab 0-04: a single plain prompt can lead to an open-ended answer, while an agent specification plus a mini case packet turns the same model into a bounded workflow that produces structured output for human review.*

Next, open [03_agent_walkthrough.ipynb](03_agent_walkthrough.ipynb). You will compare the two paths using the same model and synthetic case packet.
