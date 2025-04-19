class Solution:
    def maxXor(self, arr):
        max_xor = 0
        mask = 0
        # Iterate from the highest bit down to the lowest (30 bits covers up to 2^30 which is sufficient for 1e6)
        for i in range(30, -1, -1):
            mask |= (1 << i)  # Update the mask to include the current bit
            candidate = max_xor | (1 << i)  # Try to set this bit in the candidate max_xor
            prefixes = set()
            found = False
            for num in arr:
                current_prefix = num & mask  # Apply the mask to get the higher bits up to i
                # Check if there's a prefix that XORs with current_prefix to give the candidate
                if (current_prefix ^ candidate) in prefixes:
                    found = True
                    break
                prefixes.add(current_prefix)
            if found:
                max_xor = candidate  # Update max_xor if the candidate is achievable
        return max_xor
