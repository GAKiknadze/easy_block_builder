from .base import BaseBlock
from typing import Literal
from ..object.file import FileObject


class FileBlock(BaseBlock):
    type: Literal["file"] = "file"
    id: FileObject
