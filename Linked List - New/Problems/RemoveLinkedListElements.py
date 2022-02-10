# Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

def removeElements(head, val):
    # checking head is None or not if it is none then return None
    if not head:
        return None
    
    # checking if head.val is equal to val if it is equal then move head to next node
    while head and head.val == val:
        head = head.next
    traverse = head
    
    while traverse and traverse.next:
        if traverse.next.val == val:
            traverse.next = traverse.next.next
        else:
            traverse = traverse.next
    return head

