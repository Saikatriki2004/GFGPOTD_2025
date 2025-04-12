import heapq

class Solution:
    def dijkstra(self, V, edges, src):
        # Define a large value for infinity (10^10 is safe given constraints)
        INF = 10**10
        
        # Build adjacency list: adj[u] contains list of (v, w) pairs
        adj = [[] for _ in range(V)]
        for edge in edges:
            u, v, w = edge
            adj[u].append((v, w))
            adj[v].append((u, w))  # Undirected graph
        
        # Initialize distances array
        distances = [INF] * V
        distances[src] = 0
        
        # Initialize min-heap with (distance, vertex) pairs
        heap = [(0, src)]
        
        # Track visited vertices
        visited = [False] * V
        
        # Process vertices until heap is empty
        while heap:
            distance, vertex = heapq.heappop(heap)
            
            # Skip if vertex is already visited
            if visited[vertex]:
                continue
            
            # Mark vertex as visited (its distance is now finalized)
            visited[vertex] = True
            
            # Check all neighbors
            for neighbor, weight in adj[vertex]:
                new_distance = distance + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(heap, (new_distance, neighbor))
        
        return distances
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
