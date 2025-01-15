class Solution:
    def findEquilibrium(self, arr):
        # Step 1: Calculate the total sum of the array
        total_sum = sum(arr)
        
        # Step 2: Initialize left_sum
        left_sum = 0
        
        # Step 3: Iterate through the array
        for i in range(len(arr)):
            # Calculate right sum
            right_sum = total_sum - left_sum - arr[i]
            
            # Check for equilibrium
            if left_sum == right_sum:
                return i
            
            # Update left_sum for the next index
            left_sum += arr[i]
        
        # Step 4: Return -1 if no equilibrium is found
        return -1
