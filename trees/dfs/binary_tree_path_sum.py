class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def has_path(root, sum):
    return hasPathRec(root, sum)

def hasPathRec(currentNode, currentSum):
    if currentNode is None:
        return False
    currentSum -= currentNode.value
    if currentNode.left is None and currentNode.right is None and currentNode.value == currentSum:
        return True
    return hasPathRec(currentNode.left, currentSum) or hasPathRec(currentNode.right, currentSum)

def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()