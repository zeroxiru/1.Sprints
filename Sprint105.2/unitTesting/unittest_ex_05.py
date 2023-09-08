def avg(nums):
    """Returns the average of the list
    Precondition: List is not empty
    """
    assert len(nums) != 0
    return sum(nums) / len(nums)

print(avg([60, 50, 60]))
#print(avg([]))