import requests
import re
from .exceptions import ParseVersionException
from dataclasses import dataclass


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
    except requests.exceptions.httperror as e:
        raise e
    versionText = re.search(r"([0-9]\.){2}[0-9]", page)
    if versionText is None:
        raise ParseVersionException()
    versionText = versionText.group()
    versionNumbers = list(map(int, versionText.split(".")))
    semanticVersion = Version(
        versionNumbers[0], versionNumbers[1], versionNumbers[2], versionText
    )
    return semanticVersion


version = get_latest_version()
