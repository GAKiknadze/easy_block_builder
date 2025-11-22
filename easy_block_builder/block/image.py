from .base import BaseBlock
from typing import Literal
from pydantic import Field
from ..object.file import FileObject
from ..object.size import SizedObject

class ImageBlock(BaseBlock):
    type: Literal["image"] = "image"
    title: str | None = Field(default=None, max_length=200)
    alt_text: str = Field(default="Image", max_length=200)
    images: list[SizedObject[FileObject]] | None = None