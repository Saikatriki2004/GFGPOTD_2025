from collections import deque
from typing import List

class Solution:
    def isBridge(self, V: int, edges: List[List[int]], c: int, d: int) -> bool:
        # Count occurrences of the edge (c, d)
        count = 0
        for u, v in edges:
            if (u == c and v == d) or (u == d and v == c):
                count += 1
        if count == 0:
            return False  # Edge doesn't exist
        if count > 1:
            return False  # Multiple edges, not a bridge
        
        # Build adjacency list
        adj = [[] for _ in range(V)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        # BFS to check connectivity after removing the edge (c, d)
        visited = [False] * V
        q = deque()
        q.append(c)
        visited[c] = True
        found = False
        
        while q:
            u = q.popleft()
            if u == d:
                found = True
                break
            for v in adj[u]:
                # Skip the edge (c, d) or (d, c)
                if (u == c and v == d) or (u == d and v == c):
                    continue
                if not visited[v]:
                    visited[v] = True
                    q.append(v)
        
        return not found
