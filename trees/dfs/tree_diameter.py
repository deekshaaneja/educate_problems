class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeDiameter:
    def __init__(self):
        self.treeDiameter = 0

    def find_diameter(self, root):
        pass

    def find_diameter_recursive(self, currentNode, currentPath, maxLen):
        if currentNode is None:
            return 
        currentPath.append(currentNode.value)
        maxLen = max(maxLen, len(currentPath))
        if currentNode.left == None and currentNode.right == None:
            return maxLen
        else:
            maxLen = maxLen(find_diameter_recursive())

