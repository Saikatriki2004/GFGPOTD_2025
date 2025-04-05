from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    self.bfs(grid, i, j, rows, cols)
                    count += 1
        return count
    
    def bfs(self, grid: List[List[str]], i: int, j: int, rows: int, cols: int) -> None:
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),           (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        queue = deque()
        queue.append((i, j))
        grid[i][j] = 'W'  # Mark as visited
        
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 'L':
                    grid[nx][ny] = 'W'  # Mark as visited before enqueueing
                    queue.append((nx, ny))
