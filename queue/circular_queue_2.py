

class Node:
    value = None
    nextNode = None

    def __init__(self, value):
        self.value = value

class CircularList:
    head = None
    tail = None

    def __init__(self):
        pass

    def enqueue(self, elem):
        node = Node(elem)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.nextNode = node
            self.tail = node
            
        tail.nextNode = head



head = Node(1)
head_2 = Node(2)
head_3 = Node(3)
head_4 = Node(4)
head_5 = Node(5)

head.nextNode = head_2
head_2.nextNode = head_3
head_3.nextNode = head_4
head_4.nextNode = head_5
head_5.nextNode = head

tail = head_5



