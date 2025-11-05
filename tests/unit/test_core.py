import textutils.core as c
from textutils.core import is_anagram

def test_is_anagram_true_cases():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("evil", "vile") is True
    assert is_anagram("amor", "roma") is True
    assert is_anagram("A gentleman", "Elegant man") is True

def test_is_anagram_false_cases():
    assert is_anagram("hello", "world") is False
    assert is_anagram("python", "java") is False
    assert is_anagram("test", "tess") is False

def test_reverse_words_basic():
    text = "Hello world"
    expected = "olleH dlrow"
    assert c.reverse_words(text) == expected

def test_reverse_words_with_punctuation():
    text = "Good morning!"
    expected = "dooG !gninrom"
    assert c.reverse_words(text) == expected

def test_reverse_words_mixed_case():
    text = "Open the Door"
    expected = "nepO eht rooD"
    assert c.reverse_words(text) == expected

def test_strip_accents_basic():
    text = "canción Café mañana Árbol ñandú"
    expected = "cancion Cafe manana Arbol nandu"
    assert c.strip_accents(text) == expected

def test_count_vowels():
    text = "HELLO world"
    assert c.count_vowels(text) == 3

def test_replace_numbers_basic():
    text = "Tengo 2 perros y 5 gatos"
    expected = "Tengo two perros y five gatos"
    assert c.replace_numbers(text) == expected

def test_replace_numbers_mixed():
    text = "Compré 1 manzana, 3 peras y 10 plátanos"
    expected = "Compré one manzana, three peras y ten plátanos"
    assert c.replace_numbers(text) == expected


