class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, num):
        self.stack_list.append(num)
        return True

    def pop(self):
        return self.stack_list.pop(0)

    def is_empty(self):
        if len(self.stack_list) == 0:
            return True
        return False

class Queue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, num):
        self.inbox.push(num)
        self.outbox.push(self.inbox.pop())

    
    def dequeue(self):
        value = self.outbox.pop()
        return value

    def is_empty(self):
        if len(self.outbox) == 0:
            return True
        return False

def main():
    if __name__ == '__main__': 
        q = Queue() 
        q.enqueue(1)  
        q.enqueue(2)  
        q.enqueue(3)  
        print(q.dequeue()) 
        print(q.dequeue()) 
        print(q.dequeue()) 

main()
