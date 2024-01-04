from typing import List
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ops = 0
        for num in counts:
            val_ops = self.val_min_ops(counts[num])
            if val_ops != float('inf'):
                ops += val_ops
            else: 
                return -1            
        return ops


    def val_min_ops(self,n: int,memo = {}) -> int:

        if n == 0:
            memo[n] = 0
            return memo[n] 
        
        if n == 1 or n < 0:
            memo[n] = float('inf')
            return memo[n]

        if n in memo:
            return memo[n]

        memo[n-3] = self.val_min_ops(n-3,memo)
        memo[n-2] = self.val_min_ops(n-2,memo)
        
        ops = 1 + min(memo[n-3], memo[n-2])

        return ops if ops != float('inf') else -1
    

sol = Solution()

print(sol.minOperations([2,3,3,2,2,4,2,3,4]))
print(sol.minOperations([2,1,2,2,3,3]))