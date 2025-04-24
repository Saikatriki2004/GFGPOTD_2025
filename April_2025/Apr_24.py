class Solution:
    def getSingle(self, arr):
        result = 0
        for bit in range(32):  # Check each bit from 0 to 31
            sum_bits = 0
            for num in arr:
                # Use bitwise AND to check if the bit is set
                sum_bits += (num >> bit) & 1
            sum_bits %= 3
            if sum_bits == 1:
                result |= (1 << bit)  # Set the corresponding bit in the result
        
        # Adjust for 32-bit signed integer
        if result >= (1 << 31):
            result -= (1 << 32)
        
        return result
