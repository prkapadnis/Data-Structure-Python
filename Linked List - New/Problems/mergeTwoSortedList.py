class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # def __init__(self):
    #     self.head = None

    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        node = Node(data)
        if self.head:
            traverse = self.head
            while traverse.next != None:
                traverse = traverse.next
            traverse.next = node
        else:
            self.head = node
    
    def display(self):
        traverse = self.head
        while traverse != None:
            print(traverse.data, end=' -> ')
            traverse = traverse.next
        print('END ')
    
# First Approch
def merge(head1, head2):
    node1 = head1
    node2 = head2
    newList = LinkedList()
    while node1 != None and node2 != None:
        if node1.data < node2.data:
            newList.append(node1.data)
            node1 = node1.next
        else:
            newList.append(node2.data)
            node2 = node2.next
    if node1 != None:
        while node1 != None:
            newList.append(node1.data)
            node1 = node1.next
    if node2 != None:
        while node2 != None:
            newList.append(node2.data)
            node2 = node2.next
    return newList

# Second Approch
def merge_2(head1, head2):
    node1 = head1
    node2 = head2
    newList = LinkedList(0)
    tail = newList
    while node1 != None and node2 != None:
        if node1.data < node2.data:
            tail.next = node1
            node1 = node1.next
        else:
            tail.next = node2
            node2 = node2.next
        tail = tail.next

    while node1 != None:
        tail.next = node1
        node1 = node1.next
        tail = tail.next

    while node2 != None:
        tail.next = node2
        node2 = node2.next
        tail = tail.next

    return newList.next

            

list1 = LinkedList(1)
# list1.append(1)
list1.append(2)
list1.append(3)
list1.display()

list2 = LinkedList(1)
# list2.append(1)
list2.append(3)
list2.append(5)
list2.display()

# newlist = merge(list1.head, list2.head)
# newlist.display()

list1.head = merge_2(list1.head, list2.head)
list1.display()