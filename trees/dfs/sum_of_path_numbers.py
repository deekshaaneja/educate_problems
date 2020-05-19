class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_sum_of_path_numbers(root):
    return find_root_to_leaf_path_numbers(root, 0)

def find_root_to_leaf_path_numbers(currentNode, pathSum):
    if currentNode is None:
        return 0
    pathSum = 10 * pathSum + currentNode.value

    if currentNode.left == None and currentNode.right == None:
        return pathSum

    return find_root_to_leaf_path_numbers(currentNode.left, pathSum) + find_root_to_leaf_path_numbers(currentNode.right, pathSum)
    
def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()