from textutils.core import is_anagram

<<<<<<< HEAD
def test_reverse_words_basic():
    text = "Hello world"
    expected = "olleH dlrow"
    assert c.reverse_words(text) == expected
=======
def test_is_anagram_true_cases():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("evil", "vile") is True
    assert is_anagram("amor", "roma") is True
    assert is_anagram("A gentleman", "Elegant man") is True

def test_is_anagram_false_cases():
    assert is_anagram("hello", "world") is False
    assert is_anagram("python", "java") is False
    assert is_anagram("test", "tess") is False
>>>>>>> 3d8e4aa (changed code in test_core)

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
