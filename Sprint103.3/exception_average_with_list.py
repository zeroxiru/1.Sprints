def average(nums):
    if not type(nums) is list:
        raise TypeError("Given parameter is not a list!")
    if len(nums) == 0:
        raise ValueError("Cannot calculate the average of an empty list")
    return sum(nums) / len(nums)
try:
   # print(average([]))
   # print(average("cat"))
    print(average([2, 3, 44, 34, 333]))
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
