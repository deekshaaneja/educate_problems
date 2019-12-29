class TreeNode:
    def __init__(self, val, left=None, right = None):
        self.left = left
        self.right = right
        self.val = val

def find_paths(root, sum):
    allPaths = []
    find_paths_recursive(root, sum, [],allPaths)
    return allPaths

def find_paths_recursive(currentNode, sum, currentPath, allPaths):
    if currentNode is None:
        return
    currentPath.append(currentNode.val)

    if currentNode.val == sum and currentNode.left == None and currentNode.right == None:
        allPaths.append(list(currentPath))
    else:
        find_paths_recursive(currentNode.left, sum-currentNode.val, currentPath, allPaths)
        find_paths_recursive(currentNode.left, sum-currentNode.val, currentPath, allPaths)
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
            ": " + str(find_paths(root, sum)))


main()