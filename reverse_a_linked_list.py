class Node:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next

    def print_list(self):
        curr = self
        temp = ""
        while curr != None:
            if curr.next != None:
                temp = temp + str(curr.head) + "->"
            else:
                temp = temp + str(curr.head)
            curr = curr.next
        print(temp)

    def reverse_list(self):
        curr = self
        prev = None
        while curr != None:
            temp = prev
            prev = curr
            curr = curr.next
            prev.next = temp
        return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are: ", end='')
    head.print_list()
    result = head.reverse_list()
    print("Nodes of reversed LinkedList are: ", end='')
    result.print_list()


main()