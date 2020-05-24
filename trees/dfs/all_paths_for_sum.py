class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def getAllPaths(root, sum):
    allPaths = []
    findPath(root, [], allPaths, sum)
    return allPaths


def findPath(currentNode, currentPath, allPaths, currentSum):
    if currentNode is None:
        return
    currentPath.append(currentNode.value)
    if currentNode.value == currentSum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    findPath(currentNode.left, currentPath, allPaths, currentSum-currentNode.value)
    findPath(currentNode.right, currentPath, allPaths, currentSum-currentNode.value)
    del currentPath[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
            ": " + str(getAllPaths(root, sum)))


main()