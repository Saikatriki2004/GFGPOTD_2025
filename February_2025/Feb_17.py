import heapq
from typing import List

class Solution:
    def kLargest(self, arr: List[int], k: int) -> List[int]:
        # heapq.nlargest returns the k largest elements in descending order.
        return heapq.nlargest(k, arr)
#Have a Good Day!
