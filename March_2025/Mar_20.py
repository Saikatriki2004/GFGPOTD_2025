class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        # If there are fewer than 2 prices, no profit is possible
        if n < 2:
            return 0
        
        # Array to store maximum profit from first transaction up to each day
        max_profit_first = [0] * n
        min_price = prices[0]
        for d in range(1, n):
            min_price = min(min_price, prices[d])
            max_profit_first[d] = max(max_profit_first[d-1], prices[d] - min_price)
        
        # Array to store maximum profit from second transaction from each day onwards
        max_profit_second = [0] * n
        max_price = prices[-1]
        for d in range(n-2, -1, -1):
            max_price = max(max_price, prices[d])
            max_profit_second[d] = max(max_profit_second[d+1], max_price - prices[d])
        
        # Find the maximum total profit by combining the two transactions
        max_profit = max_profit_first[-1]  # Case of only one transaction
        for d in range(n-1):
            total = max_profit_first[d] + max_profit_second[d+1]
            max_profit = max(max_profit, total)
        
        return max_profit
