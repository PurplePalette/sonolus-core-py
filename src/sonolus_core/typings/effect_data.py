from dataclasses import dataclass
from enum import Enum
from typing import List, Literal

from dataclasses_json import dataclass_json

from .general import SRL


class EffectClip(Enum):
    Miss = 0
    Perfect = 1
    Great = 2
    Good = 3
    MissAlternative = 1000
    PerfectAlternative = 1001
    GreatAlternative = 1002
    GoodAlternative = 1003
    Stage = 10000


def customEffectClip(engineId: int, clipId: int) -> int:
    return 100000 + engineId * 100 + clipId


@dataclass_json
@dataclass
class EffectDataSRL(SRL):
    type: Literal["EffectData"]


@dataclass_json
@dataclass
class EffectDataClip:
    id: EffectClip
    clip: EffectDataSRL


@dataclass_json
@dataclass
class EffectData:
    clips: List[EffectDataClip]
