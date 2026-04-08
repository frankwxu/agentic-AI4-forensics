from importlib import import_module

__all__ = [
    "Agent",
    "Crew",
    "PlanningAgent",
    "ReactAgent",
    "ReflectionAgent",
    "Tool",
    "ToolAgent",
    "tool",
]

_EXPORTS = {
    "Agent": ("agentic_patterns.multiagent_pattern", "Agent"),
    "Crew": ("agentic_patterns.multiagent_pattern", "Crew"),
    "PlanningAgent": ("agentic_patterns.planning_pattern", "PlanningAgent"),
    "ReactAgent": ("agentic_patterns.react_pattern", "ReactAgent"),
    "ReflectionAgent": ("agentic_patterns.reflection_pattern", "ReflectionAgent"),
    "Tool": ("agentic_patterns.tool_pattern", "Tool"),
    "ToolAgent": ("agentic_patterns.tool_pattern", "ToolAgent"),
    "tool": ("agentic_patterns.tool_pattern", "tool"),
}


def __getattr__(name: str):
    if name not in _EXPORTS:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")

    module_name, attr_name = _EXPORTS[name]
    value = getattr(import_module(module_name), attr_name)
    globals()[name] = value
    return value


def __dir__():
    return sorted(list(globals().keys()) + __all__)
