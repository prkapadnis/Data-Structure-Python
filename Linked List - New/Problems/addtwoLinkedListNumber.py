# Add Two numbers
# https://leetcode.com/problems/add-two-numbers/
# Statement:
#   You are given two non-empty linked lists representing two non-negative integers. The digits are 
#   stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and 
#   return the sum as a linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(head1, head2):
    dummy = ListNode()
    current = dummy
    first = head1
    second = head2
    carry = 0

    while first and second:
        val1 = first.val
        val2 = second.val

        addition = val1 + val2 + carry
        carry = addition // 10
        value = addition % 10
        current.next = ListNode(value)

        current = current.next
        first = first.next
        second = second.next

    while first:
        value = first.val + carry
        carry = value // 10
        value = value % 10
        current.next = ListNode(value)
        current = current.next
        first = first.next

    while second:
        value = second.val + carry
        carry = value // 10
        value = value % 10
        current.next = ListNode(value)
        current = current.next
        second = second.next
    
    if carry :
        current.next = ListNode(carry)
    
    return dummy.next


