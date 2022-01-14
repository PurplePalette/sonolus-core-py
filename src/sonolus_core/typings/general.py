from dataclasses import dataclass
from typing import Generic, Literal, TypeVar

from dataclasses_json import dataclass_json


@dataclass
class ItemBase:
    name: str
    version: int
    title: str
    subtitle: str
    author: str


ResourceTypeLiteral = Literal[
    "LevelCover",
    "LevelBgm",
    "LevelData",
    "SkinThumbnail",
    "SkinData",
    "SkinTexture",
    "BackgroundThumbnail",
    "BackgroundData",
    "BackgroundImage",
    "BackgroundConfiguration",
    "EffectThumbnail",
    "EffectData",
    "EffectClip",
    "ParticleThumbnail",
    "ParticleData",
    "ParticleTexture",
    "EngineThumbnail",
    "EngineData",
    "EngineConfiguration",
]


ResourceType = TypeVar("ResourceType", bound=ResourceTypeLiteral)


@dataclass_json
@dataclass
class SRL(Generic[ResourceType]):
    type: ResourceType
    hash: str
    url: str
