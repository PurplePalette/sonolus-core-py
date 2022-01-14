from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class BackgroundItem(ItemBase):
    thumbnail: SRL[Literal["BackgroundThumbnail"]]
    data: SRL[Literal["BackgroundData"]]
    image: SRL[Literal["BackgroundImage"]]
    configuration: SRL[Literal["BackgroundConfiguration"]]
