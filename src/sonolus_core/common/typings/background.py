from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase
from enum import Enum
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


class BackgroundResourceType(Enum):
    background_thumbnail = "BackgroundThumbnail"
    background_data = "BackgroundData"
    background_image = "BackgroundImage"
    background_configuration = "BackgroundConfiguration"


@dataclass_json
@dataclass
class BackgroundSRL(SRL):
    type: BackgroundResourceType


@dataclass_json
@dataclass
class BackgroundItem(ItemBase):
    thumbnail: BackgroundSRL
    data: BackgroundSRL
    image: BackgroundSRL
    configuration: BackgroundSRL
