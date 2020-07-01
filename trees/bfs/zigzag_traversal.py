from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right= None):
        self.value = value
        self.left = left
        self.right = right

def zigzag_traversal(root):
    queue = deque()
    queue.append(root)
    isRev = False
    result = []
    while queue:
        lenCurrLevel = len(queue)
        currLevel = deque()
        for i in range(lenCurrLevel):
            currNode = queue.popleft()
            if isRev == True:
                currLevel.appendleft(currNode.value)
            else:
                currLevel.append(currNode.value)
            if currNode.left:
                queue.append(currNode.left)
            if currNode.right:
                queue.append(currNode.right)
        isRev = not isRev
        result.append(list(currLevel))
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
            