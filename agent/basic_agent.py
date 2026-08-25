"""Basic Agent implementation.

This is the first minimal agent layer:
User task -> Agent -> Response

Future modules:
- Model interface
- Tool calling
- Memory retrieval
- Planning
"""

from typing import Any


class Agent:
    """Minimal agent skeleton."""

    def __init__(self, name: str = "basic-agent"):
        self.name = name
        self.history = []

    def run(self, task: str) -> str:
        """Execute one agent turn."""
        self.observe(task)
        response = self.think(task)
        self.update(response)
        return response

    def observe(self, task: str) -> None:
        self.history.append({"role": "user", "content": task})

    def think(self, task: str) -> str:
        """Placeholder reasoning step.

        Will be replaced by LLM inference later.
        """
        return f"I received task: {task}"

    def update(self, response: str) -> None:
        self.history.append({"role": "agent", "content": response})
