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

    # curr = node1
    # while curr != None:
    #     if curr.next == None:
    #         last_node_pointer = curr
    #     curr = curr.next

    sublist_start = Node(None, None)
    sublist_end = Node(None,None)

    while node != None:
        elem = Node(node.value, None)
        if node.value > pivot:
            if sublist_end.value != None:
                elem.next = sublist_end
                sublist_end = elem 
            else:
                sublist_end.value = elem.value

        if node.value <= pivot:
            if sublist_start.value != None:
                elem.next = sublist_start
                sublist_start = elem
            else:
                sublist_start.value = elem.value
        node = node.next

    tail = sublist_start
    while tail is not None:
        if tail.next == None:
            break
        tail = tail.next
    
    tail.next = sublist_end
    return sublist_start



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

            

