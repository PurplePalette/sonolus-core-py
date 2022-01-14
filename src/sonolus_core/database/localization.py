from typing import Dict

LocalizationText = Dict[str, str]


def localize(texts: LocalizationText, locale: str, fallback_locale: str) -> str:
    """
    Localize a text using the given locale.
    If the locale is not found, fallback to the given locale.
    If the fallback locale is not found, return the first element of text.
    """
    if locale in texts:
        return texts[locale]
    elif fallback_locale in texts:
        return texts[fallback_locale]
    else:
        return texts[texts.keys()[0]]
