import textutils.core as c

def test_pipeline_strip_accents_then_replace_numbers():
    # End-to-end: remove accents, then replace numbers
    text = "Mañana compraré 2 cafés y 10 tortas."
    no_accents = c.strip_accents(text)
    assert no_accents == "Manana comprare 2 cafes y 10 tortas."

    final_text = c.replace_numbers(no_accents)
    assert final_text == "Manana comprare two cafes y ten tortas."


def test_replace_numbers_preserves_punctuation():
    # Numbers with trailing punctuation should be converted and keep punctuation
    text = "Tengo 3, 7. y 10?"
    out = c.replace_numbers(text)
    assert out == "Tengo three, seven. y ten?"


def test_count_vowels_after_strip_accents():
    # Vowel counting should be accent-insensitive once accents are stripped
    text = "canción Café mañana Árbol ñandú"
    no_accents = c.strip_accents(text)  # "cancion Cafe manana Arbol nandu"
    assert c.count_vowels(no_accents) == 12


def test_is_anagram_ignores_case_and_spaces():
    # Classic anagram checks ignoring case and spaces
    assert c.is_anagram("Listen", "Silent") is True
    assert c.is_anagram("A gentleman", "Elegant man") is True
    assert c.is_anagram("Hello", "Olelh ") is True
    assert c.is_anagram("Hello", "World") is False


def test_reverse_words_after_replacements():
    # Replace numbers first, then reverse each word, keeping word order
    text = "Tengo 2 perros y 5 gatos"
    replaced = c.replace_numbers(text)  # "Tengo two perros y five gatos"
    out = c.reverse_words(replaced)
    # Each token reversed, same positions
    assert out == "ogneT owt sorrep y evif sotag"


def test_full_text_processing_pipeline():
    # A slightly longer integrated flow
    text = "Mañana 0 cafés y 10 tortas."
    # 1) strip accents
    step1 = c.strip_accents(text)         # "Manana 0 cafes y 10 tortas."
    # 2) replace numbers
    step2 = c.replace_numbers(step1)      # "Manana zero cafes y ten tortas."
    # 3) reverse words
    final_text = c.reverse_words(step2)   # reverse each word, keep spaces
    assert final_text == "ananaM orez secaf y net .satrot"
