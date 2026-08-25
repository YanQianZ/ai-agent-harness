from .short_term import ShortTermMemory
from .long_term import LongTermMemory
from .mem0_adapter import Mem0Adapter


class MemoryManager:
    """Unified memory interface for agent.

    Layers:
    - short-term: current execution context
    - long-term: local persistent memory
    - mem0: external semantic long-term memory
    """

    def __init__(self, use_mem0=False, mem0_config=None):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()
        self.mem0 = Mem0Adapter(config=mem0_config) if use_mem0 else None

    def remember(self, key, value, memory_type="short_term"):
        if memory_type == "mem0" and self.mem0:
            return self.mem0.add(f"{key}: {value}")

        if memory_type == "long_term":
            return self.long_term.save(key, value)

        return self.short_term.save(key, value)

    def recall(self, key=None):
        result = {
            "short_term": self.short_term.search(key),
            "long_term": self.long_term.search(key),
        }

        if self.mem0 and key:
            result["mem0"] = self.mem0.search(key)

        return result
