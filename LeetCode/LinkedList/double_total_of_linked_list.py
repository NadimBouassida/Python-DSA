"""2816. Double a Number Represented as a Linked List"""

from linked_list_helper import list_to_sllist, ListNode, print_llist


class Solution(object):
    
    def doubleIt(self, head):
        curr = head 
        if curr.val > 4: 
            head = ListNode(1, head) 
            # ans = ListNode(1, head)
        while curr.next: 
            curr.val = (curr.val * 2 + (curr.next.val > 4)) % 10
            curr = curr.next 
        curr.val = (curr.val * 2) % 10

        return head

lst = [9,9,9]
head = list_to_sllist(lst)

sol = Solution()
print_llist(sol.doubleIt(head))