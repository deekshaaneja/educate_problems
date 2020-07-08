import math

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def checkBST(root):
    maxValue = math.inf
    minValue = - math.inf
    return isBSTRec(root, minValue, maxValue)

def isBSTRec(currentNode, minValue, maxValue):
    if currentNode.value > maxValue or currentNode.value < minValue:
        return False
    if currentNode.left is None and currentNode.right is None and currentNode.value < maxValue and currentNode.value > minValue:
        return True
    if currentNode.left is not None:
        return isBSTRec(currentNode.left, minValue, currentNode.value)
    if currentNode.right is not None:
        return isBSTRec(currentNode.right, currentNode.value, maxValue)


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