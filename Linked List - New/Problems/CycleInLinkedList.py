class Node:
    def __init__(self,  data, next_noded):
        self.data = data
        self.next = next_noded  

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        node = Node(data)
        if self.head:
            traverse = self.head
            while traverse.next:
                traverse = traverse.next
            traverse.next = node
        else:
            self.head = node
    
    def display(self):
        traverse = self.head
        while traverse:
            print(traverse.data, end=' -> ')
            traverse = traverse.next
        print('End ')
    

def isCyclePresent(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            return True
    return False

# Length of the cycle

def lengthCycle(head):
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if fast == slow:
            slow = slow.next
            count = 1
            while slow != fast:
                slow = slow.next
                count += 1
            break
    return count
        



obj = LinkedList()
obj.append(10)
obj.append(20)
obj.append(30)
obj.append(40)
obj.display()