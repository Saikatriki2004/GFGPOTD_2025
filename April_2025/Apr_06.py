from collections import deque

class Solution:
    def topoSort(self, V, edges):
        adj = [[] for _ in range(V)]
        in_degree = [0] * V
        
        # Build adjacency list and in-degree array
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
        
        # Initialize queue with all nodes of in-degree 0
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)
        
        topo_order = []
        while queue:
            u = queue.popleft()
            topo_order.append(u)
            # Reduce in-degree for each neighbor
            for v in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        
        return topo_order
