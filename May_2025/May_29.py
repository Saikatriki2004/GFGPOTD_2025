class Solution:
    def sumOfLongRootToLeafPath(self, root):
        if not root:
            return 0  # According to constraints, root is not null, but this handles edge case
        
        memo = {}
        stack = [(root, False)]
        
        while stack:
            node, visited = stack.pop()
            
            if not visited:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                if not node.left and not node.right:
                    memo[node] = (1, node.data)
                else:
                    left_depth = 0
                    left_sum = 0
                    if node.left:
                        left_depth, left_sum = memo.get(node.left, (0, 0))
                    right_depth = 0
                    right_sum = 0
                    if node.right:
                        right_depth, right_sum = memo.get(node.right, (0, 0))
                    
                    if left_depth > right_depth:
                        current_depth = left_depth
                        current_sum = left_sum
                    elif right_depth > left_depth:
                        current_depth = right_depth
                        current_sum = right_sum
                    else:
                        current_depth = left_depth
                        current_sum = max(left_sum, right_sum)
                    
                    current_depth += 1
                    current_sum += node.data
                    memo[node] = (current_depth, current_sum)
        
        return memo[root][1]
