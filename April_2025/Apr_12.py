from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # If the starting pixel is already the new color, return the image as is
        if image[sr][sc] == newColor:
            return image
        
        # Get the original color and grid dimensions
        original_color = image[sr][sc]
        n, m = len(image), len(image[0])
        
        # Initialize queue with the starting pixel
        queue = deque([(sr, sc)])
        
        # Process pixels using BFS
        while queue:
            r, c = queue.popleft()
            # Only update if the pixel still has the original color
            if image[r][c] == original_color:
                image[r][c] = newColor
                # Check all 4-directional neighbors
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    # If neighbor is within bounds and has original color, add to queue
                    if 0 <= nr < n and 0 <= nc < m and image[nr][nc] == original_color:
                        queue.append((nr, nc))
        
        return image



#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends
