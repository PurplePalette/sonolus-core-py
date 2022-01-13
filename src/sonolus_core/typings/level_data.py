from dataclasses import dataclass
from typing import List, Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class LevelDataEntityData:
    index: int
    values: List[int]


@dataclass_json
@dataclass
class LevelDataEntity:
    archetype: int
    data: Optional[LevelDataEntityData]


@dataclass_json
@dataclass
class LevelData:
    entities: List[LevelDataEntity]
