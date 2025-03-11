class Solution:
    def countWays(self, n):
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize for n=1 and n=2
        a = 1  # ways(1)
        b = 2  # ways(2)
        
        # Compute ways for n >= 3
        for i in range(3, n + 1):
            c = a + b  # ways(i) = ways(i-1) + ways(i-2)
            a = b      # Shift: a becomes ways(i-1)
            b = c      # b becomes ways(i)
        
        return b
