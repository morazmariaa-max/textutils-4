import textutils.core as c

def test_strip_accents_basic():
    text = "canción Café mañana Árbol ñandú"
    expected = "cancion Cafe manana Arbol nandu"
    assert c.strip_accents(text) == expected
