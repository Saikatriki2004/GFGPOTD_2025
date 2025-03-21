class Solution:
    def findMaxSum(self, arr):
        n = len(arr)
        # Base case: if array is empty (optional due to n ≥ 1 constraint)
        if n == 0:
            return 0
        # Base case: if only one house
        if n == 1:
            return arr[0]
        
        # Initialize variables
        prev2 = 0  # Max loot up to two houses back
        prev = arr[0]  # Max loot up to previous house
        
        # Iterate from second house to the last
        for i in range(1, n):
            # Max loot if we loot current house vs skip it
            current = max(prev, prev2 + arr[i])
            # Update previous values
            prev2 = prev
            prev = current
        
        return prev
