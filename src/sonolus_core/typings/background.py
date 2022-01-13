from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from enum import Enum
from typing import Literal
from .general import ItemBase, SRL


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


@dataclass_json
@dataclass
class BackgroundSRL(SRL):
    type: Literal[
        "BackgroundThumbnail",
        "BackgroundData",
        "BackgroundImage",
        "BackgroundConfiguration"
    ]


@dataclass_json
@dataclass
class BackgroundItem(ItemBase):
    thumbnail: BackgroundSRL
    data: BackgroundSRL
    image: BackgroundSRL
    configuration: BackgroundSRL
