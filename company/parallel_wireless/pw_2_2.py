# m->a->d->a->m
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

def palindrome(node):
    ls = []
    while node is not None:
        ls.append(node.value)
        node = node.next
    i = 0
    j = len(ls) -1
    while i < j:
        if ls[i] != ls[j]:
            return False
        i += 1
        j -= 1
    return True

def main():
    start = Node('m')
    start.next = Node('a')
    start.next.next = Node('d')
    start.next.next.next = Node('a')
    start.next.next.next.next = Node('b')
    print(palindrome(start))

main()