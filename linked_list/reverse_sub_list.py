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

def reverse_sub_list(head, p, q):
    if p == q:
        return head
    
    current, previous = head, None
    i = 0
    while current is not None and i< p-1:
        previous = current
        current = current.next
        i += 1

    last_node_of_first_part = previous
    last_node_of_sublist = current
    next = None
    i = 0

    while current is not None and i < q - p + 1:
        next = current.next
        current.next = previous
        previous = current
        current = next
        i += 1

    if last_node_of_first_part is not None:
        last_node_of_first_part.next = previous

    else:
        head= previous

    last_node_of_sublist.next = current
    return head


def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    print(head.print_list())
    result = reverse_sub_list(head, 2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    print(result.print_list())


main()