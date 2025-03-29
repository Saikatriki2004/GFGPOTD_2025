class Solution:
    def jobSequencing(self, deadline, profit):
        # Combine the deadlines and profits into a list of tuples
        jobs = list(zip(deadline, profit))
        # Sort jobs by profit in descending order
        jobs.sort(key=lambda x: -x[1])
        
        if not jobs:
            return [0, 0]
        
        max_deadline = max(deadline)
        # Initialize the parent array for Union-Find
        parent = list(range(max_deadline + 1))
        
        total_profit = 0
        count = 0
        
        for d, p in jobs:
            # Find the latest available slot for deadline 'd'
            available_slot = self.find(parent, d)
            if available_slot > 0:
                count += 1
                total_profit += p
                # Union the slot with the previous one
                parent[available_slot] = available_slot - 1
        
        return [count, total_profit]
    
    def find(self, parent, x):
        # Find with path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
