"""
1614. Maximum Nesting Depth of the Parentheses
"""

class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        count = 0 
        
        for ch in s:
            if ch == '(':
                count += 1
            if ch == ')':
                res = max(res, count)
                count -= 1 
        
        return res




case1 = "(1+(2*3)+((8)/4))+1"
case2 = "(1)+((2))+(((3)))"

sol = Solution()
print(sol.maxDepth(case1))
print(sol.maxDepth(case2))

