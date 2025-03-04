import bisect

class Solution:
    def lis(self, arr):
        L = []
        for x in arr:
            k = bisect.bisect_left(L, x)
            if k == len(L):
                L.append(x)
            else:
                L[k] = x
        return len(L)
