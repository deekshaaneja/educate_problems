class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
def print_list(node):
    s = ""
    while node is not None:
        if node.next is not None:
            s += str(node.value) + "->"
        else:
            s += str(node.value)
        node = node.next
    return s

def pivot_list_sorting(node, pivot):
    prev = None
    head = node

    while node != None:
        if node.value < pivot and prev is not None:
            next = node.next
            node.next = head
            head = node
            prev.next = next
            node = next
        else:
            prev = node
            node = node.next

    return head



def main():
    pivot = 5
    head = Node(2)
    head.next = Node(6)
    head.next.next= Node(5)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(4)

    print("Nodes of original LinkedList are: ", end='')
    print(print_list(head))
    result = pivot_list_sorting(head, pivot)
    print("Nodes of reversed LinkedList are: ", end='')
    print(print_list(result))


main()

            

