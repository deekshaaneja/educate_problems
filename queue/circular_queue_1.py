class Queue:
    def __init__(self, size):
        self.size = size
        self.arr = [-1] * size
        self.head, self.tail = 0, 0


    def is_full(self):
        if self.tail + 1 == self.head:
            return True
        elif self.tail == self.size - 1 and self.head == 0:
            return True
        return False

    def enque(self, num):
        if self.is_full():
            return "Queue is full"
        self.arr[self.tail] = num 
        self.tail += 1
        return "number added"

    def enque_penultimate(self, num):
        if self.is_full():
            return "Queue is full"

        if self.head == self.tail:
            self.arr[self.head] = num
            self.tail = 0 if self.tail == self.size-1 else self.tail+1
        else:
            elem_at_index = self.arr[self.size-1] if self.tail == 0 else self.arr[self.tail-1]
            if self.tail == 0:
                self.arr[self.size-1] = num
                self.arr[self.tail] = elem_at_index
                self.tail += 1
            else:
                self.arr[self.tail-1] = num
                self.arr[self.tail] = elem_at_index
                if self.tail == self.size-1:
                    self.tail = 0
                else:
                    self.tail += 1

        # if self.tail == 0:
        #     elem_at_index = self.arr[self.size-1]

        # self.arr[self.tail - 1] = num 
        # self.arr[self.tail] = elem_at_index
        # self.tail += 1
        return "number added on 2nd last"

    def deque(self):
        if self.head == self.tail:
            return "Queue is empty"
        num = self.arr[self.head]
        if self.head == self.size - 1:
            self.head = 0
        else:
            self.head += 1
        return num

    def print_queue(self):
        if self.tail > self.head:
            print(self.arr[self.head : self.tail])

q = Queue(5)
# print(q.enque(1))
# print(q.enque(2))
# print(q.enque(3))
# print(q.enque(4))
# print(q.enque_penultimate(10))
# print(q.deque())
# print(q.enque_penultimate(10))
# print(q.arr, q.head, q.tail)
# print(q.deque())
# print(q.deque())
# print(q.deque())
# # print(q.deque())
print(q.enque_penultimate(11))
print(q.arr, q.head, q.tail)
