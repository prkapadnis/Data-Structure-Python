# Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
# statement
#   Given the head of the first level of the list, flatten the list so that all the nodes appear in a 
#   single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list 
#   should appear after curr and before curr.next in the flattened list.
#   Return the head of the flattened list. The nodes in the list must have all of their child pointers 
#   set to null.

def flatten(head):
    if head:
        return flatten_rec(head)
    return head

def flatten_rec(head):
    current = head
    tail = head
    while current:
        nextnode = current.next
        child = current.child
        if child:
            child_tail = flatten_rec(child)
            child_tail.next = nextnode
            if nextnode:
                nextnode.prev = child_tail
            current.next = child
            child.prev = current
            current.child = None
        else:
            current = nextnode
            if current:
                tail = current
    return tail