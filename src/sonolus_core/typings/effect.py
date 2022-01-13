from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class EffectSRL(SRL):
    type: Literal["EffectThumbnail", "EffectData"]


@dataclass_json
@dataclass
class EffectItem(ItemBase):
    thumbnail: EffectSRL
    data: EffectSRL
    version: int = 2
