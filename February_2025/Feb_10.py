from collections import defaultdict

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def sumK(self, root: Node, k: int) -> int:
        self.count = 0  # Global counter to store the number of valid paths
        prefix = defaultdict(int)
        prefix[0] = 1  # Base case: one way to have a prefix sum of 0
        
        def dfs(node, curr_sum):
            if node is None:
                return
            
            # Update the current sum with the node's value
            curr_sum += node.data
            
            # Check if there is a prefix sum such that curr_sum - prefix_sum == k
            self.count += prefix[curr_sum - k]
            
            # Increment the count for the current prefix sum
            prefix[curr_sum] += 1
            
            # Recursively traverse left and right children
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            # Backtrack: remove the current prefix sum count as we return to the parent
            prefix[curr_sum] -= 1
        
        # Start DFS with initial sum 0
        dfs(root, 0)
        
        return self.count
