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
    current, previous = head, None
    alternate_flag = True
    last_node_of_previous_list = previous
    last_node_of_sublist = current
    i = 0

    while True:
        if i < k:
            next = current.next
            if alternate_flag == True:
                current.next = previous
            previous = current
            current = next

        if i == k or current is None:
            alternate_flag = False if alternate_flag == True else True
            i = -1
            if alternate_flag == False:
                last_node_of_sublist.next = current
                if last_node_of_previous_list is None:
                    head = previous
                else:
                    last_node_of_previous_list.next = previous
            else:
                last_node_of_sublist = current
                last_node_of_previous_list = previous

        i += 1
        if current is None:
            break
        
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

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
        
        
