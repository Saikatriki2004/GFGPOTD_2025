class Solution:
    def nthRowOfPascalTriangle(self, n):
        if n == 0:
            return []
        row = [1]
        for k in range(1, n):
            next_element = row[-1] * ( (n - 1) - (k - 1) ) // k
            row.append(next_element)
        return row


