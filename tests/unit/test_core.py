import unicodedata

def strip_accents(text: str) -> str:
    """
    Remove accents from characters.
    Example: 'café mañana árbol ñandú' -> 'cafe manana arbol nandu'
    """
    if not text:
        return ""
    normalized = unicodedata.normalize("NFD", text)
    without_accents = "".join(
        ch for ch in normalized if unicodedata.category(ch) != "Mn"
    )
    return unicodedata.normalize("NFC", without_accents)

