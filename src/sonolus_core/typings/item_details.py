from dataclasses import dataclass
from typing import Generic, List, TypeVar

from dataclasses_json import dataclass_json

T = TypeVar("T")


@dataclass_json
@dataclass
class ItemDetails(Generic[T]):
    item: T
    description: str
    recommended: List[T]
