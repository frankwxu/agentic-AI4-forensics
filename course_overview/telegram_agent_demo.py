# telegram_agent_demo.py - Telegram agent with personality, persistent sessions, and tool use

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

# Load .env from either your project folder or current directory
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

client = OpenAI(api_key=OPENAI_API_KEY)

SESSIONS_DIR = "./sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

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


def get_session_path(user_id: str) -> str:
    return os.path.join(SESSIONS_DIR, f"{user_id}.jsonl")


def load_session(user_id: str) -> list[dict]:
    """Load conversation history from disk."""
    path = get_session_path(user_id)
    messages: list[dict] = []
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    messages.append(json.loads(line))
    return messages


def save_session(user_id: str, messages: list[dict]) -> None:
    """Overwrite the session file with the full message list."""
    path = get_session_path(user_id)
    with open(path, "w", encoding="utf-8") as f:
        for message in messages:
            f.write(json.dumps(message, ensure_ascii=False) + "\n")


def truncate_text(text: str, limit: int = 4000) -> str:
    if len(text) <= limit:
        return text
    return text[:limit] + "\n...[truncated]"


def execute_tool(name: str, tool_input: dict) -> str:
    if name == "run_command":
        result = subprocess.run(
            tool_input["command"],
            shell=True,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return truncate_text((result.stdout or "") + (result.stderr or ""))

    if name == "read_file":
        with open(tool_input["path"], "r", encoding="utf-8") as f:
            return truncate_text(f.read())

    if name == "write_file":
        with open(tool_input["path"], "w", encoding="utf-8") as f:
            f.write(tool_input["content"])
        return f"Wrote to {tool_input['path']}"

    if name == "web_search":
        # Placeholder implementation
        return f"Search results for: {tool_input['query']}"

    return f"Unknown tool: {name}"


def run_agent_turn(messages: list[dict], system_prompt: str) -> tuple[str, list[dict]]:
    """Run one full agent turn, including any tool calls."""
    while True:
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

        # Final response with no tool calls
        if not assistant_message.tool_calls:
            text = assistant_message.content or ""
            messages.append({
                "role": "assistant",
                "content": text,
            })
            return text, messages

        # Save assistant message containing tool calls
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

        # Execute tool calls and feed results back
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


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        if update.message is None or update.message.text is None:
            return

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
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()


if __name__ == "__main__":
    main()
