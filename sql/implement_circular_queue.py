
class CircularQueue:
    def __init__(self, maxSize, head = None, tail = None):
        self.maxSize = maxSize
        self.head = head
        self.tail = tail

    def enqueue(self, elem):
        if self.size() == self.maxSize - 1:
            return "Queue Empty"
        else:
            elem = tail
            tail = tail + 1

    def deque(self):
        if self.size() == 0:
            return "Queue Empty"
        else:
            head = head + 1

    def size(self):
        if tail >= head:
            qsize = tail - head
        else:
            qsize = maxSize - (head - tail)
        return qsize
