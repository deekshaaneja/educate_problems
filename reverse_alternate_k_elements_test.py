class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        current = self
        s = ""
        while current != None:
            if current.next != None:
                s += str(current.value) + "->"
            else:
                s += str(current.value)
            current = current.next
        print(s)

def reverse_alternate_k_elements(head, k):
    i = 0
    alternate_flag = False
    current, previous = head, None
    last_node_of_previous_part = previous
    last_node_of_sublist = current

    while True:

        if current is None:
            break
        elif current.next is None:
            if alternate_flag == False:
                last_node_of_previous_part.next = current
                last_node_of_sublist.next = None
        if i < k:
            next = current.next
            if alternate_flag == False:
                current.next = previous
            previous = current
            current = next
        elif i == k:
            i = -1
            if alternate_flag == False:
                if last_node_of_previous_part is None:
                    head = previous
                else:
                    last_node_of_previous_part.next = previous
                previous = last_node_of_sublist
                last_node_of_sublist.next = current
            else:
                last_node_of_previous_part = previous
                last_node_of_sublist = current
            alternate_flag = not alternate_flag
        i += 1
        # if current.next is None:
        #     previous = last_node_of_sublist
        #     last_node_of_sublist.next = current

    return head

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    head.next.next.next.next.next.next.next.next = Node(9)
    head.next.next.next.next.next.next.next.next.next = Node(10)
    head.next.next.next.next.next.next.next.next.next.next = Node(11)
    head.next.next.next.next.next.next.next.next.next.next.next = Node(12)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()

            