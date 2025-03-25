class Solution:
    def countWays(self, s):
        n = len(s)
        m = (n + 1) // 2  # Number of operands
        # Initialize DP tables
        true_ways = [[0] * m for _ in range(m)]
        false_ways = [[0] * m for _ in range(m)]
        
        # Base case: single operands
        for i in range(m):
            if s[2 * i] == 'T':
                true_ways[i][i] = 1
            else:  # s[2 * i] == 'F'
                false_ways[i][i] = 1
        
        # Iterate over all subexpression lengths
        for length in range(2, m + 1):
            for left in range(m - length + 1):
                right = left + length - 1
                # Try each split point
                for k in range(left, right):
                    op = s[2 * k + 1]
                    if op == '&':
                        true_ways[left][right] += true_ways[left][k] * true_ways[k + 1][right]
                        false_ways[left][right] += (true_ways[left][k] * false_ways[k + 1][right] +
                                                    false_ways[left][k] * true_ways[k + 1][right] +
                                                    false_ways[left][k] * false_ways[k + 1][right])
                    elif op == '|':
                        true_ways[left][right] += (true_ways[left][k] * true_ways[k + 1][right] +
                                                   true_ways[left][k] * false_ways[k + 1][right] +
                                                   false_ways[left][k] * true_ways[k + 1][right])
                        false_ways[left][right] += false_ways[left][k] * false_ways[k + 1][right]
                    elif op == '^':
                        true_ways[left][right] += (true_ways[left][k] * false_ways[k + 1][right] +
                                                   false_ways[left][k] * true_ways[k + 1][right])
                        false_ways[left][right] += (true_ways[left][k] * true_ways[k + 1][right] +
                                                    false_ways[left][k] * false_ways[k + 1][right])
        
        return true_ways[0][m - 1]
