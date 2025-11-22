from typing import Literal
from pydantic import BaseModel, Field
from ..utils.generate import generate_id
from ..utils.dynamic_values import DynamicValuesMixin


class BaseObject(BaseModel, DynamicValuesMixin):
    object_id: str = Field(default_factory=lambda: generate_id("object"))
    type: Literal["base"] = "base"
