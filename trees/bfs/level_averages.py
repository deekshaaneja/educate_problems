from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def level_averages(root):
    q = deque()
    result = []
    q.append(root)
    while q:
        levelSize = len(q)
        levelArr = []
        for _ in range(levelSize):
            currentNode = q.popleft()
            levelArr.append(currentNode.value)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        result.append(sum(levelArr)/len(levelArr))
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(level_averages(root)))


main()