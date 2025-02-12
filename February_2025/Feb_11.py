class Solution:
    # Function to check whether a Binary Tree is BST or not.
    def isBST(self, root) -> bool:
        # Helper function with bounds.
        def isBSTUtil(node, min_val, max_val):
            # An empty node is considered valid.
            if node is None:
                return True
            
            # The current node's value must be strictly between min_val and max_val.
            if not (min_val < node.data < max_val):
                return False
            
            # Recursively check the left and right subtrees with updated bounds.
            return isBSTUtil(node.left, min_val, node.data) and isBSTUtil(node.right, node.data, max_val)
        
        # Start with the full range of possible values.
        return isBSTUtil(root, float('-inf'), float('inf'))
