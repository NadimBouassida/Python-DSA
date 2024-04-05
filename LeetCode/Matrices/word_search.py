"""
79. Word Search
"""
from typing import List

# Couldn't find a solution but found one on a video from Neetcode youtube channel
# Link: https://www.youtube.com/watch?v=pfiQ_PS1g8E
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        path = set()
        def dfs(row, col, i):
            if i == len(word):
                return True


            if col >= cols or col < 0 or row >= rows or row < 0 or word[i] != board[row][col] \
            or (row,col) in path or i >= len(word):
                return False
            
            path.add((row,col))
            res =   dfs(row+1, col, i+1) or \
                    dfs(row-1, col, i+1) or \
                    dfs(row, col+1, i+1) or \
                    dfs(row, col-1, i+1)
            path.remove((row,col))

            return  res


        target = word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == target:
                    if dfs(i,j,0):
                        return True
            
        return False
                    
                    



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

sol = Solution()
print(sol.exist(board,word1))
print(sol.exist(board,word2))
print(sol.exist(board,word3))