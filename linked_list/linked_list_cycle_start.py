class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    
    def print_list(self):
        current = self
        s = ""
        while current is not None:
            if current.next is not None:
                s += str(current.value) + "->"
            else:
                s += str(current.value)
            current = current.next
        print(s)

def linked_list_cycle(head):
    slow, fast = head, head
    while slow.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length_list = find_cycle_length(slow)
            return length_list
    return -1

def find_cycle_length(pointer):
    pointer1, pointer2 = pointer, pointer.next
    length_list = 1
    while True:
        pointer2 = pointer2.next
        length_list += 1
        if pointer1 == pointer2:
            break
    return length_list
    

def find_cycle_start(head):
    pointer = head
    length_list = linked_list_cycle(pointer)
    if length_list > 0:
        pointer1, pointer2 = head, head
        while length_list != 0:
            pointer1 = pointer1.next
            length_list -= 1
        while True:
            if pointer1 == pointer2:
                return pointer1
            pointer1 = pointer1.next
            pointer2 = pointer2.next


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()