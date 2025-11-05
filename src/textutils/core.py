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

def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
import textutils.core as c

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring spaces and case).
    Example:
        is_anagram("amor", "roma") -> True
        is_anagram("Listen", "Silent") -> True
    """
    
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)

def is_anagram(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)
