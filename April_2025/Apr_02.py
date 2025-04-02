from collections import deque

class Solution:
    def bfs(self, adj):
        if not adj:
            return []
        
        n = len(adj)
        visited = [False] * n
        queue = deque([0])
        visited[0] = True
        result = []
        
        while queue:
            u = queue.popleft()
            result.append(u)
            for v in adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
        
        return result
