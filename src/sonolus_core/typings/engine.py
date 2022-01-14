from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .background import BackgroundItem
from .effect import EffectItem
from .general import SRL, ItemBase
from .particle import ParticleItem
from .skin import SkinItem


@dataclass_json
@dataclass
class EngineItem(ItemBase):
    skin: SkinItem
    background: BackgroundItem
    effect: EffectItem
    particle: ParticleItem
    thumbnail: SRL[Literal["EngineThumbnail"]]
    data: SRL[Literal["EngineData"]]
    configuration: SRL[Literal["EngineConfiguration"]]
