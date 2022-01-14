from dataclasses import dataclass

from ..typings.background import BackgroundItem
from .general import InfoBase


@dataclass
class BackgroundInfo(InfoBase, BackgroundItem):
    pass
