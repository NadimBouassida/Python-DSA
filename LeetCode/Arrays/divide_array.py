"""
2966. Divide Array Into Arrays With Max Difference
"""
from typing import List

class Solution:
    def divide_array(self, nums: List[int], k: int) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        answer = []
        prev = 0
        for i in range(3,len(nums),3):
            answer.append(nums[prev:i])
            prev = i
        answer.append(nums[-3:])

        for ans in answer:
            for i in range(len(ans)-1):
                for j in range(i,len(ans)):
                    if ans[j] - ans [i] > k:
                        return [] 

        return answer 

s = Solution()
print(s.divide_array([1,3,4,8,7,9,3,5,1],2))