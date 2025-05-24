class Solution:
    def noOfWays(self, m: int, n: int, x: int) -> int:
        """
        Returns the number of ways to get total sum x using n dice,
        each having faces numbered from 1 to m.
        Time: O(n * x * m)
        Space: O(n * x)
        """
        # Quick bounds check: smallest sum is n*1, largest is n*m
        if x < n or x > n * m:
            return 0

        # dp[d][s] = ways to get sum s with d dice
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Build up from 1 die to n dice
        for d in range(1, n + 1):
            # For each possible target sum s with d dice
            for s in range(d, min(x, d * m) + 1):
                total = 0
                # Try each face value k on the d-th die
                for k in range(1, m + 1):
                    if s - k >= 0:
                        total += dp[d - 1][s - k]
                dp[d][s] = total

        return dp[n][x]
