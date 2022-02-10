# Swapping Nodes in linked list
# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
# Statement:
    # You are given the head  of the list and integer value K, return the head after swapping kth node from the
    # begining and kth node from the ending.

def swapNodes(head, k):
    front = head
    right = head
    left = head
#   Move right by k times and front by k-1 times
#   At this point the front is at the kth node from begining
    for i in range(k):
        right = right.next
        if i < k-1:
            front = front.next
#   move right and left until right reaches to None
    while right:
        right = right.next
        left = left.next
#   At this point Left is at the kth node from last and right goes to None
#   We got the kth node from begining and kth node from the ending then swap the values
    # swap
    front.val, left.val = left.val, front.val
    return head


def secondApproch(head, k):
    p1 = head
    p2 = head
    p3 = head

    while p1.next:
        if k != 1:
            p3 = p3.next
            k -= 1
        else:
            p2 = p2.next
        p1 = p1.next
    
    p3.val , p2.val = p2.val, p3.val