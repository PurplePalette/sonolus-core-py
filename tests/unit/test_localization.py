from src.sonolus_core.database import LocalizationText, localize


class TestLocalization:
    def test_localize_with_specify_lang(self) -> None:
        texts: LocalizationText = {"en": "chino", "ja": "チノ"}
        localized_text = localize(texts, "en", "ja")
        assert localized_text == "chino"

    def test_localize_with_undefined_locale(self) -> None:
        texts: LocalizationText = {"ja": "チノ"}
        localized_text = localize(texts, "en", "ja")
        assert localized_text == "チノ"

    def test_localize_with_undefined_fallback(self) -> None:
        texts: LocalizationText = {"ja": "チノ"}
        localized_text = localize(texts, "en", "en")
        assert localized_text == "チノ"
