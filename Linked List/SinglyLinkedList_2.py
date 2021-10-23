class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        """
        Appends the new node at the end of the list
        """
        node = Node(data)
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = node
        else :
            self.head = node

    def insert(self, node, position):
        """
            Inserting a new Node at givern Position        
        """
        traverse = self.head
        index = 1
        if position == 1:
            node.next = self.head
            self.head = node
        else:
            while index != position - 1:
                traverse = traverse.next
                index += 1
            node.next = traverse.next
            traverse.next = node


    def get_position(self, position):
        """
            It return the node of given position
        """
        index = 1
        traverse = self.head
        while traverse:
            if index == position:
                return traverse.data
            traverse = traverse.next
            index += 1
        return None

    def delete(self, data):
        """
            It deletes the node of given data
        """
        traverse = self.head
        temp = self.head.next
        if self.head.data == data:
            self.head = self.head.next
            del traverse
            return
        while traverse:
            if(temp.data == data):
                traverse.next = temp.next
                del temp
                return
            temp = temp.next
            traverse = traverse.next

    def display(self):
        traverse = self.head
        print("The data is: ", end="")
        while traverse:
            print(traverse.data, end=" ")
            traverse = traverse.next
        print()

first = LinkedList(10)
first.append(20)
first.append(30)
first.append(40)
first.append(50)
first.insert(Node(25), 1)
first.display()
first.delete(30)
first.display()
print(first.get_position(5))