class Solution:
    def countPS(self, s):
        n = len(s)
        count = 0
        
        # Iterate over each possible center
        for i in range(n):
            # Odd-length palindromes centered at i
            left = i
            right = i
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1
            
            # Even-length palindromes centered between i and i+1
            left = i
            right = i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                if right - left + 1 >= 2:
                    count += 1
                left -= 1
                right += 1
        
        return count
