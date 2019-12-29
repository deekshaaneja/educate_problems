from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def find_minimum_depth(self):
        queue = deque()
        queue.append(self)
        depth = 0
        while queue:
            lengthLevel = len(queue)
            depth += 1
            for i in range(lengthLevel):
                currentNode = queue.popleft()
                if not currentNode.left and not currentNode.right:
                    return depth
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
            # depth += 1


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(root.find_minimum_depth()))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(root.find_minimum_depth()))


main()