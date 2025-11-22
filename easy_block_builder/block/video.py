from .base import BaseBlock
from typing import Literal
from ..object.text import TextObject
from pydantic import Field
from ..object.file import FileObject


class VideoBlock(BaseBlock):
    type: Literal['video'] = 'video'
    title: TextObject
    description: TextObject | None = None
    alt_text: str | None = Field(max_length=200)
    file: FileObject
