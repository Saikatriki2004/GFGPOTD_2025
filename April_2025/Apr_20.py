class Solution:
    def findDuplicate(self, arr):
        n = len(arr)
        expected_sum = (n - 1) * n // 2
        actual_sum = sum(arr)
        return actual_sum - expected_sum
