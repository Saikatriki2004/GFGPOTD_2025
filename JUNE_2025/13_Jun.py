class Solution:
    def kokoEat(self, arr, k):
        """
        :param arr: List[int]  -- sizes of banana piles
        :param k:   int        -- hours available
        :return:    int        -- minimum eating speed s
        """
        def hours_needed(s):
            return sum((pile + s - 1) // s for pile in arr)

        lo, hi = 1, max(arr)
        while lo < hi:
            mid = (lo + hi) // 2
            if hours_needed(mid) <= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
