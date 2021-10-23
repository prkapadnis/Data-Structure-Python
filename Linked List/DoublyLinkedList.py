class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, data) -> None:
        self.head = Node(data)
    
    def append(self, data):
        """
            It appends the node in linked list at the end
        """
        node = Node(data)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
            
        else:
            self.head = Node(data)

    def insert(self, data, position):
        """
            It insert the element at given position
        """
        node = Node(data)
        current = self.head
        temp = self.head.next
        index = 1
        while index != position - 1:
            temp = temp.next
            current = current.next
            index += 1
        current.next = node
        node.prev = current
        node.next = temp
        temp.prev = node


    def display(self):
        """
            It displays the linked list
        """
        current = self.head
        while current:
            print(current.data , end=" ")
            current = current.next
        print()

list = LinkedList(10)
list.append(20)
list.append(30)
list.append(40)
list.display()
list.insert(25, 3)
list.display()