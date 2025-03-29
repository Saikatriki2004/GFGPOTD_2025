class Solution:
    def activitySelection(self, start, finish):
        # Combine the start and finish times into a list of tuples
        activities = list(zip(start, finish))
        # Sort the activities based on their finish times
        activities.sort(key=lambda x: x[1])
        
        count = 0
        last_end = 0
        
        for s, f in activities:
            if s > last_end:
                count += 1
                last_end = f
        
        return count
