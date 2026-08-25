"""Mem0 adapter for long-term agent memory.

This adapter keeps the Agent independent from the Mem0 implementation.
"""


class Mem0Adapter:
    def __init__(self, user_id="default", config=None):
        self.user_id = user_id
        self.config = config or {}
        self.client = None

        try:
            from mem0 import Memory
            self.client = Memory.from_config(self.config)
        except ImportError:
            # Allow the framework to run without mem0 installed.
            self.client = None

    def add(self, content):
        if self.client is None:
            return None

        return self.client.add(
            content,
            user_id=self.user_id,
        )

    def search(self, query, limit=5):
        if self.client is None:
            return []

        return self.client.search(
            query,
            user_id=self.user_id,
            limit=limit,
        )
