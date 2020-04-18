class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def print_list(self):
        s = ""
        curr = self
        while curr != None:
            if curr.next != None:
                s += str(curr.value) + "->"
            else:
                s += str(curr.value)
            curr = curr.next
        print(s)

def merge_lists(head1, head2):
    previous1, current1 = None, head1
    previous2, current2 = None, head2
    while True:
        if current1 is None and current2 is None:
            break
        elif current1 is None:
            temp = Node(current2.value)
            previous1.next = temp
            temp.next = current1
            current2 = current2.next
            previous1 = temp
        elif current2 is None or current1.value <= current2.value:
            previous1 = current1
            current1 = current1.next
        else:
            temp = Node(current2.value)
            previous1.next = temp
            temp.next = current1
            current2 = current2.next
            previous1 = temp
    return head1

def main():
    l1 = Node(2)
    l1.next = Node(6)
    l1.next.next = Node(8)
    l1.print_list()

    l2 = Node(3)
    l2.next = Node(5)
    l2.next.next = Node(7)
    l2.next.next.next = Node(9)
    l2.print_list()

    merge_list = merge_lists(l1, l2)
    merge_list.print_list()
    

main()
