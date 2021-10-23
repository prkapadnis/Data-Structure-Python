class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.top = Node(data)

    def insert(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node

    def delete(self):
        elementTodel = self.top
        if self.top:
            self.top = self.top.next
            elementTodel.next = None
            return elementTodel.data
        else:
            return "Stack is UnderFlow!!!"

    def display(self):
        traverse = self.top
        if traverse:
            while traverse:
                print(traverse.data)
                traverse = traverse.next
            print()
        else:
            print("Stack is Empty!!!")

class Stack:
    def __init__(self, data):
        self.list = LinkedList(data)

    def push(self, element):
        self.list.insert(element)
    
    def pop(self):
        return self.list.delete()
    
    def display(self):
        self.list.display()

s1 = Stack(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.display()
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print(s1.pop())
print()
s1.display()