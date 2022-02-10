# Linked List Cycle
# Slow and Fast Pointer

def hasCycle(head):
    slow = head
    fast = head
    while fast != None and slow != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


def cycleLength(head):
    slow = head
    fast = head
    while fast != None and slow != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                length += 1
            return length
