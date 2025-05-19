from collections import deque

class Solution:
    def findSpiral(self, root):
        """
        Returns the spiral (zigzag) level-order traversal of a binary tree.
        
        Even-numbered levels (0, 2, 4, …) are output right-to-left;
        odd-numbered levels (1, 3, 5, …) are output left-to-right.
        
        :param root: TreeNode, the root of the binary tree
        :return: List[int], the spiral order traversal
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])
        level = 0
        
        while queue:
            size = len(queue)
            # collect values of this level
            level_vals = []
            
            for _ in range(size):
                node = queue.popleft()
                level_vals.append(node.data)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # decide order based on level index
            if level % 2 == 0:
                # even level: right-to-left
                result.extend(reversed(level_vals))
            else:
                # odd level: left-to-right
                result.extend(level_vals)
            
            level += 1
        
        return result
