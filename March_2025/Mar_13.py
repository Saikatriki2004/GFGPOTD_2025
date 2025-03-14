class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)  # Number of items
        dp = [0] * (W + 1)  # DP array of size W+1, initialized to 0
        
        # Process each item
        for i in range(n):
            # Update dp array from W down to wt[i]
            for w in range(W, wt[i] - 1, -1):
                if wt[i] <= w:  # If the item can fit
                    dp[w] = max(dp[w], val[i] + dp[w - wt[i]])
        
        return dp[W]  # Maximum value achievable with capacity W
