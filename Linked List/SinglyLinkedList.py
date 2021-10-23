class Node:
    def __init__(self, data):       # defination of Node
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def reverse(self):
        privious = None
        current = self.head
        next = None
        while current!= None:
            next = current.next_node
            current.next_node = privious
            privious = current
            current = next
        self.head = privious
        print("The linked list is reversed!!")
    
    def get_size(self):
        return self.size

    def display(self):
        current = self.head
        print("The Data: ",end="")
        while current:
            print(current.data, end=" ")
            current = current.next_node
    
    #Insertion Operation

    def insert_at_first(self, data):
        new_node = Node(data)
        self.size+=1
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def insert_at_middle(self, data, position):
        new_node = Node(data)
        self.size += 1
        current = self.head
        for i in range(1, position-1):
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node

    def insert_at_last(self, data):
        new_node = Node(data)
        self.size += 1
        current = self.head
        while current.next_node:
            current = current.next_node
        current.next_node = new_node
    
    #deleting Operations the nodes 

    def delete_first(self):
        delete_node = self.head
        self.head = self.head.next_node
        del delete_node
        print("The first node Deleted!!")

    def delete_middle(self, position):
        delete_node = self.head.next_node
        temp_node = self.head
        for i in range(1, position-1):
            delete_node = delete_node.next_node
            temp_node = temp_node.next_node
        temp_node.next_node = delete_node.next_node
        del delete_node
        print(f"{position}th node deleted!!")
        
    def delete_last(self):
        current = self.head.next_node
        last_second_node = self.head 
        while current.next_node:
            current = current.next_node
            last_second_node = last_second_node.next_node
        last_second_node.next_node = None
        del current

list = LinkedList()
list.insert_at_first(10)
list.insert_at_last(20)
list.insert_at_last(30)
list.insert_at_middle(25, 3)
list.display()
print()
print("The size is:",list.get_size())
list.delete_first()
list.delete_last()
list.delete_middle(2)
list.reverse()
list.display()