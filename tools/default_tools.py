from .registry import ToolRegistry
from .file_tool import read_file
from .shell_tool import run_shell


def create_default_tools():
    registry = ToolRegistry()

    registry.register("read_file", read_file)
    registry.register("run_shell", run_shell)

    return registry
