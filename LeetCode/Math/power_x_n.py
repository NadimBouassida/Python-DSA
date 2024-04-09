"""
50. Pow(x, n)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def abs_n_pow(x, n, memo = {}):
            if n in memo:
                return memo[n]
            
            if n == 0:
                return 1

            if n == 1:
                return x

            mid = n // 2
            
            memo[n] = abs_n_pow(x, mid) * abs_n_pow(x, n-mid)

            return memo[n]

        res = abs_n_pow(x, abs(n))
        
        if n >= 0:
            return res
        
        else:
            return 1 / res
        

x_list =  [2.00000,2.10000,2.00000,0.00001]
n_list = [10,3,-2,2147483647]

sol = Solution()

for i in range(len(x_list)):
    print(sol.myPow(x_list[i],n_list[i]))
