class Solution:
    def nQueen(self, n):
        results = []
        cols = set()   # Columns where queens are placed
        diag1 = set()  # Diagonal 1 (row - col)
        diag2 = set()  # Diagonal 2 (row + col)
        
        def backtrack(col, positions):
            if col == n:  # If all columns are filled, add the solution
                results.append(positions[:])
                return
            
            for row in range(1, n + 1):  # Try placing the queen in each row (1-based index)
                if row not in cols and (row - col) not in diag1 and (row + col) not in diag2:
                    # Place queen
                    positions.append(row)
                    cols.add(row)
                    diag1.add(row - col)
                    diag2.add(row + col)

                    backtrack(col + 1, positions)  # Recur for the next column

                    # Remove queen (Backtrack)
                    positions.pop()
                    cols.remove(row)
                    diag1.remove(row - col)
                    diag2.remove(row + col)

        backtrack(0, [])  # Start from column 0
        return results
