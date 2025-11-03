import pytest
from textutils.core import strip_accents
@pytest.mark.parametrize("inp,exp", [
    ("canción Café mañana Árbol ñandú", "cancion Cafe manana Arbol nandu"),
    ("ÁÉÍÓÚ áéíóú", "AEIOU aeiou"),
    ("", ""),
    (None, ""),
])
