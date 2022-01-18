#Queue is linear structure. follows FIFO structure. Insertion and Deletions happen at both the ends.
#It has 4 operations - Enqueue, Dequeue, Front, Rear
#Used in resource management, cpu/disk scheduling.

class Queue:

    def __init__(self,capacity):
        self.front = self.size = 0 #first index as front
        self.rear = capacity -1 #last index as rear
        self.Q = [None]*capacity # initializing it as empty, none values
        self.capacity = capacity # declaring capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0
        
    def EnQueue(self,item):
        if self.isFull():
            print("Full")
            return
        self.rear = (self.rear + 1) % (self.capacity)
        self.Q[self.rear] = item
        self.size = self.size + 1
        print("Enqueued to the queue",str(item))

    def DeQueue(self):
        if self.isEmpty():
            print("Empty")
            return

        print("dequeued from the queue",str(self.Q[self.front]))
        self.front = (self.front + 1) * (self.capacity)
        self.size = self.size - 1 

    def que_front(self):
        if self.isEmpty():
            print("Queue is Empty")
        print("Front item is", self.Q[self.front])

    def que_rear(self):
        if self.isEmpty():
            print("Queue is Empty")
        print("rear item is", self.Q[self.rear])

if __name__ == "__main__":

    queue = Queue(30) #30 is the capacity of queue
    queue.EnQueue(10)
    queue.EnQueue(20)
    queue.EnQueue(30)
    queue.EnQueue(40)
    print(queue.Q)
    queue.DeQueue()