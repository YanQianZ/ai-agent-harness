from .short_term import ShortTermMemory
from .long_term import LongTermMemory


class MemoryManager:
    """Unified interface for agent memory.

    Current implementation provides:
    - short-term memory: current task context
    - long-term memory: persistent facts/preferences
    """

    def __init__(self):
        self.short_term = ShortTermMemory()
        self.long_term = LongTermMemory()

    def remember(self, key, value, memory_type="short_term"):
        if memory_type == "long_term":
            return self.long_term.save(key, value)
        return self.short_term.save(key, value)

    def recall(self, key=None):
        return {
            "short_term": self.short_term.search(key),
            "long_term": self.long_term.search(key),
        }
