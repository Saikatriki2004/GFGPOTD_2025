from collections import deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution():
    def cloneGraph(self, node):
        if not node:
            return None
        
        visited = {}
        queue = deque([node])
        visited[node] = Node(node.val)
        
        while queue:
            current = queue.popleft()
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[current].neighbors.append(visited[neighbor])
        
        return visited[node]
