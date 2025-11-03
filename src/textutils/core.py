def reverse_words(text: str) -> str:
    """
    Reverse each word in the input string, keeping the word order.
    Example:
        'Hello world' -> 'olleH dlrow'
    """

    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)