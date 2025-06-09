import sys

class Solution:
    def isDeadEnd(self, root):
        # helper takes the allowable range [low..high]
        def dfs(node, low, high):
            # empty subtree → no dead end here
            if not node:
                return False
            # leaf: if low==high, there's no integer left to insert
            if not node.left and not node.right:
                return low == high
            # otherwise check both sides with tightened bounds
            return (dfs(node.left,  low,       node.data - 1) or
                    dfs(node.right, node.data + 1, high))
        
        # start with values ≥1 up to “infinity”
        return dfs(root, 1, sys.maxsize)
