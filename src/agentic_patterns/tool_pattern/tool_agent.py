# Adapted from The Neural Maze's agentic-patterns-course (MIT License):
# https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/tool_pattern/tool_agent.py
# Original copyright: Copyright (c) 2024 The Neural Maze

import json
import os
from typing import Any

from colorama import Fore
from dotenv import load_dotenv
from openai import OpenAI

from agentic_patterns.tool_pattern.tool import Tool
from agentic_patterns.tool_pattern.tool import validate_arguments
from agentic_patterns.utils.completions import build_prompt_structure
from agentic_patterns.utils.completions import ChatHistory
from agentic_patterns.utils.completions import completions_create
from agentic_patterns.utils.completions import update_chat_history
from agentic_patterns.utils.extraction import extract_tag_content

load_dotenv()


TOOL_SYSTEM_PROMPT = """
You are a function calling AI model. You are provided with function signatures within <tools></tools> XML tags.
You may call one or more functions to assist with the user query. Don't make assumptions about what values to plug
into functions. Pay special attention to the properties 'types'. You should use those types as in a Python dict.
For each function call return a json object with function name and arguments within <tool_call></tool_call>
XML tags as follows:

<tool_call>
{"name": <function-name>,"arguments": <args-dict>,  "id": <monotonically-increasing-id>}
</tool_call>

Here are the available tools:

<tools>
%s
</tools>

Each <tool_call> block must contain exactly one valid JSON object with the keys "name", "arguments", and "id".
Do not put commentary, explanations, or nested <tool_call> tags inside a <tool_call> block.

When you have enough information from the tools, answer the user's question directly in plain text and do not
return any more <tool_call> tags.
"""


