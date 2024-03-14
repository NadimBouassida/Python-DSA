"""
1171. Remove Zero Sum Consecutive Nodes from Linked List
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        currSum = 0
        d = {}
        d[currSum] = dummy
        while head:
            currSum += head.val
            if currSum in d:
                d[currSum].next = head.next
            else:
                d[currSum] = head

            head = head.next

        return dummy.next

my_list = [1,3,2,-3,-2,5,5,-5,1]


def list_to_linked(nodes_list):
    head = ListNode(val=nodes_list[0])
    curr = head
    for i in range(1,len(nodes_list)):
        curr.next = ListNode(val = nodes_list[i])
        curr = curr.next
    return head
    
head = list_to_linked(my_list)

def linked_to_list(lnk_list):
    head = lnk_list
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

s = Solution()
print(linked_to_list(s.removeZeroSumSublists(head)))