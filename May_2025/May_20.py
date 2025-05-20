from collections import defaultdict, deque

# Definition for a binary tree node.
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def minTime(self, root: Node, target: int) -> int:
        if not root:
            return 0

        # 1) Build an adjacency list over node values.
        adj = defaultdict(list)
        stack = [(root, None)]
        while stack:
            node, parent = stack.pop()
            if parent:
                adj[node.data].append(parent.data)
                adj[parent.data].append(node.data)
            if node.left:
                stack.append((node.left, node))
            if node.right:
                stack.append((node.right, node))

        # 2) BFS from target value, counting levels until everything burns.
        visited = set([target])
        q = deque([target])
        time = 0

        while q:
            # Process current "front" of the fire
            size = len(q)
            any_new = False
            for _ in range(size):
                u = q.popleft()
                for v in adj[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append(v)
                        any_new = True
            # If we spread to any new node this round, that's +1 second
            if any_new:
                time += 1

        return time
