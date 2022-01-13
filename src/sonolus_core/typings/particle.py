from dataclasses import dataclass
from typing import Literal

from dataclasses_json import dataclass_json

from .general import SRL, ItemBase


@dataclass_json
@dataclass
class ParticleSRL(SRL):
    type: Literal["ParticleThumbnail", "ParticleData", "ParticleTexture"]


@dataclass_json
@dataclass
class ParticleItem(ItemBase):
    thumbnail: ParticleSRL
    data: ParticleSRL
    texture: ParticleSRL
    version: int = 1
