class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def print_list(self):
        curr = self
        while curr != None:
            if curr.next != None:
                print(curr.value, end="->")
            else:
                print(curr.value)
            curr = curr.next
    def reverse_every_k_elements(self, k):
        curr = self
        prev = None
        while True:
            i = 0
            last_point_of_prev_part = prev
            last_node_of_sublist = curr
            while curr != None and i<k:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
                i += 1
            if last_point_of_prev_part is not None:
                last_point_of_prev_part.next = prev
            else:
                self = prev
            last_node_of_sublist.next = curr
            if curr == None:
                break
            prev = last_node_of_sublist
        return self
        
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = head.reverse_every_k_elements(3)
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()
