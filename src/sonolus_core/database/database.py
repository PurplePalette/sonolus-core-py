from dataclasses import dataclass
from typing import List

from .background import BackgroundInfo
from .effect import EffectInfo
from .engine import EngineInfo
from .level import LevelInfo
from .particle import ParticleInfo
from .skin import SkinInfo


@dataclass
class Database:
    levels: List[LevelInfo]
    skins: List[SkinInfo]
    backgrounds: List[BackgroundInfo]
    effects: List[EffectInfo]
    particles: List[ParticleInfo]
    engines: List[EngineInfo]
