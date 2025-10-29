import textutils.core as c

def test_full_text_processing_pipeline():
    text = "Mañana compraré 2 cafés y 5 tortas."

    no_accents = c.strip_accents(text)
    # "Manana comprare 2 cafes y 5 tortas."

    final_text = c.replace_numbers(no_accents)
    # "Manana comprare two cafes y five tortas."

    expected = "Manana comprare two cafes y five tortas."
    assert final_text == expected
