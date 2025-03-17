class Solution:
    def isSubsetSum(self, arr, sum):
        # Initialize DP array
        dp = [False] * (sum + 1)
        dp[0] = True  # Sum of 0 is achievable with empty subset
        
        # Process each element in the array
        for num in arr:
            # Update dp array from sum down to num
            for j in range(sum, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        return dp[sum]
