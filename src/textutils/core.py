def count_vowels(text: str) -> int:
    """
    Count the number of vowels (a, e, i, o, u) in the given text.

    Args:
        text (str): The text to analyze.

    Returns:
        int: The number of vowels in the text.
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)