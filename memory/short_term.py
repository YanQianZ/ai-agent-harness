class ShortTermMemory:
    """Memory for current agent execution context."""

    def __init__(self):
        self.store = {}

    def save(self, key, value):
        self.store[key] = value

    def search(self, key=None):
        if key is None:
            return self.store
        return self.store.get(key)
