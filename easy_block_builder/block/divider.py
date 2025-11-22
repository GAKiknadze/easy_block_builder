from .base import BaseBlock
from typing import Literal


class DividerBlock(BaseBlock):
    type: Literal["divider"] = "divider"
