def replace_numbers(text: str) -> str:
    """
    Replace numbers from 0 to 10 with their English word equivalents.
    Example:
        'Tengo 2 perros y 5 gatos' -> 'Tengo two perros y five gatos'
    """
    num_map = {
        "0": "zero",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "10": "ten"
    }

    words = text.split()
    replaced = []
    for word in words:
        # Si el token es exactamente un número del diccionario
        if word in num_map:
            replaced.append(num_map[word])
        else:
            # Si tiene signos de puntuación (por ejemplo "10," o "3.")
            clean_word = word.strip(".,;:!?")
            if clean_word in num_map:
                new_word = word.replace(clean_word, num_map[clean_word])
                replaced.append(new_word)
            else:
                replaced.append(word)
    return " ".join(replaced)