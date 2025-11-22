from pydantic import BaseModel, Field
from typing import Literal
from ..utils.generate import generate_id
from ..block.base import BaseBlock


class Page(BaseModel):
    type: Literal["page"] = "page"
    page_id: str = Field(default_factory=lambda: generate_id("page"))
    title: str = Field(default="Untitled Page")
    meta: dict[str, str] = Field(default_factory=dict)
    blocks: list[BaseBlock] = Field(default_factory=list)
