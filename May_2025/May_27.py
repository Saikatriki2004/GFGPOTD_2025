class Solution:
    def leafNodes(self, preorder):
        """
        :type preorder: List[int]
        :rtype: List[int]
        """
        n = len(preorder)
        idx = 0
        leaves = []
        
        def dfs(min_val, max_val):
            nonlocal idx
            # If we're out of elements or the next element
            # does not lie in the (min_val, max_val) range,
            # there's no node to consume here.
            if idx >= n or not (min_val < preorder[idx] < max_val):
                return False
            
            root = preorder[idx]
            idx += 1
            
            # Try to build left subtree with valid keys < root
            left_used = dfs(min_val, root)
            # Then right subtree with valid keys > root
            right_used = dfs(root, max_val)
            
            # If neither child exists, this was a leaf
            if not left_used and not right_used:
                leaves.append(root)
            
            # We did consume one node at this call
            return True
        
        # Start recursion over the full key range
        dfs(float('-inf'), float('inf'))
        return leaves
