class Solution:
    def matrixMultiplication(self, arr):
        m = len(arr)        # Size of the input array
        N = m - 1          # Number of matrices
        dp = [[0] * (N + 1) for _ in range(N + 1)]  # DP table (1-based indexing)
        
        # Iterate over chain lengths from 2 to N
        for L in range(2, N + 1):
            # Iterate over starting points
            for i in range(1, N - L + 2):
                j = i + L - 1  # Ending point
                # Compute minimum cost for dp[i][j]
                dp[i][j] = min(dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j] 
                              for k in range(i, j))
        
        return dp[1][N]  # Minimum cost to multiply matrices M1 to MN
