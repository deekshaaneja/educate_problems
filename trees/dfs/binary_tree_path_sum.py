class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path(currentNode, sum):
    if currentNode is None:
        return False
    if currentNode.value == sum and currentNode.left is None and currentNode.right is None:
        return True
    return has_path(currentNode.left, sum - currentNode.value) or has_path(currentNode.right, sum - currentNode.value)


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    # print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()