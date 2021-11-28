class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def append(self, data):
        node = Node(data)
        if self.head:
            self.tail.next = node
            node.next = self.head
            self.tail = node
            self.size += 1
        else:
            self.head = node
            self.size += 1

    def insert(self, data, position):
        node = Node(data)
        if position == 1:
            node.next = self.head
            self.tail.next = node
            self.head = node
            self.size += 1
            return            
        if self.size > position:
            traverse = self.head
            for i in range(1, position-1):
                traverse = traverse.next
            node.next = traverse.next
            traverse.next = node
            self.size += 1
        if self.size == position:
            self.append(data)
        
    def delete(self, data):
        if data == self.head.data:
            temp = self.head
            self.tail.next = self.head.next
            self.head = self.head.next
            del temp
            self.size -= 1
            return
        if data == self.tail.data:
            traverse = self.head
            temp = self.tail
            while traverse.next != self.tail:
                traverse = traverse.next
            traverse.next = self.head
            traverse = self.tail
            del temp
            self.size -= 1
            return
        traverse = self.head
        next_node = self.head.next
        while next_node != self.tail:
            if next_node.data == data:
                traverse.next = next_node.next
                del next_node
                self.size -= 1
                return
            traverse = traverse.next
            next_node = next_node.next



    def display(self):
        traverse = self.head
        while traverse.next != self.head:
            print(traverse.data, end=' -> ')
            traverse = traverse.next
        print(traverse.data)

obj = CircularLinkedList(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.append(50)
obj.append(60)
obj.display()
obj.insert(5, 1)
obj.delete(40)
# obj.delete(10)
# obj.delete(60)
obj.display()
print('The Head is', obj.head.data)
print('The tail is', obj.tail.data)
print("The Total nodes are: ", obj.size)