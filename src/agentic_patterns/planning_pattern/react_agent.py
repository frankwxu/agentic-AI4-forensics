"""
Deprecated compatibility shim.

Repo-owned code should import `ReactAgent` from `agentic_patterns.react_pattern.react_agent`.
This file remains temporarily so older imports continue to resolve during the transition.
"""

from agentic_patterns.react_pattern.react_agent import ReactAgent

__all__ = ["ReactAgent"]
