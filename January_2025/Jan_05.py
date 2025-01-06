class Solution:
    def countPairs(self, arr, target):
        # Sort the array
        arr.sort()
        count = 0
        left, right = 0, len(arr) - 1
        
        # Two-pointer approach
        while left < right:
            if arr[left] + arr[right] < target:
                # All pairs (arr[left], arr[left+1]...arr[right]) are valid
                count += (right - left)
                left += 1
            else:
                right -= 1
        
        return count
