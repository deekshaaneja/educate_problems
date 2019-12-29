from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def find_successor(self, node):
        queue = deque()
        queue.append(self)
        while queue:
            currentLevel = []
            lenCurrent = len(queue)
            for i in range(lenCurrent):
                currentNode = queue.popleft()
                currentLevel.append(currentNode.value)
                if currentNode.value == node:
                    if len(queue) >= 1:
                        return queue.popleft()
                    if len(queue) == 0:
                        if currentNode.left:
                            queue.append(currentNode.left)
                            return currentNode.left
                        if currentNode.right:
                            queue.append(currentNode.right)
                            return currentNode.right
                else:
                    if currentNode.left:
                        queue.append(currentNode.left)
                    if currentNode.right:
                        queue.append(currentNode.right)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = root.find_successor(12)
    if result:
        print(result.value)
    result = root.find_successor(9)
    if result:
        print(result.value)


main()
