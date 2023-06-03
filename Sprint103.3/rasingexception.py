def cal_average(nums):
    if not type(nums) is list:
        raise TypeError("Given in parameter is not list")
    if (len(nums) == 0):
        raise ValueError("Can't calculate average of an empty list!")
    return sum(nums) / len(nums)

try:

    #print(cal_average([2, 4, 10, 19]))
    #print(cal_average([]))
    print(cal_average("bat"))
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)