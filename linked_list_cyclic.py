class Node:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next

    def print_list(self):
        curr = self
        while curr != None:
            print(str(curr.head) + " ")
            curr = curr.next
    def has_cycle(self):
        slow = self
        fast = slow.next.next
        while fast != None and fast.next != None:
            slow = slow.next
            if fast != None:
                fast = fast.next.next
            if slow == fast:
                return True
        return False

    
def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LinkedList has cycle: " + str(head.has_cycle()))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(head.has_cycle()))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(head.has_cycle()))
    # head.print_list()


main()