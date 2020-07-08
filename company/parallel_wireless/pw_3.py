class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    def print_list(self):
        current = self
        s = ""
        while current is not None:
            if current.next is not None:
                s += str(current.value) + "->"
            else:
                s += str(current.value)
            current = current.next
        print(s)

#  1->2->3->4->3->2->1

# slow.next
# fast.next,next
# ls[]