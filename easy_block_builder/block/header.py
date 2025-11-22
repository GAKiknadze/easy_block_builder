from .base import BaseBlock
from typing import Literal
from ..object.text import TextObject
from pydantic import Field


class HeaderBlock(BaseBlock):
    type: Literal["header"] = "header"
    text: TextObject
    level: int = Field(default=1, ge=1, le=6)
