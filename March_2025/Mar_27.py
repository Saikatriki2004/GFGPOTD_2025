class Solution:
    def minimumPlatform(self, arr, dep):
        # Sort arrival and departure times
        arr.sort()
        dep.sort()
        
        # Initialize variables
        i = 0              # Pointer for arrivals
        j = 0              # Pointer for departures
        platforms = 0      # Current number of platforms in use
        max_platforms = 0  # Maximum platforms needed
        
        # Process all events
        while i < len(arr) and j < len(dep):
            if arr[i] <= dep[j]:
                # Train arrives, need a platform
                platforms += 1
                i += 1
                max_platforms = max(max_platforms, platforms)
            else:
                # Train departs, free a platform
                platforms -= 1
                j += 1
        
        return max_platforms  # Corrected from max_platformse
