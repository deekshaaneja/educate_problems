from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_minimum_depth(root):
    q = deque()
    q.append(root)
    minimumTreeDepth = 0
    while q:
        minimumTreeDepth += 1
        levelSize = len(q)
        # levelArr = []
        for _ in range(levelSize):
            currentNode = q.popleft()
            if not currentNode.left and not currentNode.right:
                return minimumTreeDepth
            else:
                if currentNode.left:
                    q.append(currentNode.left)
                if currentNode.right:
                    q.append(currentNode.right)
    return minimumTreeDepth

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
