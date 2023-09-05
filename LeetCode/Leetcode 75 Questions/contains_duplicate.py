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