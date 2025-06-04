class Solution:
    def lcsOf3(self, s1, s2, s3):
        # Let n, m, p be the lengths of s1, s2, s3
        n, m, p = len(s1), len(s2), len(s3)

        # Create a 3D DP array of size (n+1) x (m+1) x (p+1)
        # dp[i][j][k] = length of LCS of s1[:i], s2[:j], s3[:k]
        dp = [[[0] * (p + 1) for _ in range(m + 1)] for __ in range(n + 1)]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                for k in range(1, p + 1):
                    if s1[i - 1] == s2[j - 1] == s3[k - 1]:
                        # If the current character matches in all three strings,
                        # extend the previous LCS by 1.
                        dp[i][j][k] = 1 + dp[i - 1][j - 1][k - 1]
                    else:
                        # Otherwise, take the maximum among dropping one index
                        dp[i][j][k] = max(
                            dp[i - 1][j][k],
                            dp[i][j - 1][k],
                            dp[i][j][k - 1]
                        )

        # The answer is dp[n][m][p]
        return dp[n][m][p]
