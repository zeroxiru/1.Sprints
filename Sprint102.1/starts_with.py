# Add your function definition here
def starts_with(str1, str2):

    if str1[0] == str2[0]:

        return True
    else:
        return False


# A call like this should return True:
print(starts_with("banana", "bread"))

# And one like this should return False:
print(starts_with("zebonkey", "kiwi"))