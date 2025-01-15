class Solution:
    def longestSubarray(self, arr, k):  
        prefix_sum_map = {}
        current_sum = 0
        max_length = 0
        
        for i in range(len(arr)):
            current_sum += arr[i]
            
            # Check if the current sum itself is equal to k
            if current_sum == k:
                max_length = i + 1
            
            # Check if there is a prefix sum that when subtracted gives k
            if (current_sum - k) in prefix_sum_map:
                max_length = max(max_length, i - prefix_sum_map[current_sum - k])
            
            # Record the first occurrence of the current_sum
            if current_sum not in prefix_sum_map:
                prefix_sum_map[current_sum] = i
        
        return max_length
