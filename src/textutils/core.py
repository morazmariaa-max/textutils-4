def reverse_words(text: str) -> str:
    """
    Reverse each word in the input string, keeping the word order.
    Example:
        'Hello world' -> 'olleH dlrow'
    """

    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

def strip_accents(text):
    """
    Remove accents from the input string.
    Example: 'canción Café mañana Árbol ñandú' -> 'cancion Cafe manana Arbol nandu'
    """
    # Normaliza el texto (descompone letras y acentos)
    normalized = unicodedata.normalize('NFD', text)
    # Elimina los caracteres diacríticos (acentos, tildes, etc.)
    return ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')

