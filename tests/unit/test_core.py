import textutils.core as c

def test_is_anagram(a,b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)

def test_count_vowels():
    text = "David likes beer."
    assert c.count_vowels(text) == 6

def test_strip_accents_basic():
    text = "canción Café mañana Árbol ñandú"
    assert strip_accents(text) == "cancion Cafe manana Arbol nandu"
