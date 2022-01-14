from dataclasses import dataclass
from typing import Optional

from ..typings.level import LevelItem
from .general import InfoBase


@dataclass
class UseInfo:
    useDefault: bool
    item: Optional[str]


@dataclass
class LevelInfo(InfoBase, LevelItem):
    engine: str
    useSkin: UseInfo
    useBackground: UseInfo
    useEffect: UseInfo
    useParticle: UseInfo
