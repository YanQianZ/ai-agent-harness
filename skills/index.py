class SkillIndex:
    """Lightweight skill metadata index.

    Keeps only name and description available for routing.
    Full skill instructions are loaded later.
    """

    def __init__(self, registry=None):
        self.registry = registry

    def build(self):
        if self.registry is None:
            return []

        return [
            {
                "name": skill["name"],
                "description": skill["description"],
            }
            for skill in self.registry.list_skills()
        ]
