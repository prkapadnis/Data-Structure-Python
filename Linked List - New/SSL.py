from typing_extensions import ParamSpec


class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head
        self.size = 1

    def append(self, data):
        if self.head:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.size += 1
        else:
            self.head = Node(data)
            self.size += 1

    def insert(self, data, position):
        if position <= self.size:
            node = Node(data)
            temp = self.head
            index = 1
            if position == 1:
                node.next = self.head
                self.head = node
                self.size += 1
            else:
                while index != position - 1:
                    temp = temp.next
                    index += 1
                node.next = temp.next
                temp.next = node
                self.size += 1
        else:
            print("Plzz Enter the valid position!!!")
            
    def delete(self, data):
        temp = self.head
        traverse = self.head.next
        if self.head.data == data:
            self.head = self.head.next
            del temp        
            self.size -= 1
            return
        else:   
            while temp:
                if traverse and temp:
                    if traverse.data == data:
                        temp.next = traverse.next
                        del traverse
                        self.size -= 1
                        return
                    temp = temp.next
                    traverse = traverse.next
                else:
                    print('Plzz enter valid data!!')
                    return
        
        

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print('END')
        
ssl = SinglyLinkedList(10)
ssl.append(20)
ssl.append(30)
ssl.append(40)
ssl.append(50)
ssl.append(60)
ssl.display()
# ssl.insert(25, 8)
ssl.delete(90)
ssl.display()
print(ssl.head.data)
print(ssl.tail.data)
print(f"The size of the List is {ssl.size}")