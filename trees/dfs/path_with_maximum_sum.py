class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_maximum_path_sum(root):
    allPaths = []
    maxSum = max_sum_path_rec(root, [], allPaths, 0)
    return maxSum

def max_sum_path_rec(currentNode, currentPath, allPaths, maxSum):
    if currentNode is None:
        pass
    currentPath.append(currentNode.value)
    if currentNode.left:
        


def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))


main()


