from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value =value
        self.left = left
        self.right = right

def level_order_traversal(root):
    q = deque()
    q.append(root)
    result = []
    while q:
        len_curr_level = len(q)
        curr_ls = []
        for i in range(len_curr_level):
            currentNode = q.popleft()
            curr_ls.append(currentNode.value)
            if currentNode.left:
                q.append(currentNode.left)
            if currentNode.right:
                q.append(currentNode.right)
        print(curr_ls)
        result.append(curr_ls)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(level_order_traversal(root)))


main()