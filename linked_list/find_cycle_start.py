class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = None

    def print_list(self):
        current = self
        s = ""
        while current is not None:
            if current.next is not None:
                s += str(current.val) + "->"
            else:
                s += str(current.val)
            current = current.next
        return s

def has_cycle(node):
    slow = node
    fast = node
    while fast is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = find_cycle_length(slow)
            return cycle_length
    return None

def find_cycle_length(slow):
    node1 = slow
    node2 = slow.next
    cycle_length = 1
    while node2 != node1:
        node2 = node2.next
        cycle_length += 1
    return cycle_length


def find_cycle_start(node):
    cycle_length = has_cycle(node)
    node1 = node
    node2 = node
    while cycle_length != 0:
        node1 = node1.next
        cycle_length -= 1
    while node1 != node2:
        node1 = node1.next
        node2 = node2.next
    return node1


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