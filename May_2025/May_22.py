class Solution:
    def minDeletions(self, s: str) -> int:
        """
        Returns the minimum number of deletions needed to make s a palindrome.
        This equals len(s) minus the length of the longest palindromic subsequence (LPS).
        We compute LPS by finding the LCS between s and its reverse.
        Time: O(n^2), Space: O(n^2), where n = len(s)
        """
        n = len(s)
        # s_rev is the reverse of s
        s_rev = s[::-1]

        # dp[i][j] = LCS length of s[:i] and s_rev[:j]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s_rev[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        lps = dp[n][n]
        return n - lps
