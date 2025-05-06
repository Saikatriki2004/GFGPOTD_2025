class Solution:
    def LeftView(self, root):
        # Base case: if tree is empty, return empty list
        if not root:
            return []
        
        # Initialize result list to store left view
        result = []
        
        # Queue for level order traversal
        queue = [(root, 0)]  # (node, level)
        current_level = -1
        
        # Perform level order traversal
        while queue:
            node, level = queue.pop(0)
            
            # If this is the first node of the current level, add to result
            if level > current_level:
                result.append(node.data)
                current_level = level
            
            # Add left child first (important for left view)
            if node.left:
                queue.append((node.left, level + 1))
            
            # Then add right child
            if node.right:
                queue.append((node.right, level + 1))
        
        return result
