from dataclasses import dataclass


@dataclass
class ToolSchema:
    name: str
    description: str
    parameters: dict

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
        }


READ_FILE_TOOL = ToolSchema(
    name="read_file",
    description="Read content from a local file",
    parameters={"path": "string"},
)

SHELL_TOOL = ToolSchema(
    name="run_shell",
    description="Execute a local shell command",
    parameters={"command": "string"},
)
