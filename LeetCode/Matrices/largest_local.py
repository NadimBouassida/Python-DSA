"""
2373. Largest Local Values in a Matrix
"""
from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = []
        for i in range(2,n):
            row = []
            for j in range(2,n):
                grid3x3 = [
                    grid[i-2][j-2],
                    grid[i-2][j-1],
                    grid[i-2][j],
                    grid[i-1][j-2],
                    grid[i-1][j-1],
                    grid[i-1][j],
                    grid[i][j-2],
                    grid[i][j-1],
                    grid[i][j],
                ]
                row.append(max(grid3x3))
            res += [row]

        return res
    

sol = Solution()
sol.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])