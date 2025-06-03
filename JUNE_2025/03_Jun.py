class Solution:
    def countSubstr(self, s: str, k: int) -> int:
        # Helper to count substrings with at most K distinct characters
        def at_most_k(s: str, K: int) -> int:
            count = 0
            freq = [0] * 26
            distinct = 0
            left = 0

            for right, ch in enumerate(s):
                idx = ord(ch) - ord('a')
                if freq[idx] == 0:
                    distinct += 1
                freq[idx] += 1

                # Shrink from the left until we have at most K distinct
                while distinct > K:
                    left_idx = ord(s[left]) - ord('a')
                    freq[left_idx] -= 1
                    if freq[left_idx] == 0:
                        distinct -= 1
                    left += 1

                # All substrings ending at 'right' with the current 'left' are valid
                count += (right - left + 1)

            return count

        # Exactly k = at_most_k(k) - at_most_k(k - 1)
        if k == 0:
            return 0
        return at_most_k(s, k) - at_most_k(s, k - 1)