class ToolAgent:
    """
    The ToolAgent class represents an agent that can interact with a language model and use tools
    to assist with user queries. It generates function calls based on user input, validates arguments,
    and runs the respective tools.

    Attributes:
        tools (Tool | list[Tool]): A list of tools available to the agent.
        model (str): The model to be used for generating tool calls and responses.
        client (Any): OpenAI-compatible client used to interact with the language model.
        tools_dict (dict): A dictionary mapping tool names to their corresponding Tool objects.
    """

    def __init__(
        self,
        tools: Tool | list[Tool],
        model: str = "llama-3.3-70b-versatile",
        client: Any | None = None,
    ) -> None:
        self.client = client if client is not None else self._build_default_client()
        self.model = model
        self.tools = tools if isinstance(tools, list) else [tools]
        self.tools_dict = {tool.name: tool for tool in self.tools}

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
            "No default client configuration found. Pass `client=...` to ToolAgent, "
            "or set OPENAI_API_KEY, or set OPENAI_BASE_URL/OLLAMA_BASE_URL."
        )

    def add_tool_signatures(self) -> str:
        """
        Collects the function signatures of all available tools.

        Returns:
            str: A concatenated string of all tool function signatures in JSON format.
        """
        return "".join([tool.fn_signature for tool in self.tools])

    def process_tool_calls(self, tool_calls_content: list) -> dict:
        """
        Processes each tool call, validates arguments, executes the tools, and collects results.

        Args:
            tool_calls_content (list): List of strings, each representing a tool call in JSON format.

        Returns:
            dict: A dictionary where the keys are tool call IDs and values are the results from the tools.
        """
        observations = {}
        fallback_id = 0
        for tool_call_str in tool_calls_content:
            parsed_candidates = self._parse_tool_call_candidates(tool_call_str)

            if not parsed_candidates:
                print(
                    Fore.YELLOW
                    + "\nSkipping malformed tool call block because no valid JSON object could be recovered."
                )
                continue

            for tool_call in parsed_candidates:
                normalized_tool_call = self._normalize_tool_call_dict(tool_call)
                if normalized_tool_call is None:
                    print(
                        Fore.YELLOW
                        + f"\nSkipping malformed tool call payload: {tool_call}"
                    )
                    continue

                tool_name = normalized_tool_call["name"]
                tool = self.tools_dict.get(tool_name)
                if tool is None:
                    print(
                        Fore.YELLOW
                        + f"\nSkipping unknown tool request: {tool_name}"
                    )
                    continue

                fallback_id += 1
                normalized_tool_call.setdefault("id", fallback_id)

                print(Fore.GREEN + f"\nUsing Tool: {tool_name}")

                # Validate and execute the tool call
                validated_tool_call = validate_arguments(
                    normalized_tool_call, json.loads(tool.fn_signature)
                )
                print(Fore.GREEN + f"\nTool call dict: \n{validated_tool_call}")

                result = tool.run(**validated_tool_call["arguments"])
                print(Fore.GREEN + f"\nTool result: \n{result}")

                # Store the result using the tool call ID
                observations[validated_tool_call["id"]] = result

        return observations

    @staticmethod
    def _parse_tool_call_candidates(tool_call_str: str) -> list[dict]:
        """
        Recovers one or more JSON objects from a raw tool-call block.

        Some local models emit malformed wrappers, nested <tool_call> tags, or stray prose inside
        a tool_call block. This parser tries the simple case first, then falls back to scanning for
        valid JSON objects so the agent can continue when at least one object is recoverable.
        """
        stripped = tool_call_str.strip()
        candidates: list[dict] = []

        try:
            parsed = json.loads(stripped)
            if isinstance(parsed, dict):
                return [parsed]
        except json.JSONDecodeError:
            pass

        nested_tool_calls = extract_tag_content(stripped, "tool_call")
        if nested_tool_calls.found:
            for nested in nested_tool_calls.content:
                candidates.extend(ToolAgent._parse_tool_call_candidates(nested))
            if candidates:
                return candidates

        decoder = json.JSONDecoder()
        cursor = 0
        while cursor < len(stripped):
            start = stripped.find("{", cursor)
            if start == -1:
                break

            try:
                parsed, end = decoder.raw_decode(stripped[start:])
                if isinstance(parsed, dict):
                    candidates.append(parsed)
                    cursor = start + end
                    continue
            except json.JSONDecodeError:
                pass

            cursor = start + 1

        return candidates

    @staticmethod
    def _normalize_tool_call_dict(tool_call: dict) -> dict | None:
        """
        Normalizes small model deviations into the expected tool-call schema.
        """
        if not isinstance(tool_call, dict):
            return None

        normalized = dict(tool_call)
        if "name" not in normalized:
            for key, value in normalized.items():
                if key in {"arguments", "id"}:
                    continue
                if isinstance(value, str):
                    normalized["name"] = value
                    break

        if "name" not in normalized or "arguments" not in normalized:
            return None

        if not isinstance(normalized["arguments"], dict):
            return None

        return normalized

    def run(
        self,
        user_msg: str,
    ) -> str:
        """
        Handles the full process of interacting with the language model and executing a tool based on user input.

        Args:
            user_msg (str): The user's message that prompts the tool agent to act.

        Returns:
            str: The final output after executing the tool and generating a response from the model.
        """
        tool_chat_history = ChatHistory(
            [
                build_prompt_structure(
                    prompt=TOOL_SYSTEM_PROMPT % self.add_tool_signatures(),
                    role="system",
                ),
                build_prompt_structure(prompt=user_msg, role="user"),
            ]
        )

        max_rounds = max(3, len(self.tools) + 1)
        last_output = ""

        for _ in range(max_rounds):
            last_output = completions_create(
                self.client, messages=tool_chat_history, model=self.model
            )
            tool_calls = extract_tag_content(str(last_output), "tool_call")

            if not tool_calls.found:
                return last_output

            update_chat_history(tool_chat_history, last_output, "assistant")
            observations = self.process_tool_calls(tool_calls.content)
            update_chat_history(
                tool_chat_history,
                f"Observation: {json.dumps(observations)}",
                "user",
            )

        update_chat_history(
            tool_chat_history,
            "You have reached the tool-call limit. Provide the best final answer from the available observations.",
            "user",
        )
        return completions_create(self.client, tool_chat_history, self.model)
