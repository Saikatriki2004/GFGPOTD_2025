class Solution:
    def sortArray(self, arr, A, B, C):
        """
        Given a sorted array arr[], applies f(x)=A x^2 + B x + C to each element
        and returns the transformed values in sorted order.
        """

        def f(x):
            return A*x*x + B*x + C

        n = len(arr)
        # Special case: if A == 0, f is linear.  f(x)=B*x+C is monotonic if B!=0.
        if A == 0:
            res = [B*x + C for x in arr]
            # If B<0 the linear function is decreasing, so we need to reverse.
            return res if B >= 0 else res[::-1]

        # For A != 0, f is a parabola.  If A>0 it opens upward (values largest at the ends),
        # if A<0 it opens downward (values smallest at the ends).
        res = [0] * n
        left, right = 0, n - 1
        # If A>0 we want to fill from the end backwards with the larger of f(arr[left]) and f(arr[right]).
        # If A<0 we fill from the start forwards with the smaller of the two.
        idx = n - 1 if A > 0 else 0

        while left <= right:
            fl = f(arr[left])
            fr = f(arr[right])
            if A > 0:
                # place the larger one at idx, move idx backwards
                if fl > fr:
                    res[idx] = fl
                    left += 1
                else:
                    res[idx] = fr
                    right -= 1
                idx -= 1
            else:  # A < 0
                # place the smaller one at idx, move idx forwards
                if fl < fr:
                    res[idx] = fl
                    left += 1
                else:
                    res[idx] = fr
                    right -= 1
                idx += 1

        return res
