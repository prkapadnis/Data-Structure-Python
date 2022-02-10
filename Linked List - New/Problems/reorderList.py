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
list.append(2)
list.append(3)
list.append(4)
# list.append(5)
# list.append(6)
# list.append(7)

# get Middle

def getMiddle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    
    return slow

# reverse the list
def reverse(head):
    previous = None
    current = head
    nextnode = current.next

    while current != None:
        current.next = previous
        previous = current
        current = nextnode
        if nextnode != None:
            nextnode = nextnode.next

    return previous

def reorder(head):
    firsthead = head
    middle = getMiddle(head)
    print(middle.data)
    secondhead = reverse(middle)

    while firsthead != None and secondhead != None:
        temp = firsthead.next
        firsthead.next = secondhead
        firsthead = temp
        temp = secondhead.next
        secondhead.next = firsthead
        secondhead = temp

    if firsthead != None:
        firsthead.next = None

def display(head):
    traverse = head
    while traverse:
        print(traverse.data)
        traverse = traverse.next
    print('end')

reorder(list.head)
list.display()