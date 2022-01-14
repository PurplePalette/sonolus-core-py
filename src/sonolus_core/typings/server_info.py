from dataclasses import dataclass
from typing import List

from dataclasses_json import dataclass_json

from .background import BackgroundItem
from .effect import EffectItem
from .engine import EngineItem
from .level import LevelItem
from .particle import ParticleItem
from .skin import SkinItem


@dataclass_json
@dataclass
class ServerInfo:
    levels: List[LevelItem]
    skins: List[SkinItem]
    backgrounds: List[BackgroundItem]
    effects: List[EffectItem]
    particles: List[ParticleItem]
    engines: List[EngineItem]
