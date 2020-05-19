class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_path(root, sequence):
    if not root:
        return len(sequence) == 0
    return find_paths_recursive(root, sequence, 0)

def find_paths_recursive(currentNode, sequence, sequenceIndex):
    if currentNode is None:
        return False
    seqLen = len(sequence)
    if sequenceIndex >= seqLen or currentNode.value != sequence[sequenceIndex]:
        return False
    elif sequenceIndex == len(sequence) - 1 and currentNode.value == sequence[sequenceIndex]:
        return True
    else:
        if currentNode.value == sequence[sequenceIndex]:
            return find_paths_recursive(currentNode.left, sequence, sequenceIndex+1) or find_paths_recursive(currentNode.right, sequence, sequenceIndex+1)

def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()