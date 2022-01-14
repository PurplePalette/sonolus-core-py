from dataclasses import dataclass
from typing import List, Literal, Optional, Union

from dataclasses_json import dataclass_json

from .skin_data import SkinSprite

EngineDataFunctionName = Literal[
    "Constant",
    "Execute",
    "Execute0",
    "If",
    "Switch",
    "SwitchWithDefault",
    "SwitchInteger",
    "SwitchIntegerWithDefault",
    "While",
    "Add",
    "Subtract",
    "Multiply",
    "Divide",
    "Mod",
    "Power",
    "Log",
    "Equal",
    "NotEqual",
    "Greater",
    "GreaterOr",
    "Less",
    "LessOr",
    "And",
    "Or",
    "Not",
    "Abs",
    "Sign",
    "Min",
    "Max",
    "Ceil",
    "Floor",
    "Round",
    "Frac",
    "Trunc",
    "Degree",
    "Radian",
    "Sin",
    "Cos",
    "Tan",
    "Sinh",
    "Cosh",
    "Tanh",
    "Arcsin",
    "Arccos",
    "Arctan",
    "Arctan2",
    "Clamp",
    "Lerp",
    "LerpClamped",
    "Unlerp",
    "UnlerpClamped",
    "Remap",
    "RemapClamped",
    "Smoothstep",
    "Random",
    "RandomInteger",
    "Get",
    "GetShifted",
    "Set",
    "SetShifted",
    "Draw",
    "DrawCurvedL",
    "DrawCurvedR",
    "DrawCurvedLR",
    "DrawCurvedB",
    "DrawCurvedT",
    "DrawCurvedBT",
    "Play",
    "PlayScheduled",
    "Spawn",
    "SpawnParticleEffect",
    "MoveParticleEffect",
    "DestroyParticleEffect",
    "HasSkinSprite",
    "HasEffectClip",
    "HasParticleEffect",
    "Judge",
    "JudgeSimple",
    "InSine",
    "InQuad",
    "InCubic",
    "InQuart",
    "InQuint",
    "InExpo",
    "InCirc",
    "InBack",
    "InElastic",
    "OutSine",
    "OutQuad",
    "OutCubic",
    "OutQuart",
    "OutQuint",
    "OutExpo",
    "OutCirc",
    "OutBack",
    "OutElastic",
    "InOutSine",
    "InOutQuad",
    "InOutCubic",
    "InOutQuart",
    "InOutQuint",
    "InOutExpo",
    "InOutCirc",
    "InOutBack",
    "InOutElastic",
    "OutInSine",
    "OutInQuad",
    "OutInCubic",
    "OutInQuart",
    "OutInQuint",
    "OutInExpo",
    "OutInCirc",
    "OutInBack",
    "OutInElastic",
    "IsDebug",
    "DebugPause",
    "DebugLog",
]


@dataclass_json
@dataclass
class EngineDataSprite:
    id: SkinSprite
    x: int
    y: int
    w: int
    h: int
    rotation: int


@dataclass_json
@dataclass
class EngineDataBucket:
    sprites: List[EngineDataSprite]


@dataclass_json
@dataclass
class EngineDataArchetypeData:
    index: int
    values: List[int]


@dataclass_json
@dataclass
class EngineDataArchetype:
    script: int
    data: Optional[EngineDataArchetypeData]
    input: Optional[bool]


@dataclass_json
@dataclass
class EngineDataScriptCallback:
    index: int
    order: Optional[int]


@dataclass_json
@dataclass
class EngineDataScript:
    preprocess: Optional[EngineDataScriptCallback]
    spawnOrder: Optional[EngineDataScriptCallback]
    shouldSpawn: Optional[EngineDataScriptCallback]
    initialize: Optional[EngineDataScriptCallback]
    updateSequential: Optional[EngineDataScriptCallback]
    touch: Optional[EngineDataScriptCallback]
    updateParallel: Optional[EngineDataScriptCallback]
    terminate: Optional[EngineDataScriptCallback]


@dataclass_json
@dataclass
class EngineDataValueNode:
    value: int


@dataclass_json
@dataclass
class EngineDataFunctionNode:
    func: EngineDataFunctionName
    args: List[float]


EngineDataNode = Union[EngineDataValueNode, EngineDataFunctionNode]


@dataclass_json
@dataclass
class EngineData:
    buckets: List[EngineDataBucket]
    archetypes: List[EngineDataArchetype]
    scripts: List[EngineDataScript]
    nodes: List[EngineDataNode]
