import heapq

class Solution:
    def findSmallestRange(self, arr):
        """
        :param arr: List[List[int]] -- k sorted lists of length n
        :return: List[int] -- [low, high] smallest range that includes at least one number from each list
        """
        k = len(arr)
        if k == 0:
            return []

        # initialize heap with the first element of each list
        # heap entries are (value, list_index, element_index)
        heap = []
        current_max = float('-inf')
        for i in range(k):
            if not arr[i]:
                return []  # one of the lists is empty, no valid range
            val = arr[i][0]
            heap.append((val, i, 0))
            current_max = max(current_max, val)
        heapq.heapify(heap)

        # best range found so far
        best_low, best_high = -10**9, 10**9

        # keep pulling the minimum element and then pushing the next element from that list
        while True:
            current_min, row, idx = heapq.heappop(heap)

            # update best range if this is smaller
            if current_max - current_min < best_high - best_low:
                best_low, best_high = current_min, current_max

            # advance in the list from which we popped
            if idx + 1 < len(arr[row]):
                next_val = arr[row][idx + 1]
                # push the next element
                heapq.heappush(heap, (next_val, row, idx + 1))
                # update the current_max if needed
                if next_val > current_max:
                    current_max = next_val
            else:
                # we've exhausted one list—no further complete ranges possible
                break

        return [best_low, best_high]
