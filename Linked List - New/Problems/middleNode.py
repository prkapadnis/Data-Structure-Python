class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1
    
    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.size += 1

    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.value, end=' -> ')
            traverse = traverse.next
        print(' END')
    
def middleNode(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

obj = LinkedList(10)
obj.append(20)
obj.append(30)
obj.append(40)
# obj.append(50)
obj.display()
print('The Middle node is: ',middleNode(obj.head).value)