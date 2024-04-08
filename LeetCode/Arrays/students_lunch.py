"""
1700. Number of Students Unable to Eat Lunch
"""
from typing import List
from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)
        sandwiches.reverse()

        count = 0
        while students and count <= len(students):
            curr = students.popleft()
            if curr == sandwiches[-1]:
                sandwiches.pop()
                count  = 0
            else:
                students.append(curr)
                count += 1

        return len(students)
    


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]

sol = Solution()
print(sol.countStudents(students,sandwiches))