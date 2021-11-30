class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
    
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if self.head:
            traverse = self.head
            while traverse.next != None:
                traverse = traverse.next
            traverse.next = node
        else:
            self.head = Node(data)
    
    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.data, end=' -> ')
            traverse = traverse.next
        print('end')

    def deleteDuplicates(self, head):
        if head:
            node = head
            while node.next != None:
                if node.data == node.next.data:
                    node.next = node.next.next
                else:
                    node = node.next
                
obj = LinkedList()
obj.append(1)
obj.append(1)
obj.append(2)
# obj.append(3)
# obj.append(3)
obj.display()
obj.deleteDuplicates(obj.head)
obj.display()