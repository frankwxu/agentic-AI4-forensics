"""Telegram agent classroom demo: personality, memory, and tool use.

Read this file in six sections:

1. Configuration loads credentials and creates the OpenAI client.
2. Tool definitions describe what the model is allowed to request.
3. Persistent memory saves one JSONL conversation file per Telegram user.
4. ``execute_tool`` runs a tool request and returns its result.
5. ``run_agent_turn`` repeats model -> tool -> model until there is a final reply.
6. ``handle_message`` connects that agent loop to each incoming Telegram message.

Message flow:
Telegram message -> load saved memory -> run agent and tools -> save memory
-> send the final answer back to Telegram.
"""

SOUL = """
# Who You Are

**Name:** Jarvis
**Role:** Personal AI assistant

## Personality
- Be genuinely helpful, not performatively helpful
- Skip filler and get to the point
- Have opinions when useful
- Be concise when needed, thorough when it matters

## Boundaries
- Private things stay private
- Ask before taking external actions
- You're not the user's voice

## Tool Use
- When the user asks you to inspect files, run commands, or modify files, use tools instead of only describing what to do
- Before writing files or running potentially risky commands, confirm the user's intent unless the request is explicit and safe
"""

import json
import os
import subprocess
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

# --- Configuration ---------------------------------------------------------

# Prefer the course's secure credentials file. The fallback makes local testing
# convenient without putting credentials in source code.
for env_path in (Path("/home/frank/projects/telegram_bot/.env"), Path.cwd() / ".env"):
    if env_path.exists():
        load_dotenv(env_path, override=True)
        if os.getenv("OPENAI_API_KEY"):
            break

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL")

if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("Missing TELEGRAM_BOT_TOKEN in .env")
if not OPENAI_API_KEY:
    raise RuntimeError("Missing OPENAI_API_KEY in .env")
if not OPENAI_MODEL:
    raise RuntimeError("Missing OPENAI_MODEL in .env")

# The OpenAI client is reused for every incoming Telegram message.
client = OpenAI(api_key=OPENAI_API_KEY)

# Use the script's folder as the demo workspace, regardless of where Python is
# launched. Relative tool-created files and persistent sessions live here.
DEMO_DIR = Path(__file__).resolve().parent
SESSIONS_DIR = DEMO_DIR / "sessions"
SESSIONS_DIR.mkdir(exist_ok=True)

# --- Tool definitions ------------------------------------------------------

# These JSON-schema definitions are sent with every model request. With
# ``tool_choice="auto"``, the model compares the user request with each tool's
# name and description, then either returns normal text or a structured call.
TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "run_command",
            "description": "Run a shell command on the user's computer",
            "parameters": {
                "type": "object",
                "properties": {
                    "command": {
                        "type": "string",
                        "description": "The command to run"
                    }
                },
                "required": ["command"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Read a file from the filesystem",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    }
                },
                "required": ["path"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Write content to a file",
            "parameters": {
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "Path to the file"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write"
                    }
                },
                "required": ["path", "content"],
                "additionalProperties": False
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Search the web for information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Search query"
                    }
                },
                "required": ["query"],
                "additionalProperties": False
            }
        }
    }
]


# --- Persistent conversation memory ---------------------------------------


def get_session_path(user_id: str) -> str:
    """Give every Telegram user a separate persistent memory file."""
    return str(SESSIONS_DIR / f"{user_id}.jsonl")


def load_session(user_id: str) -> list[dict]:
    """Load a user's JSONL messages so the model can remember prior turns."""
    path = get_session_path(user_id)
    messages: list[dict] = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
    return messages


def save_session(user_id: str, messages: list[dict]) -> None:
    """Save the complete updated history; JSONL stores one message per line."""
    path = get_session_path(user_id)
    with open(path, "w", encoding="utf-8") as f:
        for message in messages:
            f.write(json.dumps(message, ensure_ascii=False) + "\n")


def truncate_text(text: str, limit: int = 4000) -> str:
    """Keep tool results small enough to send back to the model."""
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated]"


# --- Tool execution --------------------------------------------------------


def get_demo_file_path(path: str) -> Path:
    """Resolve a generated file path and keep it inside the demo folder."""
    resolved_path = (DEMO_DIR / path).resolve()
    if not resolved_path.is_relative_to(DEMO_DIR):
        raise ValueError("Files created by this demo must stay in the demo folder")
    return resolved_path


def execute_tool(name: str, tool_input: dict) -> str:
    """Run one tool requested by the model and return its text result."""
    if name == "run_command":
        # This is deliberately broad for the classroom demo; do not expose it
        # to untrusted users in a production bot.
        result = subprocess.run(
            tool_input["command"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
            # Relative files made by a command are created beside this script.
            cwd=DEMO_DIR,
        )
        return truncate_text((result.stdout or "") + (result.stderr or ""))

    if name == "read_file":
        with open(tool_input["path"], "r", encoding="utf-8") as f:
            return truncate_text(f.read())

    if name == "write_file":
        output_path = get_demo_file_path(tool_input["path"])
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(tool_input["content"])
        return f"Wrote to {output_path}"

    if name == "web_search":
        # Placeholder implementation
        return f"Search results for: {tool_input['query']}"

    return f"Unknown tool: {name}"


# --- Agent loop ------------------------------------------------------------


def run_agent_turn(messages: list[dict], system_prompt: str) -> tuple[str, list[dict]]:
    """Return a final answer after the model has finished requesting tools.

    A model response is either a final text answer or one or more tool calls.
    Tool results are appended to ``messages`` and the model is called again.
    """
    while True:
        # Give the model the personality prompt, this user's saved conversation,
        # and the allowed tool schemas. ``auto`` lets the model choose a tool
        # only when it believes a tool would help answer the user.
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[
                {"role": "system", "content": system_prompt},
                *messages,
            ],
            tools=TOOLS,
            tool_choice="auto",
        )

        assistant_message = response.choices[0].message

        # A response without tool calls is the agent's final answer for this turn.
        if not assistant_message.tool_calls:
            text = assistant_message.content or ""
            messages.append({
                "role": "assistant",
                "content": text,
            })
            return text, messages

        # Preserve the tool-call request in memory so the next API call has the
        # complete conversation required by the Chat Completions API.
        messages.append({
            "role": "assistant",
            "content": assistant_message.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in assistant_message.tool_calls
            ],
        })

        # Execute every requested tool, then append its result as a tool message.
        # The loop gives that result back to the model, which may request another
        # tool or turn the result into the final answer sent to Telegram.
        for tc in assistant_message.tool_calls:
            tool_name = tc.function.name
            tool_args = json.loads(tc.function.arguments or "{}")

            print(f"Tool: {tool_name}({json.dumps(tool_args)})")

            result = execute_tool(tool_name, tool_args)

            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": str(result),
            })


# --- Telegram integration --------------------------------------------------


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Turn one Telegram text message into one persistent agent interaction."""
    try:
        if update.message is None or update.message.text is None:
            return

        # Load this sender's prior conversation to provide short-term memory.
        user_id = str(update.effective_user.id)
        messages = load_session(user_id)

        messages.append({
            "role": "user",
            "content": update.message.text,
        })

        response_text, messages = run_agent_turn(messages, SOUL)

        save_session(user_id, messages)
        await update.message.reply_text(response_text)

    except Exception as e:
        if update.message is not None:
            await update.message.reply_text(f"Error: {e}")


def main():
    """Configure Telegram polling and receive messages until Ctrl+C is pressed."""
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
