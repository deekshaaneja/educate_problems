class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def count_paths(root, s):
    return count_paths_recursive(root, s, [])

def count_paths_recursive(currentNode, s, currentPath):
    if currentNode is None:
        return 0
    currentPath.append(currentNode.value)
    pathCount, pathSum = 0, 0
    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == s:
            pathCount += 1
    pathCount += count_paths_recursive(currentNode.left, s, currentPath)
    pathCount += count_paths_recursive(currentNode.right, s, currentPath)

    del currentPath[-1]
    return pathCount

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
    

