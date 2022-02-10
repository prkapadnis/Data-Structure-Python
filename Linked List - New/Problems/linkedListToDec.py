# Convert Binary Number of linked list to Decimal 
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

from dis import dis


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

#   Insertoin using recursion
    def insertion(self, data, index, node):
        if index == 0:
            temp = Node(data)
            temp.next = node
            self.size += 1
            return temp
        
        node.next = self.insertion(data, index-1, node.next)
        return node

#   Inserrtion operation

    def append(self, data):
        """
            it appends to the node to the last of the list
        """
        node = Node(data)
        self.tail.next = node
        self.tail = node
        self.size += 1
    
    def insert(self, data, position):
        """
            Insert the Node at specific position
        """
        if position < self.size:
            node = Node(data)
            traverse = self.head
            for i in range(position-2):
                traverse = traverse.next
            node.next = traverse.next
            traverse.next = node
            self.size += 1
        else:
            print(f'{position} position does not exit')

    def insertFirst(self, data):
        """
            Insert at the first position
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

#   Deletion operation

    def deleteFirst(self):
        """
            Deletes the first Node
        """
        temp = self.head
        self.head = self.head.next
        del temp
    
    def deleteLast(self):
        """
            Deletes the last node
        """
        traverse = self.head
        while traverse.next != self.tail:
            traverse = traverse.next
        temp = self.tail
        self.tail = traverse
        del temp
    
    def delete(self, index):
        """
            deletes the node at specific index
        """
        traverse = self.head
        for i in range(index-2):
            traverse = traverse.next
        temp = traverse.next
        traverse.next = temp.next
        del temp

    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.data)
            traverse = traverse.next
        print('end')

list = Linkedlist(1)
list.append(1)
list.append(0)
list.append(1)

def display(head):
    traverse = head
    while traverse:
        print(traverse.data)
        traverse = traverse.next
    print('end')


def reverse(head):
    previous = None
    current = head
    nextnode = current.next
    while current != None:
        current.next = previous
        previous = current
        current = nextnode
        if nextnode:
            nextnode = nextnode.next

    head = previous
    return head

def getDecimalValue(head):
    traverse = head
    value = 0
    i = 0
    while traverse:
        if traverse.data == 1:
            value = value + pow(2, i)
        i += 1
        traverse = traverse.next
    return value


newhead = reverse(list.head)
display(newhead)
print(getDecimalValue(newhead))
