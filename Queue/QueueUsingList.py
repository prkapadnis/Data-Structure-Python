class Node:
    def __init__(self, data = None) -> None:
        self.data = data
        self.next = None

class Queue:
    def __init__(self, data) -> None:
        self.front = Node(data)
        self.rear = self.front

    def enqueue(self, data):
        """
            The Enqueue function insert the node at the rear of the queue
        """
        node = Node(data)
        if self.front:
            self.rear.next = node
            self.rear = node
        else:
            self.front = self.rear = node
    
    def get_front(self):
        """
            The get_front return the front element of the queue
        """
        if self.is_empty():
            return "The Queue is Empty"
        else :
            return self.front.data 

    def get_rear(self):
        """
            It get_rear return thr last element of the queue.
        """
        if self.is_empty():
            return "The Queue is Empty"
        else :
            return self.rear.data

    def is_empty(self):
        """
            It return the true if the queue is empty else false
        """
        return self.front == None

    def dequeue(self):
        """
            The Dequeue funtion delete the first node of the queue
            Because the queue is LIFO structure
        """
        if self.is_empty():
            print("The Queue is underflow!!")
        else:
            delNode = self.front
            self.front = self.front.next
            del delNode
            
    
    def display(self):
        traverse = self.front
        if(self.front):
            print("The Queue is: ", end=" ")
            while traverse:
                print(traverse.data, end=" ")
                traverse = traverse.next
            print()
        else:
            print("The queue is empty!!!")

queue = Queue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.dequeue()
queue.enqueue(10)
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.enqueue(10)
print(queue.get_front())
print(queue.get_rear())
queue.display()