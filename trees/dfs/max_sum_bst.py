class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def max_sum_bst(root):
    if root is None:
        return 0

    left_sum = max_sum_bst(root.left)
    right_sum = max_sum_bst(root.right)
    return root.value + max(left_sum, right_sum)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    # root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    # print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(max_sum_bst(root)))


main()