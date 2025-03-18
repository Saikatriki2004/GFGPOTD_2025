class Solution:
    def equalPartition(self, arr):
        # Calculate total sum of the array
        total_sum = sum(arr)
        
        # If total sum is odd, equal partition is impossible
        if total_sum % 2 != 0:
            return False
        
        # Target sum for each subset
        target = total_sum // 2
        
        # Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True  # Sum of 0 is possible with empty subset
        
        # Process each element in the array
        for num in arr:
            # Update dp array from target down to num
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # Return whether target sum is achievable
        return dp[target]
