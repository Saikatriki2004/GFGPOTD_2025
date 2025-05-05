class Solution:
    def findTarget(self, arr, target):
        if not arr:
            return -1
            
        n = len(arr)
        
        # Edge case: Single element array
        if n == 1:
            return 0 if arr[0] == target else -1
            
        # For almost sorted arrays where elements can be at adjacent positions,
        # we need to check mid and its neighbors
        left, right = 0, n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            # Check if the target is at mid
            if arr[mid] == target:
                return mid
                
            # Check adjacent positions if they're within bounds
            if mid > 0 and arr[mid - 1] == target:
                return mid - 1
                
            if mid < n - 1 and arr[mid + 1] == target:
                return mid + 1
                
            # Since the array was originally sorted and elements moved by at most one position,
            # if target is smaller than arr[mid-1], it must be in the left half
            if mid > 0 and target < arr[mid - 1]:
                right = mid - 2
            # If target is larger than arr[mid+1], it must be in the right half
            elif mid < n - 1 and target > arr[mid + 1]:
                left = mid + 2
            # If we can't make a clear decision, we reduce the search space by 1
            else:
                if target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1
