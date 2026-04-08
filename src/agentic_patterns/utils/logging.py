# Adapted from The Neural Maze's agentic-patterns-course (MIT License):
# https://github.com/neural-maze/agentic-patterns-course/blob/main/src/agentic_patterns/utils/logging.py
# Original copyright: Copyright (c) 2024 The Neural Maze

import time

from colorama import Fore
from colorama import Style


def fancy_print(message: str) -> None:
    """
    Displays a fancy print message.

    Args:
        message (str): The message to display.
    """
    print(Style.BRIGHT + Fore.CYAN + f"\n{'=' * 50}")
    print(Fore.MAGENTA + f"{message}")
    print(Style.BRIGHT + Fore.CYAN + f"{'=' * 50}\n")
    time.sleep(0.5)


def fancy_step_tracker(step: int, total_steps: int) -> None:
    """
    Displays a fancy step tracker for each iteration of the generation-reflection loop.

    Args:
        step (int): The current step in the loop.
        total_steps (int): The total number of steps in the loop.
    """
    fancy_print(f"STEP {step + 1}/{total_steps}")
