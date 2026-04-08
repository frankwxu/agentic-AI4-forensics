# Adapted from The Neural Maze's agentic-patterns-course (MIT License):
# https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/utils/completions.py
# Original copyright: Copyright (c) 2024 The Neural Maze

def completions_create(client, messages: list, model: str) -> str:
    """
    Sends a request to the client's `completions.create` method to interact with the language model.

    Args:
        client : The client object
        messages (list[dict]): A list of message objects containing chat history for the model.
        model (str): The model to use for generating tool calls and responses.

    Returns:
        str: The content of the model's response.

    Example:
        >>> messages = [{"role": "user", "content": "Say hello"}]
        >>> completions_create(client, messages, "qwen3:8b")
        'Hello!'
    """
    response = client.chat.completions.create(messages=messages, model=model)
    return str(response.choices[0].message.content)


def build_prompt_structure(prompt: str, role: str, tag: str = "") -> dict:
    """
    Builds a structured prompt that includes the role and content.

    Args:
        prompt (str): The actual content of the prompt.
        role (str): The role of the speaker (e.g., user, assistant).

    Returns:
        dict: A dictionary representing the structured prompt.

    Example:
        >>> build_prompt_structure("What happened?", "user")
        {'role': 'user', 'content': 'What happened?'}
        >>> build_prompt_structure("Search the logs", "user", tag="question")
        {'role': 'user', 'content': '<question>Search the logs</question>'}
    """
    if tag:
        prompt = f"<{tag}>{prompt}</{tag}>"
    return {"role": role, "content": prompt}


def update_chat_history(history: list, msg: str, role: str):
    """
    Updates the chat history by appending the latest response.

    Args:
        history (list): The list representing the current chat history.
        msg (str): The message to append.
        role (str): The role type (e.g. 'user', 'assistant', 'system')

    Example:
        >>> history = []
        >>> update_chat_history(history, "Please summarize the case.", "user")
        >>> history
        [{'role': 'user', 'content': 'Please summarize the case.'}]
    """
    history.append(build_prompt_structure(prompt=msg, role=role))


class ChatHistory(list):
    """
    A list-like chat history with an optional maximum length.

    Example:
        >>> history = ChatHistory(total_length=3)
        >>> history.append({"role": "system", "content": "You are helpful."})
        >>> history.append({"role": "user", "content": "Hi"})
        >>> history.append({"role": "assistant", "content": "Hello"})
        >>> history.append({"role": "user", "content": "Summarize the case"})
        >>> len(history)
        3
    """

    def __init__(self, messages: list | None = None, total_length: int = -1):
        """Initialise the queue with a fixed total length.

        Args:
            messages (list | None): A list of initial messages
            total_length (int): The maximum number of messages the chat history can hold.

        Example:
            >>> ChatHistory(messages=[{"role": "user", "content": "Hello"}], total_length=5)
            [{'role': 'user', 'content': 'Hello'}]
        """
        if messages is None:
            messages = []

        super().__init__(messages)
        self.total_length = total_length

    def append(self, msg: str):
        """Add a message to the queue.

        Args:
            msg (str): The message to be added to the queue

        Example:
            >>> history = ChatHistory(total_length=2)
            >>> history.append({"role": "user", "content": "First"})
            >>> history.append({"role": "assistant", "content": "Second"})
            >>> history.append({"role": "user", "content": "Third"})
            >>> history
            [{'role': 'assistant', 'content': 'Second'}, {'role': 'user', 'content': 'Third'}]
        """
        if len(self) == self.total_length:
            self.pop(0)
        super().append(msg)

    def show_messages(self):
        """Print all messages currently stored in the chat history.

        Example:
            >>> history = ChatHistory([{"role": "user", "content": "Hello"}])
            >>> history.show_messages()
            1. [user] Hello
        """
        if not self:
            print("ChatHistory is empty.")
            return

        for idx, message in enumerate(self, start=1):
            if isinstance(message, dict):
                role = message.get("role", "unknown")
                content = message.get("content", "")
                print(f"{idx}. [{role}] {content}")
            else:
                print(f"{idx}. {message}")



class FixedPrefixChatHistory(ChatHistory):
    """
    A chat history that keeps an initial prefix pinned while newer messages rotate.

    Example:
        >>> history = FixedPrefixChatHistory(
        ...     messages=[
        ...         {"role": "system", "content": "Always stay concise."},
        ...         {"role": "user", "content": "Question 1"},
        ...     ],
        ...     total_length=3,
        ...     pinned_prefix_len=1,
        ... )
        >>> history.append({"role": "assistant", "content": "Answer 1"})
        >>> history.append({"role": "user", "content": "Question 2"})
        >>> history[0]
        {'role': 'system', 'content': 'Always stay concise.'}
    """

    def __init__(self, messages=None, total_length=-1, pinned_prefix_len=1):
        super().__init__(messages, total_length)
        self.pinned_prefix_len = pinned_prefix_len

    def append(self, msg):
        if self.total_length != -1 and len(self) == self.total_length:
            # Evict the oldest message after the pinned prefix
            self.pop(self.pinned_prefix_len)
        super().append(msg)
