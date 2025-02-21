import heapq
from typing import List

class Solution:
    def getMedian(self, arr: List[int]) -> List[float]:
        lo = []  # max heap (store negative values)
        hi = []  # min heap
        result = []
        
        for num in arr:
            # Decide which heap to push the number into.
            if not lo or num <= -lo[0]:
                heapq.heappush(lo, -num)
            else:
                heapq.heappush(hi, num)
            
            # Balance the heaps so that their size difference is at most 1.
            if len(lo) > len(hi) + 1:
                heapq.heappush(hi, -heapq.heappop(lo))
            elif len(hi) > len(lo) + 1:
                heapq.heappush(lo, -heapq.heappop(hi))
            
            # Calculate the median.
            if len(lo) == len(hi):
                median = (-lo[0] + hi[0]) / 2.0
            elif len(lo) > len(hi):
                median = float(-lo[0])
            else:
                median = float(hi[0])
            
            result.append(median)
        
        return result

# Example usage:
# sol = Solution()
# print(sol.getMedian([5,15,1,3,2,8]))  # Output: [5.0, 10.0, 5.0, 4.0, 3.0, 4.0]
