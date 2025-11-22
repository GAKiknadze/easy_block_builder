from ..base import BaseObject
from typing import Literal
from pydantic_extra_types.color import Color
from datetime import datetime


class RichTextLinkElement(BaseObject):
    type: Literal['link'] = 'link'
    url: str


class RichTextDateElement(BaseObject):
    type: Literal['date'] = 'date'
    timestamp: datetime


class RichTextTextElement(BaseObject):
    type: Literal['text'] = 'text'
    text: str
    style: Literal[
            'bold',
            'italic',
            'underline',
            'strikethrough',
            'code',
            'superscript',
            'subscript',
            'highlight',
        ] | None = 'bold'
    color: Color | None = None


RICH_TEXT_ELEMENT_TYPES = RichTextLinkElement | RichTextTextElement | RichTextDateElement

