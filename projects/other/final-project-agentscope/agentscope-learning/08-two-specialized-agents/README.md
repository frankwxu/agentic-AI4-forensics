# Two specialized agents

**Time:** 35–45 minutes  
**Outcome:** Create two agents with distinct responsibilities, give them the same case materials, and compare their independent findings.

## Background story

Practice case `INC-204` contains an automated network-monitoring alert and a small evidence note. The alert records that a workstation repeatedly contacted one destination IP address; it does not explain the process, user action, payload, or service behind those contacts. One general-purpose agent can summarize both, but separate specialists make it easier to see which question each answer addresses. In this lesson, a network specialist reports what the connection data supports, while an evidence specialist identifies what remains unverified.

The two agents work independently. They do not talk to one another, share short-term state, or decide the final conclusion. Lesson 09 adds a sequential handoff; later lessons add routing and supervision.

## Before you start

Complete [Lesson 07](../07-long-term-memory-rag/README.md). Run the notebook from this folder so it loads the local `.env` file.

## Specialization versus multiple copies

| One general agent | Two specialized agents in this lab |
| --- | --- |
| One prompt covers every question | Each prompt owns one clearly stated question |
| One blended response | Two labeled findings that can be compared |
| Harder to notice a missing responsibility | The specialist's scope makes omissions easier to spot |

Specialization is not a guarantee of correctness. Each agent can still make a mistake or overstate evidence. The prompts therefore require factual, limited findings and clear statements about missing information.

## What the notebook demonstrates

1. Configure one shared model connection.
2. Create a `network_specialist` and an `evidence_specialist` with different system prompts.
3. Send the same structured practice case to both agents independently.
4. Print each finding under a clear label and compare the responsibilities.

## Why use one model object?

Both agents use the same local model settings, but they remain different agents because each has its own name, prompt, and state. Reusing the model object avoids repeating connection configuration; it does not merge agent memories or instructions.

## Checkpoint

Add a third specialist that lists only practical next evidence to collect. Keep its prompt narrow, then compare its output with the first two. Do not ask it to decide whether the activity is malicious—the practice facts are insufficient for that conclusion.
