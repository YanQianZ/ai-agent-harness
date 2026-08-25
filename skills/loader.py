from pathlib import Path


class SkillLoader:
    """Load skill definitions from SKILL.md files."""

    def load(self, path):
        path = Path(path)

        if not path.exists():
            raise FileNotFoundError(path)

        return {
            "name": path.parent.name,
            "content": path.read_text(encoding="utf-8"),
        }
