# Add Two Linked List Number -II
# https://leetcode.com/problems/add-two-numbers-ii/
# You are given two non-empty linked lists representing two non-negative integers. The most significant 
# digit comes first and each of their nodes contains a single digit. Add the two numbers and return the 
# sum as a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    previous = None
    current = head
    nextnode = current.next

    while current:
        current.next = previous 
        previous = current
        current = nextnode
        if nextnode:
            nextnode = nextnode.next
    head = previous
    return head

def addTwoNumbers(l1, l2):
    first = reverse(l1)
    second = reverse(l2)
    dummy = ListNode()
    current = dummy
    carry = 0
    
    while first or second or carry:
        val1 = first.val if first else 0
        val2 = second.val if second else 0

        value = val1 + val2 + carry
        carry = carry // 10
        value = value % 10
        current.next = ListNode(value)

        current = current.next
        first = first.next if first else None
        second = second.next if second else None

    return reverse(dummy.next)