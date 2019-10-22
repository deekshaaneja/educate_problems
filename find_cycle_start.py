class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def find_cycle_start(head):
        pointer1 = pointer2 = head
        cycle_length = pointer2.find_cycle()
        while cycle_length > 0:
            pointer2 = pointer2.next
            cycle_length -= 1
        while pointer1 != pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next
        return pointer1.value

    def find_cycle_length(slow):
        length = 0
        curr = slow
        while curr:
            curr = curr.next
            length += 1
            if curr == slow:
                break
        return length

    def find_cycle(head):
        slow, fast = head, head
        while fast is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return slow.find_cycle_length()

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(Node.find_cycle_start(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(Node.find_cycle_start(head)))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(Node.find_cycle_start(head)))


main()