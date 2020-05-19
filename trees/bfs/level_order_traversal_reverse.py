from queue import deque

class  TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def traverse(root):
    q = deque()
    q.append(root)
    result = deque()
    while q:
        length = len(q)
        currentLevel = []
        for _ in range(length):
            currentNode = q.popleft()
            currentLevel.append(currentNode.value)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        result.appendleft(currentLevel)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()