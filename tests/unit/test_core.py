import textutils.core as c

def test_replace_numbers_basic():
    text = "Tengo 2 perros y 5 gatos"
    expected = "Tengo two perros y five gatos"
    assert c.replace_numbers(text) == expected

def test_replace_numbers_mixed():
    text = "Compré 1 manzana, 3 peras y 10 plátanos"
    expected = "Compré one manzana, three peras y ten plátanos"
    assert c.replace_numbers(text) == expected