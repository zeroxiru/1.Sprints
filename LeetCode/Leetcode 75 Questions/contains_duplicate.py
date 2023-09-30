# Given an integer array nums, return true if any value
# appears at least twice in the array, and return false if every element is distinct.
#
# Example
# 1:
#
# Input: nums = [1, 2, 3, 1]
# Output: true
# Example
# 2:
#
# Input: nums = [1, 2, 3, 4]
# Output: false
# Example
# 3:
#
# Input: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
# Output: true
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Accepted
# 3.1
# M
# Submissions
# 5.1
# M
# Acceptance
# Rate
# 61.0 %
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        exist_num = set ()
        for number in nums:
            if number in exist_num:
                return True
            else:
                exist_num.add(number)
        return False

solution = Solution()

List = [2, 7, 11, 11, 15]


result = solution.containsDuplicate(List)
print(result)  # Output: [0, 1]


class Solution2():

    def find_duplicate(self, nums: list[int]) -> bool:
        num_exists_in_list = []

        for i in nums:
            if i in num_exists_in_list:
                return True
            num_exists_in_list.append(i)
        return False


solution = Solution2()

List = [2, 7, 11, 11, 15]


result = solution.find_duplicate(List)
print(result)  # Output: [0, 1]


class Solution3():
    def find_similar_number(self, nums: list[int]) -> bool:

        exists_num = set()
        for num in nums:
            if num in exists_num:
                return True
            else:
                exists_num.add(num)
        return False

solution = Solution3()

List = [2, 7, 11, 15]


result = solution.find_similar_number(List)
print(result)  # Output: [0, 1]


class Soluiton4():

    def find_duplicates(self, nums: list[int]) -> bool:
        exists_num = []
        for number in nums:
            if number in exists_num:
                return True
            else:
                exists_num.append(number)
        return False


solution = Soluiton4()

List = [2, 7, 11, 15]


result = solution.find_duplicates(List)
print(result)  # Output: [0, 1]


class Solution5():
    def find_same_number(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,  (len(nums))):
                if nums[i]== nums[j]:
                    return True
            return False


solution = Solution5()

List = [2, 7, 2, 11, 15]


result = solution.find_same_number(List)
print(result)  # Output: [0, 1]




