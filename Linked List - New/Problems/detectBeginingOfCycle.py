class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList :
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        node = Node(data)
        if self.head:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = node
            # node.next = self.head.next
        else:
            self.head = node
    
    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.value, end=' -> ')
            traverse = traverse.next
        print('END ')

def lengthCycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            break
    return count

def beginingCycle(head):
    length = 0
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length = lengthCycle(head)
        break
    if length == 0:
        return None
    # Find the starting of cycle
    first = head
    second = head
    for i in range(0, length):
        second = second.next
    while second != first:
        first = first.next
        second = second.next
    return first



obj = LinkedList(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)
obj.display()