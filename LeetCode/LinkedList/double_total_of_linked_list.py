"""2816. Double a Number Represented as a Linked List"""

from linked_list_helper import list_to_sllist, ListNode, print_llist


class Solution(object):
    def doubleIt(self, head):
        prv = ListNode()
        prv.next = head
        dummy = prv
        while head:
            head.val *= 2
            if head.val >= 10:
                head.val -= 10
                prv.val += 1

            prv = head
            head = head.next

        return dummy if dummy.val > 0 else dummy.next
    
lst = [9,9,9]
head = list_to_sllist(lst)

sol = Solution()
print_llist(sol.doubleIt(head))