from dataclasses import dataclass
from enum import Enum
from typing import List, Literal, Optional

from dataclasses_json import dataclass_json


class OptionName(Enum):
    level_speed = "#SPEED"
    auto_play = "#AUTO"
    mirror_level = "#MIRROR"
    random = "#RANDOM"
    hidden = "#HIDDEN"
    strict_judgment = "#JUDGEMENT_STRICT"
    loose_judgment = "#JUDGEMENT_LOOSE"
    sfx = "#EFFECT"
    stage_visibility = "#STAGE"
    stage_size = "#STAGE_SIZE"
    stage_transparency = "#STAGE_ALPHA"
    stage_tilt = "#STAGE_TILT"
    vertical_stage_cover = "#STAGE_COVER_VERTICAL"
    horizontal_stage_cover = "#STAGE_COVER_HORIZONTAL"
    stage_cover_transparency = "#STAGE_COVER_ALPHA"
    lock_stage_aspect_ratio = "#STAGE_ASPECT_RATIO_LOCK"
    stage_effect = "#STAGE_EFFECT"
    stage_effect_size = "#STAGE_EFFECT_SIZE"
    stage_effect_transparency = "#STAGE_EFFECT_ALPHA"
    lane_visibility = "#LANE"
    lane_size = "#LANE_SIZE"
    lane_transparency = "#LANE_ALPHA"
    lane_effect = "#LANE_EFFECT"
    lane_effect_size = "#LANE_EFFECT_SIZE"
    lane_effect_transparency = "#LANE_EFFECT_ALPHA"
    judgment_line_visibility = "#JUDGELINE"
    judgment_line_size = "#JUDGELINE_SIZE"
    judgment_line_transparency = "#JUDGELINE_ALPHA"
    judgment_line_effect = "#JUDGELINE_EFFECT"
    judgment_line_effect_size = "#JUDGELINE_EFFECT_SIZE"
    judgment_line_effect_transparency = "#JUDGELINE_EFFECT_ALPHA"
    slot_visibility = "#SLOT"
    slot_size = "#SLOT_SIZE"
    slot_transparency = "#SLOT_ALPHA"
    slot_effect = "#SLOT_EFFECT"
    slot_effect_size = "#SLOT_EFFECT_SIZE"
    slot_effect_transparency = "#SLOT_EFFECT_ALPHA"
    note_visibility = "#NOTE"
    note_speed = "#NOTE_SPEED"
    random_note_speed = "#NOTE_SPEED_RANDOM"
    note_size = "#NOTE_SIZE"
    note_transparency = "#NOTE_ALPHA"
    note_effect = "#NOTE_EFFECT"
    note_effect_size = "#NOTE_EFFECT_SIZE"
    note_effect_transparency = "#NOTE_EFFECT_ALPHA"
    marker_visibility = "#MARKER"
    marker_size = "#MARKER_SIZE"
    marker_transparency = "#MARKER_ALPHA"
    connector_visibility = "#CONNECTOR"
    connector_size = "#CONNECTOR_SIZE"
    connector_transparency = "#CONNECTOR_ALPHA"
    simultaneous_line_visibility = "#SIMLINE"
    simultaneous_line_size = "#SIMLINE_SIZE"
    simultaneous_line_transparency = "#SIMLINE_ALPHA"


EngineConfigurationMetric = Literal[
    "arcade", "accuracy", "life", "perfectRate", "errorHeatmap"
]


@dataclass_json
@dataclass
class EngineConfigurationVisibility:
    scale: float
    alpha: float


@dataclass_json
@dataclass
class EngineConfigurationAnimationTween:
    from_: int
    to: int
    duration: int
    ease: str


@dataclass_json
@dataclass
class EngineConfigurationAnimation:
    scale: EngineConfigurationAnimationTween
    alpha: EngineConfigurationAnimationTween


EngineConfigurationJudgmentErrorStyle = Literal[
    "none",
    "plus",
    "minus",
    "arrowUp",
    "arrowDown",
    "arrowLeft",
    "arrowRight",
    "triangleUp",
    "triangleDown",
    "triangleLeft",
    "triangleRight",
]

EngineConfigurationJudgmentErrorPlacement = Literal["both", "left", "right"]


@dataclass_json
@dataclass
class EngineConfigurationUI:
    scope: Optional[str]
    primary_metric: EngineConfigurationMetric
    secondary_metric: EngineConfigurationMetric
    menu_visibility: EngineConfigurationVisibility
    judgment_visibility: EngineConfigurationVisibility
    combo_visibility: EngineConfigurationVisibility
    primary_metric_visibility: EngineConfigurationVisibility
    secondary_metric_visibility: EngineConfigurationVisibility
    judgment_animation: EngineConfigurationAnimation
    combo_animation: EngineConfigurationAnimation
    judgment_error_style: EngineConfigurationJudgmentErrorStyle
    judgment_error_placement: EngineConfigurationJudgmentErrorPlacement
    judgment_error_min: float | int


@dataclass_json
@dataclass
class EngineConfigurationToggleOption:
    name: OptionName
    standard: Optional[bool]
    scope: Optional[str]
    type: Literal["toggle"]
    def_: Literal[0, 1]


@dataclass_json
@dataclass
class EngineConfigurationSliderOption:
    name: OptionName
    standard: Optional[bool]
    scope: Optional[str]
    type: Literal["slider"]
    def_: float
    min: float
    max: float
    step: float
    display: Literal["number", "percentage"]


EngineConfigurationOption = (
    EngineConfigurationSliderOption | EngineConfigurationToggleOption
)


@dataclass_json
@dataclass
class EngineConfiguration:
    options: List[EngineConfigurationOption]
    ui: EngineConfigurationUI
