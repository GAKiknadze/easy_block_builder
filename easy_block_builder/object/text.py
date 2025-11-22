from typing import Literal
from .base import BaseObject
from pydantic import Field


class TextObject(BaseObject):
    type: Literal["text", "markdown"] = "text"
    text: str = Field(min_length=1, max_length=3000)
