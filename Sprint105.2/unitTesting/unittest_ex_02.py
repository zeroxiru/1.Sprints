# Automated Unit Tests with assert

def round6(num):
    """ returns num rounded to nearest int if fractional part is >= .6 """
    return int(num + .4)


result = round6(3.5)
assert result == 3

result = round6(3.6)
assert result == 4

print("All test are passed")

