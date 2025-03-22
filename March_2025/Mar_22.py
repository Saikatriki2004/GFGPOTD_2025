class Solution:
    def maxValue(self, arr):
        def helper(start, end):
            prev = 0  # Max value excluding the previous house
            curr = 0  # Max value including up to the previous house
            for i in range(start, end):
                temp = curr
                curr = max(curr, prev + arr[i])
                prev = temp
            return curr
        
        n = len(arr)
        # Since constraints guarantee n >= 2, we can skip edge cases for n < 2
        # Case 1: Exclude first house, rob from index 1 to n-1
        max1 = helper(1, n)
        # Case 2: Exclude last house, rob from index 0 to n-2
        max2 = helper(0, n-1)
        return max(max1, max2)
