# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list_to_sllist(lst):
    if not lst:
        return ListNode()
    
    head = ListNode(lst[0])

    if len(lst) == 1:
        return head
    
    cur = head

    for i in range(1,len(lst)):
        cur.next = ListNode(lst[i])
        cur = cur.next

    return head

def print_llist(head):
    while head:
        print(f"{head.val} ->",end=" ")
        head = head.next

