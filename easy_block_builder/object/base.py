from typing import Literal
from pydantic import BaseModel, Field
from ..utils.generate import generate_id


class BaseObject(BaseModel):
    object_id: str = Field(default_factory=lambda: generate_id("object"))
    type: Literal["base"] = "base"
