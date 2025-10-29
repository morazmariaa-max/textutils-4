import textutils.core as c

def test_word_lenghts():
    text = "Hello world"
    assert c.word_lengths(text) == [5, 5]
    