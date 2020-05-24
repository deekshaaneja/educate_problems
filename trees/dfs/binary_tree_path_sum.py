class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def has_path(root, k):
    allPaths = []
    return find_paths(root, k, [], allPaths)

def find_paths(currentNode, currentSum, currentPath, allPaths):
    allPaths.append(currentNode.value)
    if currentNode is None:
        return numPaths
    if currentNode.value == currentSum:
        numPaths += 1
    find_paths(currentNode.left, currentSum-currentNode.value, numPaths)
    find_paths(currentNode.right, currentSum-currentNode.value, numPaths)



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