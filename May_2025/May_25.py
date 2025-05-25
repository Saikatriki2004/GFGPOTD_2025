import math
class Solution:
    def pythagoreanTriplet(self, arr):
        # Step 1: frequency map
        freq = {}
        for v in arr:
            freq[v] = freq.get(v, 0) + 1

        # Step 2: sorted distinct values
        vals = sorted(freq)

        # Precompute squares for speed
        # (but computing on the fly is also fine)
        for i, x in enumerate(vals):
            x2 = x*x
            for y in vals[i:]:
                y2 = y*y
                s = x2 + y2
                c = int(math.isqrt(s))
                # check perfect square
                if c*c != s:
                    continue
                # c must be a valid array value
                if c not in freq:
                    continue

                # Now check we have enough distinct indices:
                # Count how many of x,y,c are equal
                if x == y == c:
                    # need at least 3 occurrences
                    if freq[x] >= 3:
                        return True
                elif x == y:
                    # x==y!=c, need two x's and one c
                    if freq[x] >= 2 and freq[c] >= 1:
                        return True
                elif x == c:
                    # x==c!=y
                    if freq[x] >= 2 and freq[y] >= 1:
                        return True
                elif y == c:
                    # y==c!=x
                    if freq[y] >= 2 and freq[x] >= 1:
                        return True
                else:
                    # all distinct
                    return True

        return False
