import pytest
from first_substring import first_sub_word

def test_last_character():
    assert first_sub_word('Zohan', 'n') == None

def test_character_not_in_word():
    assert first_sub_word("Ibrahim", "z") == None

def test_word_is_less_Three_character():
    assert first_sub_word("zo", "z") == None

def test_find_sub_string():
    assert first_sub_word("Ibrahim", "h") == "him"

def test_empty_string():
    assert first_sub_word("", "d") == None


