class Solution:
    def nCr(self, n: int, r: int) -> int:
        # If r > n, there are no ways to choose r items from n.
        if r > n:
            return 0
        
        # Take advantage of symmetry: C(n, r) == C(n, n-r)
        r = min(r, n - r)
        
        # Build up the result multiplicatively:
        #   C(n, r) = n! / (r!(n-r)!) 
        #           = (n * (n-1) * ... * (n-r+1)) / (r * (r-1) * ... * 1)
        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) // i
        
        return res
