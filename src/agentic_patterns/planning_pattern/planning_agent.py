import os
from typing import Any

from dotenv import load_dotenv
from openai import OpenAI

from agentic_patterns.utils.completions import FixedPrefixChatHistory
from agentic_patterns.utils.completions import build_prompt_structure
from agentic_patterns.utils.completions import completions_create
from agentic_patterns.utils.completions import update_chat_history

load_dotenv()

BASE_SYSTEM_PROMPT = ""


PLANNING_SYSTEM_PROMPT = """
You are a digital forensics planning agent.

Your job is to break a forensic question into an ordered investigation plan, identify what evidence is needed,
and revise the plan when new observations expose a missing dependency, contradiction, or timing conflict.

When building an initial plan:
- state the investigation goal in plain language
- produce an ordered step-by-step plan
- note the evidence needed for each major step
- identify clear replanning triggers

When revising a plan:
- preserve still-useful steps
- reorder steps when new observations change dependencies
- explain how the new observations change the investigation path
- keep the revised plan concise and evidence-focused

Always avoid unsupported conclusions. Treat planning as an aid to the student, not as final decision authority.
"""


class PlanningAgent:
    """
    A planning-first agent for building and revising investigation plans.

    The agent supports three entry points:
    - `build_initial_plan(...)` to create the first ordered plan
    - `revise_plan(...)` to update the plan after new observations
    - `run(...)` to generate a plan and iteratively improve it through self-review
    """

    def __init__(
        self,
        model: str = "llama-3.3-70b-versatile",
        system_prompt: str = BASE_SYSTEM_PROMPT,
        client: Any | None = None,
    ) -> None:
        self.client = client if client is not None else self._build_default_client()
        self.model = model
        self.system_prompt = system_prompt

    @staticmethod
    def _build_default_client() -> OpenAI:
        """
        Builds a default OpenAI-compatible client.

        Resolution order:
        1. OPENAI_BASE_URL / OLLAMA_BASE_URL (with OPENAI_API_KEY or fallback "ollama")
        2. OPENAI_API_KEY
        """
        base_url = os.getenv("OPENAI_BASE_URL") or os.getenv("OLLAMA_BASE_URL")
        api_key = os.getenv("OPENAI_API_KEY")

        if base_url:
            return OpenAI(base_url=base_url, api_key=api_key or "ollama")

        if api_key:
            return OpenAI(api_key=api_key)

        raise ValueError(
            "No default client configuration found. Pass `client=...` to PlanningAgent, "
            "or set OPENAI_API_KEY, or set OPENAI_BASE_URL/OLLAMA_BASE_URL."
        )

    def _build_system_prompt(self) -> str:
        return (self.system_prompt + "\n" + PLANNING_SYSTEM_PROMPT).strip()

    def _complete(self, user_msg: str) -> str:
        history = [
            build_prompt_structure(prompt=self._build_system_prompt(), role="system"),
            build_prompt_structure(prompt=user_msg, role="user"),
        ]
        return completions_create(self.client, history, self.model)

    def build_initial_plan(self, user_msg: str) -> str:
        """
        Build an ordered initial investigation plan for the supplied task.
        """
        planning_request = (
            "Build an initial investigation plan for the following forensic task.\n\n"
            "Return:\n"
            "1. Investigation goal\n"
            "2. Ordered steps\n"
            "3. Evidence needed for each major step\n"
            "4. Replanning triggers\n\n"
            f"Task:\n{user_msg}"
        )
        return self._complete(planning_request)

    def revise_plan(self, user_msg: str, current_plan: str, observations: str) -> str:
        """
        Revise an existing plan using new observations or contradictions.
        """
        revision_request = (
            "Revise the current forensic investigation plan using the new observations below.\n\n"
            "Return:\n"
            "1. What changed\n"
            "2. Revised ordered steps\n"
            "3. Updated evidence priorities\n"
            "4. Remaining replanning triggers\n\n"
            f"Original task:\n{user_msg}\n\n"
            f"Current plan:\n{current_plan}\n\n"
            f"New observations:\n{observations}"
        )
        return self._complete(revision_request)

    def run(self, user_msg: str, max_replans: int = 3) -> str:
        """
        Build an initial plan and iteratively improve it through planning-focused self-review.
        """
        history = FixedPrefixChatHistory(
            [
                build_prompt_structure(prompt=self._build_system_prompt(), role="system"),
                build_prompt_structure(prompt=user_msg, role="user"),
            ],
            total_length=max(6, (max_replans * 2) + 2),
            pinned_prefix_len=2,
        )

        plan = self.build_initial_plan(user_msg)
        update_chat_history(history, plan, "assistant")

        for _ in range(max_replans):
            review_prompt = (
                "Review the current investigation plan.\n"
                "If the plan is already well ordered, evidence-focused, and includes clear replanning triggers, "
                "reply exactly [[OK]].\n"
                "Otherwise, identify the most important missing dependency, contradiction, or observation "
                "that should trigger replanning."
            )
            update_chat_history(history, review_prompt, "user")
            review = completions_create(self.client, history, self.model)
            update_chat_history(history, review, "assistant")

            if "[[OK]]" in review:
                break

            revision_request = (
                "Revise the current plan using the following review notes.\n\n"
                f"Current plan:\n{plan}\n\n"
                f"Review notes:\n{review}"
            )
            update_chat_history(history, revision_request, "user")
            plan = completions_create(self.client, history, self.model)
            update_chat_history(history, plan, "assistant")

        return plan
