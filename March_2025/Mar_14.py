class Solution:
    def count(self, coins, sum):
        # Initialize dp array with 0s
        dp = [0] * (sum + 1)
        # Base case: one way to make sum 0
        dp[0] = 1
        
        # Process each coin
        for coin in coins:
            # Update dp for all sums from coin to sum
            for s in range(coin, sum + 1):
                dp[s] += dp[s - coin]
        
        return dp[sum]
