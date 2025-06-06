class Solution:
    def search(self, pat, txt):
        """
        Returns a list of 1-based positions where 'pat' occurs in 'txt'.
        If there are no occurrences, returns an empty list.
        """

        n, m = len(txt), len(pat)
        if m == 0 or n < m:
            return []  # empty pattern or pattern longer than text → no matches

        # Step 1: Build LPS array for 'pat'.
        # lps[i] = length of the longest proper prefix of pat[:i+1]
        #          which is also a suffix of pat[:i+1].
        lps = [0] * m
        length = 0  # length of the previous longest prefix‐suffix
        i = 1
        while i < m:
            if pat[i] == pat[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    # fall back to the previous longest prefix‐suffix
                    length = lps[length - 1]
                    # (no increment of i here)
                else:
                    # no proper prefix that matches suffix at this point
                    lps[i] = 0
                    i += 1

        # Step 2: Scan 'txt' with two indices: i over txt, j over pat.
        res = []
        i = 0  # index in txt
        j = 0  # index in pat
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    # we found a complete match ending at txt[i-1].
                    # Start index in 'txt' (0-based) is i-j.
                    # Convert to 1-based:
                    res.append((i - j) + 1)
                    # Prepare j for the next possible match
                    j = lps[j - 1]
            else:
                if j != 0:
                    # slide pattern to the right, based on LPS
                    j = lps[j - 1]
                else:
                    i += 1

        return res
