from collections import defaultdict

class Solution:
    def findSubString(self, s):
        # Get all unique characters in the string
        unique_chars = set(s)
        required = len(unique_chars)
        if required == 0:
            return 0
        
        current_counts = defaultdict(int)
        left = 0
        min_len = float('inf')
        formed = 0
        
        for right in range(len(s)):
            char = s[right]
            current_counts[char] += 1
            
            # Check if this character just met the required count (1)
            if current_counts[char] == 1:
                formed += 1
            
            # Try to contract the window as long as it remains valid
            while formed == required and left <= right:
                current_window_size = right - left + 1
                if current_window_size < min_len:
                    min_len = current_window_size
                
                # Move the left pointer to try a smaller window
                left_char = s[left]
                current_counts[left_char] -= 1
                if current_counts[left_char] == 0:
                    formed -= 1
                left += 1
        
        return min_len if min_len != float('inf') else 0
