class LongTermMemory:
    """Persistent memory placeholder for future storage backend.

    This can later be replaced by SQLite, vector database, or other storage.
    """

    def __init__(self):
        self.store = {}

    def save(self, key, value):
        self.store[key] = value

    def search(self, key=None):
        if key is None:
            return self.store
        return self.store.get(key)
