from collections import deque

class Solution:
    @staticmethod
    def findOrder(words):
        if not words:
            return ""
        
        # Collect all unique characters
        chars = set()
        for word in words:
            for c in word:
                chars.add(c)
        if not chars:
            return ""
        
        # Initialize adjacency list and in-degree dictionary
        adj = {c: set() for c in chars}
        in_degree = {c: 0 for c in chars}
        
        # Process consecutive word pairs to build the graph
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]
            min_len = min(len(word1), len(word2))
            found = False
            for j in range(min_len):
                c1 = word1[j]
                c2 = word2[j]
                if c1 != c2:
                    # Add edge from c1 to c2 if not already present
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        in_degree[c2] += 1
                    found = True
                    break
            if not found:
                # Check if the first word is longer than the second, which is invalid
                if len(word1) > len(word2):
                    return ""
        
        # Perform Kahn's algorithm for topological sort
        queue = deque([c for c in chars if in_degree[c] == 0])
        order = []
        
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all characters are included (no cycles)
        if len(order) != len(chars):
            return ""
        
        return ''.join(order)
