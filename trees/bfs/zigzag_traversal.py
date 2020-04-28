from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzag_traversal(root):
    q = deque()
    q.append(root)
    result = []
    i = True
    while q:
        levelSize = len(q)
        levelArr = deque()
        for _ in range(levelSize):
            currentNode = q.popleft()
            if i == True:
                levelArr.append(currentNode.value)
            else:
                levelArr.appendleft(currentNode.value)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        i = not i
        result.append(list(levelArr))
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(zigzag_traversal(root)))


main()
            