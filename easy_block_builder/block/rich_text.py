from .base import BaseBlock
from typing import Literal
from ..object.rich_text import RICH_TEXT_COMPLEX_TYPES


class RichTextBlock(BaseBlock):
    type: Literal["rich_text"] = "rich_text"
    elements: list[RICH_TEXT_COMPLEX_TYPES]
