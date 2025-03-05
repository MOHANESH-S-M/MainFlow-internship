# This is Task 8
""" 58. K-th Smallest Element in a BST
 Objective    : Find the K-th smallest element in a binary search tree (BST).
 Input        : A BST and an integer kkk.
 Output       : The K-th smallest element in the BST.
 Hint         : Perform an in-order traversal and return the K-th element."""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# Example usage:
tree = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(tree, 2))  # Output: 2
