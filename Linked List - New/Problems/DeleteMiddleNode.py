class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
    
    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
    
    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.value, end=' -> ')
            traverse = traverse.next
        print(' END')

def deleteMiddle(head):
    if head and not head.next:
        return None
    slow = head
    fast = head
    back = slow
    while fast and fast.next:
        back = slow
        slow = slow.next
        fast = fast.next.next
    
    back.next = slow.next
    del slow



obj = LinkedList(1)
# obj.append(2)
# obj.append(3)
# obj.append(4)
# obj.append(5)
# obj.append(6)
obj.display()
deleteMiddle(obj.head)
obj.display()
