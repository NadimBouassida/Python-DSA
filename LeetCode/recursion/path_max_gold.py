"""
1219. Path with Maximum Gold
"""

from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])


        def DFS(i, j,key,vis = set(), cache = {}):
            if (i,j) in cache:
                return cache[i,j]
            if (i, j, key) in vis:
                return 0

            if  i < 0 or i >= n or j < 0 or j >= m:
                return 0

            if grid[i][j] == 0:
                return 0

            vis.add((i,j,key))

            cache[(i,j)] = grid[i][j] + max(DFS(i+1,j,key),DFS(i-1, j,key),DFS(i, j+1,key),DFS(i, j-1,key))

            return cache[(i,j)]

        res = 0
        count = 0
        for i in range(n):
            for j in range(m):
                count += 1
                if grid[i][j] != 0:
                    res = max(res,DFS(i,j,key=count))
        
        return res
        
sol = Solution()
# print(sol.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))
# print(sol.getMaximumGold([[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]))
print(sol.getMaximumGold([[1,0,7,0,0,0],[2,0,6,0,1,0],[3,5,6,7,4,2],[4,3,1,0,2,0],[3,0,5,0,20,0]]))