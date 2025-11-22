from .base import BaseObject
from typing import Generic, Literal, TypeVar

T = TypeVar("T")

class SizedObject(BaseObject, Generic[T]):
    size: Literal["small", "medium", "large"] = "medium"
    content: T
