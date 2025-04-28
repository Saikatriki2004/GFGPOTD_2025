class Solution:
    def getMaxSum(self, root):
        if not root:
            return 0
        
        take_notake = { None: (0, 0) }
        stack = [(root, False)]
        
        while stack:
            node, processed = stack.pop()
            if not processed:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
            else:
                left_take, left_notake = take_notake[node.left]
                right_take, right_notake = take_notake[node.right]
                take = node.data + left_notake + right_notake
                notake = max(left_take, left_notake) + max(right_take, right_notake)
                take_notake[node] = (take, notake)
        
        max_take, max_notake = take_notake[root]
        return max(max_take, max_notake)
