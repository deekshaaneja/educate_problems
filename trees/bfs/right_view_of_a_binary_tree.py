from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def tree_right_view(root):
    q = deque()
    q.append(root)
    res = []
    while q:
        currentSize = len(q)
        for i in range(len(q)):
            currentLevel = []
            currentNode = q.popleft()
            currentLevel.append(currentNode)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        res.append(currentLevel[-1])
    return res

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')

main()