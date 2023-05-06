def starts_with_slicing(long, short):
    if long[0:len(short)] == short:
        return True
    return False


print(starts_with_slicing("Apple", "App"))
print(starts_with_slicing("banana", "ban"))
