import textutils.core as c

def test_reverse_words_basic():
    text = "Hello world"
    expected = "olleH dlrow"
    assert c.reverse_words(text) == expected
