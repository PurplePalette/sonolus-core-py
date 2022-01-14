from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class EffectItem(ItemBase):
    thumbnail: SRL[Literal["EffectThumbnail"]]
    data: SRL[Literal["EffectData"]]
