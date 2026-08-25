from typing import Any


class AgentLoop:
    """Agent loop with model, tools and memory integration.

    Flow:
    recall memory -> observe -> decide -> act -> update memory
    """

    def __init__(self, model=None, tools=None, memory=None):
        self.model = model
        self.tools = tools
        self.memory = memory
        self.history = []

    def run(self, task: str) -> Any:
        context = self.observe(task)

        action = self.decide(task, context)

        result = self.act(action)

        self.update(task, result)

        return result

    def observe(self, task: str):
        """Retrieve related memory before reasoning."""
        context = {}

        if self.memory:
            context = self.memory.recall(task)
            self.memory.remember("current_task", task)

        return context

    def decide(self, task: str, context=None):
        """Use memory context when creating model prompt."""
        if self.model is None:
            return {
                "type": "response",
                "content": task,
            }

        prompt = f"""
Task:
{task}

Relevant memory:
{context}

Decide the next action.
"""

        response = self.model.generate([
            {
                "role": "user",
                "content": prompt,
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
            self.memory.remember(
                "experience",
                {
                    "task": task,
                    "result": result,
                },
                memory_type="long_term"
            )
