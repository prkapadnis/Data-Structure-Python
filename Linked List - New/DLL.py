class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None

class DoublyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def append(self, data):
        node = Node(data)
        if self.head:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = node
            node.previous = traverse
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.tail = node
            self.size += 1
    
    def insert(self, data, position):
        if position == 1:
            node = Node(data)
            node.next = self.head
            self.head.previous = node
            self.head = node
            return
        if self.size > position:
            node = Node(data)
            current = self.head
            for i in range(1, position-1):
                current = current.next
            node.next = current.next
            node.previous = current
            current.next.previous = node
            current.next = node
            self.size += 1

    def delete(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            self.head.previous = None
            del temp
            self.size -= 1
            return
        traverse = self.head
        while traverse:
            if data == traverse.data:
                temp = traverse
                temp.next.previous = temp.previous
                temp.previous.next = temp.next
                del temp
                self.size -= 1
                return
            traverse = traverse.next


    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.data, end=" -> ")
            traverse = traverse.next
        print("Null")
    
    def display_rev(self):
        traverse = self.tail
        while traverse:
            print(traverse.data, end=' <- ')
            traverse = traverse.previous
        print('Null')



obj = DoublyLinkedList(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)
obj.insert(25, 2)
obj.display()
obj.delete(10)
obj.display()
# obj.display_rev()
print('The head is ', obj.head.data)
print('Total number of node: ', obj.size)