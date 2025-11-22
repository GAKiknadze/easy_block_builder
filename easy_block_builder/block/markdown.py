from .base import BaseBlock
from typing import Literal
from pydantic import Field


class MarkdownBlock(BaseBlock):
    type: Literal["markdown"] = "markdown"
    text: str = Field(default="", max_length=12000)
