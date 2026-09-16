# Persist and retrieve case memory

**Time:** 35–45 minutes  
**Outcome:** Save case facts beyond one notebook run, retrieve records relevant to a new question, and distinguish durable memory from short-term conversation context.

## Background story

An analyst pauses a practice investigation and returns the next day. The previous conversation is no longer in memory, but a few verified case facts should still be available. The agent needs only the records relevant to the new question—not every message from the old session.

This lesson uses a small local JSON file and fictional data. It does not require an external database, embedding model, or AgentScope optional memory backend.

## Before you start

Complete [Lesson 06](../06-tracing-and-evaluation/README.md).

## Long-term memory versus short-term state

| Short-term state | Long-term memory in this lab |
| --- | --- |
| Exists while the current agent/session is active | Is saved to a local JSON file and can be loaded in a later run |
| Holds the recent conversation context | Holds selected, verified case records with sources |
| Is cleared when a case session ends | Must be reviewed, updated, and protected as persistent data |

The memory file is not automatically true. A record is useful only when it includes a source and is appropriate to retain.

## What the notebook demonstrates

1. Create and save three structured practice records to `data/practice_case_memory.json`.
2. Load those records as though a new notebook session had started.
3. Retrieve records that overlap with a question’s keywords.
4. Turn the retrieved records into a bounded context message an agent could use on its next turn.

## Is this RAG?

This is a transparent baseline for retrieval-augmented generation (RAG), not full semantic RAG. It retrieves records by shared keywords, so students can see exactly why each record was selected. A production RAG system generally uses embeddings and similarity search to retrieve related material even when it does not share exact words.

The important workflow is the same: retrieve a small, relevant set of durable records, provide that context to the agent, and require the agent to distinguish retrieved facts from unsupported assumptions.

## Checkpoint

Add a record about a different case, `INC-319`, then repeat the retrieval for `INC-204`. Confirm that the unrelated record is not included. This illustrates why stored memory needs case identifiers and focused retrieval.
