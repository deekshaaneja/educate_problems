from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def find_level_averages(self):
        queue = deque()
        queue.append(self)
        result = []
        while queue:
            currentLevelSum = 0
            lengthLevel = len(queue)
            for i in range(lengthLevel):
                currentNode = queue.popleft()
                currentLevelSum += currentNode.value
            if lengthLevel != 0:
                avg = currentLevelSum/lengthLevel
                result.append(avg)
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)
        return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(root.find_level_averages()))


main()