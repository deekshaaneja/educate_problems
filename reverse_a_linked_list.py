class Node:
    def __init__(self, val, next= None):
        self.val = val
        self.next = next
    def reverse_linked_list(head):
        previous, current, next = None, head, None
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next
        print()      

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = head.reverse_linked_list()
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()