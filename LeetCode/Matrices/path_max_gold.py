"""
1219. Path with Maximum Gold
"""

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        def DFS(i, j, vis= set()):
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            
            if (i, j) in vis:
                return 0
            
            if grid[i][j] == 0:
                return 0
            
            vis.add((i,j))

            return grid[i][j] + max(DFS(i+1,j),DFS(i-1,j),DFS(i,j+1),DFS(i,j-1))
        
        res = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    res = max(res, DFS(i,j))

        return res

sol = Solution()
# print(sol.getMaximumGold([[0, 6, 0], [5, 8, 7], [0, 9, 0]]))
# print(sol.getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))
print(sol.getMaximumGold([[1, 0, 7, 0, 0, 0], [2, 0, 6, 0, 1, 0], [3, 5, 6, 7, 4, 2], [4, 3, 1, 0, 2, 0], [3, 0, 5, 0, 20, 0]]))

