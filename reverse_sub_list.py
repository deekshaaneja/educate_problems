class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()

    def reverse_sub_list(self, start, end):
        current = self
        next, previous1, previous2, previous3 = start, None, None, None
        while current != None:
            if current.value != start:
                previous1 = current
                current = current.next
            else:
                while current.value != end:
                    next = current.next
                    current.next = previous2
                    previous2 = current
                    current = next
                previous1.next = current
        return current
    

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = head.reverse_sub_list(2, 4)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
