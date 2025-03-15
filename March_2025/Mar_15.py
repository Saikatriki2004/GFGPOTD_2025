class Solution:
    def minCoins(self, coins, sum):
        # Create DP array with size sum + 1, initialized to "infinity"
        dp = [sum + 1] * (sum + 1)
        dp[0] = 0  # Base case: 0 coins needed for sum 0
        
        # Process each coin
        for coin in coins:
            # Update dp[i] for all sums from coin to sum
            for i in range(coin, sum + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return result: -1 if impossible, otherwise dp[sum]
        return dp[sum] if dp[sum] <= sum else -1
