def upper_lower(text):
    """
    Checks if a given string contains an occurrence of upper case letter followed by lower case letter
    Returns True if such thing exists, False otherwise
    """
    for i in range(1, len(text)):
        if text[i].isupper():
            if text[i+1].islower():
                return True
    return False