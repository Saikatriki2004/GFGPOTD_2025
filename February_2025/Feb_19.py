import heapq
from typing import List

# Node class definition
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def mergeKLists(self, arr: List[Node]) -> Node:
        # Create a dummy node to ease list construction
        dummy = Node(0)
        curr = dummy
        
        # Min-heap to store (node.data, counter, node)
        # We use a counter as a tie-breaker to avoid comparing Node objects directly.
        heap = []
        count = 0
        
        # Push the head of each non-empty list into the heap.
        for node in arr:
            if node:
                heapq.heappush(heap, (node.data, count, node))
                count += 1
        
        # Process the heap until it's empty.
        while heap:
            value, _, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.data, count, node.next))
                count += 1
        
        # The merged linked list is dummy.next.
        return dummy.next
