import textutils.core as c

def replace_numbers():
    input_text = "There are 2 apples and 5 oranges."
    expected_output = "There are two apples and five oranges."
    assert c.replace_numbers(input_text) == expected_output