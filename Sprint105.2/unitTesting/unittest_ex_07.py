def upper_lower(text):
    """
    Checks if a given string contains an occurrence
    of upper case letter followed by lower case letter.
    Returns True if such thing exists, False otherwise.
    """
    # for character in range(1, len(text)):
    #     if text[character].isupper():
    #         if text[character].islower():
    #             return True
    # return False

    for character in range(1, len(text)):
        if text[character].isupper():
            if text[character].islower():
                return True
    return False


