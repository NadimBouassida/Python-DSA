"""
79. Word Search
"""
from typing import List
from collections import defaultdict

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_length = len(board)
        column_length = len(board[0])

        board_map = defaultdict(list)

        for i in range(row_length):
            for j in range(column_length):
                board_map[board[i][j]].append((i,j))

        word_indecies = []

        for letter in word:
            if letter in board_map:
                word_indecies.append(board_map[letter])
            else: 
                return False

        for index, coordinates_list in enumerate(word_indecies):
            if index + 1 < len(word_indecies):
                possibly_exists = False
                for coordinate in coordinates_list:
                    adjacent_left = coordinate[0], coordinate[1] - 1
                    adjacent_right = coordinate[0] , coordinate[1] + 1
                    adjacent_bottom =  coordinate[0] + 1 , coordinate[1] 
                    adjacent_top = coordinate[0] - 1, coordinate[1]
                    current_words = word_indecies[index + 1]
                    for current_word in current_words:
                        if current_word in (adjacent_left,adjacent_right,adjacent_bottom,adjacent_top):
                            possibly_exists = True
                            break
                if not possibly_exists:
                    return False
                    
        return True            

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
word2 = "SEE"
word3 = "ABCB"

sol = Solution()
print(sol.exist(board,word3))