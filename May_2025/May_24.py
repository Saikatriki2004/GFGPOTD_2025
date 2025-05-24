class Solution:
    def sumSubstrings(self, s: str) -> int:
        """
        Given a numeric string s, returns the sum of all substrings
        interpreted as integers.
        """
        total = 0
        # f will hold the sum of all substrings ending at the current position
        f = 0

        # We’ll use 1-based indexing in the math below, but
        # iterate 0-based over Python’s string.
        for i, ch in enumerate(s):
            digit = ord(ch) - ord('0')
            # Recurrence: 
            # f_i = 10 * f_{i-1} + (i+1) * digit
            f = f * 10 + (i + 1) * digit
            # Add all substrings ending here into total
            total += f

        return total
