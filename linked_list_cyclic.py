
class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    # def get_data(self):
    #     return self.data

    # def set_data(self, val):
    #     self.data = val
    
    # def get_next_node(self):
    #     return self.nextNode

    # def set_next_node(self, node):
    #     self.nextNode = node

    def has_cycle(head):
        slow, fast = head, head
        while fast is not None and fast.nextNode is not None:
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
            if slow == fast:
                return True
        return False            

def main():
    head = Node(1)
    head.nextNode = Node(2)
    head.nextNode.nextNode = Node(3)
    head.nextNode.nextNode.nextNode = Node(4)
    head.nextNode.nextNode.nextNode.nextNode = Node(5)
    head.nextNode.nextNode.nextNode.nextNode.nextNode = Node(6)
    print("LinkedList has cycle: " + str(Node.has_cycle(head)))

    head.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode = head.nextNode.nextNode
    print("LinkedList has cycle: " + str(Node.has_cycle(head)))

    head.nextNode.nextNode.nextNode.nextNode.nextNode.nextNode = head.nextNode.nextNode.nextNode
    print("LinkedList has cycle: " + str(Node.has_cycle(head)))


main()

# class LinkedList:
#     def __init__(self, head=None):
#         self.head = head
#         self.size = 0

#     def get_size(self):
#         return self.size

#     def addNode(self, data):
#         newNode = Node(data, self.head)
#         self.head = newNode
#         self.size += 1
#         return True

#     def printNode(self):
#         curr = self.head
#         while curr:
#             print(curr.head)
#             curr.get_next_node






    