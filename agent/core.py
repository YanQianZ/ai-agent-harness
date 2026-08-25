from memory.manager import MemoryManager


class SimpleAgent:
    """A minimal agent loop.

    Flow:
    user task -> memory -> reasoning placeholder -> response -> memory
    """

    def __init__(self):
        self.memory = MemoryManager()

    def run(self, task: str) -> str:
        self.memory.remember("last_task", task)

        context = self.memory.recall("last_task")

        response = self.think(context)

        self.memory.remember("last_response", response)
        return response

    def think(self, context: str) -> str:
        return f"Agent received task: {context}"
