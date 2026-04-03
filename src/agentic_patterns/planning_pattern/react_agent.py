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

BASE_SYSTEM_PROMPT = ""


REACT_SYSTEM_PROMPT = """
## Role
You are a function-calling AI model that reasons and acts in a loop until you can deliver a final response to the user.

## Loop Structure
Each iteration of your loop consists of three steps:

1. **Thought** — Reason about the current situation and decide what to do next. Wrap in <thought></thought> tags.
2. **Action** — Call one or more tools by emitting a <tool_call> JSON object (see format below). This is your action step.
3. **Observation** — The tool result will be returned to you wrapped in <observation></observation> tags. Use it to inform your next thought.

Repeat this loop until you have enough information to give a final answer, then wrap it in <response></response> tags.

## Tool Call Format
For each function call, return a JSON object within <tool_call></tool_call> tags:

<tool_call>
{"name": <function-name>, "arguments": <args-dict>, "id": <monotonically-increasing-id>}
</tool_call>

- Do NOT make assumptions about parameter values.
- Pay close attention to each parameter's `type` and use the correct Python types.
- You may make multiple tool calls sequentially; increment `id` for each call.

## Available Tools

<tools>
%s
</tools>

## Example Session

<question>What's the current temperature in Madrid?</question>

<thought>I need to retrieve the current weather in Madrid.</thought>
<tool_call>{"name": "get_current_weather", "arguments": {"location": "Madrid", "unit": "celsius"}, "id": 0}</tool_call>

<observation>{0: {"temperature": 25, "unit": "celsius"}}</observation>

<thought>I now have the temperature for Madrid. I can respond to the user.</thought>
<response>The current temperature in Madrid is 25 degrees Celsius.</response>

## Additional Constraints
- If the user's question is unrelated to any available tool, answer freely within <response></response> tags.
- Never leave the loop without eventually producing a <response>.
"""


class ReactAgent:
    """
    A class that represents an agent using the ReAct logic that interacts with tools to process
    user inputs, make decisions, and execute tool calls. The agent can run interactive sessions,
    collect tool signatures, and process multiple tool calls in a given round of interaction.

    Attributes:
        client (Any): OpenAI-compatible client used to handle model-based completions.
        model (str): The name of the model used for generating responses. Default is "llama-3.3-70b-versatile".
        tools (list[Tool]): A list of Tool instances available for execution.
        tools_dict (dict): A dictionary mapping tool names to their corresponding Tool instances.
    """

    def __init__(
        self,
        tools: Tool | list[Tool],
        model: str = "llama-3.3-70b-versatile",
        system_prompt: str = BASE_SYSTEM_PROMPT,
        client: Any | None = None,
    ) -> None:
        self.client = client if client is not None else self._build_default_client()
        self.model = model
        self.system_prompt = system_prompt
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
            "No default client configuration found. Pass `client=...` to ReactAgent, "
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
        for tool_call_str in tool_calls_content:
            tool_call = json.loads(tool_call_str)
            tool_name = tool_call["name"]
            tool = self.tools_dict[tool_name]

            print(Fore.GREEN + f"\nUsing Tool: {tool_name}")

            # Validate and execute the tool call
            validated_tool_call = validate_arguments(
                tool_call, json.loads(tool.fn_signature)
            )
            print(Fore.GREEN + f"\nTool call dict: \n{validated_tool_call}")

            result = tool.run(**validated_tool_call["arguments"])
            print(Fore.GREEN + f"\nTool result: \n{result}")

            # Store the result using the tool call ID
            observations[validated_tool_call["id"]] = result

        return observations

    def run(
        self,
        user_msg: str,
        max_rounds: int = 10,
    ) -> str:
        """
        Executes a user interaction session, where the agent processes user input, generates responses,
        handles tool calls, and updates chat history until a final response is ready or the maximum
        number of rounds is reached.

        Args:
            user_msg (str): The user's input message to start the interaction.
            max_rounds (int, optional): Maximum number of interaction rounds the agent should perform. Default is 10.

        Returns:
            str: The final response generated by the agent after processing user input and any tool calls.
        """
        # Wrap the user request in the expected XML tag so the model follows the ReAct prompt format.
        user_prompt = build_prompt_structure(
            prompt=user_msg, role="user", tag="question"
        )
        if self.tools:
            # Inject tool signatures into the ReAct system prompt once per run.
            self.system_prompt += (
                "\n" + REACT_SYSTEM_PROMPT % self.add_tool_signatures()
            )

        # Initialize conversation state with system instructions and the user question.
        chat_history = ChatHistory(
            [
                build_prompt_structure(
                    prompt=self.system_prompt,
                    role="system",
                ),
                user_prompt,
            ]
        )

        if self.tools:
            # Run the ReAct loop for max_rounds
            for _ in range(max_rounds):
                # Ask the model for the next step (thought/tool call/response) given current history.
                completion = completions_create(self.client, chat_history, self.model)

                # Exit early when the model emits a final answer.
                response = extract_tag_content(str(completion), "response")
                if response.found:
                    return response.content[0]

                # Parse reasoning and actions from the model output.
                thought = extract_tag_content(str(completion), "thought")
                tool_calls = extract_tag_content(str(completion), "tool_call")

                # Keep assistant output in history so future rounds can build on it.
                update_chat_history(chat_history, completion, "assistant")

                # Some models may skip <thought> tags; avoid crashing on empty content.
                if thought.found and thought.content:
                    print(Fore.MAGENTA + f"\nThought: {thought.content[0]}")
                else:
                    print(Fore.MAGENTA + "\nThought: [missing/Some models may skip <thought> tags]")

                if tool_calls.found:
                    # Execute tool calls and feed the tool results back as the next observation.
                    observations = self.process_tool_calls(tool_calls.content)
                    print(Fore.BLUE + f"\nObservations: {observations}")
                    update_chat_history(chat_history, f"{observations}", "user")

        # Fallback: if no tagged <response> appeared in-loop, return one final model completion.
        return completions_create(self.client, chat_history, self.model)
