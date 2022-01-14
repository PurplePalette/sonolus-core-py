from dataclasses import dataclass
from typing import Generic, List, TypeVar

from dataclasses_json import dataclass_json
from .localization import LocalizationText

T = TypeVar("T")


@dataclass_json
@dataclass
class InfoDetails(Generic[T]):
    item: T
    description: LocalizationText
    recommended: List[T]
