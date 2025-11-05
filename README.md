# textutils-4
Small Python packaggit fige for text utilities — group assignment.

# textutils

A small collaborative Python package that provides simple text utilities for text processing, normalization, and frequency analysis.
Installation


# Clone the repository:
git clone https://github.com/morazmariaa-max/textutils-4.git
cd textutils-4


# Create the environment (with micromamba):
micromamba create -f environment.yml -y
micromamba activate textutils


# Install the package in editable mode:
pip install -e .


# Running Tests

To run all tests and check code coverage:
pytest



# Features

is_anagram -> Create anagrams
reverse_words -> reverse words you give to the function
replace_numbers -> Replaces numbers for letters
strip_accents -> Strips the accents of every word in a sentence
count_vowels -> Counts the vowels in a sentence

# Example Usage

from textutils import is_anagram, reverse_words, replace_numbers, strip_accents, count_vowels

text = "Héllo wørld 123"

print(is_anagram("listen", "silent"))
Output: True

print(reverse_words("Hello world"))
Output: "world Hello"

print(replace_numbers("H3ll0"))
Output: "Hello"

print(strip_accents(text))
Output: "Hello world 123"

print(count_vowels("This is a test sentence"))


# Project Structure:
textutils-4/
├── environment.yml
├── pyproject.toml
├── README.md
├── src/
│   └── textutils/
│       ├── __init__.py
│       └── core.py
└── tests/
    ├── integration/
    │   └── test_end_to_end.py
    └── unit/
        └── test_core.py

# Team:
Name	            GitHub Username
Maria Mora	        @morazmariaa-max
Jakob Kohrgruber    @jakobkohr
David Puchala       @davidpprg-hub
Warren Liu          @warrenliu87
Giorgio Fiorentino  @Giorgio-Fiorentino
