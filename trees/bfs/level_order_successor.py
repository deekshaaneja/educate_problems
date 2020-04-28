from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_successor(root, target):
    q = deque()
    q.append(root)
    is_target = False
    while q:
        levelSize = len(q)
        for _ in range(levelSize):
            currentNode = q.popleft()
            if is_target == True:
                return currentNode
            if currentNode.value == target:
                is_target = True
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)

    return -1

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_successor(root, 12)
    if result:
        print(result.value)
    result = find_successor(root, 9)
    if result:
        print(result.value)


main()