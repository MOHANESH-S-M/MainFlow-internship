# This is Task 8
""" 55. Serialize and Deserialize Binary Tree
 Objective     : Design an algorithm to serialize and deserialize a binary tree.
 Input         : A binary tree root.
 Output        : A serialized string for storing the tree and a deserialized tree from the string.
 Hint          : Use pre-order traversal for serialization and recursion for deserialization."""
import json

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root):
        def helper(node):
            if not node:
                return "null"
            return f"{node.val},{helper(node.left)},{helper(node.right)}"
        
        return helper(root)

    def deserialize(self, data):
        values = iter(data.split(','))
        
        def helper():
            val = next(values)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()
            return node
        
        return helper()

# Example usage:
codec = Codec()
tree = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
serialized = codec.serialize(tree)
print(serialized)
deserialized = codec.deserialize(serialized)
