"""
1544. Make The String Great
"""
class Solution:
    def makeGood(self, s: str) -> str:
        res = []
        for ch in s:
            if res and ch.islower() and res[-1] == chr(ord(ch) - 32):
                    res.pop()
        
            elif res and ch.isupper() and res[-1] == chr(ord(ch) + 32):
                    res.pop()
            else:
                res.append(ch)
        
        return ''.join(res)
    

sol = Solution()
print(sol.makeGood("Pp"))