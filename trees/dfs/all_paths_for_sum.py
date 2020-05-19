class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_paths(root, sum):
    allPaths = []
    find_path_sum(root, [], allPaths, sum) 
    return allPaths

    

def find_path_sum(currentNode, currentPath, allPaths, sum):
    if currentNode is None:
        return 
    currentPath.append(currentNode.value)
    if currentNode.value == sum and currentNode.left is None and currentNode.right is None:
        allPaths.append(list(currentPath))
    else:
        find_path_sum(currentNode.left, currentPath, allPaths, sum - currentNode.value)
        find_path_sum(currentNode.right, currentPath, allPaths, sum - currentNode.value)
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