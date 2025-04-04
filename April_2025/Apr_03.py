from collections import deque

class Solution:
    def orangesRotting(self, mat):
        n = len(mat)
        if n == 0:
            return -1
        m = len(mat[0])
        q = deque()
        fresh = 0
        
        # Initialize queue with all initial rotten oranges and count fresh
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 2:
                    q.append((i, j))
                elif mat[i][j] == 1:
                    fresh += 1
        
        # If there are no fresh oranges, return 0 immediately
        if fresh == 0:
            return 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        time = 0
        
        while q:
            level_size = len(q)
            for _ in range(level_size):
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    # Check if the neighbor is within bounds and is a fresh orange
                    if 0 <= ni < n and 0 <= nj < m and mat[ni][nj] == 1:
                        mat[ni][nj] = 2
                        fresh -= 1
                        q.append((ni, nj))
            # Increment time only if there are more oranges to process
            if q:
                time += 1
        
        # Check if all fresh oranges have been rotted
        return time if fresh == 0 else -1
