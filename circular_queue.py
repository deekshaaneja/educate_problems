class Queue:
    head, tail = 0, 0
    size = 0
    arr = None
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size 

    def enqueue(self, elem):
        if self.is_full():
            return "Queue full"
        self.arr[self.tail] = elem
        if self.tail == self.size -1:
            self.tail = 0
        else:
            self.tail += 1
                
    def dequeue(self):
        if self.head == self.tail:
            return "Empty Queue"
        elem = self.arr[self.head]
        if self.head == self.size -1:
            self.head = 0
        else:
            self.head += 1
        return elem

    def is_full(self):
        if self.head == 0 and self.tail == self.size - 1:
            return True
        if self.tail + 1 == self.head:
            return True
        return False

q = Queue(3)
q.enqueue(1)
q.enqueue(2)
print(q.enqueue(4))
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())
print(q.dequeue())


    







