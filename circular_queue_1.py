class Queue:
    def __init__(self, size):
        self.size = size
        self.head, self.tail = 0, 0
        self.arr = [-1] * size

    def enque(self, elem):
        if self.is_full():
            return "Queue is Full"
        self.arr[self.tail] = elem
        self.tail += 1
        if self.tail == self.size:
            self.tail = 0
        return "added"

    def deque(self):
        if self.head ==self.tail:
            return "Queue Empty"
        elem = self.arr[self.head]
        self.head += 1
        if self.head == self.size:
            self.head = 0
        return elem

    def is_full(self):
        if self.tail == self.size -1 and self.head == 0:
            return True
        if self.head - self.tail == 1:
            return True
        return False


q = Queue(3)
print(q.deque())
print(q.enque(1))
print(q.enque(2))
print(q.enque(3))
print(q.enque(4))
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())




    
