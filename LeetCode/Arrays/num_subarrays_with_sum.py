"""
930. Binary Subarrays With Sum
"""

# Brut Force Solution time limit exceeded at testcase 54
from collections import deque
from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        nums = deque(nums)
        summ = 0
        res = 0
        while nums:
            fst = nums.popleft()
            summ += fst
            if summ == goal:
                res += 1
            for num in nums:
                summ += num
                if summ == goal:
                    res += 1
                elif summ > goal:
                    break
                    
            summ = 0

        return res
    

sol = Solution()
print(sol.numSubarraysWithSum([0,0,0,0,0],0))
