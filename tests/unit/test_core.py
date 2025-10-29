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

def replace_numbers(text: str) -> str:
    """
    Replace digits with their English word equivalents.
    Example: 'There are 2 apples and 5 oranges.' ->
             'There are two apples and five oranges.'
    """
    num_map = {
        "0": "zero", "1": "one", "2": "two", "3": "three", "4": "four",
        "5": "five", "6": "six", "7": "seven", "8": "eight", "9": "nine"
    }
    result = []
    for ch in text:
        result.append(num_map.get(ch, ch))
    return "".join(result)