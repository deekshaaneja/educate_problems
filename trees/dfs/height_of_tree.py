class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def find_height(root):
    if root is None:
        return 0
    left_height = find_height(root.left)
    right_height = find_height(root.right)
    return 1 + max(left_height, right_height)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.right.right = TreeNode(8)

    print("Tree has height: " + str(find_height(root)))


main()