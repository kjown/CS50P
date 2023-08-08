import pytest
from twttr import shorten

def test_lowercase_vowel():
    assert shorten("aeiou") == ""

def test_capitalized_vowel():
    assert shorten("AEIOU") == ""

def test_number():
    assert shorten("1") == "1"

def test_capitalized_consonant():
    assert shorten("B") == "B"

def test_lowercase_consonant():
    assert shorten("b") == "b"

def test_punctuation():
    assert shorten(".") == "."