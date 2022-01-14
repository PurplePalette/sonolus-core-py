from dataclasses import dataclass
from typing import Generic, Literal, Optional, TypeVar

from dataclasses_json import dataclass_json

from .background import BackgroundItem
from .effect import EffectItem
from .engine import EngineItem
from .general import SRL, ItemBase
from .particle import ParticleItem
from .skin import SkinItem

T = TypeVar("T")


@dataclass_json
@dataclass
class UseItem(Generic[T]):
    useDefault: bool
    item: Optional[T]


@dataclass_json
@dataclass
class LevelItem(ItemBase):
    rating: int
    engine: EngineItem
    useSkin: UseItem[SkinItem]
    useBackground: UseItem[BackgroundItem]
    useEffect: UseItem[EffectItem]
    useParticle: UseItem[ParticleItem]
    cover: SRL[Literal["LevelCover"]]
    bgm: SRL[Literal["LevelBgm"]]
    data: SRL[Literal["LevelData"]]
