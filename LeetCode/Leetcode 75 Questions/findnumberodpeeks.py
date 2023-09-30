class Solution:
    def findPeakElements(self, nums):
        peaks = []  # Store the indices of all peak elements

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) >> 1

            if nums[mid] > nums[mid + 1]:
                # Peak found in the left half, update right and add the index to peaks
                right = mid
                if not peaks or peaks[-1] != mid:  # Check if the same index was already added
                    peaks.append(mid)
            else:
                # Peak found in the right half, update left
                left = mid + 1

        # Check if the last element is a peak (it's always a peak if it's in the range)
        if left == right and (not peaks or peaks[-1] != left):  # Check if the same index was already added
            peaks.append(left)

        return peaks

solution = Solution()
nums = [1, 3, 7, 1, 2, 6, 4]
result = solution.findPeakElements(nums)
print(f"Peak element indices: {result}")
