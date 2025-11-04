import textutils.core as c

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
