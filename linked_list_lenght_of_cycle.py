class Node:
    def __init__(self, value, next = None):
        self.value =value
        self.next = next

    def calculate_length(slow):
        length = 0
        curr = slow
        while curr:
            curr = curr.next
            length += 1
            if curr == slow:
                break
        return length

    def find_length(head):
        slow, fast = head, head
        while fast.next is not None and fast is not None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return slow.calculate_length()
        # return length



def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle length: " + str(Node.find_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle length: " + str(Node.find_length(head)))


main()