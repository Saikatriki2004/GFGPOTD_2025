class Solution:
    def findMaxFork(self, root, k):
        result = None
        current = root
        
        while current:
            if current.data == k:
                return current.data
            elif current.data < k:
                if (result is None) or (current.data > result):
                    result = current.data
                current = current.right
            else:
                current = current.left
        
        return result if result is not None else -1
