class Solution:
    # Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # Sort the array
        arr.sort()
        n = len(arr)
        count = 0

        # Iterate over each possible largest side of the triangle
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            # Check for the triangle condition
            while i < j:
                if arr[i] + arr[j] > arr[k]:
                    count += (j - i)  # All pairs (i, i+1, ..., j-1) satisfy the condition
                    j -= 1
                else:
                    i += 1
        
        return count
