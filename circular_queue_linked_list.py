class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enque(self, elem):
        node_elem = Node(elem)
        if self.head is None:
            self.head = node_elem
            self.tail = node_elem
        else:
            self.tail.next = node_elem
            self.tail = node_elem
        self.size += 1

    def deque(self):
        if self.head is None:
            return "Queue Empty"
        head_node = self.head
        self.head = self.head.next
        self.size -= 1
        return head_node.value

    def getSize(self):
        return self.size

q = Queue()
print(q.deque())
print(q.enque(1))
print(q.enque(2))
print(q.enque(3))
print(q.enque(4))
print(q.getSize())
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())


    