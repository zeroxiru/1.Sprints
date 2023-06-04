def make_capital(text):
    if not type(text) is str:
        raise Exception("Error, wrong type sent!.")
    return text[0].upper() + text[1:].lower()

try:
    print(make_capital("hello"))
    print(make_capital("Hello"))
    print(make_capital(12))
except Exception as e:
    print(e)
