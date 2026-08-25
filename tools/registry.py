class ToolRegistry:
    """Registry for agent tools.

    Agent should not directly call functions.
    It requests a tool by name, then the registry executes it.
    """

    def __init__(self):
        self.tools = {}

    def register(self, name, func):
        self.tools[name] = func

    def run(self, name, *args, **kwargs):
        if name not in self.tools:
            raise ValueError(f"Tool not found: {name}")

        return self.tools[name](*args, **kwargs)
