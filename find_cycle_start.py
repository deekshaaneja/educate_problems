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
        print(s)

def find_cycle_start(head):
    slow, fast = head, head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            length_of_cycle = find_cycle_length(slow)
            start = cycle_start(head, length_of_cycle)
            return start
    return None

def cycle_start(head, length_of_cycle):
    pointer1, pointer2 = head, head
    while length_of_cycle > 0:
        pointer2 = pointer2.next
        length_of_cycle -= 1
    while True:
        if pointer1 == pointer2:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return None


def find_cycle_length(slow):
    pointer1, pointer2 = slow.next, slow
    length = 1
    while True:
        if pointer1 != pointer2:
            pointer1 = pointer1.next
            length += 1
        else:
            return length




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