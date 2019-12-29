from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None
    def traverse(self):
        queue = deque()
        queue.append(self)
        result = []
        flag = True
        while queue:
            currentLevel = deque()
            levelLength = len(queue)
            for i in range(levelLength):
                currentNode = queue.popleft()
                if flag == True:
                    currentLevel.append(currentNode.value)
                else:
                    currentLevel.appendleft(currentNode.value)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            flag = not flag
            result.append(currentLevel)
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
    print("Zigzag traversal: " + str(root.traverse()))


main()