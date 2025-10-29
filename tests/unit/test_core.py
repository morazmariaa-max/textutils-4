import textutils.core as c

def test_reverse_words():
    text = "Hello World"
    assert c.reverse_words(text) == "olleH dlroW"
    