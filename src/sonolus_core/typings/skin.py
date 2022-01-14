from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class SkinItem(ItemBase):
    thumbnail: SRL[Literal["SkinThumbnail"]]
    data: SRL[Literal["SkinData"]]
    texture: SRL[Literal["SkinTexture"]]
