import textutils.core as c

def is_anagram(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams (ignoring spaces and case).
    Example:
        is_anagram("amor", "roma") -> True
        is_anagram("Listen", "Silent") -> True
    """
    
    s1 = str1.replace(" ", "").lower()
    s2 = str2.replace(" ", "").lower()

    return sorted(s1) == sorted(s2)