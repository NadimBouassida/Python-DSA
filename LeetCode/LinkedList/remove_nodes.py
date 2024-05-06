"""
2487. Remove Nodes From Linked List
"""

from linked_list_helper import list_to_sllist, print_llist, ListNode

def delete_nodes(head):
    nodes_list = []
    cur = head
    while cur:
        nodes_list.append(cur.val)
        cur = cur.next

    mx = nodes_list[-1]
    for i in range(len(nodes_list)-1,-1,-1):
        if nodes_list[i] < mx:
            nodes_list.pop(i)
        mx = max(mx,nodes_list[i])


    head = ListNode(nodes_list[0])
    if len(nodes_list) == 1:
        return head

    cur = head

    for i in range(1,len(nodes_list)):
        cur.next = ListNode(nodes_list[i])
        cur = cur.next

    return head

head = list_to_sllist([5,2,13,3,8])
print_llist(delete_nodes(head))




