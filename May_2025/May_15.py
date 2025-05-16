class Solution:
    def countSubstring(self, s: str) -> int:
        """
        Count all substrings of s which start and end with the same character.
        Time: O(n), Space: O(1) (just a fixed-size array of length 26).
        """
        # frequency of each lowercase letter
        freq = [0] * 26
        base = ord('a')
        for ch in s:
            freq[ord(ch) - base] += 1

        total = 0
        for cnt in freq:
            # for each character: cnt single-char substrings + C(cnt,2) longer ones
            total += cnt * (cnt + 1) // 2
        return total
