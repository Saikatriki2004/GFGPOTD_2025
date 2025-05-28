class Solution:    
    def ValidCorner(self, mat):
        n = len(mat)
        m = len(mat[0]) if n > 0 else 0
        
        # Store the positions of 1s in each row using sets
        row_ones = []
        for i in range(n):
            ones = set()
            for j in range(m):
                if mat[i][j] == 1:
                    ones.add(j)
            row_ones.append(ones)
        
        # Check for any two rows that share at least two 1s in the same columns
        for i in range(n):
            for j in range(i + 1, n):
                common = row_ones[i].intersection(row_ones[j])
                if len(common) >= 2:
                    return True
        
        return False
