from typing import Literal, Self
from pydantic import BaseModel, Field
from ..utils.generate import generate_id


class BaseBlock(BaseModel):
    block_id: str = Field(default_factory=lambda: generate_id("block"))
    type: Literal["base"] = "base"
    
    @classmethod
    def create(cls) -> Self:
        raise NotImplementedError("Subclasses must implement the create method.")
    
    def render(self, **kwargs):
        raise NotImplementedError("Subclasses must implement the render method.")
