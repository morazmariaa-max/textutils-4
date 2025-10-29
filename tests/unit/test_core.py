import textutils.core as c

def test_reverse_words():
    text = "Hello World"
    assert c.reverse_words(text) == "olleH dlroW"
    

def test_is_anagram(a,b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    return sorted(a) == sorted(b)


