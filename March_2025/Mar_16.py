class Solution:
    def minJumps(self, arr):
        n = len(arr)
        # Base case: if array has 1 or fewer elements, no jumps needed
        if n <= 1:
            return 0
        # If first element is 0, can't move anywhere
        if arr[0] == 0:
            return -1
        
        # Initialize for the first jump
        jumps = 1
        maxReach = arr[0]
        steps = arr[0]
        
        # Traverse from index 1 to n-1
        for i in range(1, n):
            # If we’ve reached the last index, return jumps
            if i == n - 1:
                return jumps
            
            # Update the farthest we can reach
            maxReach = max(maxReach, i + arr[i])
            # Use one step to move to the current position
            steps -= 1
            
            # If no steps remain, take a new jump
            if steps == 0:
                jumps += 1
                # If we can’t reach beyond current position, impossible
                if i >= maxReach:
                    return -1
                # Set steps to the remaining distance in the new range
                steps = maxReach - i
        
        # If we exit the loop without reaching the end, it’s impossible
        return -1
