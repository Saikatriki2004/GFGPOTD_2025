# Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def LCA(self, root: Node, n1: Node, n2: Node) -> Node:
        while root:
            # Compare the data fields of the given nodes with the current node's data.
            if n1.data < root.data and n2.data < root.data:
                root = root.left
            elif n1.data > root.data and n2.data > root.data:
                root = root.right
            else:
                # Either one equals root or they lie on different sides.
                return root
        return None  # This line should never be reached if n1 and n2 are guaranteed to be in the BST.
