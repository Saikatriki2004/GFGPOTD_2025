class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        # If string length is 1, it's trivially a palindrome
        if n < 2:
            return s
        
        # Helper function to expand around a center
        def expand_around_center(left, right):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            # After loop, left and right are one step beyond the palindrome
            return left + 1, right - 1
        
        start = 0          # Starting index of the longest palindrome
        max_length = 1     # Length of the longest palindrome (at least 1)
        
        # Iterate through each possible center
        for i in range(n):
            # Check odd-length palindromes centered at i
            left, right = expand_around_center(i, i)
            length = right - left + 1
            if length > max_length:
                start = left
                max_length = length
            
            # Check even-length palindromes centered between i and i+1
            if i + 1 < n:
                left, right = expand_around_center(i, i + 1)
                length = right - left + 1
                if length > max_length:
                    start = left
                    max_length = length
        
        # Return the substring from start to start + max_length
        return s[start:start + max_length]
