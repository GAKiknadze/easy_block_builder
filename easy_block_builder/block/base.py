from typing import Literal, Self
from pydantic import BaseModel, Field
from ..utils.generate import generate_id
from datetime import datetime
from collections import defaultdict
from ..utils.dynamic_values import DynamicValuesMixin


class BaseBlock(BaseModel, DynamicValuesMixin):
    block_id: str = Field(default_factory=lambda: generate_id("block"))
    type: Literal["base"] = "base"
    
    __dynamic_values__: dict[str, int | str | bool | datetime | None] = Field(
        default_factory=lambda: defaultdict(lambda: None))
    
    @classmethod
    def create(cls) -> Self:
        raise NotImplementedError("Subclasses must implement the create method.")
    
    def render(self, **kwargs):
        raise NotImplementedError("Subclasses must implement the render method.")
