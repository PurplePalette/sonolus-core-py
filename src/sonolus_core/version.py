import re
from dataclasses import dataclass

import requests

from .exceptions import ParseVersionException


@dataclass
class Version:
    """parsed semantic versioning object"""

    major: int
    minor: int
    patch: int
    text: str


def get_latest_version() -> Version:
    try:
        page = requests.get("https://sonolus.com").text
    except requests.exceptions.RequestException as e:
        raise e
    versionRegex = re.search(r"([0-9]\.){2}[0-9]", page)
    if versionRegex is None:
        raise ParseVersionException()
    versionText: str = versionRegex.group()
    versionNumbers = list(map(int, versionText.split(".")))
    semanticVersion = Version(
        versionNumbers[0], versionNumbers[1], versionNumbers[2], versionText
    )
    return semanticVersion


current_version = get_latest_version()
