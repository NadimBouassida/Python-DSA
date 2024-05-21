"""
1863. Sum of All Subset XOR Totals
"""
from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        dp = [0]
        for i in reversed(range(len(nums))):
            for num in dp.copy():
                dp.append(num ^ nums[i])
        return sum(dp)

sol = Solution()
print(sol.subsetXORSum([5,1,6]))