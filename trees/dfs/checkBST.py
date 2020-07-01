import math

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def checkBST(root):
    max_num = math.inf
    min_num = - math.inf
    return checkBSTRec(root, max_num, min_num)

def checkBSTRec(root, max_num, min_num):
    if root == None:
        return True
    if root.value > max_num or root.value < min_num:
        return False
    if root.right is not None and root.left is None:
        return False
    if root.left is not None and root.right is None:
        return False 
    return checkBSTRec(root.left, root.value, min_num) and checkBSTRec(root.right, max_num, root.value)

def main():
    root = TreeNode(6)
    root.left = TreeNode(3)
    root.right = TreeNode(9)
    root.left.left = TreeNode(1)
    root.left.right= TreeNode(5)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(11)
    print(checkBST(root))

main()