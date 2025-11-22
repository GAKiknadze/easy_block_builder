from .base import BaseBlock
from typing import Literal
from .rich_text import RichTextBlock

class TableBlock(BaseBlock):
    type: Literal['table'] = 'table'
    rows: list[RichTextBlock]