

class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# [90,69, ,49,89,null,52,null,null,null,null]




root = TreeNode(90)
root.left = TreeNode(69)
root.left.left = TreeNode(49)
root.left.right= TreeNode(89)
root.left.left.right = TreeNode(52)


# root.left.left = TreeNode(5)
# root.left.right= TreeNode(8)
# root.right = TreeNode(16)
# root.right.left = TreeNode(12)
# root.right.right = TreeNode(20)

def min_diff(root, max_value, max_node):

    if root is None:
        return

    if max_value == -1:
        min_diff(root.left, all_vals)

    all_values.append(root.value)
    min_diff(root.right, all_vals)


all_vals = []
min_diff(root, all_vals)

min_val = float('inf')
for i in range(len(all_vals)):
    if i == 0 :
        continue
    else:
        min_val = min(min_val, all_vals[i]-all_vals[i-1])

print(min_val)




