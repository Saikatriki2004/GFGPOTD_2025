from collections import deque
from typing import List

class Solution:
    def isCycle(self, V: int, edges: List[List[int]]) -> bool:
        # Build adjacency list and in-degree array
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Initialize queue with all nodes of in-degree 0
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        processed_count = 0
        
        while queue:
            u = queue.popleft()
            processed_count += 1
            # Decrement in-degree for each neighbor
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        # If not all nodes are processed, there is a cycle
        return processed_count != V
