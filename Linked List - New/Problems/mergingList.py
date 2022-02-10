# merf the two sorted list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

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

ssl1 = Linkedlist(1)
ssl1.append(2)
ssl1.append(4)

ssl2 = Linkedlist(1)
ssl2.append(3)
ssl2.append(4)



def mergeList(head_1, head_2):
    head1 = head_1
    head2 = head_2
    newHead = Linkedlist(0)
    while head1 != None and head2 != None:
        
        if head1.data < head2.data:
            newHead.append(head1.data)
            head1 = head1.next
        else:
            newHead.append(head2.data)
            head2 = head2.next
    
    while head1 != None:
        newHead.append(head1.data)
        head1 = head1.next
        # newHead = newHead.next
    
    while head2 != None:
        newHead.append(head2.data)
        head2 = head2.next
        # newHead = newHead.next

    return newHead.head.next

def display(head):
    traverse = head
    while traverse:
        print(traverse.data)
        traverse = traverse.next
    print('end')

newHead = mergeList(ssl1.head, ssl2.head)
display(newHead)