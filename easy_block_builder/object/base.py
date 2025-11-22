from typing import Literal
from pydantic import BaseModel, Field
from ..utils.generate import generate_id
from datetime import datetime
from collections import defaultdict


class BaseObject(BaseModel):
    object_id: str = Field(default_factory=lambda: generate_id("object"))
    type: Literal["base"] = "base"

    __dynamic_values__: dict[str, int | str | bool | datetime | None] = Field(
        default_factory=lambda: defaultdict(lambda: None))