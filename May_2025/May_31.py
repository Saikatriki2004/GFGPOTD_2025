import heapq

class Solution:
    def kthSmallest(self, matrix, k):
        """
        Return the k-th smallest element in an n×n matrix where each row and column is sorted in non-decreasing order.
        
        Approach: Use a min-heap of size at most n.  Initially push (value, row, col) for each row’s first column.
        Pop from the heap k−1 times, each time pushing the next element in that row (if any).  Finally, the top of
        the heap is the k-th smallest.
        
        Time: O(k log n), Space: O(n).
        """
        n = len(matrix)
        # A min-heap of tuples (value, row_index, col_index)
        min_heap = []
        
        # 1) Seed the heap with the first element of each row (col = 0).
        for r in range(n):
            # (value, row, col)
            heapq.heappush(min_heap, (matrix[r][0], r, 0))
        
        # 2) Pop (k-1) times; each time we pop (val, r, c), we push (matrix[r][c+1], r, c+1) if c+1 < n.
        for _ in range(k - 1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))
        
        # 3) The top of the heap is now the k-th smallest.
        return min_heap[0][0]
