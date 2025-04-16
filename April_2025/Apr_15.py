from typing import List

class Solution:
    def bellmanFord(self, V: int, edges: List[List[int]], src: int) -> List[int]:
        INF = 10**8
        dist = [INF] * V
        dist[src] = 0
        
        # Relax edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != INF and dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
        
        # Check for negative cycles
        has_negative_cycle = False
        for u, v, w in edges:
            if dist[u] != INF and dist[v] > dist[u] + w:
                has_negative_cycle = True
                break
        
        if has_negative_cycle:
            return [-1]
        else:
            return dist
