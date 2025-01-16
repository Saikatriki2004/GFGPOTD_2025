class Solution:
    def maxLen(self, arr):
        # Replace 0s with -1s
        arr = [-1 if x == 0 else 1 for x in arr]
        
        prefix_map = {}
        prefix_sum = 0
        max_len = 0

        for i, value in enumerate(arr):
            prefix_sum += value
            
            # If prefix_sum is 0, the subarray from the start to i has a sum of 0
            if prefix_sum == 0:
                max_len = max(max_len, i + 1)
            
            # If prefix_sum is seen before, calculate the subarray length
            if prefix_sum in prefix_map:
                max_len = max(max_len, i - prefix_map[prefix_sum])
            else:
                # Store the first occurrence of this prefix_sum
                prefix_map[prefix_sum] = i
        
        return max_len
