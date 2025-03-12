class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        if n == 2:
            return min(cost[0], cost[1])
        
        # Initialize costs for steps 0 and 1
        prev2 = cost[0]  # Cost to reach step 0
        prev1 = cost[1]  # Cost to reach step 1
        
        # Iterate from step 2 to n-1
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
        
        # Minimum cost to reach the top from n-1 or n-2
        return min(prev1, prev2)
