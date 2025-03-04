# This is Task 7
""" 53. Zigzag Level Order Traversal of Binary Tree
 Objective   : Traverse a binary tree in a zigzag level order.
 Input       : A binary tree root.
 Output      : A list of lists, where each list represents a level in zigzag order.
 Hint        : Use two stacks to alternate between left-to-right and right-to-left traversal."""
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def zigzag_level_order(root):
    if not root:
        return []
    result, queue, direction = [], deque([root]), 1
    while queue:
        level = deque()
        for _ in range(len(queue)):
            node = queue.popleft()
            if direction:
                level.append(node.val)
            else:
                level.appendleft(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(list(level))
        direction ^= 1
    return result

# Example
root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.left.right = TreeNode(4), TreeNode(5)
print(zigzag_level_order(root))
