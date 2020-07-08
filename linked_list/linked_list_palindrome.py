from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def append(self, num):
        self.stack.append(num)
        return True
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return None

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def is_palindromic_linked_list(node):
    fast = node
    slow = node
    stk = Stack()
    while fast.next is not None and fast.next.next is not None:
        fast = fast.next.next
        stk.append(slow.value)
        slow = slow.next    
    # print(slow.next)
    while slow.next is not None:
        if slow.next.value != stk.pop():
            return False
        slow = slow.next
    return True

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()
    