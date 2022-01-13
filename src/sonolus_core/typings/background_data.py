from dataclasses import dataclass
from enum import Enum

from dataclasses_json import LetterCase, dataclass_json


class Fit(Enum):
    width = "width"
    weight = "height"
    contain = "contain"
    cover = "cover"


@dataclass_json
@dataclass
class BackgroundConfiguration:
    blur: float
    mask: str


@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass
class BackgroundData:
    aspect_ratio: float
    fit: Fit
    color: str
