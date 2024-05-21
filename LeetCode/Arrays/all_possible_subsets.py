"""
78. Subsets
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]
        for i in range(len(nums)):
            for sub in dp.copy():
                dp.append(sub+[nums[i]])
        return dp
    

sol = Solution()
print(sol.subsets([1,2,3]))