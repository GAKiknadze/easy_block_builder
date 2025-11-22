from .base import BaseObject
from typing import Literal


class FileObject(BaseObject):
    type: Literal["file"] = "file"
    url: str | None = None
    file_id: str | None = None
