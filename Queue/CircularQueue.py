class CircularQueue:
    def __init__(self, size) -> None:
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def isEmpty(self):
        if self.front == -1 and self.rear == -1:
            return True
        return False
    
    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        return False

    def enqueue(self, data):
        if self.isFull():
            print("The Queue is Overflow!!!")
        else :
            if self.front == -1:
                self.front = self.rear = 0
                self.queue[self.front] = data
            else:
                self.rear = (self.rear + 1) % self.size
                self.queue[self.rear] = data
    
    def dequeue(self):
        if self.isEmpty():
            print("The Queue is UnderFlow!!")
        elif self.front == self.rear:
            temp = self.queue[self.front] 
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp
    
    def display(self):
        if self.isEmpty():
            print("The Queue is empty!!")
            return
        print("The Queue is: ", end=" ")
        if (self.rear >= self.front):
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

queue = CircularQueue(5)
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
            