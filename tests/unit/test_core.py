import textutils.core as c
def test_count_vowels():
    text = "David likes beer."
    assert c.count_vowels(text) == 6