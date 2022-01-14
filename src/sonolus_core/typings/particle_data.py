from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Literal, Optional

from dataclasses_json import dataclass_json


class ParticleEffect(Enum):
    NoteCircularTapBase = 110000
    NoteCircularTapRed = 110001
    NoteCircularTapGreen = 110002
    NoteCircularTapBlue = 110003
    NoteCircularTapYellow = 110004
    NoteCircularTapPurple = 110005
    NoteCircularTapCyan = 110006

    NoteCircularAlternativeBase = 111000
    NoteCircularAlternativeRed = 111001
    NoteCircularAlternativeGreen = 111002
    NoteCircularAlternativeBlue = 111003
    NoteCircularAlternativeYellow = 111004
    NoteCircularAlternativePurple = 111005
    NoteCircularAlternativeCyan = 111006

    NoteCircularHoldBase = 112000
    NoteCircularHoldRed = 112001
    NoteCircularHoldGreen = 112002
    NoteCircularHoldBlue = 112003
    NoteCircularHoldYellow = 112004
    NoteCircularHoldPurple = 112005
    NoteCircularHoldCyan = 112006

    NoteLinearTapBase = 120000
    NoteLinearTapRed = 120001
    NoteLinearTapGreen = 120002
    NoteLinearTapBlue = 120003
    NoteLinearTapYellow = 120004
    NoteLinearTapPurple = 120005
    NoteLinearTapCyan = 120006

    NoteLinearAlternativeBase = 121000
    NoteLinearAlternativeRed = 121001
    NoteLinearAlternativeGreen = 121002
    NoteLinearAlternativeBlue = 121003
    NoteLinearAlternativeYellow = 121004
    NoteLinearAlternativePurple = 121005
    NoteLinearAlternativeCyan = 121006

    NoteLinearHoldBase = 122000
    NoteLinearHoldRed = 122001
    NoteLinearHoldGreen = 122002
    NoteLinearHoldBlue = 122003
    NoteLinearHoldYellow = 122004
    NoteLinearHoldPurple = 122005
    NoteLinearHoldCyan = 122006

    LaneCircular = 310000
    LaneLinear = 320000

    SlotCircular = 410000
    SlotLinear = 420000

    JudgeLineCircular = 510000
    JudgeLineLinear = 520000


def customParticleEffect(engineId: int, effectId: int) -> int:
    return 100000 + engineId * 100 + effectId


ParticleDataGroupParticlePropertyExpression = Dict[str, int]

easeTypes = Literal[
    "Linear",
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
]


@dataclass_json
@dataclass
class ParticleDataGroupParticleProperty:
    from_: Optional[ParticleDataGroupParticlePropertyExpression]
    to: Optional[ParticleDataGroupParticlePropertyExpression]
    ease: Optional[Literal[easeTypes]]


@dataclass_json
@dataclass
class ParticleDataGroupParticle:
    sprite: int
    color: str
    start: float
    duration: float
    x: ParticleDataGroupParticleProperty
    y: ParticleDataGroupParticleProperty
    w: ParticleDataGroupParticleProperty
    h: ParticleDataGroupParticleProperty
    r: ParticleDataGroupParticleProperty
    a: ParticleDataGroupParticleProperty


@dataclass_json
@dataclass
class ParticleDataGroup:
    count: int
    particles: List[ParticleDataGroupParticle]


@dataclass_json
@dataclass
class ParticleDataEffect:
    id: ParticleEffect
    transform: Dict
    groups: List[ParticleDataGroup]


@dataclass_json
@dataclass
class ParticleDataSprite:
    x: int
    y: int
    w: int
    h: int


@dataclass_json
@dataclass
class ParticleData:
    width: int
    height: int
    interpolation: bool
    sprites: List[ParticleDataSprite]
    effects: List[ParticleDataEffect]
