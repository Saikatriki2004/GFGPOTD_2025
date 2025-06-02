class Solution:
    def uniquePaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        Given an n×m grid of 0’s (free) and 1’s (blocked), count how many ways to go
        from top-left (0,0) to bottom-right (n-1,m-1), moving only right or down.
        """

        # If grid is empty
        if not grid or not grid[0]:
            return 0

        n, m = len(grid), len(grid[0])
        # 1D DP array: dp[j] = # of ways to reach cell (current_row, j)
        dp = [0] * m

        # Initialize dp[0] based on the starting cell (0,0).
        # If grid[0][0] is blocked (1), then no path even starts.
        dp[0] = 1 if grid[0][0] == 0 else 0

        # Fill in first row (i = 0).  You can only come from the left.
        for j in range(1, m):
            if grid[0][j] == 1:
                dp[j] = 0
            else:
                dp[j] = dp[j - 1]  # inherit from the cell immediately to the left

        # Now process rows i = 1..n-1
        for i in range(1, n):
            # Update dp[0] for the first column of the new row.
            # You can only come from above (i-1,0), which is dp[0] before overwriting.
            if grid[i][0] == 1:
                dp[0] = 0
            # otherwise dp[0] stays as it was (number of ways to reach the cell above),
            # because there is no "left cell" for j=0.

            # Update the rest of columns j = 1..m-1 in this row
            for j in range(1, m):
                if grid[i][j] == 1:
                    dp[j] = 0  # blocked cell ⇒ zero ways
                else:
                    # dp[j] (old value) is “ways from above”; dp[j-1] is “ways from left”
                    dp[j] = dp[j] + dp[j - 1]

        # dp[m-1] now holds the number of ways to reach (n-1, m-1)
        return dp[m - 1]
