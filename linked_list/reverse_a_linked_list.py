class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        current = self
        s =""
        while current is not None:
            if current.next is not None:
                s += str(current.value) + "->"
            else:
                s += str(current.value)
            current = current.next
        return s

def reverse_list(node):
    current = node
    previous = None
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
    return previous

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    print(head.print_list())
    result = reverse_list(head)
    print("Nodes of reversed LinkedList are: ", end='')
    print(result.print_list())

main()
