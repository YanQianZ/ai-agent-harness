from abc import ABC, abstractmethod


class BaseModel(ABC):
    """Abstract interface for language models."""

    @abstractmethod
    def generate(self, messages: list[dict]) -> str:
        """Generate response from messages."""
        pass
