import pytest

def get_n_word(text, n):
    """
    This function gets string and a number (n). It should
    return the N word from the text. For example, given the
    sentence "Hello dear world" and n=3, it should return `world`
    as it is the third word.
    If there is a problem with input types, raises a TypeError.
    If there is any other problem, return ValueError.
    """
    if not isinstance(text, str) or not isinstance(n, int):
        raise TypeError(" Input must be string and integer")

    words = text.split()
    if n < 1 or n > len(words):
        raise ValueError("Invalid value for n")

    return words[n - 1]

def test_normal1():
    assert get_n_word("Hello dear world", 3)

def test_empty_text():
    with pytest.raises(ValueError):
        get_n_word('', 1)

def test_integer_zero():
    with pytest.raises(ValueError):
        get_n_word("Hello dear world", 0)

def test_exceed_words():
    with pytest.raises(ValueError):
     get_n_word("Hello dear world", 5)


