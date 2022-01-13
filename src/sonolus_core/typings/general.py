from dataclasses import dataclass
from enum import Enum


@dataclass
class ItemBase:
    name: str
    version: int
    title: str
    subtitle: str
    author: str


class ResourceType(Enum):
    level_cover = "LevelCover"
    level_bgm = "LevelBgm"
    level_data = "LevelData"
    skin_thumbnail = "SkinThumbnail"
    skin_data = "SkinData"
    skin_texture = "SkinTexture"
    background_thumbnail = "BackgroundThumbnail"
    background_data = "BackgroundData"
    background_image = "BackgroundImage"
    background_configuration = "BackgroundConfiguration"
    effect_thumbnail = "EffectThumbnail"
    effect_data = "EffectData"
    effect_clip = "EffectClip"
    particle_thumbnail = "ParticleThumbnail"
    particle_data = "ParticleData"
    particle_texture = "ParticleTexture"
    engine_thumbnail = "EngineThumbnail"
    engine_data = "EngineData"
    engine_configuration = "EngineConfiguration"


@dataclass
class SRL:
    type: ResourceType
    hash: str
    url: str
