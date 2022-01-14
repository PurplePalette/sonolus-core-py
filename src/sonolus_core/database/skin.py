from dataclasses import dataclass

from ..typings.skin import SkinItem
from .general import InfoBase


@dataclass
class SkinInfo(InfoBase, SkinItem):
    pass
