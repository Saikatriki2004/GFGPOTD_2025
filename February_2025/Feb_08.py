# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def boundaryTraversal(self, root: Node) -> list:
        # Helper function to check if a node is a leaf.
        def isLeaf(node):
            return node.left is None and node.right is None

        if root is None:
            return []

        result = []
        
        # Add root data if it's not a leaf. If the tree has only one node,
        # it is both the boundary and the leaf.
        if not isLeaf(root):
            result.append(root.data)
        
        # Add left boundary (excluding leaves)
        cur = root.left
        while cur:
            if not isLeaf(cur):
                result.append(cur.data)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        # Add leaf nodes (from left to right)
        def addLeaves(node):
            if node is None:
                return
            if isLeaf(node):
                result.append(node.data)
            else:
                addLeaves(node.left)
                addLeaves(node.right)
        
        addLeaves(root)
        
        # Add right boundary in reverse order (excluding leaves)
        temp = []
        cur = root.right
        while cur:
            if not isLeaf(cur):
                temp.append(cur.data)
            if cur.right:
                cur = cur.right
            else:
                cur = cur.left
        
        # Append the right boundary in reverse
        result.extend(reversed(temp))
        
        return result
