from dataclasses import dataclass

from ..typings.particle import ParticleItem
from .general import InfoBase


@dataclass
class ParticleInfo(InfoBase, ParticleItem):
    pass
