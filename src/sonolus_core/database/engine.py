from dataclasses import dataclass

from ..typings.engine import EngineItem
from .general import InfoBase


@dataclass
class EngineInfo(InfoBase, EngineItem):
    skin: str
    background: str
    effect: str
    particle: str
