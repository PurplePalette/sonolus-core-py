from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class BackgroundSRL(SRL):
    type: Literal[
        "BackgroundThumbnail",
        "BackgroundData",
        "BackgroundImage",
        "BackgroundConfiguration",
    ]


@dataclass_json
@dataclass
class BackgroundItem(ItemBase):
    thumbnail: BackgroundSRL
    data: BackgroundSRL
    image: BackgroundSRL
    configuration: BackgroundSRL
    version: int = 2
