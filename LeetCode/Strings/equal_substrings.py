'''
1208. Get Equal Substrings Within Budget
'''

class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        diffs = [0] * n
        for i in range(n):
            diff = abs(ord(s[i]) - ord(t[i]))
            diffs[i] = diff

        res = 0
        l = 0
        total = 0
        sub_len = 0
        for r in range(n):
            total += diffs[r]
            sub_len += 1
            if total <= maxCost:
                res = max(res,sub_len)
            else: 
                total -= diffs[l]
                sub_len -= 1
                l += 1

        return res


    
sol = Solution()
print(sol.equalSubstring("krrgw","zjxss",19))