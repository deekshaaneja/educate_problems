
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(1)
root.right.right = TreeNode(5)

def unipath(root):
    if root is None:
        return 0

    left = unipath(root.left)
    right = unipath(root.right)

    if root.left is not None and root.right is not None and root.value == root.left.value and root.value == root.right.value:
        return 1 + max(left, right)
    elif root.left is not None and root.value == root.left.value:
        return 1 + left
    elif root.right is not None and root.value == root.right.value:
        return 1 + right
    else:
        return max(1, left, right)

print(unipath(root))
