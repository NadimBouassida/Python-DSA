"""
"486. Predict the Winner":
You are given an integer array nums. Two players are playing a game with this array: player 1 and player 2.

Player 1 and player 2 take turns, with player 1 starting first. Both players start the game with a score of 0.
At each turn, the player takes one of the numbers from either end of the array (i.e., nums[0] or nums[nums.length - 1])
which reduces the size of the array by 1. The player adds the chosen number to their score.
The game ends when there are no more elements in the array.

Return true if Player 1 can win the game. If the scores of both players are equal, then player 1 is still the winner, 
and you should also return true. You may assume that both players are playing optimally.

"""


from collections import deque


def PredictTheWinner(nums) -> bool:
    deq = deque(nums)
    pl1 = 0 # set player 1 score to zero initially
    pl2 = 0 # set player 2 score to zero initially
    turn = True # Used to track turns True means player 1's turn False means player 2's turn
    while deq:
        l = deq[0]
        r = deq[-1]
        if turn:
            if l >= r:
                pl1 += deq.popleft()
            else: 
                pl1 += deq.pop()
        else:
            if l >= r:
                pl2 += deq.popleft()
            else: 
                pl2 += deq.pop()
                
        turn = not turn

    return True if pl1 >= pl2 else False
    
PredictTheWinner([1,5,233,7])