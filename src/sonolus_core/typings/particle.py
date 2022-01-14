from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class ParticleItem(ItemBase):
    thumbnail: SRL[Literal["ParticleThumbnail"]]
    data: SRL[Literal["ParticleData"]]
    texture: SRL[Literal["ParticleTexture"]]
