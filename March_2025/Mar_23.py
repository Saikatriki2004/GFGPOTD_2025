class Solution:
    def countWays(self, digits):
        n = len(digits)
        # Initialize for empty string and first digit
        prev2 = 1  # dp[0]
        if digits[0] != '0':
            prev1 = 1  # dp[1]
        else:
            prev1 = 0  # dp[1]
        if n == 1:
            return prev1
        # Process from second digit onward
        for i in range(2, n + 1):
            current = 0
            # Check if current digit can be decoded alone
            if digits[i - 1] != '0':
                current += prev1
            # Check if last two digits can be decoded together
            if 10 <= int(digits[i - 2:i]) <= 26:
                current += prev2
            # Update previous values
            prev2 = prev1
            prev1 = current
        return prev1
