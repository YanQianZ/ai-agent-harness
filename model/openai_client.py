from openai import OpenAI

from .base import BaseModel


class OpenAICompatibleModel(BaseModel):
    """Client for OpenAI-compatible APIs.

    Example:
        http://localhost:65145/v1
    """

    def __init__(self, base_url: str, api_key: str, model: str):
        self.client = OpenAI(
            base_url=base_url,
            api_key=api_key,
        )
        self.model = model

    def generate(self, messages: list[dict]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )

        return response.choices[0].message.content
