class Solution:
    def longestCommonSum(self, a1, a2):
        """
        :type a1: List[int]
        :type a2: List[int]
        :rtype: int
        """
        n = len(a1)
        # map from prefix‐sum to earliest index at which it occurred
        first_idx = {}
        max_len = 0
        prefix = 0
        
        for i in range(n):
            # build diff array on the fly:
            prefix += (a1[i] - a2[i])
            
            if prefix == 0:
                # from 0..i sums to 0
                max_len = i + 1
            else:
                # if we've seen this prefix before, 
                # subarray (first_idx[prefix]+1 .. i) sums to 0
                if prefix in first_idx:
                    curr_len = i - first_idx[prefix]
                    if curr_len > max_len:
                        max_len = curr_len
                else:
                    # record first time we see this prefix
                    first_idx[prefix] = i
        
        return max_len
