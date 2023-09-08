def sum_nums(lo, hi):
    """Returns the sum of the numbers in the range [lo..hi]"""
    assert lo < hi
    my_sum = 0
    for i in range(lo, hi + 1):
        my_sum += i
    return my_sum

print(sum_nums(1, 3))
print(sum_nums(3, 1))

# def sum_of_num(lo, hi):
#     result = 0
#     for i in range(lo, hi +1):
#         result += i
#     return result

