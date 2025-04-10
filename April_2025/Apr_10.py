import math

class Solution:
    def minCost(self, houses):
        n = len(houses)
        if n <= 1:
            return 0
            
        def get_manhattan_distance(house1_index, house2_index):
            x1 = houses[house1_index][0]
            y1 = houses[house1_index][1]
            x2 = houses[house2_index][0]
            y2 = houses[house2_index][1]
            return abs(x1 - x2) + abs(y1 - y2)
            
        min_cost_to_S = [float('inf')] * n
        in_S = [False] * n
        total_min_cost = 0
        
        # Start with the first house (index 0) in S
        min_cost_to_S[0] = 0
        
        for i in range(n):
            # Find the vertex u not in S with the minimum cost to S
            u = -1
            min_cost = float('inf')
            for v in range(n):
                if not in_S[v] and min_cost_to_S[v] < min_cost:
                    min_cost = min_cost_to_S[v]
                    u = v
                    
            if u == -1:
                # This should not happen if the graph is connected (which it is here)
                break
                
            in_S[u] = True
            if i > 0:
                total_min_cost += min_cost
                
            # Update the min_cost_to_S for all neighbors v of u that are not in S
            for v in range(n):
                if not in_S[v]:
                    distance = get_manhattan_distance(u, v)
                    if distance < min_cost_to_S[v]:
                        min_cost_to_S[v] = distance
                        
        return total_min_cost
