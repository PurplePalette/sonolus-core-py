from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional, Union

from dataclasses_json import dataclass_json


class SkinSprite(Enum):
    NoteHeadNeutral = 1000
    NoteHeadRed = 1001
    NoteHeadGreen = 1002
    NoteHeadBlue = 1003
    NoteHeadYellow = 1004
    NoteHeadPurple = 1005
    NoteHeadCyan = 1006

    NoteTickNeutral = 2000
    NoteTickRed = 2001
    NoteTickGreen = 2002
    NoteTickBlue = 2003
    NoteTickYellow = 2004
    NoteTickPurple = 2005
    NoteTickCyan = 2006

    NoteTailNeutral = 3000
    NoteTailRed = 3001
    NoteTailGreen = 3002
    NoteTailBlue = 3003
    NoteTailYellow = 3004
    NoteTailPurple = 3005
    NoteTailCyan = 3006

    NoteConnectionNeutral = 11000
    NoteConnectionRed = 11001
    NoteConnectionGreen = 11002
    NoteConnectionBlue = 11003
    NoteConnectionYellow = 11004
    NoteConnectionPurple = 11005
    NoteConnectionCyan = 11006

    NoteConnectionNeutralSeamless = 11100
    NoteConnectionRedSeamless = 11101
    NoteConnectionGreenSeamless = 11102
    NoteConnectionBlueSeamless = 11103
    NoteConnectionYellowSeamless = 11104
    NoteConnectionPurpleSeamless = 11105
    NoteConnectionCyanSeamless = 11106

    SimultaneousConnectionNeutral = 12000
    SimultaneousConnectionRed = 12001
    SimultaneousConnectionGreen = 12002
    SimultaneousConnectionBlue = 12003
    SimultaneousConnectionYellow = 12004
    SimultaneousConnectionPurple = 12005
    SimultaneousConnectionCyan = 12006

    SimultaneousConnectionNeutralSeamless = 12100
    SimultaneousConnectionRedSeamless = 12101
    SimultaneousConnectionGreenSeamless = 12102
    SimultaneousConnectionBlueSeamless = 12103
    SimultaneousConnectionYellowSeamless = 12104
    SimultaneousConnectionPurpleSeamless = 12105
    SimultaneousConnectionCyanSeamless = 12106

    DirectionalMarkerNeutral = 21000
    DirectionalMarkerRed = 21001
    DirectionalMarkerGreen = 21002
    DirectionalMarkerBlue = 21003
    DirectionalMarkerYellow = 21004
    DirectionalMarkerPurple = 21005
    DirectionalMarkerCyan = 21006

    SimultaneousMarkerNeutral = 22000
    SimultaneousMarkerRed = 22001
    SimultaneousMarkerGreen = 22002
    SimultaneousMarkerBlue = 22003
    SimultaneousMarkerYellow = 22004
    SimultaneousMarkerPurple = 22005
    SimultaneousMarkerCyan = 22006

    StageMiddle = 40000

    StageLeftBorder = 40001
    StageRightBorder = 40002
    StageTopBorder = 40004
    StageBottomBorder = 40008

    StageTopLeftCorner = 40005
    StageTopRightCorner = 40006
    StageBottomLeftCorner = 40009
    StageBottomRightCorner = 40010

    Lane = 40100
    LaneSeamless = 40110

    LaneAlternative = 40200
    LaneAlternativeSeamless = 40210

    JudgmentLine = 41000
    NoteSlot = 41001

    StageCover = 42000


def customSkinSprite(engineId: int, spriteId: int) -> int:
    return 100000 + engineId * 100 + spriteId


SkinDataExpression = Optional[Dict[Union[str, int], int]]

SkinDataTransform = Dict[Union[str, int], SkinDataExpression]


@dataclass_json
@dataclass
class SkinDataSprite:
    id: SkinSprite
    x: int
    y: int
    w: int
    h: int
    transform: SkinDataTransform


@dataclass_json
@dataclass
class SkinData:
    width: int
    height: int
    interpolation: bool
    sprites: List[SkinDataSprite]
