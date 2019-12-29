


class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def print_list(self):
        curr = self
        # temp = ""
        while curr != None:
            if curr.next != None:
                print(curr.value , end="->")
            else:
                print(curr.value)
            curr = curr.next
        print()

    def reverse_sub_list(self, p, q):
        i = 0
        curr = self
        prev = None
        while i < p-1 and curr.next != None:
            prev = curr
            curr = curr.next
            i += 1
        last_node = prev
        last_node_of_sublist = curr
        i = 0
        while i < q-p+1 and curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            i += 1
        last_node.next = prev
        last_node_of_sublist.next = curr
        return self

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
