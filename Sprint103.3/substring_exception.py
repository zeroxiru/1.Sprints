def is_substring(small, big):
    if small == "" or big == "":
        raise Exception("Error! empty string found")
    return small in big

try:
    print(is_substring('', 'hello'))
    print(is_substring('he', 'hello'))
except Exception as e:
    print(e)