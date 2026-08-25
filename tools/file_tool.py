from pathlib import Path


def read_file(path: str) -> str:
    """Read a text file for agent."""
    return Path(path).read_text(encoding="utf-8")
