from pathlib import Path

from single_source import get_version

from .version import get_latest_version, version

__version__ = get_version(__name__, Path(__file__).parent.parent.parent)

__all__ = [
    "get_latest_version",
    "version",
]
