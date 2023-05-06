def validate_number(number):
    # check the length of the number.
    if not 6 <= len(number) <= 11:
        return False
    # check all the allowed characters are available in the number.
    allowed_characters = set("0123456789-+")
    if not all (char in allowed_characters for char in number):
        return False
    # checking the placement of "-" and "+" sign
    if number.count("-") != 1 and number.count("+") > 1 or (number.count("+") == 1 and number[0] != "+"):
        return False
    # checking if there are digits between the hyphen and plus sign (if present)
    if '_' in number and not number.split("-")[1].isdigit():
        return False
    return True



validate_number("123224343234248")



