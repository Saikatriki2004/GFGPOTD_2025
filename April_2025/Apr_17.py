import heapq

class Solution:
    def findMinCycle(self, V, edges):
        def dijkstra(adj, start, end):
            n = len(adj)
            dist = [float('inf')] * n
            dist[start] = 0
            heap = [(0, start)]
            visited = [False] * n
            
            while heap:
                current_dist, u = heapq.heappop(heap)
                if visited[u]:
                    continue
                visited[u] = True
                if u == end:
                    break
                for v, w in adj[u]:
                    if not visited[v] and dist[v] > current_dist + w:
                        dist[v] = current_dist + w
                        heapq.heappush(heap, (dist[v], v))
            return dist[end]
        
        min_cycle = float('inf')
        
        for edge in edges:
            u, v, w = edge
            new_edges = []
            for e in edges:
                x, y, weight = e
                if (x == u and y == v and weight == w) or (x == v and y == u and weight == w):
                    continue
                new_edges.append(e)
            
            new_adj = [[] for _ in range(V)]
            for x, y, weight in new_edges:
                new_adj[x].append((y, weight))
                new_adj[y].append((x, weight))
            
            shortest_path = dijkstra(new_adj, u, v)
            if shortest_path != float('inf'):
                candidate = shortest_path + w
                if candidate < min_cycle:
                    min_cycle = candidate
        
        return min_cycle if min_cycle != float('inf') else -1
