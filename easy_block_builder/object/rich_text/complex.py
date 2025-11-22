from ..base import BaseObject
from typing import Literal
from pydantic import Field
from .elements import RICH_TEXT_ELEMENT_TYPES


class RichTextSection(BaseObject):
    type: Literal["rich_text_section"] = "rich_text_section"
    elements: list[RICH_TEXT_ELEMENT_TYPES]


class RichTextList(BaseObject):
    type: Literal["rich_text_list"] = "rich_text_list"
    elements: list[RICH_TEXT_ELEMENT_TYPES]
    style: Literal["bullet", "numbered"] = "bullet"
    offset: int = Field(default=0, ge=0)
    indent: int = Field(default=1, ge=0)
    border: int = Field(default=1, ge=0)


class RichTextPreformatted(BaseObject):
    type: Literal["rich_text_preformatted"] = "rich_text_preformatted"
    elements: list[RICH_TEXT_ELEMENT_TYPES]
    border: int = Field(default=1, ge=0)


class RichTextQuote(BaseObject):
    type: Literal["rich_text_quote"] = "rich_text_quote"
    elements: list[RICH_TEXT_ELEMENT_TYPES]
    border: int = Field(default=1, ge=0)


RICH_TEXT_COMPLEX_TYPES = (
    RichTextSection | RichTextList | RichTextPreformatted | RichTextQuote
)
