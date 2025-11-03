from textutils.core import is_anagram

def test_is_anagram_true_cases():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("evil", "vile") is True
    assert is_anagram("amor", "roma") is True
    assert is_anagram("A gentleman", "Elegant man") is True

def test_is_anagram_false_cases():
    assert is_anagram("hello", "world") is False
    assert is_anagram("python", "java") is False
    assert is_anagram("test", "tess") is False

