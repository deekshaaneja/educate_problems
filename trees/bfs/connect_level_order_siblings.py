from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.value) + "->", end = '')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

def connect_level_order_siblings(root1):
    root = root1
    q = deque()
    q.append(root)
    while q:
        previousNode = None
        levelSize = len(q)
        for _ in range(levelSize):
            currentNode = q.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
    return root
    
            
def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointer: ")
    root.print_level_order()


main()

            
    