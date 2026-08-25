from typing import Callable, Any


class AgentLoop:
    """Minimal agent execution loop.

    Flow:
    observe -> decide -> act -> update

    This is the foundation for adding:
    - LLM reasoning
    - tool calling
    - memory integration
    - reflection
    """

    def __init__(self, model=None, tools=None, memory=None):
        self.model = model
        self.tools = tools or {}
        self.memory = memory
        self.history = []

    def run(self, task: str) -> Any:
        self.observe(task)

        action = self.decide(task)

        result = self.act(action)

        self.update(task, result)

        return result

    def observe(self, task: str):
        if self.memory:
            self.memory.remember("current_task", task)

    def decide(self, task: str):
        """Placeholder for LLM decision making."""
        return {
            "type": "response",
            "content": task,
        }

    def act(self, action):
        if action.get("type") == "tool":
            tool_name = action["name"]
            return self.tools[tool_name](**action.get("args", {}))

        return action.get("content")

    def update(self, task: str, result: Any):
        self.history.append({
            "task": task,
            "result": result,
        })

        if self.memory:
            self.memory.remember("last_result", result)
