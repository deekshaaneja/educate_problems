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
    current = head
    i = 0
    previous = None
    alternating = True
    start = head
    previous_to_start = None
    new_head = None

    while True:

        if i < k:
            next = current.next
            if previous is not None and alternating == True:
                current.next = previous
            previous = current
            current = next

        if i == k or current is None:
            if alternating == True:
                start.next = current
                if previous_to_start is not None:
                    previous_to_start.next = previous 
                if new_head is None:
                    new_head = previous
            else:
                previous_to_start = previous
                start = current

            i = -1
            alternating = True if alternating == False else False 

        i = i + 1
        if current is None:
            break

    return new_head
            
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    # head.next.next.next.next.next.next.next.next = Node(9)
    # head.next.next.next.next.next.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = reverse_alternate_k_elements(head, 3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()