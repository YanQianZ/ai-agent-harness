import os


class SkillRegistry:
    """Registry for reusable agent skills.

    A skill describes a workflow and guides the agent
    on when and how to use tools.
    """

    def __init__(self, skill_dir="skills"):
        self.skill_dir = skill_dir
        self.skills = {}

    def register(self, name, description):
        self.skills[name] = {
            "name": name,
            "description": description,
        }

    def list_skills(self):
        return list(self.skills.values())

    def get(self, name):
        return self.skills.get(name)
