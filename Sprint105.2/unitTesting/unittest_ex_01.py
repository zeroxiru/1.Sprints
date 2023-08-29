def round6(num):
    """ returns num rounded to nearest int if fractional part is >= .6 """
    return int(num + .4)


# ---- automated unit test------

result = round(3.5)
if result == 3:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

result = round(3.6)
if result == 4:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")
    