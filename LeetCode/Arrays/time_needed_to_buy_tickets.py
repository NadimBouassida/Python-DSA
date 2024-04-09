"""
2073. Time Needed to Buy Tickets
"""
from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        for num in tickets:
            if num <= tickets[k]:
                res += num
            else:
                res += tickets[k]

        for num in tickets[k:]:
            if num > tickets[k]:
                res -= 1

        return res

tickets_list = [[84,49,5,24,70,77,87,8],[2,3,2],[5,1,1,1]]
indecies = [3,2,0]

sol = Solution()

for i in range(len(tickets_list)):
    print(sol.timeRequiredToBuy(tickets_list[i], indecies[i]))