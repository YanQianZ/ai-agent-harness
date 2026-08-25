from typing import Any


class AgentLoop:
    """Minimal agent loop with model and tool execution.

    Flow:
    observe -> decide -> act -> update
    """

    def __init__(self, model=None, tools=None, memory=None):
        self.model = model
        self.tools = tools
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
        """Use LLM to decide the next action.

        Future versions will parse structured tool calls from the model.
        """
        if self.model is None:
            return {
                "type": "response",
                "content": task,
            }

        response = self.model.generate([
            {
                "role": "user",
                "content": task,
            }
        ])

        return {
            "type": "response",
            "content": response,
        }

    def act(self, action):
        if action.get("type") == "tool":
            if self.tools is None:
                raise RuntimeError("Tools are not configured")

            return self.tools.run(
                action["name"],
                **action.get("args", {})
            )

        return action.get("content")

    def update(self, task: str, result: Any):
        self.history.append({
            "task": task,
            "result": result,
        })

        if self.memory:
            self.memory.remember("last_result", result)
