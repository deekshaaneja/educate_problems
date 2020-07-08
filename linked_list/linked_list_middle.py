class Node:
    def __init__(self, value, next=None):
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

def find_middle_node(node):
    slow = node
    fast = node
    while fast is not None:
        if fast.next.next is None:
            if fast.next is None:
                return slow.value
            elif fast.next is not None:
                return slow.next.value
        slow = slow.next
        fast = fast.next.next
    return None

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    head.print_list()
    result = find_middle_node(head)
    print(result)


main()