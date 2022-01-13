import src.sonolus_core.common

LATEST_VERSION = "0.5.9"


class TestVersion(object):
    def test_get_version(self) -> None:
        current_version = src.sonolus_core.common.get_latest_version()
        assert current_version.text == LATEST_VERSION

    def test_version(self) -> None:
        version = src.sonolus_core.common.version
        assert version.text == LATEST_VERSION
