def avg(nums):
    assert len(nums) != 0, "List is empty!"
    return sum(nums) / len(nums)

numbers = [1,2, 3, 4]
print(avg(numbers))
#print([])


# 1.Write a function called add10 that adds 10 to a given number and returns the new number.
# If the function receives a parameter that is not int, it will use assert to stop the program.


def add10(num):

    assert type(num) == int, 'Parameter value must be intger'
    add_10 = 10
    return num + add_10

print(add10(20))
#print(add10('as'))

# 2. Write a function called add_txt that adds the extension “.txt” to a
# filename and returns the new filename. Add assertions that
# the variable given is a string, and that it is not empty. Add error messages to your assertions.

def add_text(file_path):

    file_extension = ".txt"
    assert type(file_path) == str,  "variable should string"
    assert  file_path  != '', "file Name cannot be empty"
    return file_path + file_extension

print(add_text("user_info"))



def round6(num):
    """returns num rounded to nearest int if fractional part is >= .6"""
    return int(num + .4)

# ---- automated unit test ----

result = round6(3.5)
if result == 3:
    print("Test 1: PASS")
else:
    print("Test 1: FAIL")

result = round6(3.6)
if result == 4:
    print("Test 2: PASS")
else:
    print("Test 2: FAIL")


def round6(num):
    return num + .4

result = round6(3.5)
if result == 3:
    print("pass")
else:
    print("Failed")

result = round6(3.6)
if result == 4:
    print("Pass")
else:
    print("Failed")

round6(5.0)


