def starts_with_all_index(long, short):
    for position in range(len(short)):
        if long[position] == short[position]:
            return True
    return False


print(starts_with_all_index("Apple", "App"))
print(starts_with_all_index("Manatee", "Mango"))


