from typing import Any


class SkillSelector:
    """Select a skill based on task and skill metadata.

    This follows a progressive disclosure pattern:
    1. expose skill name + description
    2. let model select a skill
    3. load full SKILL.md afterwards
    """

    def __init__(self, model=None, registry=None):
        self.model = model
        self.registry = registry

    def select(self, task: str) -> Any:
        if self.registry is None:
            return None

        skills = self.registry.list_skills()

        if not skills:
            return None

        if self.model is None:
            return skills[0]["name"]

        prompt = self._build_prompt(task, skills)

        response = self.model.generate([
            {
                "role": "user",
                "content": prompt,
            }
        ])

        return self._parse(response)

    def _build_prompt(self, task, skills):
        return f"""Select the most suitable skill for this task.

Available skills:
{skills}

Task:
{task}

Return only the skill name.
"""

    def _parse(self, response):
        for skill in self.registry.list_skills():
            if skill["name"] in response:
                return skill["name"]
        return None
