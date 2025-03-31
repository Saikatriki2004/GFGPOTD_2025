class Solution:
    def maxPartitions(self, s):
        last_occurrence = {}
        for i, char in enumerate(s):
            last_occurrence[char] = i  # this will store the last occurrence of each character
        
        used = set()
        result = 0
        i = 0
        n = len(s)
        
        while i < n:
            current_chars = set()
            current_end = i
            j = i
            while j <= current_end and j < n:
                char = s[j]
                if char not in used:
                    if char not in current_chars:
                        current_chars.add(char)
                        current_end = max(current_end, last_occurrence[char])
                j += 1
            # After processing this partition
            used.update(current_chars)
            result += 1
            i = current_end + 1
        
        return result
