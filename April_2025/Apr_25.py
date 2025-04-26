#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        candidate = None
        count = 0
        
        # First pass to find the candidate using Boyer-Moore algorithm
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Second pass to verify the candidate is indeed the majority
        count_candidate = 0
        for num in arr:
            if num == candidate:
                count_candidate += 1
        
        # Check if the candidate's count exceeds half the array's length
        if count_candidate > len(arr) // 2:
            return candidate
        else:
            return -1


