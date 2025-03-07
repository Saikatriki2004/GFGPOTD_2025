class Solution:
    def longestPalinSubseq(self, s):
        n = len(s)
        # Initialize DP table with zeros
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s[n - j]:  # Compare s[i-1] with s[::-1][j-1]
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][n]
