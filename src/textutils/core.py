import textutils.core as c
from textutils.core import is_anagram
import unicodedata

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
def replace_numbers(text: str) -> str:
    """
    Replace numbers from 0 to 10 with their English word equivalents.
    Example:
        'Tengo 2 perros y 5 gatos' -> 'Tengo two perros y five gatos'
    """
    num_map = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten"
    }

    words = text.split()
    replaced = []
    for word in words:
        # Si el token es exactamente un número del diccionario
        if word in num_map:
            replaced.append(num_map[word])
        else:
            # Si tiene signos de puntuación (por ejemplo "10," o "3.")
            clean_word = word.strip(".,;:!?")
            if clean_word in num_map:
                new_word = word.replace(clean_word, num_map[clean_word])
                replaced.append(new_word)
            else:
                replaced.append(word)
    return " ".join(replaced)
