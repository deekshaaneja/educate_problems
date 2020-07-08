

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
                s+= str(current.value)
            current = current.next
        print(s)

# Input:
#   First List: 5->6->3  // represents number 563
#   Second List: 8->4->2 //  represents number 842
# Output
#   Resultant list: 1->4->0->5  // represents number 1405

def add_lists(node1, node2):
    num1_str = ""
    while node1 is not None:
        num1_str += str(node1.value)
        node1 = node1.next
    num1 = int(num1_str)
    num2_str = ""
    while node2 is not None:
        num2_str += str(node2.value)
        node2 = node2.next
    num2 = int(num2_str)
    num3 = num1 + num2
    num3_str = str(num3)
    print(num3_str)
    previous = None
    current = Node(num3_str[0])
    s = ""
    for i in range(1, len(num3_str)):
        if i!= len(num3_str) -1:
            s+= str(current.value) + "->"
        else:
            s += str(current.value)
        # current.next = Node(num3_str[i])
        previous = current
        current = Node(num3_str[i])
    s += "->" + str(current.value)
    print(s)
    
def main():
    node1 = Node(5)
    node1.next = Node(6)
    node1.next.next = Node(3)

    node2 = Node(8)
    node2.next = Node(4)
    node2.next.next = Node(2)
    add_lists(node1, node2)

main()
            
