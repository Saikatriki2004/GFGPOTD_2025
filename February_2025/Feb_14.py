# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def correctBST(self, root: Node) -> int:
        # Initialize pointers for the first, middle, last, and previous nodes.
        self.first = None
        self.middle = None
        self.last = None
        self.prev = None
        
        # Helper function: In-order traversal.
        def inorder(node: Node):
            if not node:
                return
            inorder(node.left)
            
            # Check for anomaly: previous node's value should be less than current node's value.
            if self.prev and self.prev.data > node.data:
                # If this is the first anomaly, mark these nodes as first and middle.
                if self.first is None:
                    self.first = self.prev
                    self.middle = node
                else:
                    # If anomaly is found again, update the last pointer.
                    self.last = node
            self.prev = node  # Update the previous node
            inorder(node.right)
        
        # Perform the in-order traversal to detect the swapped nodes.
        inorder(root)
        
        # Correct the BST by swapping the values of the misplaced nodes.
        if self.first and self.last:
            self.first.data, self.last.data = self.last.data, self.first.data
        elif self.first and self.middle:
            self.first.data, self.middle.data = self.middle.data, self.first.data
        
        # As per the problem specification, return 1 if the BST is corrected.
        return 1
