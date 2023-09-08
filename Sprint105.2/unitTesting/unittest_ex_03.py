
#The function second_occurrence gets a
# a list and an item, and returns the index of the second occurrence of the item. If not found, it returns None.
def second_occurance(lst_items, item):
    first_found = False
    index_found = None
    for i in range(1, len(lst_items)):
        if lst_items[i] == item:
            if first_found:
                index_found = i
            else:
                first_found = True
    return index_found