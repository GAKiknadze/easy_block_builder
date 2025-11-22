from .base import BaseBlock
from typing import Literal
from ..object.text import TextObject
from pydantic import Field


class SectionBlock(BaseBlock):
    type: Literal['section'] = 'section'
    text: TextObject
    fields: list[TextObject] = Field(default_factory=list, max_items=10)
    accessory: BaseBlock | None = None # Any input block
    expanded: bool = False
