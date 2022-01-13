from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class SkinSRL(SRL):
    type: Literal["SkinThumbnail", "SkinData", "SkinTexture"]


@dataclass_json
@dataclass
class SkinItem(ItemBase):
    thumbnail: SkinSRL
    data: SkinSRL
    texture: SkinSRL
    version: int = 2
