#
# Description
#
# Submissions
#
# A peak element is an element that is strictly greater than its neighbors.
# Given a 0-indexed integer array nums, find a peak element, and return its index.
# If the array contains multiple peaks, return the index to any of the peaks.
# You may imagine that nums[-1] = nums[n] = -∞.
# In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.
# You must write an algorithm that runs in O(log n) time.
#  
# Example 1:
# Input: nums = [1,2,3,1] Output: 2 Explanation: 3 is a peak element and
# your function should return the index number 2.
# Example 2:
# Input: nums = [1,2,1,3,5,6,4] Output: 5 Explanation:
# Your function can return either index number 1 where the peak element is 2, or
# index number 5 where the peak element is 6.
#  
# Constraints:
#
# 1 <= nums.length <= 1000
#
# -231 <= nums[i] <= 231 - 1
#
# nums[i] != nums[i + 1] for all valid i.

# class Solution():
#     def find_peek_of_neighbors(self, nums: list[int]) -> int:
#         peeks = []
#         for i in range(1, len(nums)-1):
#             if nums[i] > nums[i]-1 and nums[i] > nums[i] + 1:
#                 peeks.append(nums[i])
#         return peeks

# class Solution:
#     def findPeakElement(self, nums: list[int]) -> int:
#         left, right = 0, len(nums) - 1
#         while left < right:
#             mid = (left + right) >> 1
#             if nums[mid] > nums[mid + 1]:
#                 right = mid
#             else:
#                 left = mid + 1
#         return left
#
#
# solution = Solution()
#
# List = [1, 3, 7, 1, 2, 6, 4]
#
#
# result = solution.findPeakElement(List)
# print(result)  # Output: [0, 1]



#class Solution1:
#     def findPeakElement(self, nums):
#         left, right = 0, len(nums) - 1
#
#         while left < right:
#             mid = (left + right) >> 1
#             print(f"Left: {left}, Right: {right}, Mid: {mid}")
#
#             if nums[mid] > nums[mid + 1]:
#                 print(f"Peak is in the left half, updating Right to {mid}")
#                 right = mid
#             else:
#                 print(f"Peak is in the right half, updating Left to {mid + 1}")
#                 left = mid + 1
#
#         print(f"Left: {left}, Right: {right}, Mid: {mid}")
#         return left
#
# solution = Solution1()
# nums = [1, 3, 7, 1, 2, 6, 4]
# result = solution.findPeakElement(nums)
# print(f"Peak element index: {result}")
#

class Solution2:
    def findPeakElement(self, nums:list[int]) -> int:
        left, right = 0, len(nums)-1

        while left < right:

            mid = left + right >> 1
            print(f"Left: {left}, Right: {right}, Mid:{mid}")

            if nums[mid] > nums[mid+1]:
                print(f' Peak is on the left half, update right to mid {mid}')
                right = mid
            else:
                print(f'Peak is on the right half, updating left to {mid + 1}')
                left = mid + 1
        print(f"Left: {left}, Right: {right}, Mid:{mid}")
        return  left

solution = Solution2()
nums = [1, 3, 7, 1, 2, 6, 4]
result = solution.findPeakElement(nums)
print(f"Peak element index: {result}")


class solution3:
    def find_peek_element(self, nums: list[int])-> int:
        peeks = []
        left, right = 0, len(nums)-1

        while left < right:
            mid = left + right >> 1
            print(f"Left:{left}, Right:{right}, Mid:{mid}")

            if nums[mid] > nums[mid + 1]:
                print(f"Peak is on the left half, updating right to Mid:{mid}")
                right = mid
                if not peeks or peeks[-1] != mid:
                    peeks.append(mid)

            else:
                print(f"Peak is on the right half, updating left to Mid:{mid}")
                left = mid + 1

        if left == right and (not peeks or peeks[-1] != left):
            peeks.append(left)

        print(f"Left:{left}, Right:{right}, Mid:{mid}")
        return peeks

solution = solution3()
nums = [1, 3, 7, 1, 2, 6, 4]
result = solution.find_peek_element(nums)
print(f"Peak element index: {result}")


















