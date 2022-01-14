from dataclasses import dataclass

from ..typings.effect import EffectItem
from .general import InfoBase


@dataclass
class EffectInfo(InfoBase, EffectItem):
    pass
