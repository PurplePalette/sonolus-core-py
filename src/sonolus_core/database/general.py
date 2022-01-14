from dataclasses import dataclass

from .localization import LocalizationText


@dataclass
class InfoBase:
    name: str
    version: int
    title: LocalizationText
    subtitle: LocalizationText
    author: LocalizationText
