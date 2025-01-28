from itertools import permutations

class Solution:
    def findPermutation(self, s):
        # Generate all permutations using itertools
        all_permutations = set(permutations(s))
        # Convert each tuple back to a string
        unique_permutations = [''.join(p) for p in all_permutations]
        # Return the sorted list (optional for consistency)
        return sorted(unique_permutations)
