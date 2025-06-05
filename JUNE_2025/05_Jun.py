import collections

class Solution:
    def countPaths(self, edges, V, src, dest):
        # Build adjacency list for the DAG
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
        
        # dp[u] will hold the number of paths from u to dest (–1 means “not yet computed”)
        dp = [-1] * V
        
        def dfs(u):
            # Base case: if u is the destination, there's exactly 1 path (itself).
            if u == dest:
                return 1
            if dp[u] != -1:
                return dp[u]
            
            total_paths = 0
            # Sum over all outgoing edges u -> v
            for v in adj[u]:
                total_paths += dfs(v)
            
            dp[u] = total_paths
            return total_paths
        
        return dfs(src)
