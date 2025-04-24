class Solution:
    def singleNum(self, arr):
        xor_all = 0
        for num in arr:
            xor_all ^= num
        
        mask = xor_all & (-xor_all)
        x, y = 0, 0
        for num in arr:
            if num & mask:
                x ^= num
            else:
                y ^= num
        
        return sorted([x, y])
