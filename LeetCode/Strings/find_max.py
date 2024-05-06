"""
2441. Largest Positive Integer That Exists With Its Negative

"""

from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0 , len(nums) - 1
        while l < r and nums[l] < 0:
            if abs(nums[l]) == nums[r]:
                return nums[r]
            elif abs(nums[l]) > nums[r]:
                l += 1
            else:
                r -= 1

        return -1
    

sol = Solution()
print(sol.findMaxK([4,4]))