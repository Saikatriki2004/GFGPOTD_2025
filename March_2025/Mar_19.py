class Solution:
    def maxProfit(self, prices, k):
        n = len(prices)
        if n <= 1 or k == 0:
            return 0
        
        # If k is large enough, take all possible profits
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit
        
        # Initialize DP table: dp[t][d] = max profit with t transactions up to day d
        dp = [[0] * n for _ in range(k + 1)]
        
        # For each transaction count
        for t in range(1, k + 1):
            # max_prev represents max(dp[t-1][b-1] - prices[b]) up to the previous day
            max_prev = -prices[0]
            # For each day
            for d in range(1, n):
                # Option 1: Do nothing
                dp[t][d] = dp[t][d - 1]
                # Option 2: Sell on day d
                dp[t][d] = max(dp[t][d], prices[d] + max_prev)
                # Update max_prev for the next day
                max_prev = max(max_prev, dp[t - 1][d - 1] - prices[d])
        
        return dp[k][n - 1]
